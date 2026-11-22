# Pane

Reference class `frog.pane`. [All classes](index.md) · [How to use Property and Invoke Nodes](../using-object-references.md)

Catalog value schema for this listing: target-dependent. A strict reference can supply a different schema.

## Properties

| Menu path | Saved ID | Connection | Access | Catalog availability |
| --- | --- | --- | --- | --- |
| Class ID | `identity.class` | `string` | Read | Editor |
| Class Name | `identity.class_name` | `string` | Read | Editor |
| Owner | `identity.owner` | `ref<"frog.object">` | Read | Editor |
| Owning FROG | `identity.owning_frog` | `ref<"frog.program">` | Read | Editor |
| Object ID | `identity.object_id` | `string` | Read | Editor |
| Colors › Background | `background_color` | `u32` | Read / Write | — · A separate Pane background service is not registered. |
| Owning Pane | `identity.owning_pane` | `ref<"frog.pane">` | Read | Editor |
| Controls[] | `controls` | `array<ref<"frog.control">>` | Read | Editor |
| Origin | `origin` | `cluster<"x":f64,"y":f64>` | Read / Write | — · The provider has no separate Pane-origin service. |
| Content Area Rect | `content_area_rect` | `cluster<"x":f64,"y":f64,"width":f64,"height":f64>` | Read | — · Measured Pane content bounds are not exposed. |

## Methods

No entries declared for this class.
