# Getting Started

This page describes the first path through Graiphic Studio.

## 1. Open Graiphic Studio

Launch Graiphic Studio and start from the Front Panel. The Front Panel is the
main design surface for placing controls, indicators, labels, images, and
interface-related editing affordances.

Graiphic Studio opens the Front Panel by default. The Diagram and source window
remain complementary views of the same `.frog` document, but they are not
required for this first placement workflow.

![Empty Front Panel](../assets/screenshots/front-panel/front-panel-overview.png)

## 2. Place A Widget

Open the Widget Navigator, choose a widget family, then place a widget on the
grid.

Right-click an empty part of the Front Panel to open the Widget Navigator. Move
through a family, choose a control or indicator, then click the grid to place
it. A family tile can also choose that family's default widget.

Current core families include:

- Numeric
- Boolean
- String and Path
- Ring and Enum
- Data Containers
- Image Static

Controls accept user input. Indicators display values. This distinction also
determines the direction of a future Interface Map binding.

## 3. Move And Resize

Drag a widget from its body or available frame. Drag a resize handle to change
its dimensions. Hold `Shift` while resizing to preserve proportions. When grid
snapping is active, placement follows the Front Panel grid.

Hold `Shift` while moving to constrain the motion horizontally or vertically.
Hold `Ctrl` through a drag to move a duplicate; releasing `Ctrl` before the
drop cancels the duplicate operation.

## 4. Edit A Label

Double-click an empty area on the Front Panel to create a label. A new label
starts with placeholder text so that an empty label is not accidentally kept.

If the label is validated with no text, the label is removed.

![Creating a free label](../assets/screenshots/front-panel/create-label.png)

Press `Enter` to validate a label. Press `Shift+Enter` to insert a new line.
Widget labels use a magnetic default anchor: moving a detached label back near
its default position reconnects it naturally.

## 5. Save The Document

Save the document as a `.frog` file. The `.frog` document owns the source-level
state: widgets, layout, labels, bindings, interface map data, icon data, and
instance-level overrides.

The File menu provides New, Open, Close, Save, Save As, and Recent Files.
Recent Files is updated when a document is opened or saved successfully.

## 6. Place A Diagram Operation

Open the Diagram and its Function Navigator. Enter **Programming > Numeric**,
press and hold an operation tile, drag it onto the Diagram, then release it at
the desired position. The SVG preview follows the pointer during the drag.

The resulting operation is an explicit Diagram node and is saved in
`diagram.nodes` with its FROG primitive identity and authored layout. Releasing
outside the Diagram or pressing `Escape` cancels the placement.

Only operations backed by published FROG primitive contracts can currently be
placed. See the [Function Navigator](interface/function-navigator.md) for the
complete workflow and current scope.

## 7. Configure The Studio

Open **Tools > Options...** to choose the interface theme, configure the Front
Panel grid, or manage SVG glyph folders used by the Icon Editor. The Appearance
page provides a live preview before a theme is applied.

These choices are local Studio preferences. They do not change FROG execution
semantics. See [Studio Options](interface/options.md) for the complete workflow.

## Next Steps

- Learn the [Front Panel](interface/front-panel.md).
- Configure the IDE through [Studio Options](interface/options.md).
- Learn the [Interface Map](interface/interface-map.md).
- Learn how widgets are organized in the [Widget Navigator](interface/widget-navigator.md).
- Build dataflow operations with the [Function Navigator](interface/function-navigator.md).
- Place typed containers with the [Array Container](widgets/array-container.md).
- Organize complex panels with the [Selection Pane](interface/selection-pane.md).
- Customize the project icon in the [Icon Editor](interface/icon-editor.md).
