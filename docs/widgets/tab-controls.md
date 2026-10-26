# Tab Controls

A Tab groups independent controls and indicators into pages. Only the selected
page is shown. Its contents keep their individual Block Diagram terminals;
a Tab does not combine them into a Cluster.

## Edit pages

Place **Tab Control** from the container palette. Use the tab header's context
menu to add a page before or after, rename, duplicate, remove or reorder it.
Double-click a title to edit the title. Page removal removes its contents;
Undo/Redo restores the corresponding document transaction.

Controls belong to an explicit page identity. Merely overlapping a Tab does
not make a control a page child. Create or move a control into its intended
page using the container's supported placement/drop interactions. The control
retains its own text editing, Array navigation and property menus. Use the
Tab's own frame or header for container operations.

The document stores all pages, including hidden contents and nested Tabs.
Moving or copying a Tab carries its descendants. A resize that would exclude
content is refused rather than silently discarding it. Overflowing titles have
navigation controls.

## Read or drive the selected page

The Tab terminal is an **Enum** representing the page selection. A Control
publishes that selection and can navigate without wiring its terminal. An
Indicator receives a value to choose its displayed page.

Changing pages does not reset child values, interrupt the graph or choose which
code executes. Hidden controls remain part of the program. Use a separate
Case or other explicit dataflow logic when execution must depend on selection.
The editor's displayed page, runtime selection and default value are distinct.

## Validation boundary

The V1 model, persistence and selected native/FIR execution cases were tested.
The initial 24-scenario authoring reception remained incomplete; later tests
of generated graphical applications covered keyboard page navigation separately.
These results do not establish every editor gesture, nested interaction or
Dark/Light and DPI combination. See the dated capability checkpoint before
treating the full Tab acceptance matrix as closed.

[Front Panel](../interface/front-panel.md) · [Run and Highlight](../interface/run-and-highlight.md) ·
[Build](../interface/build.md) · [Current capabilities](../reference/development-checkpoint.md)
