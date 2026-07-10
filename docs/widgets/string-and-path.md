# String And Path Widgets

String and Path widgets edit or display textual data.

## String

String widgets support control and indicator roles. The widget value text is
separate from the widget label.

String widgets support resizing, label anchoring, and color editing for the body
surface.

Double-click the value area to edit it. Formatting a selected label does not
change the value text, and formatting the value does not change the label.

## Path

Path widgets represent filesystem-style paths.

Path Control can expose a browse button. Path Indicator does not expose a
browse button because it is display-only.

Path text can be edited directly when the widget is a control.

Path Control follows the source-backed path value and opens the system browse
flow from its button. Path Indicator is display-only and therefore has no browse
button. Both use the same horizontal resize and label-anchor rules as String.
