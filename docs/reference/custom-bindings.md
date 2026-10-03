# Custom Binding Persistence

Status: implementation reference for Graiphic Studio **0.0.3.161**, checked on
19 September 2026. This page describes the data saved by Studio and its current
compatibility boundary.

## Which `.frog` Format?

Studio's default Readable authoring writer saves `"format": "frog.document.draft"`
with `"draft_revision": 2`. Opt-in Automatic/Compact numeric storage uses private
revision 3; see [FROG Properties](../interface/frog-properties.md). A `.frog`
extension alone does not identify canonical
FROG source, whose envelope uses `spec_version`. These version numbers are
independent from Custom layout descriptor versions.

The public [FROG source compatibility contract](https://github.com/Graiphic/FROG/blob/main/Expression/Source%20compatibility%20and%20profiles.md)
owns that distinction. Custom save/reopen support in Studio does not establish
canonical writer conformance or support in another editor or runtime.

## Saved Fields

| Location in a Studio document | Meaning |
| --- | --- |
| `interface.map.binding_map_profile` | `custom_v1`, the Studio Custom profile identifier. It remains this value for all three descriptor versions below. |
| `interface.map.layout_pattern_id` | Versioned descriptor containing logical dimensions, stable slot count and, when present, disabled slots or explicit positions. |
| `icon.svg` | Editable SVG. Its root `data-frog-custom-layout` attribute carries the matching descriptor; `viewBox` carries the logical canvas dimensions. |
| Widget `binding.interface_map_slot` | Stable slot identity such as `custom_1`. |
| Widget `binding.public_input_id` or `public_output_id` | Public port associated with the widget; distinct from the visual slot identity. |

The active layout travels with the document. The user's saved pattern library
is a local convenience, not a dependency required to reopen that document.
Toolbar pixels, striped drop zones, hover, capture and the closed-hand cursor
are not saved as layout data.

## Descriptor Versions

Descriptors are decimal integers separated by underscores, with these forms:

```text
custom_v1_W_H_N
custom_v2_W_H_N_D1_D2_...
custom_v3_W_H_N_P1_P2_..._PN
```

- `W` and `H` are logical diagram dimensions, each from 32 through 1024.
  This is the legacy descriptor reader's range. Current Custom authoring accepts
  at most 128 px per side; larger existing descriptors can be read and preserved
  without silently rewriting their dimensions.
- `N` is the number of stable slot identities, from 2 through 252. It includes
  disabled slots. It is not necessarily the active count shown by **Bindings**.
- `v1` uses the automatic layout and enables every slot.
- `v2` retains automatic positions and lists disabled one-based slot numbers.
  That list is nonempty, strictly increasing, unique, and within `1..N`.
- `v3` stores exactly `N` explicit perimeter positions. A nonnegative `Pi`
  enables slot `custom_i` at offset `Pi`. A negative `Pi` disables it and retains
  offset `-Pi - 1`. For example, `-100001` means disabled at offset `100000`.

The visible active count can be **zero**: the saved descriptor still retains
at least two identities, all disabled. Removing a slot does not renumber other
slots. Adding slots first reuses disabled identities when available and keeps
existing active positions.

### Perimeter Coordinates

An offset is measured in **thousandths of a logical pixel**, starting at the
bottom-left corner and travelling clockwise: up the left edge, across the top,
down the right edge, then back along the bottom. Screen coordinates have their
origin at the top-left, with Y increasing downwards.

For `P = 2 * (W + H) * 1000`, each decoded offset must satisfy `0 <= s < P`.
Corner offsets are `0`, `H * 1000`, `(H + W) * 1000` and `(2 * H + W) * 1000`.
Disabled positions stay in range but do not reserve space.

The current Studio rules for active explicit positions require:

- at least **6 logical pixels** from every corner along the perimeter;
- at least **8 logical pixels** between active centres along the perimeter,
  including across the perimeter origin;
- no more active positions than the geometric capacity or the 252-slot limit.

Exactly the minimum spacing is allowed. Invalid moves, dimensions or additions
do not commit a partial layout. The number that can be added to an existing
layout can be smaller than the capacity of an empty border, because existing
active positions stay fixed.

For an empty side of length `L`, capacity is `1 + floor((L - 12) / 8)`.
The total is `min(252, 2 * (sideCapacity(W) + sideCapacity(H)))`: a 40 × 40
border can therefore hold 16 active positions. These are Studio geometry and
resource limits, not limits on the FROG language's public interface.

## Example With A Disabled Slot

This valid JSON excerpt illustrates the fields; it is not a complete program:

```json
{
  "format": "frog.document.draft",
  "draft_revision": 2,
  "interface": {
    "map": {
      "binding_map_profile": "custom_v1",
      "layout_pattern_id": "custom_v3_40_40_3_20000_60000_-100001"
    }
  },
  "icon": {
    "svg": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 40 40\" data-frog-custom-layout=\"custom_v3_40_40_3_20000_60000_-100001\"/>"
  }
}
```

It retains three slot identities and displays two active slots:

| Slot | Position | State |
| --- | --- | --- |
| `custom_1` | Left midpoint `(0, 0.5)` | Active |
| `custom_2` | Top midpoint `(0.5, 0)` | Active |
| `custom_3` | Right midpoint `(1, 0.5)` | Disabled |

A control assigned to the first slot carries a separate binding object:

```json
{
  "binding": {
    "mode": "widget_value",
    "public_input_id": "numeric_control",
    "interface_map_slot": "custom_1",
    "connection_requirement": "recommended"
  }
}
```

An indicator uses `public_output_id`. The matching public port and widget must
also exist in the full document. A slot alone does not declare a typed port.

## Editing And Compatibility

Studio 0.0.3.161 reads `v1`, `v2` and `v3`. Existing automatic layouts keep their
established positions when reopened. Moving or removing a slot materializes
explicit positions and writes `v3`; resizing keeps normalized positions when
the new dimensions satisfy the placement rules. The SVG and map descriptors
are written together. An attribute inside a nested imported SVG is not the
document's Custom layout metadata.

Explicitly removing a slot clears that slot's widget association when the edit
is applied; it does not transfer it to another slot. Other slot identities and
associations remain intact. **Reset** restores the layout present when the
dialog opened; **Cancel** discards the dialog's changes. Switching to a standard
format is rejected if that format cannot retain the existing associations.

An older reader's support must be checked separately. The unchanged
`binding_map_profile: "custom_v1"` string is not evidence that it understands a
`custom_v3_...` descriptor. Do not convert an unfamiliar descriptor to an
automatic layout or discard disabled identities while claiming faithful
preservation. Canonical cross-tool support for these particular Studio
descriptors has not been established by this delivery.

## Custom Rotation And Flips (Prepared, Not Yet Released)

The change prepared on 19 September 2026 enables **Rotate 90 Degrees**,
**Flip Horizontal** and **Flip Vertical** for the active Custom layout.
It keeps the canvas width, height and icon drawing unchanged, matching the
standard binding-pattern commands. With normalized top-left coordinates:

| Command | New position |
| --- | --- |
| Rotate 90 Degrees, clockwise | `(1 - y, x)` |
| Flip Horizontal | `(1 - x, y)` |
| Flip Vertical | `(x, 1 - y)` |

The transformed layout uses explicit `custom_v3` offsets at the existing
0.001-pixel precision. Both the map descriptor and root SVG metadata are
updated. Slot identities, disabled slots and widget/public-port associations
stay attached to the same bindings. Undo/Redo restores the matching map and
SVG metadata. The saved pattern library remains separate from the active
document.

The same corner-clearance and spacing rules apply after transformation. On a
rectangle, a quarter-turn can move many bindings onto a shorter side; **Rotate
90 Degrees** is disabled if the resulting positions would be invalid. The
command also rejects an invalid transformation without a partial edit.

At the historical checkpoint, this addition was not included in 0.0.3.174.
That is not the current delivery version; see the
[development checkpoint](development-checkpoint.md) for present qualification limits.
The geometry/model checks passed 44,456 assertions. Native integration tests
have been added and syntax-checked but have not yet run against a rebuilt
application; final build and visual validation remain pending.

## Previous Delivery Evidence

The 0.0.3.161 delivery passed `frog-win32-custom-icon-smoke`, including descriptor
decoding, malformed-position rejection, move/remove identity preservation,
SVG reload, document save/reload, binding assignments and saved-file versus
live-drag call anchors. Its neighboring tests and real-application Custom
preview scenario also passed. This is implementation evidence for Studio;
it is not a public-format conformance or runtime certification claim.

See [Interface Map](../interface/interface-map.md) for binding actions and
[Icon Editor](../interface/icon-editor.md) for size and preview controls.
