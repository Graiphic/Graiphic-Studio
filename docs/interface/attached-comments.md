# Attach a diagram comment

A free comment can point to a function, wire or structure through a persistent
annotation arrow. Each comment has one target; multiple comments can share
that target.

1. Hover over the comment to reveal its attachment handle.
2. Click the handle and then the intended object, or drag the handle to it.
3. Check the highlighted target and arrow preview before completing the action.

Escape or an invalid destination preserves the previous association. Use the
handle again to choose another target. **Detach Label From Object** in the
context menu removes the association while keeping the comment and its text.

The arrow remains visible outside selection and follows the target when it
moves or resizes. A wire attachment belongs to the identified branch, rather
than whichever wire is later closest. A comment outside a structure may point
to an object inside without creating a data tunnel.

Text editing, resizing, movement and Undo/Redo remain comment operations.
Save the `.frog` to retain the association. The arrow carries no data and does
not participate in execution dependencies, typing or wire routing.

The recorded correction was checked against functions, structures and branches
in Dark/Light at 75%, 100% and 150% zoom, at 96 DPI. Separate native checks kept
the same results before and after annotation and reopening; this does not
certify every Windows display scale.

[Block Diagram](block-diagram.md) · [Label](../widgets/label.md) ·
[Current capabilities](../reference/development-checkpoint.md)
