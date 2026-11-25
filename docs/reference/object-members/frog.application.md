# App

Reference class `frog.application`. [All classes](index.md) · [How to use Property and Invoke Nodes](../using-object-references.md)

Catalog value schema for this listing: target-dependent. A strict reference can supply a different schema.

## Properties

| Menu path | Saved ID | Connection | Access | Catalog availability |
| --- | --- | --- | --- | --- |
| Class ID | `identity.class` | `string` | Read | Editor |
| Class Name | `identity.class_name` | `string` | Read | Editor |
| Owner | `identity.owner` | `ref<"frog.object">` | Read | Editor |
| Object ID | `identity.object_id` | `string` | Read | Editor |
| Name | `name` | `string` | Read | Editor |
| Version | `version` | `string` | Read | Editor |
| Kind | `kind` | `string` | Read | Editor · Run advertised |
| Active FROG Name | `active_frog_name` | `string` | Read | Editor |
| Executable Path | `executable_path` | `path` | Read | Editor |
| Application Directory | `application_directory` | `path` | Read | Editor |
| Command Line Arguments | `command_line_arguments` | `array<string>` | Read | Editor |
| Active FROG Reference | `active_frog` | `ref<"frog.program">` | Read | Editor |
| Open FROGs[] | `open_frogs` | `array<ref<"frog.program">>` | Read | Editor |
| Projects[] | `projects` | `array<ref<"frog.project">>` | Read | — · Project capability unavailable. |
| Active Project | `active_project` | `ref<"frog.project">` | Read | — · Project capability unavailable. |

## Methods

| Menu path | Saved ID | Connection | Access | Catalog availability |
| --- | --- | --- | --- | --- |
| Project › New | `project.new` | No parameters → void | Invoke | — · The required service is not available in this provider. |
| Project › Open | `project.open` | No parameters → void | Invoke | — · The required service is not available in this provider. |
| New FROG | `application.new_frog` | No parameters → `ref<"frog.program">` | Invoke | Editor |
| Open FROG | `application.open_frog` | in Path (`path`, `path`) → `ref<"frog.program">` | Invoke | Editor |
| Resolve FROG | `application.resolve_frog` | in Path (`path`, `path`) → `ref<"frog.program">` | Invoke | Editor |
