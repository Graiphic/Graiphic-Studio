# File

Reference class `file`. [All classes](index.md) · [How to use Property and Invoke Nodes](../using-object-references.md)

Catalog value schema for this listing: target-dependent. A strict reference can supply a different schema.

## Properties

| Menu path | Saved ID | Connection | Access | Catalog availability |
| --- | --- | --- | --- | --- |
| Class ID | `identity.class` | `string` | Read | Editor |
| Class Name | `identity.class_name` | `string` | Read | Editor |
| Owner | `identity.owner` | `ref<"frog.object">` | Read | Editor |
| Object ID | `identity.object_id` | `string` | Read | Editor |
| Valid | `file.valid` | `bool` | Read | — · The file manager has no public handle-inspection API. |
| Path | `file.path` | `path` | Read | — · The file manager has no public handle-path inspection API. |
| Position | `file.position` | `i64` | Read / Write | — · File access requires the runtime handle provider. |
| Size | `file.size` | `i64` | Read / Write | — · File access requires the runtime handle provider. |
| Access Mode | `file.access_mode` | `string` | Read | — · The file manager has no public access-mode inspection API. |

## Methods

| Menu path | Saved ID | Connection | Access | Catalog availability |
| --- | --- | --- | --- | --- |
| Seek | `file.seek` | in Offset (`offset`, `i64`), in Origin (`origin`, `u16`) → void | Invoke | — · The required service is not available in this provider. |
| Flush | `file.flush` | No parameters → void | Invoke | — · The required service is not available in this provider. |
| Close | `file.close` | No parameters → void | Invoke | — · The required service is not available in this provider. |
| Read Text | `file.read_text` | in Count (`count`, `i64`) optional = `-1`, out Data (`data`, `string`), out End of File (`eof`, `bool`) → void | Invoke | — · The required service is not available in this provider. |
| Write Text | `file.write_text` | in Data (`data`, `string`) → void | Invoke | — · The required service is not available in this provider. |
| Write Binary | `file.write_binary` | in Data (`data`, `array<u8>`) → void | Invoke | — · The required service is not available in this provider. |
