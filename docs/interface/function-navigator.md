# Function Navigator

The Function Navigator is the Diagram counterpart of the Widget Navigator. It
browses dataflow functions, opens families, and starts placement on the Diagram.

The Numeric family presents its operations as compact, source-backed tiles.

![Numeric functions in the dark Function Navigator](../../assets/screenshots/function-navigator/numeric-functions-dark.png)

## Hierarchy

The root Navigator groups functions by programming domain. Selecting
**Programming > Numeric** opens the current Numeric operations, including
arithmetic, rounding, range, random, and array-reduction functions.

The hierarchy behaves like the Widget Navigator: move into a family to open it,
choose a function to begin placement, and use `Escape` to cancel the active
placement command.

## Transient And Pinned Windows

An unpinned Navigator appears near the pointer and closes when the user clicks
elsewhere, presses `Escape`, or starts another command. Pinning keeps that
Navigator open as an independent Diagram tool window.

Pinned function windows use the same close control, sizing rules, theme, font
scale, tile spacing, and responsive reflow as pinned Widget Navigators. Several
pinned Navigator windows can remain open at the same time.

## Dataflow Role

Placing a function creates a Diagram node; it does not execute the operation
inside the palette. The Diagram remains the executable dataflow source, and the
runtime evaluates the placed node only when it participates in an executable
graph.

Numeric function icons describe operation semantics. Their connector types and
runtime behavior must remain compatible with the FROG source and runtime
contracts rather than being inferred from their visual color alone.
