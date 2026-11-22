# Project Item

Reference class `frog.project_item`. [All classes](index.md) · [How to use Property and Invoke Nodes](../using-object-references.md)

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
| Parent | `parent` | `ref<"frog.project_item">` | Read | — · Project capability unavailable. |
| Children[] | `children` | `array<ref<"frog.project_item">>` | Read | — · Project capability unavailable. |
| Project | `project` | `ref<"frog.project">` | Read | — · Project capability unavailable. |
| Target | `target` | `ref<"frog.target">` | Read | — · Project capability unavailable. |

## Methods

| Menu path | Saved ID | Connection | Access | Catalog availability |
| --- | --- | --- | --- | --- |
| Add Item | `add_item` | No parameters → void | Invoke | — · Project capability unavailable. |
| Remove From Project | `remove` | No parameters → void | Invoke | — · Project capability unavailable. |
