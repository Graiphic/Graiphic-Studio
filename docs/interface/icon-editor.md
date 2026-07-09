# Icon Editor

The Icon Editor edits the `.frog` document icon.

The document icon is stored as SVG-oriented icon data. The 40 x 40 display is a
preview size, not a pixel limitation. SVG content remains vector-based and can
be displayed clearly at different sizes.

## Canvas

The editor uses a 40 x 40 working grid as a practical icon design reference.
The grid is the minimum interaction unit for pencil-style drawing, erasing, and
simple pixel-aligned edits.

Vector objects can move outside the visible grid while editing. The final
preview uses the visible icon region.

## Layers

Icon content is layer-based. Layers can be selected, moved forward or backward,
hidden, shown, copied, pasted, and deleted.

The default template layer is a normal layer. It can be selected, moved,
resized, edited, copied, or deleted like other layers.

## Tools

Current tools include:

- Pencil
- Line
- Eyedropper
- Fill
- Rectangle
- Ellipse
- Eraser
- Text
- Selection
- Move

The Fill tool recolors the target cell and the connected region of the same
color on the target layer.

## Templates

Templates are optional helper layers. Selecting a template adds it as a layer.
Templates must remain visible against the Studio theme, so transparent regions
are shown on the editor background rather than as unreadable white-on-white
tiles.

## Saving

Pressing OK writes the current icon preview back to the `.frog` document icon.
The icon should remain editable when reopened.
