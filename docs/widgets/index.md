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
- [Error Cluster](error-cluster.md)
- [Variant](variant.md)
- [Image Static](image-static.md)
- [Label](label.md)

## Where Widget Defaults Come From

Graiphic Studio consumes the public FROG Default realization package for each
integrated widget family. The `.wfrog` manifest supplies role-specific initial
properties and references the semantic SVG skin. The `.frog` document stores
the widget identity, placement, value, binding, and explicit instance
overrides.

`placement_bounds` is the authored envelope used by Studio for placement,
hover, selection, and hit testing. The visible widget body is inset by the
manifest's `layout.aura_band_px`; the current Default profiles use 4 px. A
skin's `focus_ring` is keyboard-focus geometry and is not the Studio selection
aura.

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
