# Label Widget

Label places static text on the Front Panel. It is a support widget, not a
control or indicator, and it does not create a Diagram terminal.

Use Label for headings, annotations, units, and other text that belongs to the
interface layout but is not the caption or value text of another widget.

## Edit And Format

The text is source-owned and saved in the `.frog` document. Label supports
selection, movement, resize, visibility, lock, stacking order, undo, font
formatting, alignment, and text color through the normal Studio tools.

The Default Label `.wfrog` manifest supplies its initial dimensions, text, and
semantic SVG resource. The visible `text_value` part is distinct from the
Studio selection aura. Studio aligns hover and selection to the source-owned
`placement_bounds` and uses the manifest's 4 px aura band instead of deriving a
private rectangle from the rendered text.

## Related Text

A widget caption names that widget and moves with it. String value text is
editable or runtime-driven data. Label is independent static interface text.
