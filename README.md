# Graiphic Studio

Official user documentation for **Graiphic Studio**, the visual development
environment for `.frog` documents.

Graiphic Studio combines a vector Front Panel, source-backed widgets, a public
Interface Map, document iconography, and focused visual editing tools. This
repository explains those features from the user's point of view.

## Documentation

- [Documentation Home](docs/index.md)
- [Getting Started](docs/getting-started.md)
- [Front Panel](docs/interface/front-panel.md)
- [Studio Options](docs/interface/options.md)
- [Widget Navigator](docs/interface/widget-navigator.md)
- [Interface Map](docs/interface/interface-map.md)
- [Icon Editor](docs/interface/icon-editor.md)
- [Selection Pane](docs/interface/selection-pane.md)
- [Arrange and Resize](docs/interface/arrange-and-resize.md)
- [Color Tools](docs/interface/color-tools.md)
- [Widgets](docs/widgets/index.md)
- [Keyboard Shortcuts](docs/reference/keyboard-shortcuts.md)
- [Glossary](docs/reference/glossary.md)

## Repository Layout

```text
docs/
  index.md                     Documentation entry point
  getting-started.md           First user path
  interface/                   Studio surface documentation
  widgets/                     Widget-by-widget documentation
  reference/                   Glossary and conventions
assets/
  screenshots/                 Product screenshots used by the docs
  diagrams/                    Explanatory diagrams and exported visuals
```

## Documentation Rules

- Use the public product name: **Graiphic Studio**.
- Explain user-facing behavior before implementation details.
- Prefer screenshots for UI behavior once a feature is visually stable.
- Keep `.frog` source concepts explicit: widgets, labels, bindings, interface
  maps, icon assets, and runtime-facing artifacts are separate concepts.
- Avoid documenting experimental behavior as final unless it has been validated
  in the Studio.

## Product Status

Graiphic Studio is under active development. The documentation distinguishes
implemented behavior from future runtime or Diagram work. Screenshots are
captured from the native Windows target and updated when a workflow changes.
