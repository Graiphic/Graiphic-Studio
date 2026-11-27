# Application Control functions

[All functions](../index.md)

5 operations or editor elements; 0 palette folders. Open a page to inspect its exact connector, typing rules and execution limits.

## Operations and editor elements

| Entry | Purpose |
| --- | --- |
| [Close Reference](../application_control/close_reference.md) | Closes a borrowed reference without deleting its target or its other aliases. Check the error output for a null or stale target. This node has a reference input and no reference output. |
| [FROG Server Reference](../application_control/reference.md) | Produces a symbolic reference to this FROG, the application, the Front Panel or an identified widget. A strict reference carries the value schema. The saved identity resolves in its owning document. Wire the reference to a Property or Invoke Node to operate on that object. |
| [Invoke Node](../application_control/invoke_node.md) | Calls the selected method on the target reference. The method signature determines the required and optional inputs, outputs and return value. A void method has no result terminal. Check the error output. Availability depends on the member, its class and the execution host. |
| [Property Node](../application_control/property_node.md) | Drag the blue bottom handle to extend the Property Node. New rows follow the available properties in Select Property for the effective target, starting after the last eligible configured row. The last available property repeats at the end of the list. Existing rows keep their properties, modes and wires when you extend the node. Press Esc during the drag to restore the starting layout. Each row has a typed data terminal and uses the member’s Read or Write permissions. A wired reference determines the effective target. Reference and Error connectors remain fixed. Execution support depends on the selected property and target profile. |
| [To More Specific Class](../application_control/to_more_specific_class.md) | Specializes the input reference to the class supplied by target class. The output addresses the original control. A strict model also specifies the Value type. An incompatible target produces an invalid reference and an error. |
