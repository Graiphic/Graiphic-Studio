# Graiphic Studio

Official user documentation for Graiphic Studio.

Graiphic Studio is the visual development environment for building `.frog`
documents: front panels, widgets, public interface maps, iconography, and the
visual editing workflow around them.

This repository is the public documentation home. It explains how the Studio
works from a user point of view and keeps screenshots, examples, terminology,
and behavior notes in one place.

## Documentation

- [Documentation Home](docs/index.md)
- [Getting Started](docs/getting-started.md)
- [Front Panel](docs/interface/front-panel.md)
- [Widget Navigator](docs/interface/widget-navigator.md)
- [Interface Map](docs/interface/interface-map.md)
- [Icon Editor](docs/interface/icon-editor.md)
- [Widgets](docs/widgets/index.md)
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

## Status

This documentation is being built alongside the Studio. Pages marked as draft
describe the intended direction and will be tightened as features stabilize.
