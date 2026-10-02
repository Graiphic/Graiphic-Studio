# Icon Editor

The Icon Editor edits the `.frog` document icon. Open it by double-clicking the
document icon in the Front Panel chrome or choosing **Edit Icon...** from its
context menu.

The logical canvas size is independent of its toolbar preview. SVG remains
vector-based and is rendered cleanly at other sizes.

The editor keeps drawing tools, layers, reusable templates, colors, and the
preview visible in one workspace.

![Icon Editor with tools, layers, templates, and preview](../../assets/screenshots/icon-editor/icon-editor-dark.png)

## Canvas And Preview

The size selector offers 40 × 40, 60 × 40, 40 × 60, 60 × 60, and **Custom...**.
Custom allows 32 to 1024 logical pixels per side and a configurable binding
layout. Its striped tile identifies the custom format.

![Icon size selector with four presets and striped Custom tile](../../assets/screenshots/icon-editor/canvas-size-presets.png)

The working grid follows the selected dimensions. One grid cell is the minimum
Pencil and Eraser unit. Vector objects can move outside the visible region
while editing; only the icon region appears in Preview and in the applied
document icon.

The toolbar preview fits proportionally within 60 × 60 pixels. A Custom 40 × 40
icon fills that available preview area while its label continues to show
40 × 40. Enlarging the preview does not change the saved logical dimensions.
See [Interface Map](interface-map.md#custom-layouts) for binding placement,
striped acceptance zones, capacity and Reset.

Use View to choose a checkerboard or white editing background. This changes
the canvas background only. Zoom changes the editor view, not the SVG data.

## Layers

Content remains layer-based. Select a row, use its eye icon, drag it, or use the
arrow buttons to change visibility and stacking order. Layers can be copied,
pasted, nudged, resized, and deleted.

The Default Template and optional template layers follow the same interaction
rules as imported media and drawn objects. Layer metadata stays in the editable
SVG so work can continue after reopening the `.frog` document.

## Drawing Tools

- Pencil paints one-cell units on the selected layer.
- Line, Rectangle, and Ellipse create vector objects.
- Eyedropper samples a screen color into the active swatch.
- Fill replaces a connected region on the touched layer.
- Eraser removes cells from a layer without deleting that layer.
- Text creates an editable text object.
- Selection moves, resizes, copies, or deletes complete objects.

Fill uses four-directional connectivity. It changes the touched cell and every
connected cell of the same color on that exact layer; it never creates a second
layer for the fill result.

## Colors

The two swatches are independent quick colors. Click a swatch to activate it.
Double-click to open the single-color navigator. Drawing tools use only the
active swatch.

## Templates

Template tiles are optional helper layers. Activating a tile adds that template
to Layers. Templates remain non-destructive and can be moved, resized, hidden,
copied, reordered, or removed.

Reusable SVG glyph folders are managed through **Tools > Options... > Icon
Editor**. Adding a folder makes its SVG assets available to the local user
profile; removing the path from Options does not delete source files. See
[Studio Options](options.md).

## Import, Clipboard, And History

The File menu imports SVG or raster media. SVG stays vector-based. Clipboard
paste and drag-and-drop create an editable visual layer.

When an SVG is imported, Studio normalizes it as one logical layer while
flattening its visible paint regions for editing. Each independently visible
color region can therefore be filled without recoloring unrelated shapes such
as holes, facial details, or transparent areas. This is a general import rule,
not a special case for the default icon. The applied result remains SVG; the
toolbar preview does not rasterize it.

`Ctrl+Z` undoes; `Ctrl+Shift+Z` redoes. `Ctrl+Shift+Delete` clears all layers.
Press `Escape` to leave the current tool and return to selection without
closing the editor.

## Apply Or Cancel

**OK** writes the current Preview to the `.frog` icon and preserves editable
layer data. **Cancel** closes the editor without applying the session.

Custom geometry is also retained for reopening: dimensions, stable binding
identities, moved positions and disabled slots. The exact Studio fields and
the public-format boundary are described in
[Custom Binding Persistence](../reference/custom-bindings.md).
