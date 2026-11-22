# Label

Reference class `frog.widgets.label`. [All classes](index.md) · [How to use Property and Invoke Nodes](../using-object-references.md)

Catalog value schema for this listing: target-dependent. A strict reference can supply a different schema.

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
| Caption › Font › Name | `caption.font.name` | `string` | Read / Write | Editor |
| Caption › Font › Size | `caption.font.size` | `f64` | Read / Write | Editor · Effective text size in points, including inherited size. A write creates an override for this part; Use Default Font restores inheritance. Runtime access is unavailable. |
| Caption › Font › Use Default Font | `caption.use_default_font` | `bool` | Read / Write | Editor |
| Control Index | `control_index` | `i32` | Read | — · Indexed terminal access is not registered; an object ID is not an index. |
| Data Binding › Configuration | `data_binding.configuration` | `variant` | Read / Write | — · Data Binding provider is unavailable. |
| DataSocket › Configuration | `datasocket.configuration` | `variant` | Read / Write | — · DataSocket provider is unavailable. |
| Description | `description` | `string` | Read / Write | Editor |
| Disabled | `interaction.disabled_state` | `enum<"frog.widget.enabled_state",u8>` | Read / Write | — · The widget has no enabled-state provider. |
| Focus Key Binding | `focus_key_binding` | `variant` | Read / Write | — · A public key-binding service is not registered. |
| Indicator | `indicator` | `bool` | Read | Editor |
| Key Focus | `key_focus` | `bool` | Read / Write | — · The native focus service is not registered for property access. |
| Label › Colors › Text | `label.text_color` | `u32` | Read / Write | Editor |
| Label › Colors › Background | `label.background_color` | `u32` | Read / Write | Editor |
| Label › Colors › Transparent | `label.transparent` | `bool` | Read / Write | Editor · Transparent uses the existing transparent-color model. To make a transparent label opaque, set an explicit Background Color first; no inherited color is invented. |
| Label › Font › Name | `label.font.name` | `string` | Read / Write | Editor |
| Label › Font › Size | `label.font.size` | `f64` | Read / Write | Editor · Effective text size in points, including inherited size. A write creates an override for this part; Use Default Font restores inheritance. Runtime access is unavailable. |
| Label › Font › Bold | `label.font.bold` | `bool` | Read / Write | Editor |
| Label › Font › Italic | `label.font.italic` | `bool` | Read / Write | Editor |
| Label › Font › Use Default Font | `label.use_default_font` | `bool` | Read / Write | Editor |
| Label › Justification | `label.alignment` | `string` | Read / Write | Editor |
| Owning Pane | `identity.owning_pane` | `ref<"frog.pane">` | Read | Editor |
| Skip When Tabbing | `skip_when_tabbing` | `bool` | Read / Write | — · A per-control Tab order service is not registered. |
| Synchronous Display | `synchronous_display` | `bool` | Read / Write | — · The provider cannot guarantee synchronous rendering. |
| Tip Strip | `tip_strip` | `string` | Read / Write | Editor |
| Visible | `interaction.visible` | `bool` | Read / Write | Editor |
| XControl › Configuration | `xcontrol.configuration` | `variant` | Read / Write | — · XControl compatibility provider is unavailable. |
| Size › All Elements | `size` | `cluster<"width":f64,"height":f64>` | Read / Write | Editor · Logical document/container coordinates in model units. Root writes use the canvas bounds service and its minimum sizes; contained geometry is read-only here. Runtime access is unavailable. |
| Size › Width | `size.width` | `f64` | Read / Write | Editor |
| Size › Height | `size.height` | `f64` | Read / Write | Editor |
| Role | `identity.role` | `string` | Read | Editor |
| Enabled | `interaction.enabled` | `bool` | Read / Write | — · The widget has no enabled-state provider. |

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
| Remove DataSocket | `datasocket.remove` | No parameters → void | Invoke | — · The required service is not available in this provider. |
| Start Drag | `start_drag` | No parameters → void | Invoke | — · The required service is not available in this provider. |
| Set Focus | `set_focus` | No parameters → void | Invoke | — · No provider for this operation in the current authoring context. |
