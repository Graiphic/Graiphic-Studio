# Boolean

Reference class `frog.widgets.button`. [All classes](index.md) · [How to use Property and Invoke Nodes](../using-object-references.md)

Catalog value schema for this listing: `bool`. A strict reference can supply a different schema.

## Properties

| Menu path | Saved ID | Connection | Access | Catalog availability |
| --- | --- | --- | --- | --- |
| Class ID | `identity.class` | `string` | Read | Editor |
| Class Name | `identity.class_name` | `string` | Read | Editor |
| Owner | `identity.owner` | `ref<"frog.object">` | Read | Editor |
| Owning FROG | `identity.owning_frog` | `ref<"frog.program">` | Read | Editor |
| Object ID | `identity.object_id` | `string` | Read | Editor |
| Bounds › All Elements | `bounds` | `cluster<"x":f64,"y":f64,"width":f64,"height":f64>` | Read | Editor · Logical document/container coordinates in model units. Root writes use the canvas bounds service and its minimum sizes; contained geometry is read-only here. Runtime access is unavailable. |
| Bounds › Area Height | `bounds.area_height` | `f64` | Read | Editor |
| Bounds › Area Width | `bounds.area_width` | `f64` | Read | Editor |
| Position › All Elements | `position` | `cluster<"x":f64,"y":f64>` | Read / Write | Editor · Logical document/container coordinates in model units. Root writes use the canvas bounds service and its minimum sizes; contained geometry is read-only here. Runtime access is unavailable. |
| Position › Left | `position.left` | `f64` | Read / Write | Editor |
| Position › Top | `position.top` | `f64` | Read / Write | Editor |
| Blinking | `interaction.blinking` | `bool` | Read / Write | — · A blinking service is not registered. |
| Built-In Mouse Wheel Support | `interaction.mouse_wheel` | `bool` | Read / Write | — · Per-control wheel policy is not exposed by this provider. |
| Caption › Reference | `caption.reference` | `ref<"frog.text.caption">` | Read | Editor |
| Caption › Class ID | `caption.identity.class` | `string` | Read | Editor |
| Caption › Class Name | `caption.identity.class_name` | `string` | Read | Editor |
| Caption › Owner | `caption.identity.owner` | `ref<"frog.object">` | Read | Editor |
| Caption › Owning FROG | `caption.identity.owning_frog` | `ref<"frog.program">` | Read | Editor |
| Caption › Object ID | `caption.identity.object_id` | `string` | Read | Editor |
| Caption › Bounds › All Elements | `caption.bounds` | `cluster<"x":f64,"y":f64,"width":f64,"height":f64>` | Read | Editor |
| Caption › Bounds › Area Height | `caption.bounds.area_height` | `f64` | Read | Editor |
| Caption › Bounds › Area Width | `caption.bounds.area_width` | `f64` | Read | Editor |
| Caption › Position › All Elements | `caption.position` | `cluster<"x":f64,"y":f64>` | Read | Editor |
| Caption › Position › Left | `caption.position.left` | `f64` | Read | Editor |
| Caption › Position › Top | `caption.position.top` | `f64` | Read | Editor |
| Caption › Colors › Text | `caption.text_color` | `u32` | Read / Write | — · Caption has no independent text color field. |
| Caption › Colors › Background | `caption.background_color` | `u32` | Read / Write | — · This text part has no background color field. |
| Caption › Colors › Transparent | `caption.transparent` | `bool` | Read / Write | — · This text part has no independent transparency field. |
| Caption › Font › All Elements | `caption.font.all` | `cluster<"name":string,"size":f64,"bold":bool,"italic":bool,"underline":bool,"color":u32>` | Read / Write | — · The provider does not offer an atomic complete FontSpec operation. |
| Caption › Font › Name | `caption.font.name` | `string` | Read / Write | Editor |
| Caption › Font › Size | `caption.font.size` | `f64` | Read / Write | Editor · Effective text size in points, including inherited size. A write creates an override for this part; Use Default Font restores inheritance. Runtime access is unavailable. |
| Caption › Font › Use Default Font | `caption.use_default_font` | `bool` | Read / Write | Editor |
| Caption › Font › Bold | `caption.font.bold` | `bool` | Read / Write | — · Caption does not store an independent bold setting. |
| Caption › Font › Italic | `caption.font.italic` | `bool` | Read / Write | — · Caption does not store an independent italic setting. |
| Caption › Font › Underline | `caption.font.underline` | `bool` | Read / Write | — · Caption does not store an independent underline setting. |
| Caption › Owning Pane | `caption.identity.owning_pane` | `ref<"frog.pane">` | Read | Editor |
| Caption › Visible | `caption.visible` | `bool` | Read / Write | Editor |
| Caption › Size › All Elements | `caption.size` | `cluster<"width":f64,"height":f64>` | Read | Editor |
| Caption › Size › Width | `caption.size.width` | `f64` | Read | Editor |
| Caption › Size › Height | `caption.size.height` | `f64` | Read | Editor |
| Control Index | `control_index` | `i32` | Read | — · Indexed terminal access is not registered; an object ID is not an index. |
| Data Binding › Configuration | `data_binding.configuration` | `variant` | Read / Write | — · Data Binding provider is unavailable. |
| DataSocket › Configuration | `datasocket.configuration` | `variant` | Read / Write | — · DataSocket provider is unavailable. |
| Caption › Text | `caption.text` | `string` | Read / Write | Editor |
| Caption › Attached Object | `caption.attached_object` | `ref<"frog.object">` | Read | Editor |
| Caption › Justification | `caption.alignment` | `string` | Read / Write | — · This text part has no independent justification field. |
| Caption › Lock | `caption.lock` | `bool` | Read / Write | — · The text part has no separate manipulation lock. |
| Caption › Scroll Position | `caption.scroll_position` | `cluster<"x":f64,"y":f64>` | Read / Write | — · This text part has no independent scroll state. |
| Caption › Enable Hyperlinks | `caption.enable_hyperlinks` | `bool` | Read / Write | — · Hyperlink rendering is not registered for this text part. |
| Description | `description` | `string` | Read / Write | Editor |
| Disabled | `interaction.disabled_state` | `enum<"frog.widget.enabled_state",u8>` | Read / Write | Editor |
| Focus Key Binding | `focus_key_binding` | `variant` | Read / Write | — · A public key-binding service is not registered. |
| Indicator | `indicator` | `bool` | Read | Editor |
| Key Focus | `key_focus` | `bool` | Read / Write | — · The native focus service is not registered for property access. |
| Label › Reference | `label.reference` | `ref<"frog.text.label">` | Read | Editor |
| Label › Class ID | `label.identity.class` | `string` | Read | Editor |
| Label › Class Name | `label.identity.class_name` | `string` | Read | Editor |
| Label › Owner | `label.identity.owner` | `ref<"frog.object">` | Read | Editor |
| Label › Owning FROG | `label.identity.owning_frog` | `ref<"frog.program">` | Read | Editor |
| Label › Object ID | `label.identity.object_id` | `string` | Read | Editor |
| Label › Bounds › All Elements | `label.bounds` | `cluster<"x":f64,"y":f64,"width":f64,"height":f64>` | Read | Editor |
| Label › Bounds › Area Height | `label.bounds.area_height` | `f64` | Read | Editor |
| Label › Bounds › Area Width | `label.bounds.area_width` | `f64` | Read | Editor |
| Label › Position › All Elements | `label.position` | `cluster<"x":f64,"y":f64>` | Read | Editor |
| Label › Position › Left | `label.position.left` | `f64` | Read | Editor |
| Label › Position › Top | `label.position.top` | `f64` | Read | Editor |
| Label › Colors › Text | `label.text_color` | `u32` | Read / Write | Editor |
| Label › Colors › Background | `label.background_color` | `u32` | Read / Write | Editor |
| Label › Colors › Transparent | `label.transparent` | `bool` | Read / Write | Editor · Transparent uses the existing transparent-color model. To make a transparent label opaque, set an explicit Background Color first; no inherited color is invented. |
| Label › Font › All Elements | `label.font.all` | `cluster<"name":string,"size":f64,"bold":bool,"italic":bool,"underline":bool,"color":u32>` | Read / Write | — · The provider does not offer an atomic complete FontSpec operation. |
| Label › Font › Name | `label.font.name` | `string` | Read / Write | Editor |
| Label › Font › Size | `label.font.size` | `f64` | Read / Write | Editor · Effective text size in points, including inherited size. A write creates an override for this part; Use Default Font restores inheritance. Runtime access is unavailable. |
| Label › Font › Use Default Font | `label.use_default_font` | `bool` | Read / Write | Editor |
| Label › Font › Bold | `label.font.bold` | `bool` | Read / Write | Editor |
| Label › Font › Italic | `label.font.italic` | `bool` | Read / Write | Editor |
| Label › Font › Underline | `label.font.underline` | `bool` | Read / Write | Editor |
| Label › Owning Pane | `label.identity.owning_pane` | `ref<"frog.pane">` | Read | Editor |
| Label › Visible | `label.visible` | `bool` | Read / Write | Editor |
| Label › Size › All Elements | `label.size` | `cluster<"width":f64,"height":f64>` | Read | Editor |
| Label › Size › Width | `label.size.width` | `f64` | Read | Editor |
| Label › Size › Height | `label.size.height` | `f64` | Read | Editor |
| Owning Pane | `identity.owning_pane` | `ref<"frog.pane">` | Read | Editor |
| Skip When Tabbing | `skip_when_tabbing` | `bool` | Read / Write | — · A per-control Tab order service is not registered. |
| Synchronous Display | `synchronous_display` | `bool` | Read / Write | — · The provider cannot guarantee synchronous rendering. |
| Label › Text | `label.text` | `string` | Read / Write | Editor |
| Label › Justification | `label.alignment` | `string` | Read / Write | Editor |
| Label › Attached Object | `label.attached_object` | `ref<"frog.object">` | Read | Editor |
| Label › Lock | `label.lock` | `bool` | Read / Write | — · The text part has no separate manipulation lock. |
| Label › Scroll Position | `label.scroll_position` | `cluster<"x":f64,"y":f64>` | Read / Write | — · This text part has no independent scroll state. |
| Label › Enable Hyperlinks | `label.enable_hyperlinks` | `bool` | Read / Write | — · Hyperlink rendering is not registered for this text part. |
| Tip Strip | `tip_strip` | `string` | Read / Write | Editor |
| Value | `value` | `bool` | Read / Write | Editor |
| Value (Signaling) | `value_signaling` | `bool` | Write | — · Run advertised · Writes the current typed value and queues Value Change, including identical values. Write-only; Latch Boolean actions are unsupported. Value writes stay silent. Uses captured OldVal/NewVal and the actual control reference; handler completion is asynchronous. |
| Visible | `interaction.visible` | `bool` | Read / Write | Editor |
| XControl › Configuration | `xcontrol.configuration` | `variant` | Read / Write | — · XControl compatibility provider is unavailable. |
| Size › All Elements | `size` | `cluster<"width":f64,"height":f64>` | Read / Write | Editor · Logical document/container coordinates in model units. Root writes use the canvas bounds service and its minimum sizes; contained geometry is read-only here. Runtime access is unavailable. |
| Size › Width | `size.width` | `f64` | Read / Write | Editor |
| Size › Height | `size.height` | `f64` | Read / Write | Editor |
| Boolean Text › Reference | `boolean_text.reference` | `ref<"frog.text.boolean">` | Read | Editor |
| Boolean Text › Class ID | `boolean_text.identity.class` | `string` | Read | Editor |
| Boolean Text › Class Name | `boolean_text.identity.class_name` | `string` | Read | Editor |
| Boolean Text › Owner | `boolean_text.identity.owner` | `ref<"frog.object">` | Read | Editor |
| Boolean Text › Owning FROG | `boolean_text.identity.owning_frog` | `ref<"frog.program">` | Read | Editor |
| Boolean Text › Object ID | `boolean_text.identity.object_id` | `string` | Read | Editor |
| Boolean Text › Bounds › All Elements | `boolean_text.bounds` | `cluster<"x":f64,"y":f64,"width":f64,"height":f64>` | Read | Editor |
| Boolean Text › Bounds › Area Height | `boolean_text.bounds.area_height` | `f64` | Read | Editor |
| Boolean Text › Bounds › Area Width | `boolean_text.bounds.area_width` | `f64` | Read | Editor |
| Boolean Text › Position › All Elements | `boolean_text.position` | `cluster<"x":f64,"y":f64>` | Read | Editor |
| Boolean Text › Position › Left | `boolean_text.position.left` | `f64` | Read | Editor |
| Boolean Text › Position › Top | `boolean_text.position.top` | `f64` | Read | Editor |
| Boolean Text › Colors › Text | `boolean_text.text_color` | `u32` | Read / Write | Editor |
| Boolean Text › Colors › Background | `boolean_text.background_color` | `u32` | Read / Write | — · This text part has no background color field. |
| Boolean Text › Colors › Transparent | `boolean_text.transparent` | `bool` | Read / Write | — · This text part has no independent transparency field. |
| Boolean Text › Font › All Elements | `boolean_text.font.all` | `cluster<"name":string,"size":f64,"bold":bool,"italic":bool,"underline":bool,"color":u32>` | Read / Write | — · The provider does not offer an atomic complete FontSpec operation. |
| Boolean Text › Font › Name | `boolean_text.font.name` | `string` | Read / Write | Editor |
| Boolean Text › Font › Size | `boolean_text.font.size` | `f64` | Read / Write | Editor · Effective text size in points, including inherited size. A write creates an override for this part; Use Default Font restores inheritance. Runtime access is unavailable. |
| Boolean Text › Font › Use Default Font | `boolean_text.use_default_font` | `bool` | Read / Write | Editor |
| Boolean Text › Font › Bold | `boolean_text.font.bold` | `bool` | Read / Write | Editor |
| Boolean Text › Font › Italic | `boolean_text.font.italic` | `bool` | Read / Write | Editor |
| Boolean Text › Font › Underline | `boolean_text.font.underline` | `bool` | Read / Write | Editor |
| Boolean Text › Owning Pane | `boolean_text.identity.owning_pane` | `ref<"frog.pane">` | Read | Editor |
| Boolean Text › Visible | `boolean_text.visible` | `bool` | Read / Write | Editor |
| Boolean Text › Size › All Elements | `boolean_text.size` | `cluster<"width":f64,"height":f64>` | Read | Editor |
| Boolean Text › Size › Width | `boolean_text.size.width` | `f64` | Read | Editor |
| Boolean Text › Size › Height | `boolean_text.size.height` | `f64` | Read | Editor |
| Colors[4] | `colors` | `array<cluster<"foreground_color":u32,"background_color":u32>>` | Read / Write | — · Run advertised · Reads or writes Foreground Color and Background Color (U32 RGB) for False, True, True to False and False to True, followed by False/True mouse-over colors when supported. Write 1, 2, 4 or, on a compatible style, 6 pairs. Does not change the Boolean value or text. |
| Boolean Text › Text | `boolean_text.text` | `string` | Read / Write | Editor |
| Boolean Text › Attached Object | `boolean_text.attached_object` | `ref<"frog.object">` | Read | Editor |
| Boolean Text › Justification | `boolean_text.alignment` | `string` | Read / Write | — · This text part has no independent justification field. |
| Boolean Text › Lock | `boolean_text.lock` | `bool` | Read / Write | — · The text part has no separate manipulation lock. |
| Boolean Text › Scroll Position | `boolean_text.scroll_position` | `cluster<"x":f64,"y":f64>` | Read / Write | — · This text part has no independent scroll state. |
| Boolean Text › Enable Hyperlinks | `boolean_text.enable_hyperlinks` | `bool` | Read / Write | — · Hyperlink rendering is not registered for this text part. |
| Role | `identity.role` | `string` | Read | Editor |
| Default Value | `default_value` | `bool` | Read / Write | Editor |
| Value Type | `value_type` | `string` | Read | Editor |
| Enabled | `interaction.enabled` | `bool` | Read / Write | Editor |
| Boolean Text.False | `boolean_text.false` | `string` | Read / Write | Editor |
| Boolean Text.True | `boolean_text.true` | `string` | Read / Write | Editor |
| Mechanical Action | `mechanical_action` | `string` | Read / Write | Editor |

## Methods

| Menu path | Saved ID | Connection | Access | Catalog availability |
| --- | --- | --- | --- | --- |
| Object Highlight | `object_highlight` | No parameters → void | Invoke | Editor |
| Attach DataSocket | `datasocket.attach` | No parameters → void | Invoke | — · The required service is not available in this provider. |
| Data Binding › Bind | `data_binding.bind` | No parameters → void | Invoke | — · The required service is not available in this provider. |
| Data Binding › Unbind | `data_binding.unbind` | No parameters → void | Invoke | — · The required service is not available in this provider. |
| Fit Control To Pane | `fit_control_to_pane` | No parameters → void | Invoke | — · The required service is not available in this provider. |
| Get Image | `get_image` | No parameters → void | Invoke | — · The required service is not available in this provider. |
| Get Terminal Image | `get_terminal_image` | No parameters → void | Invoke | — · The required service is not available in this provider. |
| Reinitialize To Default | `reinitialize` | No parameters → void | Invoke | Editor |
| Remove DataSocket | `datasocket.remove` | No parameters → void | Invoke | — · The required service is not available in this provider. |
| Start Drag | `start_drag` | No parameters → void | Invoke | — · The required service is not available in this provider. |
| Make Current Value Default | `make_default` | No parameters → void | Invoke | Editor |
| Set Focus | `set_focus` | No parameters → void | Invoke | — · No provider for this operation in the current authoring context. |
