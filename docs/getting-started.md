# Getting Started

This page describes the first path through Graiphic Studio.

## 1. Open Graiphic Studio

Launch Graiphic Studio and start from the Front Panel. The Front Panel is the
main design surface for placing controls, indicators, labels, images, and
interface-related editing affordances.

The current launch path opens the Front Panel. Diagram editing is not required
for this first workflow.

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

## Next Steps

- Learn the [Front Panel](interface/front-panel.md).
- Learn the [Interface Map](interface/interface-map.md).
- Learn how widgets are organized in the [Widget Navigator](interface/widget-navigator.md).
- Organize complex panels with the [Selection Pane](interface/selection-pane.md).
- Customize the project icon in the [Icon Editor](interface/icon-editor.md).
