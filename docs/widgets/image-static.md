# Image Static Widget

Image Static displays a static media asset.

It is intended for imported or pasted media that belongs to the Front Panel
layout.

Image Static is not the same as a data-driven Picture or Screen widget. A
Picture or Screen widget displays image data produced or loaded by the program.

## Media

Image Static can reference imported media. The `.frog` source should keep the
media relationship explicit so runtime and export flows do not depend on hidden
Studio-only state.

SVG imports remain vector-based. Raster media is preserved as image data and
can lose clarity when enlarged. Images support selection, proportional resize,
rotation, horizontal or vertical flip, stacking order, grouping, visibility,
lock, clipboard copy/paste, and undo.

The widget uses `frog.widgets.image_static`. Its Default `.wfrog` manifest
provides the initial bounds, 4 px aura band, and rectangular semantic SVG skin.
The document owns the imported `media_ref` and explicit instance overrides;
the image data is not embedded as an opaque Studio-only decoration or confused
with the data-driven Picture/Screen family.
