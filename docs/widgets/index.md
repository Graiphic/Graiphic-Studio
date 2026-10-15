# Widgets

Choose a Control to supply a value, an Indicator to display a result, or a
visual element to explain the interface. The Widget Navigator places them on
the Front Panel and projects participating values into typed Diagram terminals.

## Choose a widget

| Need | Widget guide |
| --- | --- |
| Enter or display numbers; choose a representation | [Numeric](numeric.md) |
| Enter or display True/False | [Boolean and Text Button](boolean-and-button.md) |
| Enter text or a filesystem path | [String and Path](string-and-path.md) |
| Choose from named items | [Ring and Enum](ring-and-enum.md) |
| Edit a timestamp | [Timestamp](timestamp.md) |
| Repeat one element type | [Array](array-container.md) |
| Combine fields of different types | [Cluster](cluster.md) |
| Carry status, code, and error source | [Error Cluster](error-cluster.md) |
| Inspect a Variant payload | [Variant](variant.md) |
| Display a U32 pixel array | [Picture Display](picture-display.md) |
| Display a numeric dataset as plots | [Waveform Graph](waveform-graph.md) |
| Place a decorative image | [Image Static](image-static.md) |
| Add explanatory text | [Label](label.md) |

## Shared behavior

A widget's label is separate from its value text. Move a detached label back
near its default anchor to reconnect it. Most widgets support visibility,
selection, locking, context menus, and undoable layout/appearance changes.
Resize behavior depends on the type: some values fit their text automatically,
while Arrays expose a viewport and repeated cell template.

A locked widget rejects design edits while retaining its admitted value behavior.
A hidden widget stays in the document and [Selection Pane](../interface/selection-pane.md).

## Roles and bindings

Controls publish values to the graph; Indicators receive values. Use the
object's context menu to change its role where supported. For public interface
bindings, Controls connect toward inputs and Indicators from outputs. The
[Interface Map](../interface/interface-map.md) arranges those ports visually.

## Containers and types

An Array repeats one shared element design and retains distinct cell values.
A Cluster combines ordered fields with stable identities. Moving a label or a
field's visual position does not change its type identity. Use the container
guides for selection, nesting, transfer, and autosizing.

The public FROG Default realization supplies integrated widget defaults. The
saved document records authored placement and instance overrides. Editor
rendering does not by itself establish target-runtime support for that value.
Read [current capabilities](../reference/development-checkpoint.md) when running
or exchanging a document.
