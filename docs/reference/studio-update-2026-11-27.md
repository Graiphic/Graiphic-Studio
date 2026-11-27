# November 27 Studio update

The build numbers identify the Studio versions used to exercise these workflows.

| Workflow | How to use it | Studio build |
| --- | --- | --- |
| Open a second Studio window | Choose **File → New Studio Window**. Use **Open** in the second window for `.frog`, `.frprj` and `.ftype` files. If another session saves the same file first, the conflict message lets you keep your edits and save a separate copy. | 0.0.9.903 |
| Edit a class’s private data | Open **Private Data** from Project Explorer. Use the Front Panel canvas and palette to place or move fields in the existing cluster. Inherited fields are read-only. | 0.0.9.926 |
| Edit graph plots | Click the eye in the legend to show or hide a plot. Edit its name or open the line sample’s menu to change its appearance. Select the legend to move or resize it independently, or select the whole graph to move it with its legend. | 0.0.9.899 |
| Place and undo a Graph XY | Choose **Graph XY** from Visualization. Click and place it or drag the tile onto the Front Panel. **Undo** removes the graph and its terminal. **Redo** restores both at the same position. | 0.0.9.951 |
| Edit an instrument’s scale | Double-click its minimum or maximum. The scale uses the font size saved in the FROG. | 0.0.9.910 |
| Run a For Loop with a negative count | Connect the numeric count to **N**. A negative count runs zero iterations. A supported numerical coercion is applied at the receiving terminal when the diagram runs. | 0.0.9.930 |
| Reverse a Feedback Node | Choose **Change Direction** in the node’s context menu. Its input and output move to the other sides, and the existing wires follow their terminals. | 0.0.9.935 |

[Front Panel](../interface/front-panel.md) · [Window workflow](../interface/window-workflow.md) · [Numeric instruments](../widgets/numeric.md#instruments-and-sliders) · [November 25 update](studio-update-2026-11-25.md)
