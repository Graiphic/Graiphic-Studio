# Boolean And Text Button Widgets

Boolean widgets represent simple true/false state.

Text Button is a button-style boolean control or indicator with editable center
text.

## Boolean

Boolean widgets are command-style controls by default. They can be switched to
indicators.

Current visual forms:

- Square LED
- Circular LED

LED widgets use SVG geometry. Their default dimensions stay in the same visual
order of magnitude as Numeric and String widgets, while proportional resize is
available with `Shift`.

## Text Button

Text Button supports:

- label visibility
- control/indicator switching
- mechanical action
- text mode
- locked or editable center text
- state colors

## Text Mode

Text Mode controls whether the widget uses:

- Single text: one text value for all states.
- Multiple text: separate text per state.

Single keeps one shared text across ON and OFF. Multiple gives each state its
own editable text. Label formatting and center-value formatting are independent.

## Mechanical Action

Text Button can use press, release, switch, or latch actions. The action defines
when the Boolean value changes; it does not change the widget's public data type.

## Color

Boolean and Text Button widgets support color editing for visible state surfaces
and text where available.

Brush maps foreground to the displayed state's fill and background to its
border. Transparent colors are represented by the Studio checkerboard.
