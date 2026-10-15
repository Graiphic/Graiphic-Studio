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

## Current data boundary

The Studio authoring model preserves the payload as **opaque text**. It does
not provide a complete typed Variant value model with an independent attribute
dictionary. For a nonempty opaque payload, Show Type reports that its contained
type is unavailable; the inspector does not infer a type from the text spelling.

The visible preview is limited to **16 KiB**, ending at a UTF-8 character boundary.
Truncation is identified and affects the display only, preserving the stored
payload. The preview is not a reversible typed serialization format.

## Save and execution

Inspection settings and retained payload belong to the Studio draft document;
scroll offsets are temporary view state. These fields do not define a public
FROG Variant encoding or cross-tool conformance.

The [Variant function pages](../functions/variant/index.md) document declared
ports and operation-specific limits. This inspector does not certify typed
conversion, attribute operations, reference inspection, or another tool's
Variant behavior. See [current capabilities](../reference/development-checkpoint.md).
