# Widget Navigator

The Widget Navigator browses widget families and starts placement on the Front
Panel. It can appear temporarily at the pointer or remain open as a pinned tool
window. Popup dimensions follow their content and the active monitor work area.

![Ring and Enum family in the Widget Navigator](../../assets/screenshots/widget-navigator/ring-enum-family.png)

## Families

Current families include Numeric, Boolean, String and Path, and Ring and Enum.
Family tiles use rows of three where space allows and carry a visual symbol for
fast scanning.

Clicking a family opens its choices. Clicking a family as a direct placement
action chooses its default widget:

- Numeric places Numeric Control.
- Boolean places Text Button.
- String and Path places String Control.
- Ring and Enum places Ring Control.

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
