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
the source-owned numeric type. A new Numeric widget uses **Float64** (`F64`) by
default, so it accepts signed and fractional values.

The first page contains the 16 standard representations:

| Family | Canonical types | Compact codes | Color |
| --- | --- | --- | --- |
| Floating point | Float16, BFloat16, Float32, Float64 | F16, BF16, F32, F64 | Orange |
| Signed integer | Int8, Int16, Int32, Int64 | I8, I16, I32, I64 | Blue |
| Unsigned integer | UInt8, UInt16, UInt32, UInt64 | U8, U16, U32, U64 | Cyan |
| Complex | Complex\<Float32\>, Complex\<Float64\> | CF32, CF64 | Red |
| Parametric | FixedPoint\<...\>, Decimal\<precision,scale\> | FXP, DEC | Purple, brown-orange |

Select **Advanced** to replace that grid with nine specialized choices. The
switch changes to **Standard** so the main set can be restored in place.

| Group | Canonical types | Compact codes |
| --- | --- | --- |
| Low precision / AI | Int4, UInt4, Float8E4M3, Float8E5M2 | I4, U4, F8P, F8R |
| Extended precision | Int128, UInt128, Float80, Float128 | I128, U128, F80, F128 |
| Arbitrary precision | BigUInt | BIGU |

`F8P` identifies the precision-oriented E4M3 layout. `F8R` identifies the
range-oriented E5M2 layout. BigInt and BigDecimal are not part of the current
Studio menu.

The selected tile receives a high-contrast outline in both themes. Changing
the representation updates the Front Panel widget, its Diagram terminal, an
Array terminal when the widget is encapsulated, and any bound Interface Map
terminal immediately. Terminal and binding colors follow the selected numeric
family. Decimal uses `#B45309`.

The `.frog` source records the compact value type together with the explicit
representation contract, for example:

```json
{
  "valueType": "f64",
  "props": {
    "data_type.representation": "f64",
    "data_type.named_numeric_size": "Float64",
    "representation.kind": "float64"
  }
}
```

Representation selection is not hidden Studio state. The compact carrier,
canonical name, and descriptive kind must agree when more than one is present.
Runtime execution still depends on a validated FROG lowering and native ABI
corridor for the selected type; Studio reports unsupported types instead of
silently reinterpreting an executable graph.
