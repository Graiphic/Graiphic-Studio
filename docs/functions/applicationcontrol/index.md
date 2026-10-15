# Application Control functions

[All functions](../index.md)

4 operations or editor elements; 0 palette folders. Open a page to inspect its exact connector, typing rules and execution limits.

## Operations and editor elements

| Entry | Purpose |
| --- | --- |
| [Close Reference](../application_control/close_reference.md) | Private Studio borrowed-reference operation. Authoring close is a no-op for a live borrowed reference: it preserves the target and other aliases. A null or stale reference reports an access error. Reference input and Error input/output; no reference output or array lifting. Object-operation graph execution has no runtime provider in this delivery. |
| [FROG Server Reference](../application_control/reference.md) | Private Studio symbolic reference constant for This Frog, This Application, Front Panel or a widget identified by its owner document and stable identity. The single reference output is distinct from the widget data value and preserves a complete strict schema when known. Class upcasts are allowed; a generic reference does not implicitly become strict. Saved files contain no native handles. Resolution uses the live authoring provider; graph runtime execution is unavailable in this delivery. |
| [Invoke Node](../application_control/invoke_node.md) | Private Studio configuration of one exact method signature. Parameters retain their identities, types, input/output directions, requirements and declared defaults; a void method has no result terminal. The incoming object reference determines the effective class. The authoring provider supports only advertised real operations; unavailable focus and panel actions remain explicit. Reference and Error pairs stay fixed. No object-operation graph runtime provider is available in this delivery. |
| [Property Node](../application_control/property_node.md) | Private Studio configuration of ordered property rows. Each stable row chooses one real member and Read or Write; its data terminal follows the complete member type. An incoming object reference takes precedence over the implicit symbolic target. Real authoring provider access checks target permissions, latch Value and contained-widget restrictions. Reference and Error pairs stay fixed; Value (Signaling) and graph execution are unavailable in this delivery. |
