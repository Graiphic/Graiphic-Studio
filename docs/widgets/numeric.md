# Numeric Widget

The Numeric widget displays or edits a numeric value.

## Variants

- Numeric Control
- Numeric Indicator

## Visible Items

The Numeric widget can show or hide:

- Label
- Increment/Decrement controls

Increment/Decrement controls may be placed on the left or right. Selecting the
currently active side again hides them.

The control accepts direct value editing. The indicator presents the value
without offering input interaction.

## Resize

Numeric widgets resize horizontally. The label follows its default anchor while
it remains anchored.

The height is fixed for the compact numeric style. Resize Objects marks this
dimension with an asterisk rather than pretending the widget can change it.

Brush can recolor the numeric body and border. The increment/decrement pair is
one linked surface: its rectangle and triangle expose fill and border mappings.

## Context Menu

Numeric widgets expose a context menu for visible items and control/indicator
switching.

## Numeric Representation

Open the Numeric widget context menu and choose **Representation** to select
the source-owned numeric type. The submenu uses the same compact type symbols
for controls and indicators:

| Family | Representations | Interface Map color |
| --- | --- | --- |
| Floating point | EXT, DBL, SGL | Orange |
| Fixed point | FXP | Purple |
| Signed integer | I64, I32, I16, I8 | Blue |
| Unsigned integer | U64, U32, U16, U8 | Cyan |
| Complex | CXT, CDB, CSG | Red |

The selected tile receives the standard FROG selection outline. Changing the
representation updates the widget instance and any bound Interface Map terminal
immediately. The terminal therefore keeps the same type color as the Numeric
representation it exposes.

The `.frog` source records the compact value type together with the explicit
representation contract, for example:

```json
{
  "valueType": "u16",
  "props": {
    "data_type.representation": "u16",
    "data_type.named_numeric_size": "U16",
    "representation.kind": "uint16"
  }
}
```

Representation selection is not hidden Studio state. Runtime execution still
depends on a validated FROG lowering and native ABI corridor for the selected
type; Studio does not silently reinterpret unsupported executable graphs.
