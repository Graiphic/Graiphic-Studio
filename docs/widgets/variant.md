# Variant

Historical implementation note: inspector work was prepared on 19 September
2026 with native build/interaction qualification pending on that date. The then
delivered executable was 0.0.3.174. Current local delivery is 0.0.4.044; see the
[development checkpoint](../reference/development-checkpoint.md). This older
inspector note does not establish current native or runtime qualification.

## Front Panel Inspector

**Variant** in the Widget Navigator's **Data Containers** category places one
widget. Its prepared appearance is a rectangular text inspection area, inspired
by the supplied LabVIEW references. The display does not create Numeric,
Boolean, String or Cluster child controls from the payload.

The new placement size is approximately 182 × 91 logical pixels at 100% zoom.
Existing documents retain their authored dimensions. The rectangle uses Studio's
text surfaces and scrollbars; the label remains independently editable and
movable. The shared eight resize handles change the widget bounds only.

| Menu action | Effect |
| --- | --- |
| Visible Items → Label | Show or hide the widget label. |
| Visible Items → Caption | Show or hide an independent presentation caption. |
| Visible Items → Scrollbar | Show or hide horizontal and vertical scrolling tracks. |
| Show Type | Show the available type information. |
| Show Data | Show or hide the retained payload text. |
| Find Terminal | Locate the associated Block Diagram terminal. |
| Change to Control / Indicator | Change the top-level widget's interface direction. |
| Properties | Edit label visibility and inspection preferences. |

Defaults match the provided menu reference: **Show Data** and **Scrollbar** on,
**Show Type** off. The empty widget has a blank inspection area. Hidden nonempty
data retains a brief size summary. Wheel scrolling, scrollbar movement and
resizing do not edit the payload. Display changes support Undo/Redo and save/reopen.
Variants used inside Arrays and Clusters use the same inspection surface.

## Current Data Boundary

The current Studio authoring model preserves a Variant payload as opaque text.
It does not yet provide a complete typed Variant value model with an independent
attribute dictionary. For an opaque nonempty payload, **Show Type** therefore
reports that the contained type is unavailable. The inspector never infers I32,
String or another type merely from the text's spelling.

The visible preview is limited to 16 KiB, ending on a UTF-8 character boundary;
truncation is identified in the view and never applied to the stored payload.
The preview text is not a reversible typed serialization format.

The Variant function palette currently declares authoring ports; its manifest
does not advertise a runtime implementation. This widget work does not certify
`To Variant`, `Variant To Data`, attribute operations or LabVIEW-compatible
conversion behavior. A generic editor, payload replacement by drag-and-drop,
typed empty values and resource/reference inspection need their own shared
data contracts and tests.

## Studio Document Fields

These properties belong to Studio's existing draft authoring format:

| Widget property | Meaning |
| --- | --- |
| `props["variant.payload"]` | Existing opaque payload text, preserved unchanged by inspection. |
| `props["variant.show_type"]` | Optional view preference; defaults to `false`. |
| `props["variant.show_data"]` | Optional view preference; defaults to `true`. |
| `props["variant.scrollbar_visible"]` | Optional view preference; defaults to `true`. |

Scroll offsets are transient UI state. The widget and wire type remain `variant`.
These fields do not establish a canonical FROG Variant encoding or cross-tool
conformance. No new payload schema is inferred from the illustrative JSON in
the supplied design report.

## Verification Status

The standalone inspection model passes **146 assertions**, covering default
visibility, opaque data preservation, hidden-data summaries and bounded UTF-8
previews. The production catalog generator accepts the new dimensions.
Both Front Panel and Icon Editor source ownership checks pass. MSVC syntax
analysis passes; this does not replace a linked native build.

Native regression coverage has been added for menus, save/reload, Undo/Redo,
scrolling, resizing, roles, run guards and Array cell preservation. It remains
unexecuted until the canonical build is unblocked; screenshots of the completed
application are still required before delivery.
