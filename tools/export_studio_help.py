#!/usr/bin/env python3
"""Export reviewed Studio help and authoring metadata into the public reference.

Run from any directory with Python 3.11+, without application builds or packages:
  python tools/export_studio_help.py --source ../FROG-STUDIO/native-portable-engine
  python tools/export_studio_help.py --source ../FROG-STUDIO/native-portable-engine --check

The source checkout is read-only. Only docs/functions and assets/function-icons
are generated. No source paths become links to the private Studio repository.
"""

from __future__ import annotations

import argparse
import collections
import configparser
import hashlib
import html
import json
from pathlib import Path
import posixpath
import re
from urllib.parse import quote, unquote, urlsplit


BASE_URL = "https://graiphic.github.io/Graiphic-Studio/"
CATALOG_SOURCES = (
    "src/FunctionCatalogEntries.inc",
    "manifests/connectivity/entries.generated.inc",
    "manifests/math/entries.inc",
    "manifests/file/entries.inc",
)
FAMILY_NAMES = {
    "ApplicationControl": "Application Control", "StringPath": "String",
}
FOLDER_ALIASES = {
    "mathematics.numeric": "numeric",
    "mathematics.comparison": "comparison",
    "structures.synchronization": "synchronization",
}
QUEUE_DEFAULTS = {
    "timeout_ms": "-1", "max_size": "-1", "create_if_not_found": "true",
    "force_destroy": "false", "return_elements": "false", "name": '""',
}
QUEUE_DETAILS = {
    "obtain": "The optional element data type is a type specimen, not a first message. With no specimen, Studio resolves T to F64. An empty name creates a new anonymous FIFO. A nonempty name obtains an independent access to the same application queue only when the entire element schema matches; an existing queue keeps its capacity. Capacity -1 is unbounded.",
    "enqueue": "Writes exactly one complete T message at the tail. A full bounded queue waits for space; an ordinary timeout inserts nothing. It never evicts an older message. Check timed out? and error out before treating the write as successful.",
    "preview": "Returns the head without removing or reserving it. Another consumer may remove that message after the preview succeeds. Check timed out? and error out before using element as a received message.",
    "status": "Returns one coherent instant snapshot of the name, capacity, element count and waiting operations. Both Preview and Dequeue count as pending removals. With return elements? false, elements is an empty outer array; true returns the current messages without removing them.",
    "release": "Releases this obtained access. Independently obtained accesses remain valid unless force destroy? is true. Forced destruction invalidates all accesses and wakes pending operations with errors. Cleanup runs even with an incoming error. The outputs describe the FIFO before release; this function has no queue-reference output.",
    "lossy_enqueue": "Never waits. If a bounded queue is full, it atomically evicts the oldest message and appends the new one. overflow element is meaningful only when overflow? is true. Ordinary Enqueue does not perform this loss.",
    "dequeue": "Removes and returns one head message in FIFO order. An empty queue waits cooperatively. A normal timeout is distinct from invalidation and from successful receipt; check timed out? and error out before consuming element.",
    "flush": "Atomically removes the messages currently present and returns them in FIFO order. The queue remains valid. An empty FIFO returns an empty outer array. When T is itself an Array, each T stays one message rather than being flattened into the returned collection.",
}


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def prose(value) -> str:
    return html.escape(str(value), quote=False).replace("|", "\\|").replace("\n", " ")


def code(value) -> str:
    return "`" + str(value).replace("`", "'").replace("|", "\\|").replace("\n", " ") + "`"


def link(title: str, route: str) -> str:
    return f"[{prose(title)}]({quote(route, safe='/._-:#?=&%')})"


def route_for(catalog_id: str) -> str:
    if not re.fullmatch(r"[A-Za-z][A-Za-z0-9_-]*(?:\.[A-Za-z0-9_-]+)+", catalog_id):
        raise ValueError(f"Unsafe catalog ID: {catalog_id}")
    return "docs/functions/" + catalog_id.replace(".", "/") + ".md"


def relative_links(page: str, text: str) -> str:
    """Keep published logical routes stable but make Markdown portable."""
    def rewrite(match):
        target = match[1]
        path, separator, anchor = target.partition("#")
        if not path.startswith(("docs/", "assets/")):
            return match[0]
        relative = posixpath.relpath(path, posixpath.dirname(page))
        return "](" + relative + (separator + anchor if separator else "") + ")"
    return re.sub(r"\]\(([^)]+)\)", rewrite, text)


def cpp_string(value: str) -> str:
    # Reviewed catalog strings use the common JSON-compatible C++ escapes.
    return json.loads(value)


def load_catalog(source: Path):
    entries = {}
    for filename in CATALOG_SOURCES:
        for line in (source / filename).read_text(encoding="utf-8-sig").splitlines():
            match = re.match(r"\s*FROG_FUNCTION_ENTRY\(FunctionFamily::(\w+),\s*(.*)\)\s*$", line)
            if not match:
                continue
            strings = re.findall(r'"(?:\\.|[^"\\])*"', match[2])
            values = [cpp_string(s) for s in strings]
            cid, title, icon, primitive = values[:4]
            if cid in entries:
                raise ValueError(f"Duplicate catalog ID: {cid}")
            family = "String" if match[1] == "StringPath" else match[1]
            entries[cid] = {
                "catalog_id": cid, "title_en": title, "family": FAMILY_NAMES.get(family, family),
                "family_id": family.lower(), "source_icon": icon, "primitive": primitive,
                "parent": values[4] if len(values) > 4 else "",
                "kind": "folder" if "FunctionCatalogEntryKind::Folder" in line else "operation",
                "role": "structure_container" if "FunctionCatalogEntryRole::StructureContainer" in line else "node",
                "palette_visible": not line.endswith("false)"), "catalog_source": filename,
            }
    return entries


def load_inputs(source: Path):
    help_catalog = configparser.RawConfigParser(interpolation=None, strict=True)
    help_catalog.read(source / "config/context-help.ini", encoding="utf-8-sig")
    contracts, contract_sources = {}, {}
    consumed = {"config/context-help.ini", "src/FunctionCatalog.cpp", "src/FunctionCatalogLegacyAliases.inc", *CATALOG_SOURCES}
    for path in sorted((source / "manifests/function-bindings").glob("studio.*.v2.json")):
        document = read_json(path)
        if "entries" not in document:
            continue
        name = path.relative_to(source).as_posix()
        consumed.add(name)
        for entry in document["entries"]:
            cid = entry["catalog_id"]
            if cid in contracts:
                raise ValueError(f"Duplicate contract: {cid}")
            contracts[cid], contract_sources[cid] = entry, name
    supplemental, palettes = {}, {}
    for path in sorted((source / "manifests/connectivity").glob("*.json")):
        document = read_json(path)
        functions = document.get("functions", [])
        if "id" in document and "ports" in document:
            functions = [document]
        if functions or document.get("palettes"):
            consumed.add(path.relative_to(source).as_posix())
        for function in functions:
            supplemental[function["id"]] = function
        for palette in document.get("palettes", []):
            palettes[palette["id"]] = palette
    math_path = source / "manifests/math/exponential.json"
    consumed.add(math_path.relative_to(source).as_posix())
    for function in read_json(math_path)["functions"]:
        supplemental[function["id"]] = function
    file_defaults_path = source / "manifests/file/defaults.inc"
    consumed.add(file_defaults_path.relative_to(source).as_posix())
    defaults = {}
    for line in file_defaults_path.read_text(encoding="utf-8-sig").splitlines():
        values = re.findall(r'"(?:\\.|[^"\\])*"', line)
        if line.startswith("FILE_DEFAULT(") and len(values) == 3:
            cid, port, value = map(cpp_string, values)
            defaults[cid, port] = value if value else '""'
    consumed.update(("src/QueueFunctionBinding.cpp", "src/QueueRuntime.cpp"))
    aliases = collections.defaultdict(list)
    alias_text = (source / "src/FunctionCatalogLegacyAliases.inc").read_text(encoding="utf-8-sig")
    for alias, canonical in re.findall(r'FROG_FUNCTION_ALIAS\("([^"]+)",\s*"([^"]+)"\)', alias_text):
        aliases[canonical].extend((alias, "frog.studio." + alias))
    catalog_text = (source / "src/FunctionCatalog.cpp").read_text(encoding="utf-8-sig")
    array_alias_block = catalog_text.split('if (entry.catalogId == "array.constant") {', 1)[1].split("}\n", 1)[0]
    aliases["array.constant"].extend(re.findall(r'"(frog\.studio\.[^"]+)"', array_alias_block))
    label_path = "src/win32/Win32FunctionPortLabels.inc"
    label_text = (source / label_path).read_text(encoding="utf-8-sig")
    labels = {}
    for line in label_text.splitlines():
        match = re.match(r'PORT\(("(?:\\.|[^"\\])*"),\s*("(?:\\.|[^"\\])*"),\s*(Input|Output),\s*("(?:\\.|[^"\\])*")\)', line)
        if match:
            labels[cpp_string(match[1]), cpp_string(match[2]), match[3].lower()] = cpp_string(match[4])
    consumed.update((label_path, "src/win32/Win32FunctionPortLabels.cpp", "src/win32/Win32DiagramPortDisplay.cpp", "src/HighlightExecutionEvaluator.cpp", "src/win32/Win32HighlightExecutionController.cpp"))
    evaluator = (source / "src/HighlightExecutionEvaluator.cpp").read_text(encoding="utf-8-sig")
    dispatch = re.search(r"const bool implemented=(.*?);", evaluator, re.S)
    if not dispatch:
        raise ValueError("The private evaluator dispatch table has changed; review the exporter.")
    private_ids = set(re.findall(r'id=="([^"]+)"', dispatch[1]))
    private_prefixes = re.findall(r'id\.starts_with\("([^"]+)"\)', dispatch[1])
    for cid in contracts:
        if cid in private_ids or any(cid.startswith(prefix) for prefix in private_prefixes):
            supplemental.setdefault(cid, {})["studio_local_evaluator_dispatch"] = True
    return help_catalog, contracts, contract_sources, supplemental, palettes, defaults, aliases, labels, consumed


def purpose_parts(text: str):
    parts = text.split("[Types]", 1)
    purpose = parts[0].strip()
    rule = parts[1].strip() if len(parts) > 1 else ""
    if rule and rule.rstrip(".") == purpose.rstrip("."):
        rule = ""
    return purpose, rule


def table(headers, rows):
    return ["| " + " | ".join(headers) + " |", "| " + " | ".join("---" for _ in headers) + " |", *["| " + " | ".join(row) + " |" for row in rows], ""]


def default_text(cid, port, metadata, defaults, is_input=True):
    if not is_input:
        return "—"
    if cid.startswith("synchronization.queue.") and port["id"] in QUEUE_DEFAULTS:
        return code(QUEUE_DEFAULTS[port["id"]])
    if (cid, port["id"]) in defaults:
        return code(defaults[cid, port["id"]])
    for key in ("default", "default_value"):
        if key in metadata and metadata[key] != "":
            return code(metadata[key])
    return "Not specified"


def port_rows(cid, ports, supplemental, defaults, helper, direction, labels):
    metadata_ports = {p["id"]: p for p in supplemental.get("ports", [])}
    for port in ports:
        metadata = metadata_ports.get(port["id"], {})
        requirement = port["requirement"].capitalize()
        helper_flag = helper.get(f"port.{direction}.{port['id']}")
        if helper_flag and helper_flag != port["requirement"]:
            requirement = helper_flag.capitalize() + " (help); " + requirement + " (binding)"
        if metadata.get("requirement") == "unverified":
            requirement += "; NI flag unverified"
        # Configured Connectivity names take priority in diagramPortDisplayName;
        # otherwise the shared presentation table takes priority over bindings.
        display_name = metadata.get("name") if cid.startswith("connectivity.") else None
        display_name = display_name or labels.get((cid, port["id"], direction), port["display_name"])
        details = prose(metadata.get("description", ""))
        if metadata.get("unit"):
            details += (" " if details else "") + "Unit: " + code(metadata["unit"]) + "."
        yield [prose(display_name) + " " + code(port["id"]), code(port["type"]), requirement,
               default_text(cid, port, metadata, defaults, direction == "input"), details or "—"]


def render_policy(contract, supplemental):
    lines = ["## Types and connection rules", ""]
    policy = contract["overload_type_resolution"]
    if policy.get("description"):
        lines.extend((prose(policy["description"]), ""))
    lines.extend((f"- Type resolution: {code(policy['policy'])}; result expression: {code(policy['result'])}.",
                  "- Implicit coercion: " + ("permitted by this profile." if policy["implicit_coercion"] else "not enabled by this resolver; individual port policies remain explicit.")))
    array = contract["array_policy"]
    accepted = {True: "accepted", False: "not accepted", None: "not established"}[array["accepted"]]
    lines.append(f"- Arrays: {accepted}; lifting policy: {code(array['lifting'])}.")
    for name, label in (("shape_rule", "Shape rule"), ("accepted_rank", "Accepted rank"), ("result_rank", "Result rank"), ("empty_array_identity", "Empty-array identity")):
        if name in array:
            lines.append(f"- {label}: {code(array[name])}.")
    for name, label in (("scalar_lift", "Scalar lifting"), ("broadcasting", "Broadcasting"), ("produces_array", "Array output")):
        if name in array:
            lines.append(f"- {label}: {'yes' if array[name] else 'no'}.")
    if array.get("description") and array["description"] != policy.get("description"):
        lines.extend(("", prose(array["description"])))
    variadic = contract["variadicity"]
    if variadic["enabled"]:
        lines.extend(("", f"**Expandable inputs:** {variadic['minimum_input_count']} to {variadic['maximum_input_count']}. Reduction: {code(variadic['reduction'])}."))
    elif variadic.get("input_count") is not None:
        lines.extend(("", f"**Input count:** {variadic['input_count']}; this contract does not enable variadic inputs."))
    else:
        lines.extend(("", "Input count is instance-dependent or not established by this contract."))
    if variadic.get("port_order"):
        lines.extend(("", "Port order: " + " → ".join(code(p) for p in variadic["port_order"]) + "."))
    if variadic.get("description"):
        lines.extend(("", prose(variadic["description"])))
    for key, value in supplemental.get("overload_type_resolution", {}).items():
        if isinstance(value, str) and key not in ("resolver_id",):
            lines.extend(("", f"**{prose(key.replace('_', ' ').capitalize())}:** {prose(value)}"))
    lines.append("")
    return lines


def render_instances(supplemental):
    lines = []
    instances = supplemental.get("instances", [])
    if not instances:
        return lines
    lines.extend(("## Configured connector instances", "", "The selected instance supplies its own connector. Requirements and defaults are not borrowed from a different instance.", ""))
    for instance in instances:
        lines.extend((f"### {prose(instance['name'])}", "", "Instance: " + code(instance["id"]) + ".", ""))
        rows = []
        for port in instance.get("ports", []):
            value = port.get("default", port.get("default_value", ""))
            rows.append([port["direction"].upper(), prose(port.get("name", port["id"])) + " " + code(port["id"]), code(port["type"]), prose(port.get("requirement", "unverified")), code(value) if value != "" else "Not specified"])
        lines.extend(table(["Direction", "Terminal / ID", "Type", "Requirement evidence", "Default"], rows))
    return lines


def render_runtime(cid, contract, supplemental):
    runtime = contract["runtime_availability"]
    available = runtime["available"]
    lines = ["## Execution and limits", "", "**Public FROG / target Runtime:** " + ("declared available within the scope below." if available else "not declared available by this authoring contract."), ""]
    if runtime.get("availability_scope"):
        lines.extend(("Scope: " + code(runtime["availability_scope"]) + ".", ""))
    if runtime.get("implementation_id"):
        lines.extend(("Implementation: " + code(runtime["implementation_id"]) + ".", ""))
    if runtime.get("provider_requirement"):
        lines.extend(("Required provider: " + code(runtime["provider_requirement"]) + ".", ""))
    if runtime.get("notes"):
        lines.extend((prose(runtime["notes"]), ""))
    blockers = list(dict.fromkeys(contract.get("blockers", [])))
    if blockers:
        lines.extend(("**Authoring/target contract limits:**", ""))
        lines.extend("- " + prose(item) for item in blockers)
        lines.append("")
    if cid.startswith("synchronization.queue."):
        lines.extend(("**Private Studio Run/Highlight:** the local Queue execution provider implements this operation. It does not establish public FROG lowering or a target provider.", ""))
    if supplemental.get("studio_local_evaluator_dispatch"):
        lines.extend(("**Private Studio Run/Highlight:** the local function evaluator dispatches this catalogue identity. Inputs and output types must be resolved; unsupported value operations or representations fail explicitly. This local dispatch is separate from the public target Runtime declaration above.", ""))
        if cid in ("numeric.add", "numeric.subtract", "numeric.multiply", "numeric.divide"):
            lines.extend(("Local arithmetic includes F32/F64 and supported integer leaves, scalar lifting and matching-shape Arrays. It preserves the resolved aggregate shape and narrows each step of the canonical arithmetic fold. Complex and extended-precision leaf arithmetic is not implemented by this evaluator. Array execution here does not establish a public target Array provider.", ""))
    highlight = supplemental.get("highlight_availability", {})
    if highlight:
        lines.extend(("**Private Studio Run/Highlight:** " + ("a local calculation provider is declared." if highlight.get("available") else "not available."), "", prose(highlight.get("scope", "")), ""))
    extra_limits = [item for item in dict.fromkeys(supplemental.get("limitations", [])) if item not in blockers]
    if extra_limits:
        lines.extend(("**Additional connector limits:**", ""))
        lines.extend("- " + prose(item) for item in extra_limits)
        lines.append("")
    return lines


def render_page(entry, contract, help_entry, supplemental, palettes, defaults, entries, labels):
    cid = entry["catalog_id"]
    title = entry["title_en"]
    icon = quote(entry["icon"] or "", safe="/._-")
    lines = ["<!-- Generated by tools/export_studio_help.py; edit the reviewed source metadata, then regenerate. -->", f"# {prose(title)}", "",
             f'![{prose(title)} function icon]({icon})' if icon else "No icon asset is declared for this entry in the Studio catalogue.", "",
             f"{link(entry['family'] + ' functions', entry['family_route'])} · {link('All functions', 'docs/functions/index.md')}", "", prose(entry["summary"]), ""]
    if supplemental.get("formula"):
        lines.extend(("Formula: " + code(supplemental["formula"]) + ".", ""))
    if entry["title_fr"] or help_entry.get("description.fr"):
        lines.extend(("<details>", "<summary>Résumé français de l’aide Studio</summary>", ""))
        if entry["title_fr"]:
            lines.extend(("**" + prose(entry["title_fr"]) + "**", ""))
        if help_entry.get("description.fr"):
            if supplemental.get("matrix_dispatch", {}).get("available"):
                lines.extend(("Le texte existant ci-dessous ne décrit pas le profil matriciel déclaré dans les métadonnées actuelles. Les règles et limites de ce profil sont précisées dans les sections anglaises de cette fiche.", ""))
            lines.extend((prose(help_entry["description.fr"]), ""))
        lines.extend(("</details>", ""))
    if entry["kind"] == "folder":
        lines.extend(("## Browse this palette", "", "This entry opens a palette folder; it is not an executable dataflow function.", ""))
        if cid in FOLDER_ALIASES:
            family = FOLDER_ALIASES[cid]
            lines.extend((link("Open the canonical " + family + " reference", f"docs/functions/{family}/index.md") + ".", ""))
        children = [e for e in entries.values() if e["parent"] == cid]
        if children:
            lines.extend(table(["Entry", "Purpose"], [[link(e["title_en"], e["route"]), prose(e["summary"])] for e in children]))
        elif cid not in FOLDER_ALIASES:
            lines.extend(("No direct child operation is declared in the current catalogue snapshot. Browse the family reference for the entries that are available.", ""))
    elif contract:
        status = contract["contract_status"].replace("_", " ")
        lines.extend(("## Studio authoring profile", "", f"Contract status: **{status}**. " + ("This is an editor-managed element; placement and configured values are distinct from an executable function provider." if contract["contract_status"] == "editor_managed" else "The connector below describes Studio authoring; execution availability is stated separately."), ""))
        behavior = contract["behavior_summary"]
        if behavior and behavior != entry["summary"] and not behavior.startswith("Preserves the historical Studio authoring bindings for"):
            lines.extend((prose(behavior), ""))
        _, help_rules = purpose_parts(help_entry.get("description.en", ""))
        if help_rules and not supplemental.get("matrix_dispatch", {}).get("available"):
            lines.extend((prose(help_rules), ""))
        if cid.startswith("synchronization.queue."):
            lines.extend(("## Queue behavior", "", prose(QUEUE_DETAILS[cid.rsplit(".", 1)[1]]), "", "Queue&lt;T&gt; is a nominal execution-resource access reference. The complete T schema is invariant; an Array, Cluster or Enum message remains one T value. Collection outputs add one outer rank-1 Array.", ""))
            if any(p["id"] == "timeout_ms" for p in contract["ports"]["inputs"]):
                lines.extend(("Timeout is I32 milliseconds: -1 waits without a deadline, 0 attempts immediately, and nonnegative values bound the wait. Waiting is cooperative. Invalidation wakes waits with an error.", ""))
        if cid == "numeric.quotient_remainder":
            lines.extend(("## Output mapping", "", "**Upper R = remainder:** `x - y * floor(x/y)`. **Lower IQ = integer quotient:** `floor(x/y)`. Studio preserves its historical endpoint IDs: the upper R output has internal ID `quotient`, and the lower IQ output has internal ID `remainder`. Use the displayed R/IQ meanings when wiring; the legacy identifier spelling does not redefine the calculation.", ""))
        for direction, label in (("inputs", "IN — inputs"), ("outputs", "OUT — outputs")):
            ports = contract["ports"][direction]
            lines.extend((f"## {label}", ""))
            if ports:
                lines.extend(table(["Displayed terminal / internal ID", "Accepted / resolved type", "Studio connection", "Unwired input default", "Meaning"], list(port_rows(cid, ports, supplemental, defaults, help_entry, direction[:-1], labels))))
                lines.append("A default is shown only for an input with an explicitly documented value. Preview/default *types* do not imply unwired operand values. If helper and binding flags differ, both are labelled.")
                lines.append("")
            else:
                lines.extend(("No fixed " + direction + " are declared in this binding profile. " + ("The editor or selected instance owns any contextual terminals." if contract["contract_status"] == "editor_managed" or entry["role"] == "structure_container" else "No connector is invented here."), ""))
        if contract["ports"].get("optional_input_pattern"):
            lines.extend(("Additional input IDs: " + code(contract["ports"]["optional_input_pattern"]) + ", starting at " + str(contract["ports"]["optional_input_first_index"]) + ".", ""))
            if cid in ("numeric.add", "numeric.multiply"):
                lines.extend(("When expanded beyond two operands, Studio displays x1, x2, …, xN and the corresponding result expression. The persisted input IDs and canonical operand order stay unchanged.", ""))
        if cid.startswith(("array.", "string.")) and (contract["variadicity"]["enabled"] or any(p["cardinality"] == "variadic" for p in contract["ports"]["inputs"] + contract["ports"]["outputs"])):
            lines.extend(("Expanded connector rows receive their live group/dimension number in Studio. Field selections and configured instances can also supply live names; the table documents the base connector and keeps its internal IDs separate.", ""))
        lines.extend(render_policy(contract, supplemental))
        lines.extend(render_instances(supplemental))
        lines.extend(render_runtime(cid, contract, supplemental))
        lines.extend(("<details>", "<summary>Connector type defaults and persistence aliases</summary>", ""))
        rows = []
        for direction in ("inputs", "outputs"):
            for port in contract["ports"][direction]:
                rows.append([direction[:-1].upper(), code(port["id"]), code(port["default_value_type"]), code(port["connection_policy"]), code(port["cardinality"]), ", ".join(code(a) for a in port.get("legacy_aliases", [])) or "—"])
        lines.extend(table(["Direction", "ID", "Preview/default type", "Connection policy", "Cardinality", "Legacy port IDs"], rows))
        lines.extend(("</details>", ""))
    else:
        lines.extend(("## Authoring scope", "", "This catalogue entry has no versioned function binding contract in the current snapshot. Its presence and icon establish discovery only; fixed ports, defaults and execution support are not inferred.", ""))
    lines.extend(("## Identity and references", "", "- Catalogue ID: " + code(cid) + "."))
    if entry["parent"]:
        lines.append("- Parent palette: " + link(entries[entry["parent"]]["title_en"], entries[entry["parent"]]["route"]) + ".")
    if contract:
        lines.extend(("- Profile: " + code(contract["profile_id"]) + ".", "- Definition: " + code(contract["definition_ref"]) + "."))
    if not entry["palette_visible"]:
        lines.append("- This identity is retained for existing documents and is hidden from new palette placement.")
    refs = []
    for url in [help_entry.get("url", ""), supplemental.get("documentation_url", ""), *(contract.get("authority_refs", []) if contract else []), contract.get("binding_projection", {}).get("documentation_url", "") if contract else ""]:
        if url.startswith(("https://www.ni.com/", "https://github.com/Graiphic/FROG/")) and url not in refs:
            refs.append(url)
    for url in refs:
        lines.append("- " + link("NI API reference" if "ni.com/" in url else "Published FROG specification", url) + ".")
    lines.extend(("", "NI links are reference sources for the connector model; Studio support is limited to the profile above. " + link("Reference provenance and notation", "docs/functions/index.md#provenance-and-notation") + ".", ""))
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=Path(__file__).resolve().parents[2] / "FROG-STUDIO/native-portable-engine")
    parser.add_argument("--output", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--routes-output", type=Path)
    parser.add_argument("--check", action="store_true", help="Check deterministic generated files without writing.")
    args = parser.parse_args()
    source, output = args.source.resolve(), args.output.resolve()
    catalog = load_catalog(source)
    help_catalog, contracts, contract_sources, supplemental, palettes, defaults, aliases, labels, consumed = load_inputs(source)
    missing = sorted(set(contracts) - set(catalog))
    if missing:
        raise ValueError(f"Contracts absent from catalogue: {missing}")
    artifacts = {}
    for cid, entry in catalog.items():
        helper = dict(help_catalog["function." + cid]) if "function." + cid in help_catalog else {}
        metadata = supplemental.get(cid, {})
        contract = contracts.get(cid)
        description = helper.get("description.en") or metadata.get("description") or palettes.get(cid, {}).get("description") or (contract["behavior_summary"] if contract else "")
        entry["summary"] = purpose_parts(description)[0] or ("Browse the " + entry["title_en"] + " palette.")
        entry["title_en"] = helper.get("title.en") or entry["title_en"]
        entry["title_fr"] = helper.get("title.fr", "")
        entry["route"] = route_for(cid)
        family_index = "docs/functions/" + entry["family_id"] + "/index.md"
        # array.index is a real operation whose exact help route must win.
        # Reserve a separate overview only for such actual catalogue collisions.
        entry["family_route"] = family_index if entry["family_id"] + ".index" not in catalog else "docs/functions/" + entry["family_id"] + "/overview.md"
        entry["icon"] = "assets/function-icons/" + entry["source_icon"] if entry["source_icon"] else None
        entry["aliases"] = sorted(set(aliases[cid] + ([metadata["key"]] if metadata.get("key") else []) + ([entry["primitive"]] if entry["primitive"] else [])))
        if entry["parent"] and entry["parent"] not in catalog:
            raise ValueError(f"Unknown parent for {cid}: {entry['parent']}")
        if entry["source_icon"]:
            icon_file = source / "assets/icons" / entry["source_icon"]
            if not icon_file.is_file():
                raise ValueError(f"Missing authentic icon for {cid}: {icon_file}")
            artifacts[entry["icon"]] = icon_file.read_bytes()
            consumed.add(icon_file.relative_to(source).as_posix())
    for cid, entry in catalog.items():
        helper = dict(help_catalog["function." + cid]) if "function." + cid in help_catalog else {}
        artifacts[entry["route"]] = render_page(entry, contracts.get(cid), helper, supplemental.get(cid, {}), palettes, defaults, catalog, labels).encode("utf-8")
    families = []
    for family_id in sorted({e["family_id"] for e in catalog.values()}):
        members = sorted((e for e in catalog.values() if e["family_id"] == family_id), key=lambda e: (e["kind"] == "folder", e["title_en"].casefold(), e["catalog_id"]))
        family = {"id": family_id, "name": members[0]["family"], "route": members[0]["family_route"], "entries": len(members), "operations": sum(e["kind"] != "folder" for e in members)}
        families.append(family)
        lines = [f"# {family['name']} functions", "", link("All functions", "docs/functions/index.md"), "", f"{family['operations']} operations or editor elements; {len(members) - family['operations']} palette folders. Open a page to inspect its exact connector, typing rules and execution limits.", ""]
        for kind, label in (("operation", "Operations and editor elements"), ("folder", "Palette folders")):
            rows = [[link(e["title_en"], e["route"]), prose(e["summary"])] for e in members if e["kind"] == kind]
            if rows:
                lines.extend((f"## {label}", ""))
                lines.extend(table(["Entry", "Purpose"], rows))
        if family["route"] in artifacts:
            raise ValueError(f"Family overview would overwrite a function page: {family['route']}")
        artifacts[family["route"]] = "\n".join(lines).encode("utf-8")
    counts = {"catalog_entries": len(catalog), "function_contracts": len(contracts), "palette_folders": sum(e["kind"] == "folder" for e in catalog.values()), "families": len(families), "helper_entries": sum("function." + cid in help_catalog for cid in catalog), "authentic_icons": len({e["icon"] for e in catalog.values() if e["icon"]}), "entries_without_icon": sum(not e["icon"] for e in catalog.values())}
    provenance = [{"path": name, "sha256": digest((source / name).read_bytes())} for name in sorted(consumed)]
    source_hash = digest(json.dumps(provenance, ensure_ascii=False, sort_keys=True).encode("utf-8"))
    records = []
    for cid, entry in sorted(catalog.items()):
        record = {k: entry[k] for k in ("catalog_id", "title_en", "title_fr", "family", "family_id", "route", "summary", "icon", "aliases", "parent", "kind", "role", "palette_visible")}
        record["contract_status"] = contracts.get(cid, {}).get("contract_status")
        record["public_runtime_available"] = contracts.get(cid, {}).get("runtime_availability", {}).get("available")
        record["private_studio_dispatch"] = True if supplemental.get(cid, {}).get("studio_local_evaluator_dispatch") or supplemental.get(cid, {}).get("highlight_availability", {}).get("available") or cid.startswith("synchronization.queue.") else None
        contract_ports = contracts.get(cid, {}).get("ports", {})
        supplemental_ports = {p["id"]: p for p in supplemental.get(cid, {}).get("ports", [])}
        connector_names = []
        for direction in ("input", "output"):
            for port in contract_ports.get(direction + "s", []):
                metadata_name = supplemental_ports.get(port["id"], {}).get("name") if cid.startswith("connectivity.") else None
                connector_names.extend((metadata_name or labels.get((cid, port["id"], direction), port["display_name"]), port["id"]))
        record["connector_names"] = sorted(set(connector_names))
        record["icon_sha256"] = digest(artifacts[entry["icon"]]) if entry["icon"] else None
        record["contract_source"] = contract_sources.get(cid)
        records.append(record)
    export = {"schema_version": 1, "source_snapshot": {"sha256": source_hash, "files": provenance}, "counts": counts, "families": families, "entries": records}
    artifacts["docs/functions/catalog.json"] = (json.dumps(export, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    routes = []
    for entry in records:
        cid = entry["catalog_id"]
        keys = [cid, "function." + cid, "frog.studio." + cid, *entry["aliases"]]
        routes.append({"catalog_id": cid, "route": entry["route"], "keys": sorted(set(keys))})
    route_export = (json.dumps({"schema_version": 1, "base_url": BASE_URL, "source_snapshot_sha256": source_hash, "routes": routes}, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    artifacts["docs/functions/routes.json"] = route_export
    lines = ["# Function reference", "", "Browse every function, editor element and palette folder in the current Studio catalogue. Each operation has its own page with its purpose, IN/OUT connectors, type rules and execution limits. Authentic palette icons are shown wherever the catalogue declares an asset.", "", "Use the documentation search for an English or French helper title, a catalogue ID, a connector name or a legacy identity. " + link("Machine-readable catalogue", "docs/functions/catalog.json") + ".", ""]
    lines.extend(table(["Family", "Operations / editor elements", "Folders"], [[link(f["name"], f["route"]), str(f["operations"]), str(f["entries"] - f["operations"])] for f in families]))
    lines.extend(("## Read a function page", "", "**IN** terminals receive values and **OUT** terminals publish values. Required inputs must be connected for semantic readiness. Recommended and optional inputs keep their distinct Studio connection flags. A listed default is a value only when the reviewed metadata states one; the preview type is shown separately.", "", "Authoring a node does not establish execution support. Each page names the public FROG / target Runtime declaration separately from private local Run/Highlight behavior when the source describes it. A partial or blocked authoring contract remains labelled as such.", "", "Constants, terminals and structure containers are included. Their editor-managed values, dynamic boundaries and configured connectors must not be read as an ordinary fixed executable function signature.", "", "## Provenance and notation", "", f"This deterministic export covers **{counts['catalog_entries']} catalogue entries**, **{counts['function_contracts']} versioned function contracts** and **{counts['palette_folders']} palette folders** across **{counts['families']} families**. {counts['helper_entries']} entries carry an existing context-help section. The remaining purposes come from reviewed family metadata or the versioned authoring contract.", "", "The English text follows Studio help. French summaries are reproduced only where the existing helper supplies them. Missing French text, defaults, requirements or capabilities are not translated or inferred.", "", "The source snapshot combines the context-help catalogue, the four catalogue tables, v2 family binding manifests, reviewed Connectivity/Mathematics metadata, explicit File defaults, Queue contracts, shared displayed terminal labels and private evaluator dispatch sources. SHA-256 hashes for every consumed source file and copied icon are retained in the machine-readable catalogue. Private source filenames are provenance records, not public source links.", "", "The SVG icons are copied byte for byte from Studio assets. They are reference icons, not screenshots of a running diagram. No screenshot or native execution result is synthesized. Three File reference entries declare no icon; their pages say so explicitly.", "", "Type expressions preserve the contract notation: `T:` names a generic type constraint; `array<...>` includes rank/shape rules; `cluster<...>` preserves ordered fields; `ref<...>` is a nominal reference; `resolve:...` names a resolver; `unresolved:...` requires explicit configuration or metadata. `f64`, `i32` and `bool` are scalar types. Exact per-port connection policies and preview types are available in each page’s connector-details panel.", "", "NI API links document reference semantics and connector evidence. They do not promise every NI overload or a compatible Studio execution provider. NI flags marked unverified stay unverified, even when Studio has an explicit authoring connection policy.", "", "Regenerate with Python 3.11+: `python tools/export_studio_help.py --source ../FROG-STUDIO/native-portable-engine`; add `--check` for a read-only deterministic export check. This documentation check does not run application regression tests.", "", "Source snapshot SHA-256: " + code(source_hash) + ".", ""))
    artifacts["docs/functions/index.md"] = "\n".join(lines).encode("utf-8")
    for cid, entry in catalog.items():
        if ("- Catalogue ID: " + code(cid) + ".").encode("utf-8") not in artifacts[entry["route"]]:
            raise ValueError(f"Function page lost its catalogue identity: {cid}")
    for name, data in list(artifacts.items()):
        if name.endswith(".md"):
            artifacts[name] = relative_links(name, data.decode("utf-8")).encode("utf-8")
    # Validate only links owned by this export. Existing site navigation has its own owner.
    missing_links = []
    for name, data in artifacts.items():
        if not name.endswith(".md"):
            continue
        text = data.decode("utf-8")
        urls = re.findall(r'\]\(([^)]+)\)|\bsrc="([^"]+)"', text)
        for pair in urls:
            target = unquote(next(value for value in pair if value)).split("#", 1)[0]
            if urlsplit(target).scheme or not target:
                continue
            target = posixpath.normpath(posixpath.join(posixpath.dirname(name), target))
            if target not in artifacts:
                missing_links.append((name, target))
        if "github.com/Graiphic/FROG-STUDIO" in text:
            raise ValueError(f"Private source link leaked in {name}")
    if missing_links:
        raise ValueError(f"Broken generated links: {missing_links[:10]}")
    mismatches = []
    for name, data in sorted(artifacts.items()):
        path = output / name
        if not path.is_file() or path.read_bytes() != data:
            mismatches.append(name)
            if not args.check:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(data)
    if args.routes_output and not args.check:
        args.routes_output.parent.mkdir(parents=True, exist_ok=True)
        args.routes_output.write_bytes(route_export)
    print(json.dumps({"mode": "check" if args.check else "export", "counts": counts, "artifact_files": len(artifacts), "changed_or_stale": len(mismatches), "source_snapshot_sha256": source_hash, "links": "all generated links resolve", "authentic_icons": "all copied bytes match source"}, indent=2))
    if args.check and mismatches:
        raise SystemExit("Stale generated output: " + ", ".join(mismatches[:10]))


if __name__ == "__main__":
    main()
