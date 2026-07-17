# Widget Navigator

The Widget Navigator browses widget families and starts placement on the Front
Panel. It can appear temporarily at the pointer or remain open as a pinned tool
window. Popup dimensions follow their content and the active monitor work area.

The root view groups the current widget families into compact, scannable tiles.

![Widget families in the dark Widget Navigator](../../assets/screenshots/widget-navigator/widget-families-dark.png)

The same hierarchy and spacing rules remain available in the Light theme.

![Widget Navigator in the Light theme](../../assets/screenshots/front-panel/widget-navigator-light.jpg)

## Families

Current families include Numeric, Boolean, String and Path, Ring and Enum, and
Data Containers. Family tiles use rows of three where space allows and carry a
visual symbol for fast scanning.

Single-click a family to browse its folder. Double-click the family tile to
start placement of its default widget:

- Numeric places Numeric Control.
- Boolean places Text Button.
- String and Path places String Control.
- Ring and Enum places Ring Control.
- Data Containers places Array.

This separation keeps folders navigable: opening a family never places a
widget by accident. Once placement starts, a semi-transparent preview follows
the pointer. Click the Front Panel to commit it or press `Escape` to cancel.

## Controls And Indicators

A **Control** accepts interaction and provides a value. An **Indicator**
displays a value and omits command-only affordances. For example, Path Control
has a browse button while Path Indicator does not.

Ring and Enum share one family because both expose a named selection backed by
a value. Its submenu contains Ring Control, Ring Indicator, Enum Control, and
Enum Indicator.

## Place Or Cancel

After choosing a widget, its preview follows the pointer until the Front Panel
is clicked. Press `Escape` to cancel. Repeated default labels receive numeric
suffixes so every object stays identifiable.

Click outside an unpinned Navigator, press `Escape`, or begin another command
to close it. Pinning turns it into a persistent window with the standard
Graiphic Studio close button.

Pinned Navigators are independent: opening another Navigator does not close an
existing pinned window. A pinned window can be resized, and its tiles reflow to
the available width while preserving the active interface font scale.

Vertical or horizontal scrollbars appear only when the resized client area can
no longer display all tiles. A child family window remains above its owning
Navigator while that hierarchy is active.

Pinned Widget Navigators belong to the Front Panel workspace. They hide when
the Block Diagram receives focus, then return at their previous positions when
the Front Panel is raised. The restored windows remain interactive, including
drag-and-drop placement. See [Window Workflow](window-workflow.md).
