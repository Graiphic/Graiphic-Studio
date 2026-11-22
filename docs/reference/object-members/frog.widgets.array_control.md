# Array

Reference class `frog.widgets.array_control`. [All classes](index.md) · [How to use Property and Invoke Nodes](../using-object-references.md)

Catalog value schema for this listing: `array<u16>`. A strict reference can supply a different schema.

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
| Value | `value` | `array<u16>` | Read / Write | Editor |
| Value (Signaling) | `value_signaling` | `array<u16>` | Write | — · Run advertised · Writes the current typed value and queues Value Change, including identical values. Write-only; Latch Boolean actions are unsupported. Value writes stay silent. Uses captured OldVal/NewVal and the actual control reference; handler completion is asynchronous. |
| Visible | `interaction.visible` | `bool` | Read / Write | Editor |
| XControl › Configuration | `xcontrol.configuration` | `variant` | Read / Write | — · XControl compatibility provider is unavailable. |
| Size › All Elements | `size` | `cluster<"width":f64,"height":f64>` | Read / Write | Editor · Logical document/container coordinates in model units. Root writes use the canvas bounds service and its minimum sizes; contained geometry is read-only here. Runtime access is unavailable. |
| Size › Width | `size.width` | `f64` | Read / Write | Editor |
| Size › Height | `size.height` | `f64` | Read / Write | Editor |
| Array Element › Reference | `array_element` | `ref<"frog.control",u16>` | Read | Editor · Reference to the element presentation template. Value/default access is unavailable on this object; access cells through Array data operations. |
| Index Values[] | `array.index_values` | `array<u32>` | Read / Write | Editor |
| Selection Start[] | `array.selection_start` | `array<u32>` | Read / Write | — · The Array model does not store a cell selection range. |
| Selection Size[] | `array.selection_size` | `array<u32>` | Read / Write | — · The Array model does not store a cell selection range. |
| Role | `identity.role` | `string` | Read | Editor |
| Default Value | `default_value` | `array<u16>` | Read / Write | Editor |
| Value Type | `value_type` | `string` | Read | Editor |
| Enabled | `interaction.enabled` | `bool` | Read / Write | Editor |
| Array Size | `array_size` | `array<u32>` | Read | Editor |
| Visible Elements | `array.visible_elements` | `array<u32>` | Read / Write | Editor |
| Index Display Visible | `array.index_visible` | `bool` | Read / Write | Editor |
| Vertical Scrollbar Visible | `array.vertical_scrollbar` | `bool` | Read / Write | Editor |
| Horizontal Scrollbar Visible | `array.horizontal_scrollbar` | `bool` | Read / Write | Editor |
| Index Rect | `array.index_rect` | `cluster<"x":f64,"y":f64,"width":f64,"height":f64>` | Read | — · Measured index bounds are not exposed by the current provider. |
| Array Element › Class ID | `array_element.identity.class` | `string` | Read | Editor |
| Array Element › Class Name | `array_element.identity.class_name` | `string` | Read | Editor |
| Array Element › Owner | `array_element.identity.owner` | `ref<"frog.object">` | Read | Editor |
| Array Element › Owning FROG | `array_element.identity.owning_frog` | `ref<"frog.program">` | Read | Editor |
| Array Element › Object ID | `array_element.identity.object_id` | `string` | Read | Editor |
| Array Element › Bounds › All Elements | `array_element.bounds` | `cluster<"x":f64,"y":f64,"width":f64,"height":f64>` | Read | Editor · Logical document/container coordinates in model units. Root writes use the canvas bounds service and its minimum sizes; contained geometry is read-only here. Runtime access is unavailable. |
| Array Element › Bounds › Area Height | `array_element.bounds.area_height` | `f64` | Read | Editor |
| Array Element › Bounds › Area Width | `array_element.bounds.area_width` | `f64` | Read | Editor |
| Array Element › Position › All Elements | `array_element.position` | `cluster<"x":f64,"y":f64>` | Read / Write | Editor · Logical document/container coordinates in model units. Root writes use the canvas bounds service and its minimum sizes; contained geometry is read-only here. Runtime access is unavailable. |
| Array Element › Position › Left | `array_element.position.left` | `f64` | Read / Write | Editor |
| Array Element › Position › Top | `array_element.position.top` | `f64` | Read / Write | Editor |
| Array Element › Blinking | `array_element.interaction.blinking` | `bool` | Read / Write | — · A blinking service is not registered. |
| Array Element › Built-In Mouse Wheel Support | `array_element.interaction.mouse_wheel` | `bool` | Read / Write | — · Per-control wheel policy is not exposed by this provider. |
| Array Element › Caption › Reference | `array_element.caption.reference` | `ref<"frog.text.caption">` | Read | Editor |
| Array Element › Caption › Class ID | `array_element.caption.identity.class` | `string` | Read | Editor |
| Array Element › Caption › Class Name | `array_element.caption.identity.class_name` | `string` | Read | Editor |
| Array Element › Caption › Owner | `array_element.caption.identity.owner` | `ref<"frog.object">` | Read | Editor |
| Array Element › Caption › Owning FROG | `array_element.caption.identity.owning_frog` | `ref<"frog.program">` | Read | Editor |
| Array Element › Caption › Object ID | `array_element.caption.identity.object_id` | `string` | Read | Editor |
| Array Element › Caption › Bounds › All Elements | `array_element.caption.bounds` | `cluster<"x":f64,"y":f64,"width":f64,"height":f64>` | Read | Editor |
| Array Element › Caption › Bounds › Area Height | `array_element.caption.bounds.area_height` | `f64` | Read | Editor |
| Array Element › Caption › Bounds › Area Width | `array_element.caption.bounds.area_width` | `f64` | Read | Editor |
| Array Element › Caption › Position › All Elements | `array_element.caption.position` | `cluster<"x":f64,"y":f64>` | Read | Editor |
| Array Element › Caption › Position › Left | `array_element.caption.position.left` | `f64` | Read | Editor |
| Array Element › Caption › Position › Top | `array_element.caption.position.top` | `f64` | Read | Editor |
| Array Element › Caption › Colors › Text | `array_element.caption.text_color` | `u32` | Read / Write | — · Caption has no independent text color field. |
| Array Element › Caption › Colors › Background | `array_element.caption.background_color` | `u32` | Read / Write | — · This text part has no background color field. |
| Array Element › Caption › Colors › Transparent | `array_element.caption.transparent` | `bool` | Read / Write | — · This text part has no independent transparency field. |
| Array Element › Caption › Font › All Elements | `array_element.caption.font.all` | `cluster<"name":string,"size":f64,"bold":bool,"italic":bool,"underline":bool,"color":u32>` | Read / Write | — · The provider does not offer an atomic complete FontSpec operation. |
| Array Element › Caption › Font › Name | `array_element.caption.font.name` | `string` | Read / Write | Editor |
| Array Element › Caption › Font › Size | `array_element.caption.font.size` | `f64` | Read / Write | Editor · Effective text size in points, including inherited size. A write creates an override for this part; Use Default Font restores inheritance. Runtime access is unavailable. |
| Array Element › Caption › Font › Use Default Font | `array_element.caption.use_default_font` | `bool` | Read / Write | Editor |
| Array Element › Caption › Font › Bold | `array_element.caption.font.bold` | `bool` | Read / Write | — · Caption does not store an independent bold setting. |
| Array Element › Caption › Font › Italic | `array_element.caption.font.italic` | `bool` | Read / Write | — · Caption does not store an independent italic setting. |
| Array Element › Caption › Font › Underline | `array_element.caption.font.underline` | `bool` | Read / Write | — · Caption does not store an independent underline setting. |
| Array Element › Caption › Owning Pane | `array_element.caption.identity.owning_pane` | `ref<"frog.pane">` | Read | Editor |
| Array Element › Caption › Visible | `array_element.caption.visible` | `bool` | Read / Write | Editor |
| Array Element › Caption › Size › All Elements | `array_element.caption.size` | `cluster<"width":f64,"height":f64>` | Read | Editor |
| Array Element › Caption › Size › Width | `array_element.caption.size.width` | `f64` | Read | Editor |
| Array Element › Caption › Size › Height | `array_element.caption.size.height` | `f64` | Read | Editor |
| Array Element › Control Index | `array_element.control_index` | `i32` | Read | — · Indexed terminal access is not registered; an object ID is not an index. |
| Array Element › Data Binding › Configuration | `array_element.data_binding.configuration` | `variant` | Read / Write | — · Data Binding provider is unavailable. |
| Array Element › DataSocket › Configuration | `array_element.datasocket.configuration` | `variant` | Read / Write | — · DataSocket provider is unavailable. |
| Array Element › Caption › Text | `array_element.caption.text` | `string` | Read / Write | Editor |
| Array Element › Caption › Attached Object | `array_element.caption.attached_object` | `ref<"frog.object">` | Read | Editor |
| Array Element › Caption › Justification | `array_element.caption.alignment` | `string` | Read / Write | — · This text part has no independent justification field. |
| Array Element › Caption › Lock | `array_element.caption.lock` | `bool` | Read / Write | — · The text part has no separate manipulation lock. |
| Array Element › Caption › Scroll Position | `array_element.caption.scroll_position` | `cluster<"x":f64,"y":f64>` | Read / Write | — · This text part has no independent scroll state. |
| Array Element › Caption › Enable Hyperlinks | `array_element.caption.enable_hyperlinks` | `bool` | Read / Write | — · Hyperlink rendering is not registered for this text part. |
| Array Element › Description | `array_element.description` | `string` | Read / Write | Editor |
| Array Element › Disabled | `array_element.interaction.disabled_state` | `enum<"frog.widget.enabled_state",u8>` | Read / Write | Editor |
| Array Element › Focus Key Binding | `array_element.focus_key_binding` | `variant` | Read / Write | — · A public key-binding service is not registered. |
| Array Element › Indicator | `array_element.indicator` | `bool` | Read | Editor |
| Array Element › Key Focus | `array_element.key_focus` | `bool` | Read / Write | — · The native focus service is not registered for property access. |
| Array Element › Label › Reference | `array_element.label.reference` | `ref<"frog.text.label">` | Read | Editor |
| Array Element › Label › Class ID | `array_element.label.identity.class` | `string` | Read | Editor |
| Array Element › Label › Class Name | `array_element.label.identity.class_name` | `string` | Read | Editor |
| Array Element › Label › Owner | `array_element.label.identity.owner` | `ref<"frog.object">` | Read | Editor |
| Array Element › Label › Owning FROG | `array_element.label.identity.owning_frog` | `ref<"frog.program">` | Read | Editor |
| Array Element › Label › Object ID | `array_element.label.identity.object_id` | `string` | Read | Editor |
| Array Element › Label › Bounds › All Elements | `array_element.label.bounds` | `cluster<"x":f64,"y":f64,"width":f64,"height":f64>` | Read | Editor |
| Array Element › Label › Bounds › Area Height | `array_element.label.bounds.area_height` | `f64` | Read | Editor |
| Array Element › Label › Bounds › Area Width | `array_element.label.bounds.area_width` | `f64` | Read | Editor |
| Array Element › Label › Position › All Elements | `array_element.label.position` | `cluster<"x":f64,"y":f64>` | Read | Editor |
| Array Element › Label › Position › Left | `array_element.label.position.left` | `f64` | Read | Editor |
| Array Element › Label › Position › Top | `array_element.label.position.top` | `f64` | Read | Editor |
| Array Element › Label › Colors › Text | `array_element.label.text_color` | `u32` | Read / Write | Editor |
| Array Element › Label › Colors › Background | `array_element.label.background_color` | `u32` | Read / Write | Editor |
| Array Element › Label › Colors › Transparent | `array_element.label.transparent` | `bool` | Read / Write | Editor · Transparent uses the existing transparent-color model. To make a transparent label opaque, set an explicit Background Color first; no inherited color is invented. |
| Array Element › Label › Font › All Elements | `array_element.label.font.all` | `cluster<"name":string,"size":f64,"bold":bool,"italic":bool,"underline":bool,"color":u32>` | Read / Write | — · The provider does not offer an atomic complete FontSpec operation. |
| Array Element › Label › Font › Name | `array_element.label.font.name` | `string` | Read / Write | Editor |
| Array Element › Label › Font › Size | `array_element.label.font.size` | `f64` | Read / Write | Editor · Effective text size in points, including inherited size. A write creates an override for this part; Use Default Font restores inheritance. Runtime access is unavailable. |
| Array Element › Label › Font › Use Default Font | `array_element.label.use_default_font` | `bool` | Read / Write | Editor |
| Array Element › Label › Font › Bold | `array_element.label.font.bold` | `bool` | Read / Write | Editor |
| Array Element › Label › Font › Italic | `array_element.label.font.italic` | `bool` | Read / Write | Editor |
| Array Element › Label › Font › Underline | `array_element.label.font.underline` | `bool` | Read / Write | Editor |
| Array Element › Label › Owning Pane | `array_element.label.identity.owning_pane` | `ref<"frog.pane">` | Read | Editor |
| Array Element › Label › Visible | `array_element.label.visible` | `bool` | Read / Write | Editor |
| Array Element › Label › Size › All Elements | `array_element.label.size` | `cluster<"width":f64,"height":f64>` | Read | Editor |
| Array Element › Label › Size › Width | `array_element.label.size.width` | `f64` | Read | Editor |
| Array Element › Label › Size › Height | `array_element.label.size.height` | `f64` | Read | Editor |
| Array Element › Owning Pane | `array_element.identity.owning_pane` | `ref<"frog.pane">` | Read | Editor |
| Array Element › Skip When Tabbing | `array_element.skip_when_tabbing` | `bool` | Read / Write | — · A per-control Tab order service is not registered. |
| Array Element › Synchronous Display | `array_element.synchronous_display` | `bool` | Read / Write | — · The provider cannot guarantee synchronous rendering. |
| Array Element › Label › Text | `array_element.label.text` | `string` | Read / Write | Editor |
| Array Element › Label › Justification | `array_element.label.alignment` | `string` | Read / Write | Editor |
| Array Element › Label › Attached Object | `array_element.label.attached_object` | `ref<"frog.object">` | Read | Editor |
| Array Element › Label › Lock | `array_element.label.lock` | `bool` | Read / Write | — · The text part has no separate manipulation lock. |
| Array Element › Label › Scroll Position | `array_element.label.scroll_position` | `cluster<"x":f64,"y":f64>` | Read / Write | — · This text part has no independent scroll state. |
| Array Element › Label › Enable Hyperlinks | `array_element.label.enable_hyperlinks` | `bool` | Read / Write | — · Hyperlink rendering is not registered for this text part. |
| Array Element › Tip Strip | `array_element.tip_strip` | `string` | Read / Write | Editor |
| Array Element › Value | `array_element.value` | `u16` | Read / Write | — · Array Element is the shared presentation template; access data through Array Value and indexing. |
| Array Element › Value (Signaling) | `array_element.value_signaling` | `u16` | Write | — · Array Element is the shared presentation template; access data through Array Value and indexing. · Writes the current typed value and queues Value Change, including identical values. Write-only; Latch Boolean actions are unsupported. Value writes stay silent. Uses captured OldVal/NewVal and the actual control reference; handler completion is asynchronous. |
| Array Element › Visible | `array_element.interaction.visible` | `bool` | Read / Write | Editor |
| Array Element › XControl › Configuration | `array_element.xcontrol.configuration` | `variant` | Read / Write | — · XControl compatibility provider is unavailable. |
| Array Element › Size › All Elements | `array_element.size` | `cluster<"width":f64,"height":f64>` | Read / Write | Editor · Logical document/container coordinates in model units. Root writes use the canvas bounds service and its minimum sizes; contained geometry is read-only here. Runtime access is unavailable. |
| Array Element › Size › Width | `array_element.size.width` | `f64` | Read / Write | Editor |
| Array Element › Size › Height | `array_element.size.height` | `f64` | Read / Write | Editor |
| Array Element › Data Entry Limits › Minimum | `array_element.numeric.minimum` | `u16` | Read / Write | Editor · Typed Numeric Data Entry authoring property. The current model stores limits/steps as f64; values that cannot be represented exactly are rejected. Complex policy and runtime provider are unavailable. |
| Array Element › Data Entry Limits › Maximum | `array_element.numeric.maximum` | `u16` | Read / Write | Editor · Typed Numeric Data Entry authoring property. The current model stores limits/steps as f64; values that cannot be represented exactly are rejected. Complex policy and runtime provider are unavailable. |
| Array Element › Data Entry Limits › Increment | `array_element.numeric.increment` | `u16` | Read / Write | Editor · Typed Numeric Data Entry authoring property. The current model stores limits/steps as f64; values that cannot be represented exactly are rejected. Complex policy and runtime provider are unavailable. |
| Array Element › Display › Format | `array_element.numeric.format` | `string` | Read / Write | Editor |
| Array Element › Display › Precision | `array_element.numeric.precision` | `i32` | Read / Write | Editor |
| Array Element › Display › Radix | `array_element.numeric.radix` | `enum<"frog.numeric.radix",u8>` | Read / Write | Editor · View of the existing integer display format: Decimal=10, Hexadecimal=16, Octal=8, Binary=2. A write changes that format; it does not create an independent radix state. |
| Array Element › Role | `array_element.identity.role` | `string` | Read | Editor |
| Array Element › Default Value | `array_element.default_value` | `u16` | Read / Write | — · Array Element is the shared presentation template; access data through Array Value and indexing. |
| Array Element › Value Type | `array_element.value_type` | `string` | Read | Editor |
| Array Element › Enabled | `array_element.interaction.enabled` | `bool` | Read / Write | Editor |
| Array Element › Text.Font.Name | `array_element.text.font.name` | `string` | Read / Write | Editor |
| Array Element › Text.Font.Size | `array_element.text.font.size` | `f64` | Read / Write | Editor · Effective text size in points, including inherited size. A write creates an override for this part; Use Default Font restores inheritance. Runtime access is unavailable. |
| Array Element › Text.Use Default Font | `array_element.text.use_default_font` | `bool` | Read / Write | Editor |
| Array Element › Text.Font.Bold | `array_element.text.font.bold` | `bool` | Read / Write | Editor |
| Array Element › Text.Font.Italic | `array_element.text.font.italic` | `bool` | Read / Write | Editor |
| Array Element › Text.Text Color | `array_element.text.text_color` | `u32` | Read / Write | Editor |
| Array Element › Increment/Decrement Visible | `array_element.numeric.step_visible` | `bool` | Read / Write | Editor |

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
