# Source View

The Source view exposes the live `.frog` representation associated with the
current Graiphic Studio document. It complements the visual Front Panel and
Block Diagram by making serialized program structure directly inspectable.

![Live .frog source generated from the Front Panel](../../assets/screenshots/source-view/source-view-live.jpg)

## Open The View

Press `Ctrl+Shift+E` to open or raise the Source window. It has its own native
window geometry and does not resize the Front Panel or Block Diagram.

## What It Shows

The editor provides line numbers and syntax highlighting for the current JSON
source. It is useful for checking:

- metadata and schema identity;
- the public interface and Interface Map state;
- Front Panel widgets, labels, geometry, values, and bindings;
- Diagram nodes, ports, edges, annotations, and layout;
- the embedded document icon and media references;
- source-carried authoring state such as zoom and viewport origin.

The status area identifies the source as the live `.frog` projection generated
from the current document session.

## Source And Execution Boundary

The Source view does not make editor selection, hover, open menus, theme,
language, or navigation font size executable. The Diagram remains the
authoritative executable graph; the Front Panel remains the user-facing widget
composition; the Source view reveals the explicit document that connects
those concerns.

When a field is optional IDE metadata, runtimes and compilers must be able to
ignore it without changing program meaning. See [The `.frog` Document
Model](../reference/document-model.md).
