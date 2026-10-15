# Synchronization functions

[All functions](../index.md)

8 operations or editor elements; 1 palette folders. Open a page to inspect its exact connector, typing rules and execution limits.

## Operations and editor elements

| Entry | Purpose |
| --- | --- |
| [Dequeue Element](queue/dequeue.md) | Removes and returns the head element in FIFO order. An empty queue waits cooperatively: -1 means no deadline, 0 an immediate attempt. Ordinary timeout is distinguished from invalidation and from a successfully received message. Queue&lt;T&gt; is an execution resource reference; element is the ordinary T value. Public FROG target compilation remains unavailable. |
| [Enqueue Element](queue/enqueue.md) | Adds one element at the tail. A full bounded FIFO waits cooperatively for space: timeout -1 waits indefinitely, 0 attempts immediately. Expiration inserts nothing. It never silently evicts an element; invalidation interrupts the wait with an error. Queue&lt;T&gt; is an execution resource reference; element is the ordinary T value. Public FROG target compilation remains unavailable. |
| [Flush Queue](queue/flush.md) | Atomically removes the present messages and returns them in FIFO order, preserving each complete message boundary even when T itself is an Array. The queue stays valid and usable; an empty FIFO returns an empty outer array. Queue&lt;T&gt; is an execution resource reference; element is the ordinary T value. Public FROG target compilation remains unavailable. |
| [Get Queue Status](queue/status.md) | Reads a coherent instant snapshot: name, capacity, count and waiting operations. Preview and dequeue both count as pending removals. Elements are returned only when requested, without removal; otherwise that output is an empty array. Queue&lt;T&gt; is an execution resource reference; element is the ordinary T value. Public FROG target compilation remains unavailable. |
| [Lossy Enqueue Element](queue/lossy_enqueue.md) | Atomically evicts the oldest element only if a bounded FIFO is full, then appends the new element without waiting. The overflow element is meaningful only when overflow? is true. Ordinary Enqueue does not use this lossy behavior. Queue&lt;T&gt; is an execution resource reference; element is the ordinary T value. Public FROG target compilation remains unavailable. |
| [Obtain Queue](queue/obtain.md) | Creates an anonymous FIFO when name is empty, or obtains an additional access to a same-application named FIFO with exactly the complete element type. The type specimen is not an inserted message. Capacity defaults to -1; an existing named capacity is preserved. Queue&lt;T&gt; is an execution resource reference; element is the ordinary T value. Public FROG target compilation remains unavailable. |
| [Preview Queue Element](queue/preview.md) | Returns the head element without removal or reservation. An empty FIFO waits cooperatively using timeout -1 by default. A successful preview does not prevent another consumer removing that message. Queue&lt;T&gt; is an execution resource reference; element is the ordinary T value. Public FROG target compilation remains unavailable. |
| [Release Queue](queue/release.md) | Releases this obtained access, preserving independently obtained accesses unless force destroy is true. Forced destruction invalidates all accesses and wakes waits with errors. Cleanup also executes with an incoming error. Returns the FIFO snapshot before release and never returns a queue reference. Queue&lt;T&gt; is an execution resource reference; element is the ordinary T value. Public FROG target compilation remains unavailable. |

## Palette folders

| Entry | Purpose |
| --- | --- |
| [Queue](queue.md) | Typed FIFO resource operations. Queue&lt;T&gt; is the shared access reference, not a message or a Front Panel object reference. Each message retains its complete type. |
