# String and Path

Use String for text and Path for a filesystem-style path. Both have Control and
Indicator roles. Their value text and separate widget label can be formatted
independently.

## String

Double-click the Control's value area to edit text. An Indicator displays data
without accepting input. Resize the text area and use its context menu for the
available display, wrapping, single-line, and scrollbar options. Scrolling
changes the view rather than the stored text.

**Dropdown String** exposes named text choices while retaining a String value.
Its item configuration is separate from Enum's typed domain or Ring's numeric
values.

## Path

Edit a Path Control directly or use its browse button. A Path Indicator is
read-only and omits the browse button. Changing the field's dimensions does not
change the path or access the file it names.

## Diagram constants and sizing

String/Path Diagram constants retain their explicit type and value. Where
**Size to Text** is enabled, fitting follows value and typography changes in
both directions. Returning to a smaller font can shrink the fitted field.
Manual handles remain subject to the field's minimum geometry and current mode.

A container's viewport and the embedded field's dimensions are separate. A
nested field keeps its own bounds when the enclosing Array or Cluster grows.

## Create a typed peer

The current Dropdown String menu provides one **Create Constant / Create
Control / Create Indicator** trio. Creation makes a separate object and
preserves the original's value and configuration; it is separate from
**Change to Control / Indicator**. Explicit nested targets preserve their type.

The latest menu changes are compiled in the 15 October checkpoint, with their
new regression cases still unexecuted. See
[current capabilities](../reference/development-checkpoint.md).

## Related functions

[String functions](../functions/string/index.md) ·
[Path functions](../functions/path/index.md)
