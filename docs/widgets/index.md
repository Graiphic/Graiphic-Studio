# Widgets

Widgets are the reusable visual elements placed on the Front Panel.

A widget may be a control or an indicator:

- A control provides a value to the program or public interface.
- An indicator displays a value produced by the program or public interface.

Widget labels are separate from widget value text.

Controls can bind to public inputs. Indicators can bind to public outputs. The
role is a source-level property and can be changed from a widget context menu
where the widget supports both roles.

## Current Core Widgets

- [Numeric](numeric.md)
- [Boolean and Text Button](boolean-and-button.md)
- [String and Path](string-and-path.md)
- [Ring and Enum](ring-and-enum.md)
- [Array Container](array-container.md)
- [Image Static](image-static.md)

## Common Behavior

Most widgets support:

- label visibility
- control/indicator switching where meaningful
- resize handles
- context menu actions
- selection aura
- lock/unlock protection
- color editing when the widget exposes visual surfaces
- undoable movement and appearance changes
- magnetic default label anchoring

Locked widgets keep their value behavior but reject layout and appearance
editing. Hidden widgets remain in the `.frog` document and in the Selection
Pane even though they are not drawn on the Front Panel.
