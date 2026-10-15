# Structures functions

[All functions](../index.md)

16 operations or editor elements; 3 palette folders. Open a page to inspect its exact connector, typing rules and execution limits.

## Operations and editor elements

| Entry | Purpose |
| --- | --- |
| [Call Chain](call_chain.md) | Places the Call Chain utility on the Diagram. |
| [Case Structure](case_structure.md) | Places a resizable Boolean Case Structure with True and False cases on the Diagram. |
| [Conditional Disable Structure](conditional_disable_structure.md) | Selects the first compile-time condition that matches the resolved target symbols, or Default. It has no runtime selector terminal. |
| [Diagram Disable Structure](disabled_structure.md) | Retains Enabled and Disabled code regions without a condition terminal. Only the Enabled region executes; the Disabled region is shown under a translucent veil. |
| [Elapsed Time](elapsed_time.md) | Places the Elapsed Time utility on the Diagram. |
| [Event Structure](event_structure.md) | Places a resizable event-case container with a fixed timeout interface and a vertically movable typed Event Data Node. |
| [Feedback Node](feedback_node.md) | Places the Feedback Node glyph on the Diagram. |
| [Flat Sequence Structure](sequence_structure.md) | Places ordered frames side by side. Add, duplicate, reorder or resize a frame from its border. Wires may carry data to later frames, never to earlier frames. |
| [For Loop](for_loop.md) | Places a resizable counted loop. N receives and exposes the I32 count; the movable i terminal exposes the current I32 iteration inside the body diagram. |
| [In Place Element Structure](in_place_element_structure.md) | Access and replace data using paired border nodes. Right-click the border to add a pair; drag a node to move both sides or stretch its bottom edge to expose more elements. |
| [Select](select.md) | Places the Select structure glyph on the Diagram. |
| [Tick Count](tick_count.md) | Places the Tick Count utility on the Diagram. |
| [Timed Loop](timed_loop.md) | Places a resizable While-style loop with orange scheduling surfaces for initial timing, iteration feedback, next-iteration updates, and completion results. |
| [Wait](wait.md) | Places the Wait utility on the Diagram. |
| [Wait Until Next Multiple](wait_until_next.md) | Places the Wait Until Next Multiple utility on the Diagram. |
| [While Loop](while_loop.md) | Places a resizable post-test loop. Its movable I64 iteration and Boolean condition terminals belong to the encapsulated body diagram. |

## Palette folders

| Entry | Purpose |
| --- | --- |
| [Execution Control](execution_control.md) | Opens the execution-control structure repository. |
| [Synchronization](synchronization.md) | Opens the synchronization repository. |
| [Timing Utilities](timing_utilities.md) | Opens the timing utilities repository. |
