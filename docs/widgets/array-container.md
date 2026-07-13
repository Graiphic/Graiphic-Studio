# Array Container

Array is a typed Front Panel container. It repeats one embedded widget template
over one or more dimensions while keeping one coherent array value in the
`.frog` document and runtime.

The canonical runtime example below shows two dimensions, three visible rows,
numeric cells, connected index displays, and scrollbars for content outside the
visible extent.

![Numeric Array dimension runtime example](../../assets/screenshots/widgets/array-dimension-runtime.png)

## Create And Type An Array

Place **Data Containers > Array** from the Widget Navigator. A new Array starts
as a one-dimensional empty container. Drag a supported widget into its content
region to define the element template. Numeric, String, Path, Boolean, Text
Button, Enum, and Ring templates preserve their own value and appearance rules.

All cells in one Array use the same embedded widget template. Resizing the
template changes the cell size; resizing the Array changes how many rows and
columns are visible.

The focused two-dimensional view makes the separation between index controls,
typed cells, and scrollbars explicit.

![Two-dimensional Numeric Array with indices and scrollbars](../../assets/screenshots/widgets/array-numeric-2d.png)

## Dimensions And Indices

Each dimension has a compact numeric index display. Indices are interactive:
type a coordinate or use increment and decrement to choose the visible slice.
The dimension controls use the same immediate interaction behavior as a Numeric
widget.

A one-dimensional Array displays one axis. Starting at two dimensions, the
Array displays a row-and-column grid; additional dimensions select higher-order
slices through their index displays.

Extending an Array coordinate extends its dense shape. Missing positions before
the new coordinate receive the embedded widget's default value instead of
remaining visually active but absent.

## Edit Cells

An active cell behaves like its embedded widget. Numeric cells accept text,
increment and decrement, representation options, context-menu actions, and
color editing. Showing the embedded label adds label space inside every visible
cell and therefore changes row layout.

Selecting a cell targets the embedded widget. Selecting the surrounding frame
targets the Array container. The two targets intentionally expose different
resize, visibility, color, and context-menu actions.

## Resize And Scroll

The Array frame provides independent controls for visible rows and columns.
Scrollbars appear only when the current shape extends beyond the visible grid.
Their ranges follow the array shape and selected higher-dimensional slice.

Array background and border colors belong to the container. Cell body, border,
spinner, label, and text colors belong to the embedded widget template.

## Runtime Contract

The Studio edits source-owned dimensions, shape, values, visible counts,
indices, template properties, and instance styling. The runtime consumes that
same Array value and applies the behavior demonstrated by the reference
examples; the editor does not invent a second array model for display purposes.
