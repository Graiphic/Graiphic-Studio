# Color Tools

Graiphic Studio uses three coordinated Front Panel color tools: Eyedropper,
Color, and Brush.

## Foreground And Background

The overlapping swatches store foreground and background colors. Foreground is
normally the fill or body color; background is normally the border, grid, or
secondary surface. The exact mapping depends on the target.

Click a swatch to select it. The toolbar icon remains geometrically stable;
only the colors change. Transparency appears as a checkerboard preview.

## Color Navigator

Click the color control to open the movable Color Navigator. It supports visual
selection, HSV and RGB entry, hexadecimal color, opacity, transparency,
eyedropper sampling, Default, OK, and Cancel.

Transparency is a state for the selected swatch. Switching to the other swatch
does not cancel it. Editing a color control resumes normal color mode for that
swatch.

## Eyedropper

Eyedropper samples from the Front Panel or elsewhere on screen. When a target
contains foreground and background information, both are recovered. A target
with only one color supplies that color to both swatches. After sampling, Brush
becomes active.

## Brush

Brush applies the current colors to a compatible surface. Examples include:

- Front Panel background and grid
- widget body and border
- Boolean or Text Button current-state surface
- Numeric increment/decrement body and triangle
- label text and label background

Locked objects reject Brush changes. Color operations participate in undo.

Press `Escape`, choose the pointer tool, or right-click to leave an active color
tool.
