# Front Panel

The Front Panel is the main visual editing surface in Graiphic Studio. It
contains the user-facing arrangement of widgets, labels, images, and design
elements. The `.frog` document owns this layout.

![Front Panel overview](../../assets/screenshots/front-panel/front-panel-overview.png)

## Main Areas

The title bar identifies the current document. The menu bar contains file and
editing commands. The toolbar groups execution controls, selection and color
tools, arrangement tools, and text formatting. The blue status bar keeps view
controls such as grid visibility, snapping, and zoom close to the canvas.

## Grid And Navigation

The grid makes placement predictable and includes a visible origin marker.
Grid visibility and snap-to-grid are independent controls.

Scrollbars are computed from the viewport and placed content. Removing the
object furthest from the origin reduces the unnecessary empty range. When all
content fits, scrollbars are hidden. Use the middle mouse button to pan freely;
scrollbars appear when the resulting view needs them.

## Select, Move, And Copy

Select objects directly or through the [Selection Pane](selection-pane.md).
Hold `Shift` while clicking to build a multiple selection. Hovering previews an
object aura at reduced opacity; selection shows the full aura.

Drag an object to move it. Hold `Shift` to constrain the first movement axis.
Hold `Ctrl` through a drag to move a duplicate. Releasing `Ctrl` before the drop
cancels the duplicate operation.

## Resize

Drag a handle to resize. Hold `Shift` to preserve proportions. Handle density
adapts to displayed size: compact widgets use fewer handles so the pointer can
still reach the body, while larger objects expose the complete set.

## Labels

Widget labels and widget values are separate text surfaces. A widget label can
remain attached to its magnetic default anchor or be positioned freely. Moving
a detached label back near its default location reconnects it.

Double-click an empty area to create a free label. The placeholder `Write your
text here` is selected immediately and disappears when typing starts. `Enter`
validates; `Shift+Enter` inserts a line break. An empty label is removed instead
of being kept as an invisible object.

## Editing Protection

Lock prevents layout edits without disabling the widget at runtime. A locked
widget can still operate as a control or indicator, but it cannot be moved,
resized, recolored, regrouped, or edited until unlocked.

See [Arrange and Resize](arrange-and-resize.md) and [Color Tools](color-tools.md).
