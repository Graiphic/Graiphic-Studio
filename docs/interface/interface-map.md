# Interface Map

The Interface Map is the square visual representation shown in the Front Panel
chrome. It represents the public `.frog` interface layout and keeps port
placement visible without turning it into hidden runtime behavior.

## Concepts

- **Interface Map**: the visual square showing the public interface slots.
- **Interface Layout Pattern**: the selected slot distribution pattern.
- **Front Panel binding**: the explicit source-level link between a widget value
  and a public interface port.
- **interface_input**: diagram-side projection of a public input port.
- **interface_output**: diagram-side projection of a public output port.

## Binding Workflow

1. Select a slot in the Interface Map.
2. The slot enters binding mode.
3. Click a compatible Front Panel widget.
4. The widget is bound to that slot.
5. The binding remains visible in the Interface Map.

Clicking a bound slot selects the bound widget and can re-enter binding mode so
the binding can be reassigned.

## Slot Colors

The Interface Map uses data-type colors rather than connection-status colors.

Current direction:

- Double: orange
- Integer: blue
- Boolean: green
- String: pink
- Path: blue-green
- Enum and Ring: integer blue

Required connections use an additional red edge indicator on the external edge
of the slot. Recommended and optional connections keep the normal slot display.

## Layout Patterns

Interface Layout Patterns define only the visual distribution of slots. They do
not define execution semantics.

When a pattern changes, existing bindings are preserved when possible. If the
new pattern has fewer slots, bindings that no longer have a slot are removed.
