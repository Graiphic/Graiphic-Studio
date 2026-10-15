# Graiphic Studio

The visual workspace for designing interfaces and dataflow in `.frog` documents.

Design a Front Panel, connect typed operations in the Block Diagram, and inspect
the resulting document in Source. Context Help explains the object under the
pointer and links directly to the relevant reference.

**[Read the documentation](https://graiphic.github.io/Graiphic-Studio/)** ·
[Start your first document](docs/getting-started.md) ·
[Browse functions](docs/functions/index.md) ·
[Browse widgets](docs/widgets/index.md)

## Choose a starting point

| I want to… | Read |
| --- | --- |
| Learn the workspace | [Getting started](docs/getting-started.md) |
| Place and edit controls | [Front Panel](docs/interface/front-panel.md) |
| Connect operations | [Block Diagram](docs/interface/block-diagram.md) |
| Understand an icon or terminal | [Context Help](docs/interface/context-help.md) and [Functions](docs/functions/index.md) |
| Try a supported graph locally | [Run and Highlight](docs/interface/run-and-highlight.md) |
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

The documentation reflects the **15 October 2026** Studio checkpoint. Existing
screenshots illustrate named workflows; they are not new captures of every
current feature. Function SVGs and connector schematics are identified as
reference illustrations rather than application screenshots.

## Contributing

- Start with the user's task, then explain the action, result, and relevant limit.
- Keep function names and identifiers aligned with the built-in help catalog.
- Use descriptive headings, relative Markdown links, and meaningful image text.
- Use real product captures or clearly identified reference illustrations.
- Distinguish editing support, private Run/Highlight, public Source, and target execution.

`docs/` contains guides, widget pages, function pages, and reference material.
`assets/` contains screenshots and explanatory visuals.
