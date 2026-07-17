# Graiphic Studio Documentation

Welcome to the official user documentation for Graiphic Studio.

Graiphic Studio is a visual IDE for creating `.frog` documents. Its Front
Panel, Block Diagram, and Source windows are coordinated views of the same
program model. Users can design interfaces, build explicit dataflow, inspect
the source being produced, define an Interface Map, and edit the project icon.

![Graiphic Studio Front Panel](assets/screenshots/front-panel/front-panel-overview.png)

## Start Here

- [Getting Started](docs/getting-started.md)
- [Window Workflow](docs/interface/window-workflow.md)
- [Front Panel](docs/interface/front-panel.md)
- [Block Diagram](docs/interface/block-diagram.md)
- [Source View](docs/interface/source-view.md)
- [Studio Options](docs/interface/options.md)
- [Widget Navigator](docs/interface/widget-navigator.md)
- [Function Navigator](docs/interface/function-navigator.md)
- [Interface Map](docs/interface/interface-map.md)
- [Icon Editor](docs/interface/icon-editor.md)

## Design And Organize

- [Selection Pane](docs/interface/selection-pane.md)
- [Arrange and Resize](docs/interface/arrange-and-resize.md)
- [Color Tools](docs/interface/color-tools.md)

## Widget Documentation

- [Widgets Overview](docs/widgets/index.md)
- [Numeric](docs/widgets/numeric.md)
- [Boolean and Text Button](docs/widgets/boolean-and-button.md)
- [String and Path](docs/widgets/string-and-path.md)
- [Ring and Enum](docs/widgets/ring-and-enum.md)
- [Array Container](docs/widgets/array-container.md)
- [Image Static](docs/widgets/image-static.md)

## Reference

- [Glossary](docs/reference/glossary.md)
- [Screenshot Guide](docs/reference/screenshot-guide.md)
- [Keyboard Shortcuts](docs/reference/keyboard-shortcuts.md)
- [Document Model](docs/reference/document-model.md)

## Documentation Philosophy

The Studio is documented from the user workflow outward:

1. What the user sees.
2. What action the user can perform.
3. What changes in the `.frog` document.
4. Which view reflects the change.
5. What the runtime will eventually consume.

This keeps the documentation practical while preserving the source model.
When a feature is Studio-only or deliberately deferred, the page says so.
