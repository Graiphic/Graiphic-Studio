# Branch an error wire to a loop and a queue

In Graiphic Studio 0.0.9.781, one error wire can stop a loop and carry the full error in a queued message. Each destination reads the value it needs.

## Wire the two destinations

1. In the loop body, wire the error cluster to the loop's conditional terminal. For a **For Loop**, enable its **Conditional Terminal** first. The terminal offers **Stop on Error** and **Continue while Error** when the wire carries an error. While Loop and Timed Loop also accept the cluster.
2. Create a message cluster with a field declared `Variant`. On **Bundle By Name**, select that field and branch the same error wire to the field input. A small red point on the receiving row marks the implicit conversion. The wire carries the error cluster up to that row. A field of any name can have this type.
3. Wire the updated message to **Enqueue Element**. After **Dequeue Element**, extract the field with **Unbundle By Name**. Wire it to **Variant To Data** and wire an error-cluster specimen to the `type` input. Its output carries `status` (Boolean), `code` (I32) and `source` (String) from that message.

| Loop mode | `status = True` | `status = False` |
| --- | --- | --- |
| Stop on Error | Stop after this iteration | Continue |
| Continue while Error | Continue | Stop after this iteration |

A warning has `status = False`, even when `code` is nonzero. A For Loop also stops when it reaches the iteration limit set by `N` or its auto-indexed inputs.

## Check the result

Set `N` to 5. Enqueue one message per iteration. In **Stop on Error** mode, send `(False, 7, "avertissement")` first and `(True, 42, "test")` second. The loop finishes after two iterations. The first dequeue yields the warning and the second yields the error. In **Continue while Error** mode, reverse the two inputs. The loop again finishes after two iterations and the queue yields the error followed by the warning.

To check a source that already carries a Variant, insert **To Variant** on the message branch. The red point disappears from the receiving row. The same **Variant To Data** node still recovers the original cluster.

[For Loop](../functions/structures/for_loop.md) · [Bundle By Name](../functions/cluster/bundle_by_name.md) · [Working with queues](../functions/synchronization/queue.md) · [Variant To Data](../functions/variant/to_data.md)
