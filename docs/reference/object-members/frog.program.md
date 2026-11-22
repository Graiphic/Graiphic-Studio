# FROG

Reference class `frog.program`. [All classes](index.md) · [How to use Property and Invoke Nodes](../using-object-references.md)

Catalog value schema for this listing: target-dependent. A strict reference can supply a different schema.

## Properties

| Menu path | Saved ID | Connection | Access | Catalog availability |
| --- | --- | --- | --- | --- |
| Class ID | `identity.class` | `string` | Read | Editor |
| Class Name | `identity.class_name` | `string` | Read | Editor |
| Owner | `identity.owner` | `ref<"frog.object">` | Read | Editor |
| Object ID | `identity.object_id` | `string` | Read | Editor |
| Front Panel › Reference | `front_panel` | `ref<"frog.front_panel">` | Read | Editor |
| Front Panel › Open State | `front_panel.open_state` | `bool` | Read | Editor |
| Execution State | `execution.state` | `string` | Read | Editor |
| Name | `name` | `string` | Read | Editor |
| Path | `path` | `path` | Read | Editor |
| Modified | `modified` | `bool` | Read | Editor |
| Execution Instance ID | `execution.instance_id` | `string` | Read | Editor |
| Application | `application` | `ref<"frog.application">` | Read | Editor |
| Connector Pattern | `connector_pattern` | `variant` | Read | — · A public connector metadata provider is not registered. |
| Dependencies | `dependencies` | `array<path>` | Read | — · A dependency provider is not registered. |

## Methods

| Menu path | Saved ID | Connection | Access | Catalog availability |
| --- | --- | --- | --- | --- |
| Front Panel › Open | `front_panel.open` | in Activate (`activate`, `bool`) optional = `true` → void | Invoke | Editor |
| Front Panel › Close | `front_panel.close` | No parameters → void | Invoke | Editor |
| Save | `save` | No parameters → void | Invoke | Editor |
| Run | `run` | No parameters → void | Invoke | — · The required service is not available in this provider. |
| Abort | `abort` | No parameters → void | Invoke | — · The required service is not available in this provider. |
| Pause | `pause` | No parameters → void | Invoke | — · The required service is not available in this provider. |
| Resume | `resume` | No parameters → void | Invoke | — · The required service is not available in this provider. |
| Save As | `save_as` | in Path (`path`, `path`) → void | Invoke | Editor |
| Compile | `compile` | No parameters → void | Invoke | — · The required service is not available in this provider. |
