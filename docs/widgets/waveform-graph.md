# Waveform Graph

Waveform Graph displays a complete numeric dataset. Each update replaces that
dataset; it does not accumulate a scrolling history.

| Data | Plot organization |
| --- | --- |
| One-dimensional numeric array | One plot |
| Two-dimensional numeric array | One plot per row |

Right-click the plot area and choose **Properties** to edit the axes, plot
styles or initial samples. Double-click the graph body to find its terminal
on the Block Diagram. To edit an axis title, an end value or a plot name
directly, double-click that text. Enter applies the edit and Escape cancels it.

Use **Visible Items** to show or hide the graph label, X scale, Y scale or plot
legend separately. On both Waveform Graph and Graph XY, drag the legend's
frame to place it anywhere in the same container. Drag its bottom edge to
show more or fewer rows. An empty graph can show **Plot 0** through **Plot 6**
without adding samples. Moving the graph carries its legend with it.
Hiding the legend or closing and reopening the document preserves its placement
and row count. Use **Data** for actions such as copying the displayed dataset.

During Run, a wired indicator displays the dataset received at its terminal.
Saving the document preserves its authored initial samples and presentation.
See [current capabilities](../reference/development-checkpoint.md).
