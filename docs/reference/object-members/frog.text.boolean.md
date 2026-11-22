# Boolean Text

Reference class `frog.text.boolean`. [All classes](index.md) · [How to use Property and Invoke Nodes](../using-object-references.md)

Catalog value schema for this listing: target-dependent. A strict reference can supply a different schema.

## Properties

| Menu path | Saved ID | Connection | Access | Catalog availability |
| --- | --- | --- | --- | --- |
| Class ID | `identity.class` | `string` | Read | Editor |
| Class Name | `identity.class_name` | `string` | Read | Editor |
| Owner | `identity.owner` | `ref<"frog.object">` | Read | Editor |
| Owning FROG | `identity.owning_frog` | `ref<"frog.program">` | Read | Editor |
| Object ID | `identity.object_id` | `string` | Read | Editor |
| Bounds › All Elements | `bounds` | `cluster<"x":f64,"y":f64,"width":f64,"height":f64>` | Read | Editor |
| Bounds › Area Height | `bounds.area_height` | `f64` | Read | Editor |
| Bounds › Area Width | `bounds.area_width` | `f64` | Read | Editor |
| Position › All Elements | `position` | `cluster<"x":f64,"y":f64>` | Read | Editor |
| Position › Left | `position.left` | `f64` | Read | Editor |
| Position › Top | `position.top` | `f64` | Read | Editor |
| Colors › Text | `text_color` | `u32` | Read / Write | Editor |
| Colors › Background | `background_color` | `u32` | Read / Write | — · This text part has no background color field. |
| Colors › Transparent | `transparent` | `bool` | Read / Write | — · This text part has no independent transparency field. |
| Font › All Elements | `font.all` | `cluster<"name":string,"size":f64,"bold":bool,"italic":bool,"underline":bool,"color":u32>` | Read / Write | — · The provider does not offer an atomic complete FontSpec operation. |
| Font › Name | `font.name` | `string` | Read / Write | Editor |
| Font › Size | `font.size` | `f64` | Read / Write | Editor |
| Font › Bold | `font.bold` | `bool` | Read / Write | Editor |
| Font › Italic | `font.italic` | `bool` | Read / Write | Editor |
| Font › Underline | `font.underline` | `bool` | Read / Write | Editor |
| Font › Use Default Font | `use_default_font` | `bool` | Read / Write | Editor |
| Owning Pane | `identity.owning_pane` | `ref<"frog.pane">` | Read | Editor |
| Visible | `interaction.visible` | `bool` | Read / Write | Editor |
| Size › All Elements | `size` | `cluster<"width":f64,"height":f64>` | Read | Editor |
| Size › Width | `size.width` | `f64` | Read | Editor |
| Size › Height | `size.height` | `f64` | Read | Editor |
| Text | `text` | `string` | Read / Write | Editor |
| Attached Object | `attached_object` | `ref<"frog.object">` | Read | Editor |
| Justification | `alignment` | `string` | Read / Write | — · This text part has no independent justification field. |
| Lock | `lock` | `bool` | Read / Write | — · The text part has no separate manipulation lock. |
| Scroll Position | `scroll_position` | `cluster<"x":f64,"y":f64>` | Read / Write | — · This text part has no independent scroll state. |
| Enable Hyperlinks | `enable_hyperlinks` | `bool` | Read / Write | — · Hyperlink rendering is not registered for this text part. |

## Methods

No entries declared for this class.
