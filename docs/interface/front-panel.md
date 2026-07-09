# Front Panel

The Front Panel is the main visual editing surface in Graiphic Studio.

It contains the user-facing arrangement of widgets, labels, images, and design
elements. The Front Panel is source-owned by the `.frog` document.

## Grid

The Front Panel uses a grid to make placement predictable. Grid visibility and
snap-to-grid can be controlled from the Studio chrome.

The grid has a visible zero marker. Scrollbars are shown only when the current
view or placed content requires additional navigation.

## Selection

Objects can be selected directly on the Front Panel or through the Selection
pane.

Selected objects show an aura. Locked objects use a distinct locked aura and
cannot be moved, resized, recolored, grouped, or modified until unlocked.

## Move And Copy

- Drag an object to move it.
- Hold Shift while moving to constrain movement horizontally or vertically.
- Hold Ctrl while starting a drag to copy the object and move the copy.

## Resize

Widgets and visual elements expose resize handles when selected or hovered.
Very small widgets use fewer resize handles so that selection and movement stay
usable.

Holding Shift during resize preserves proportions.

## Labels

Widget labels may be anchored to the default label position. Moving a label away
detaches it from the anchor. Moving it back near the anchor snaps it into the
default position again.

Labels are independent text surfaces. Changing a widget value text must not be
confused with changing the widget label.
