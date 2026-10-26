# Run and Highlight

Normal **Run** uses the admitted **native** program/session path. Highlight
shows that session's execution; it is not a separate calculation engine.
**Simulation** remains an explicitly selected private mode for the profiles
that name it. It is not a silent fallback for unsupported native operations.
Studio Draft admission and public FROG Source lowering remain distinct.

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

Native coverage extends beyond the earlier F64/Add corridor to selected exact
integer and owned-value operations, structures and providers. The dated corpus
checkpoint records Native Fast and Native Debug cases separately from explicit
Simulation, expected errors, stops and persistence-only checks.

Selected real-target Property/Invoke operations have measured profiles; this
does not admit every property, method or host action. File and dynamic-event
examples in the dated corpus use explicit Simulation. .NET and other advanced
providers keep their operation-specific limits. Queue's private execution
provider does not establish a general public Source/lowering/target contract.

For a standalone application, open [Build](build.md) with the hammer button.
Run success does not bypass Build's toolchain, provider or presentation checks.

Read [current capabilities and limits](../reference/development-checkpoint.md)
before relying on a workflow beyond local authoring.
