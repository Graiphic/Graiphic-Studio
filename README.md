# Graiphic Studio

The [26 October documentation reconciliation](docs/reference/documentation-refresh-2026-10-26.md) brings forward Run/Highlight, standalone Build, standard Type Def, Tabs and attached-comment guides. The example results below remain a dated measurement.

The visual workspace for designing interfaces and dataflow in `.frog` documents.

Design a Front Panel, connect typed operations in the Block Diagram, and inspect
the resulting document in Source. Context Help explains the object under the
pointer and links directly to the relevant reference.

**[Read the documentation](https://graiphic.github.io/Graiphic-Studio/)** ·
[Start your first document](docs/getting-started.md) ·
[Browse functions](docs/functions/index.md) ·
[Browse actual .frog examples](docs/examples/index.md) ·
[Browse widgets](docs/widgets/index.md)

## Choose a starting point

| I want to… | Read |
| --- | --- |
| Learn the workspace | [Getting started](docs/getting-started.md) |
| Place and edit controls | [Front Panel](docs/interface/front-panel.md) |
| Connect operations | [Block Diagram](docs/interface/block-diagram.md) |
| Understand an icon or terminal | [Context Help](docs/interface/context-help.md) and [Functions](docs/functions/index.md) |
| Try a supported graph locally | [Run and Highlight](docs/interface/run-and-highlight.md) |
| Build a standalone EXE | [Build](docs/interface/build.md) |
| Share a control schema | [Type Definitions](docs/interface/type-definitions.md) |
| Organize independent controls into pages | [Tab Controls](docs/widgets/tab-controls.md) |
| Attach an annotation to a diagram object | [Attached comments](docs/interface/attached-comments.md) |
| Open an example with its explanation and expected results | [Examples](docs/examples/index.md) |
| Customize the editor | [Studio Options](docs/interface/options.md) |
| Check support and limitations | [Current capabilities](docs/reference/development-checkpoint.md) |

## About these docs

This repository contains the user guides and reference for Graiphic Studio.
Guides explain actions and their results; function pages describe purpose,
terminals, types, and current support using the Studio's existing help catalog.

The [FROG specification](https://graiphic.github.io/FROG/) defines the public
language. A feature available in Studio's editor or private local simulation
does not automatically have a public-source or target-runtime implementation.
See [the document model](docs/reference/document-model.md) for that boundary.

The [25 October 2026 checkpoint](docs/reference/development-checkpoint.md)
records **625 actual example documents and 1,219 measured checks**, with their
backend/profile limits. It is not a qualification of every function or a new
signed release. Existing screenshots illustrate named workflows; they are not
new captures of every current feature. Function SVGs and connector schematics
are identified as reference illustrations rather than application screenshots.

## Contributing

- Start with the user's task, then explain the action, result, and relevant limit.
- Keep function names and identifiers aligned with the built-in help catalog.
- Use descriptive headings, relative Markdown links, and meaningful image text.
- Use real product captures or clearly identified reference illustrations.
- Distinguish editing support, private Run/Highlight, public Source, and target execution.

`docs/` contains guides, widget pages, function pages, and reference material.
`assets/` contains screenshots and explanatory visuals.

The example pages and downloads are projections of the existing
`FROG/Examples/index.v1.json`. They preserve the actual document and dependency
bytes; they are not another operator registry or proof that a backend passed.
Studio Draft and public Source profiles remain distinct. See
[example profiles and execution scope](docs/reference/studio-draft-examples.md).

Regenerate locally with Python 3.11+ after the real corpus has been generated:

```text
python tools/export_studio_help.py --source ../FROG-STUDIO/native-portable-engine --examples-index ../FROG/Examples/index.v1.json
python tools/export_studio_help.py --source ../FROG-STUDIO/native-portable-engine --examples-index ../FROG/Examples/index.v1.json --check
python -m unittest discover -s tools -p test_export_studio_examples.py
```

An absent canonical index is an error; the exporter does not create a placeholder.
`--check` is read-only. Cleanup is limited to owned generated pages and the
example files recorded in the exporter ownership manifest, with their previous
hashes checked before deletion. Exporting locally does not push or deploy this site.
