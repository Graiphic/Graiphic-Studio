# Run and Highlight

Studio can run graphs admitted by its **private local simulation**. Run starts
the session; Highlight makes that session's execution visible. This path is
separate from compiling public FROG Source for a target runtime.

## Start and stop

1. Finish editing values and connections in the Diagram.
2. Use **Run** (`Ctrl+R`) for an admitted graph. Highlight may be off at startup.
3. Turn **Highlight Execution** on or off to change the display of the same session.
4. Use **Stop** to end the session and return to normal editing.

A broken Run icon opens compilation diagnostics. If an operation or value is
unsupported, use the reported diagnostic and its reference page; its presence
in the Navigator does not imply execution support.

## Interact while running

Supported Controls remain usable, including admitted nested fields and cells.
New input affects subsequent natural reads. Values already produced by the
session retain their earlier data. Indicators are read-only.

These runtime inputs are temporary: they do not rewrite saved default values,
Source, authored layout, or edit history. Container indices and scrolling
remain navigation. Layout selection and resize handles are disabled during the
session. Stop restores normal editing without clearing history or moving the
view automatically.

## Queue operations

Eight Queue functions are available under **Programming > Synchronization >
Queue** for private Run/Highlight. They use FIFO order, cooperative waits, real
clock deadlines, independently obtained accesses to named queues, and cleanup
at Stop or the owning scope's end.

`Queue<T>` is a resource reference; a message is an ordinary value of type `T`.
It is separate from object and file references. Queue values in Front Panel
source/indicator widgets are unavailable at runtime. See
[Queue functions](../functions/synchronization/queue.md) for each operation.

## Public execution and advanced services

The public native Numeric F64/Add corridor and the separately admitted SDK
Event/Unbundle path have their own contracts. Their existence does not provide
a general runtime for every Studio authoring object.

Reference menus, types, and authoring services are available in their documented
scope. Generic Property/Invoke nodes still lack a graph executor. .NET,
advanced Events, Matrix collections, and other families retain the limits
listed on their reference pages. Queue has no public Source/lowering/target
runtime contract in this checkpoint.

Read [current capabilities and limits](../reference/development-checkpoint.md)
before relying on a workflow beyond local authoring.
