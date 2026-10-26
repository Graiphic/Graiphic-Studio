"""Isolated export fixtures; never create a substitute canonical corpus."""
from __future__ import annotations

import collections
import configparser
import contextlib
import copy
import io
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest import mock

import export_studio_help as exporter
import studio_examples as examples


class ExampleExportTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="studio-example-export-test-")
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.root, self.site, self.engine = self.base / "FROG/Examples", self.base / "site", self.base / "engine"
        self.root.mkdir(parents=True)
        self.site.mkdir()
        (self.root.parent / "LICENSE").write_text("Fixture corpus license; not a product licensing declaration.\n", encoding="utf-8")
        self.catalog = {}
        for cid, family in (("cluster.conversion.array_to_cluster", "Cluster"), ("array.conversion.array_to_cluster", "Array"), ("numeric.add", "Numeric"), ("numeric.square", "Numeric")):
            icon = "functions/" + cid + ".svg"
            self.catalog[cid] = dict(catalog_id=cid, title_en=cid, family=family, family_id=family.lower(), source_icon=icon, primitive="", parent="", kind="operation", role="node", palette_visible=True, catalog_source="fixture")
            asset = self.engine / "assets/icons" / icon
            asset.parent.mkdir(parents=True, exist_ok=True)
            asset.write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 10 10"><path d="M1 1h8v8H1z"/></svg>', encoding="utf-8")
        self.document_bytes = b'{\r\n"format":"frog.document.draft","draft_revision":2,"language":"FROG","title":"Isolated fixture","frontPanel":{},"diagram":{"nodes":[],"edges":[]}\r\n}\r\n'
        self.rows = [dict(id="cluster.alias.sample", title="Exact Cluster example", summary="Retains an exact I64", description="Read the input and compare the typed output; this is an export fixture.", family="cluster", path="Native/cluster/cluster.alias.sample/main.frog", profile="studio-draft", mode="execution", catalog_ids=["cluster.conversion.array_to_cluster", "array.conversion.array_to_cluster"], backends=["native-fast", "native-debug"], dependencies=["Native/helper/main.frog", "Native/lib/frog-example-native-library.dll"], tags=["typed"], capability="fixture.only", order=1, expected=[dict(widget_id="result", type="i64", value_json="9007199254740993", comparator="exact", absolute_tolerance=0, relative_tolerance=0)]),
                     dict(id="numeric.nan.sample", title="Expected NaN", summary="Explicit special comparator", description="This fixture checks documentation of an expected value, without running a backend.", family="numeric", path="Native/numeric/numeric.nan.sample/main.frog", profile="source-0.1", mode="execution", catalog_ids=["numeric.add"], backends=["native-fast"], dependencies=[], tags=[], order=2, expected=[dict(widget_id="result", type="f64", value_json="", comparator="nan", absolute_tolerance=0, relative_tolerance=0)])]
        self.write("Native/cluster/cluster.alias.sample/main.frog", self.document_bytes)
        self.write("Native/helper/main.frog", self.document_bytes)
        self.write("Native/numeric/numeric.nan.sample/main.frog", b'{"spec_version":"0.1","title":"Isolated public fixture","diagram":{}}\n')
        self.write("Native/lib/frog-example-native-library.dll", b"MZ_isolated-export-fixture_not-a-loadable-library")
        for name in examples.LIBRARY_SOURCE_NAMES:
            self.write("Native/lib/" + name, ("Isolated fixture " + name + "\n").encode())
        self.index = self.root / "index.v1.json"
        self.save_index()

    def write(self, name, data):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)

    def save_index(self):
        self.index.write_text(json.dumps(dict(schema="frog.examples.index", version=1, examples=self.rows), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    def export(self, check=False):
        # Catalog/help are isolated reviewed-input fixtures, not an alternate
        # canonical index. Production main still reads its real source inputs.
        inputs = (configparser.RawConfigParser(), {}, {}, {}, {}, {}, collections.defaultdict(list), {}, set())
        argv = ["export_studio_help.py", "--source", str(self.engine), "--output", str(self.site), "--examples-index", str(self.index)] + (["--check"] if check else [])
        with mock.patch.object(exporter, "load_catalog", return_value=copy.deepcopy(self.catalog)), mock.patch.object(exporter, "load_inputs", return_value=inputs), mock.patch("sys.argv", argv), contextlib.redirect_stdout(io.StringIO()) as log:
            exporter.main()
        return json.loads(log.getvalue())

    def state(self, root):
        return {p.relative_to(root).as_posix(): (p.read_bytes(), p.stat().st_mtime_ns) for p in root.rglob("*") if p.is_file()}

    def test_exact_documents_dependencies_license_and_alias_join(self):
        before = self.state(self.root)
        result = self.export()
        self.assertEqual(result["example_documents"], 2)
        self.assertEqual(self.state(self.root), before)
        self.assertEqual((self.site / "assets/examples/index.v1.json").read_bytes(), self.index.read_bytes())
        self.assertEqual((self.site / "assets/examples/Native/cluster/cluster.alias.sample/main.frog").read_bytes(), self.document_bytes)
        for name in self.rows[0]["dependencies"] + ["Native/lib/" + n for n in examples.LIBRARY_SOURCE_NAMES]:
            self.assertEqual((self.site / "assets/examples" / name).read_bytes(), (self.root / name).read_bytes())
        self.assertEqual((self.site / "assets/examples/LICENSE").read_bytes(), (self.root.parent / "LICENSE").read_bytes())
        for cid in self.rows[0]["catalog_ids"]:
            page = (self.site / exporter.route_for(cid)).read_text(encoding="utf-8")
            self.assertIn("## Examples", page)
            self.assertIn("cluster.alias.sample.md", page)
            self.assertIn("not execution certificates", page)
        self.assertIn("No example for this object", (self.site / exporter.route_for("numeric.square")).read_text(encoding="utf-8"))
        page = (self.site / "docs/examples/cluster.alias.sample.md").read_text(encoding="utf-8")
        self.assertIn("9007199254740993", page)
        self.assertNotIn("9007199254740992", page)
        self.assertIn('download>', page)
        self.assertIn('../../assets/examples/Native/cluster/cluster.alias.sample/main.frog', page)
        self.assertIn("expected values, not a report", page)
        self.assertFalse(list(self.site.rglob("*.zip")))

    def test_check_is_deterministic_and_read_only(self):
        self.export()
        before, source_before = self.state(self.site), self.state(self.root)
        self.assertEqual(self.export(True)["changed_or_stale"], 0)
        self.assertEqual(self.export(True)["changed_or_stale"], 0)
        self.assertEqual(self.state(self.site), before)
        self.assertEqual(self.state(self.root), source_before)

    def test_check_detects_changed_copy_without_repair(self):
        self.export()
        target = self.site / "assets/examples/Native/cluster/cluster.alias.sample/main.frog"
        target.write_bytes(b"locally changed copy")
        before = self.state(self.site)
        with self.assertRaisesRegex(SystemExit, "Stale generated output"):
            self.export(True)
        self.assertEqual(self.state(self.site), before)

    def test_owned_pruning_preserves_manual_files(self):
        self.export()
        manual = self.site / "docs/examples/handwritten.md"
        manual.write_text("Manual content\n", encoding="utf-8")
        asset = self.site / "assets/examples/manual.frog"
        asset.write_bytes(b"Manual content\n")
        self.rows = self.rows[1:]
        self.save_index()
        self.export()
        self.assertFalse((self.site / "docs/examples/cluster.alias.sample.md").exists())
        self.assertFalse((self.site / "assets/examples/Native/lib/frog-example-native-library.dll").exists())
        self.assertEqual(manual.read_text(), "Manual content\n")
        self.assertEqual(asset.read_bytes(), b"Manual content\n")
        self.assertEqual(self.export(True)["changed_or_stale"], 0)

    def test_local_edit_blocks_stale_cleanup(self):
        self.export()
        target = self.site / "docs/examples/cluster.alias.sample.md"
        target.write_text("Locally edited old generated file\n", encoding="utf-8")
        self.rows = self.rows[1:]
        self.save_index()
        before = self.state(self.site)
        with self.assertRaisesRegex(ValueError, "local edits"):
            self.export()
        self.assertEqual(self.state(self.site), before)

    def test_case_only_path_update_retains_existing_physical_file(self):
        self.export()
        old_name = self.rows[1]["path"]
        new_name = old_name.replace("Native/numeric/", "Native/Numeric/")
        old_output = self.site / "assets/examples" / old_name
        new_output = self.site / "assets/examples" / new_name
        same_file = new_output.exists() and old_output.samefile(new_output)
        original = (self.root / old_name).read_bytes()
        self.write(new_name, original)
        self.rows[1]["path"] = new_name
        self.save_index()
        real_unlink = Path.unlink

        def unlink(path, *args, **kwargs):
            if same_file and path.exists() and path.samefile(old_output):
                self.fail("Case-only migration deleted a file retained by the new index")
            return real_unlink(path, *args, **kwargs)

        with mock.patch.object(Path, "unlink", unlink):
            self.export()
        self.assertEqual(new_output.read_bytes(), original)
        self.assertEqual(self.export(True)["changed_or_stale"], 0)
        ownership = examples.parse_json((self.site / examples.OWNERSHIP).read_text())
        paths = {row["path"] for row in ownership["files"]}
        self.assertIn("assets/examples/" + new_name, paths)
        self.assertNotIn("assets/examples/" + old_name, paths)

    def test_case_only_path_update_preserves_local_edit_guard(self):
        self.export()
        old_name = self.rows[1]["path"]
        new_name = old_name.replace("Native/numeric/", "Native/Numeric/")
        self.write(new_name, (self.root / old_name).read_bytes())
        (self.site / "assets/examples" / old_name).write_bytes(b"locally edited generated document")
        self.rows[1]["path"] = new_name
        self.save_index()
        before = self.state(self.site)
        with self.assertRaisesRegex(ValueError, "local edits"):
            self.export()
        self.assertEqual(self.state(self.site), before)

    def test_missing_index_never_creates_a_placeholder(self):
        self.index.unlink()
        with self.assertRaisesRegex(ValueError, "Canonical example index is missing"):
            self.export()
        self.assertFalse(list(self.site.iterdir()))
        self.assertFalse(self.index.exists())

    def test_profile_mismatch_is_refused(self):
        self.rows[0]["profile"] = "source-0.1"
        self.save_index()
        with self.assertRaisesRegex(ValueError, "profile disagrees"):
            self.export()
        self.assertFalse(list(self.site.iterdir()))

    def test_unknown_catalog_and_dependency_are_refused(self):
        self.rows[0]["catalog_ids"] = ["unknown.function"]
        self.save_index()
        with self.assertRaisesRegex(ValueError, "unknown catalog"):
            self.export()
        self.rows[0]["catalog_ids"] = ["cluster.conversion.array_to_cluster"]
        self.rows[0]["dependencies"] = ["Native/lib/unreviewed.dll"]
        self.save_index()
        with self.assertRaisesRegex(ValueError, "redistribution has not been reviewed"):
            self.export()

    def test_missing_library_sources_or_license_is_refused(self):
        source = self.root / "Native/lib/resources_structures.c"
        source.unlink()
        with self.assertRaisesRegex(ValueError, "Declared example file is missing"):
            self.export()
        self.write("Native/lib/resources_structures.c", b"restored isolated fixture\n")
        (self.root.parent / "LICENSE").unlink()
        with self.assertRaisesRegex(ValueError, "license is missing"):
            self.export()

    def test_unsafe_paths_and_case_collisions_are_refused(self):
        for path in ("../outside.frog", "Native//main.frog", "C:/private.frog", "/root.frog", "Native\\main.frog", "Native/./main.frog"):
            with self.subTest(path=path), self.assertRaises(ValueError):
                examples.within(self.root, path)
        self.rows[1]["id"] = self.rows[0]["id"].upper()
        self.save_index()
        with self.assertRaisesRegex(ValueError, "Duplicate or unsafe"):
            self.export()

    def test_symlink_cannot_escape_input_or_output_root(self):
        outside = self.base / "outside"
        outside.mkdir()
        (outside / "main.frog").write_bytes(self.document_bytes)
        try:
            os.symlink(outside, self.root / "escape", target_is_directory=True)
            os.symlink(outside, self.site / "escape", target_is_directory=True)
        except OSError as error:
            self.skipTest("Real symlink creation unavailable on this host: " + str(error))
        with self.assertRaisesRegex(ValueError, "escapes its root"):
            examples.within(self.root, "escape/main.frog")
        with self.assertRaisesRegex(ValueError, "escapes its root"):
            examples.destination(self.site, "escape/main.frog")

    def test_private_paths_are_not_redistributed_even_in_binary(self):
        self.write("Native/lib/frog-example-native-library.dll", b"MZ\0C:\\Users\\private-user\\build\\sample.pdb\0")
        with self.assertRaisesRegex(ValueError, "personal absolute path"):
            self.export()
        self.assertFalse(list(self.site.iterdir()))

    def test_output_resolution_cannot_delete_a_different_in_root_file(self):
        # Exercise the guard independently of Windows symlink privileges.
        with mock.patch.object(examples, "within", return_value=self.site / "handwritten.md"):
            with self.assertRaisesRegex(ValueError, "redirects through a link"):
                examples.destination(self.site, "assets/examples/old.frog")

    def test_expected_failure_and_context_values_are_not_pass_badges(self):
        self.rows[0]["mode"] = "expected-diagnostic"
        self.rows[0]["expected_diagnostic"] = "native.string.casefold_unavailable"
        self.rows[0]["expected"] = []
        self.rows[1]["expected"][0].update(comparator="document_path", value_json="null", type="path")
        self.save_index()
        self.export()
        page = (self.site / "docs/examples/cluster.alias.sample.md").read_text(encoding="utf-8")
        self.assertIn("native.string.casefold_unavailable", page)
        self.assertIn("unrelated refusal", page)
        self.assertNotIn("PASS", page)
        context = (self.site / "docs/examples/numeric.nan.sample.md").read_text(encoding="utf-8")
        self.assertIn("<current example document path>", context)
        self.assertNotIn(str(self.base), context)

    def test_unowned_manifest_path_and_changed_stale_hash_are_refused(self):
        self.export()
        manifest = self.site / examples.OWNERSHIP
        data = json.loads(manifest.read_text())
        data["files"][0]["path"] = "README.md"
        manifest.write_text(json.dumps(data), encoding="utf-8")
        before = self.state(self.site)
        with self.assertRaisesRegex(ValueError, "Unsafe generated-example ownership"):
            self.export()
        self.assertEqual(self.state(self.site), before)

    def test_duplicate_json_members_are_not_silently_reinterpreted(self):
        self.index.write_text('{"schema":"frog.examples.index","schema":"other","version":1,"examples":[]}', encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Duplicate JSON member"):
            self.export()


if __name__ == "__main__":
    unittest.main()
