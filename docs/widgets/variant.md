# Variant

The Variant widget inspects a retained payload without turning it into a set of
Numeric, Boolean, String, or Cluster child controls. Its Control/Indicator role
determines the direction of its Variant Diagram terminal.

## Inspect the value

Place **Variant** from **Data Containers**. Its rectangular text area supports
resizing and scrolling; its label remains independently movable and editable.

| Menu action | Result |
| --- | --- |
| Visible Items > Label / Caption | Show or hide the corresponding text surface |
| Visible Items > Scrollbar | Show or hide scrolling tracks |
| Show Type | Display available type information |
| Show Data | Display or hide retained payload text |
| Find Terminal | Locate the paired Diagram terminal |
| Change to Control / Indicator | Change the top-level role |
| Properties | Edit inspection preferences |

Defaults show data and scrollbars, with type display off. An empty value has a
blank inspection area. Hiding nonempty data retains a short size summary.
Scrolling and resizing do not edit the payload. Arrays and Clusters use the
same inspection surface for contained Variants.

## Wire a typed value

A terminal declared `Variant` accepts a typed value directly. The small red
coercion dot at the receiving terminal identifies where Studio wraps the value
with its type. A wire that already carries a Variant connects directly. To
recover a payload, supply its expected type to **Variant To Data**. A cluster
retains its fields, and an array retains its element type and shape.
[Variant To Data](../functions/variant/to_data.md) · [Queue and error-cluster example](../interface/error-variant-loop.md).

Older documents can contain opaque display text. For that representation,
**Show Type** reports that the contained type is unavailable.

The visible preview is limited to **16 KiB**, ending at a UTF-8 character boundary.
Truncation is identified and affects the display only, preserving the stored
payload. The preview is not a reversible typed serialization format.

## Save and execution

Inspection settings and retained payload belong to the Studio draft document;
scroll offsets are temporary view state. These fields do not define a public
FROG Variant encoding or cross-tool conformance.

Consult the [Variant function pages](../functions/variant/index.md) for the
ports and supported operations, including reading and writing attributes.
