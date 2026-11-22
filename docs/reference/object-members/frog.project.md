# Project

Reference class `frog.project`. [All classes](index.md) · [How to use Property and Invoke Nodes](../using-object-references.md)

Catalog value schema for this listing: target-dependent. A strict reference can supply a different schema.

## Properties

| Menu path | Saved ID | Connection | Access | Catalog availability |
| --- | --- | --- | --- | --- |
| Class ID | `identity.class` | `string` | Read | — · Project capability unavailable. |
| Class Name | `identity.class_name` | `string` | Read | — · Project capability unavailable. |
| Owner | `identity.owner` | `ref<"frog.object">` | Read | — · Project capability unavailable. |
| Object ID | `identity.object_id` | `string` | Read | — · Project capability unavailable. |
| Name | `name` | `string` | Read | — · Project capability unavailable. |
| Path | `path` | `path` | Read | — · Project capability unavailable. |
| Application | `application` | `ref<"frog.application">` | Read | — · Project capability unavailable. |
| Root | `root` | `ref<"frog.project_item">` | Read | — · Project capability unavailable. |
| Targets[] | `targets` | `array<ref<"frog.target">>` | Read | — · Project capability unavailable. |
| Modified | `modified` | `bool` | Read | — · Project capability unavailable. |

## Methods

| Menu path | Saved ID | Connection | Access | Catalog availability |
| --- | --- | --- | --- | --- |
| Save | `save` | No parameters → void | Invoke | — · Project capability unavailable. |
| Close | `close` | No parameters → void | Invoke | — · Project capability unavailable. |
