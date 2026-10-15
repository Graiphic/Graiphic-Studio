# Picture Display

Picture Display shows a rank-2 U32 pixel array, with one pixel per cell. Use it
for explicit pixel data; use [Image Static](image-static.md) for a decorative
image placed on the design surface.

Resizing preserves existing pixels and adds zero-valued pixels where the array
grows. It does not scale or interpolate the existing picture. Its pixel-array
value is separate from the widget's label and visual frame.

Picture Display is a typed Indicator. A visible picture does not certify a
particular image codec, graph operation, or target-runtime path. Consult
[current capabilities](../reference/development-checkpoint.md) for the current
execution boundary.
