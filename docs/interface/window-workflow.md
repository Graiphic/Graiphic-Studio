# Window Workflow

Graiphic Studio presents one `.frog` program through three coordinated windows.
Each window has a distinct responsibility, but all three edit or inspect the
same in-memory Program Model.

| Window | Primary responsibility | Source ownership |
| --- | --- | --- |
| Front Panel | User-facing widgets, labels, media, layout, and public bindings | `front_panel`, `interface`, and document presentation data |
| Block Diagram | Executable dataflow nodes, typed terminals, operations, and connections | `diagram.nodes`, `diagram.edges`, ports, and authored Diagram layout |
| Source | Live inspection of the serialized `.frog` document | The complete source representation |

## The Three Windows

### Front Panel

The Front Panel is the authored user interface. It contains controls,
indicators, labels, images, Array containers, and the Interface Map.

![Graiphic Studio Front Panel](../../assets/screenshots/front-panel/front-panel-overview.png)

### Block Diagram

The Block Diagram contains the executable dataflow representation. Widget
terminals, typed operations, comments, images, and connections are authored
here. The Function Navigator supplies operations without changing the Front
Panel layout.

![Graiphic Studio Block Diagram](../../assets/screenshots/block-diagram/function-navigator-numeric.jpg)

### Source

The Source window shows the canonical `.frog` document produced by the other
views. It is the direct inspection surface for object identity, types,
bindings, view state, and authored layout.

![Graiphic Studio Source view](../../assets/screenshots/source-view/source-view-live.jpg)

## Switch Without Rearranging

`Ctrl+E` raises the companion Front Panel or Block Diagram. It is a focus and
visibility shortcut only: it does not tile, resize, or reposition either
window. `Ctrl+T` is the explicit command for tiling the Front Panel and Block
Diagram. `Ctrl+Shift+E` opens or raises the Source view.

This distinction protects a user-arranged desktop. A carefully positioned
Front Panel remains unchanged when the user briefly checks the Diagram.

## Coordinated Changes

The views update from one Program Model rather than from delayed file reloads:

- Placing a Front Panel widget creates or updates its typed Diagram terminal.
- Changing Control/Indicator role updates terminal direction and icon posture.
- Changing a Numeric representation updates terminal type and binding color.
- Encapsulating a widget in an Array replaces the scalar terminal with the
  matching typed Array terminal.
- Deleting the widget terminal or its Front Panel peer removes the same logical
  object from both views.
- Source reflects the resulting `.frog` structure and authored layout.

`Find Terminal` and `Find Control` navigate between paired objects. The target
uses one short, high-contrast fade so the relationship is visible without
leaving persistent decoration.

## Focus-Scoped Navigators

Pinned Widget Navigators belong to the Front Panel workspace. They hide when
the Block Diagram receives focus and return at their saved positions when the
Front Panel is raised. Pinned Function Navigators follow the reciprocal rule
for the Block Diagram. Restored windows remain interactive, including widget
and operation drag-and-drop.

Several pinned Navigator windows may coexist. They can be resized; tiles reflow
to the available width and scrollbars appear when the content no longer fits.

## Saved State And Local Preferences

Authored object positions, Front Panel canvas dimensions, view origins, and
document zoom are source-carried reopen state. Native monitor placement is a
recoverable hint. Theme, interface language, navigation font size, and local
SVG glyph folders are user preferences stored outside the `.frog` document.

See [The `.frog` Document Model](../reference/document-model.md) for the exact
boundary.
