# Context Help

Context Help is a modeless companion window that explains the source object
under the pointer while leaving the active editor usable.

> This page documents the first implemented version. A current product
> screenshot will be added after the native Windows validation pass; until
> then, this draft is intentionally not linked from the main documentation
> index.

## Open And Close

- Press `Ctrl+H` to show or hide Context Help.
- Choose **Help > Context Help** for the same command.
- Closing Context Help does not close the `.frog` document.

The window is modeless and resizable. It follows semantic objects rather than
raw pointer coordinates, so moving within one object does not continuously
rebuild the help surface.

## Live Front Panel Help

Hover a Front Panel widget to see:

- its stable widget name;
- its concise purpose;
- whether it is a Control or Indicator;
- its value type, including the contained type for an Array;
- its visible label when one is present;
- a detailed-help link when documentation is available.

Labels are identified as documentation elements rather than dataflow controls.

## Live Block Diagram Help

Hover a widget terminal or native function on the Block Diagram to see its
role in the dataflow. Native functions use the same stable catalog identifiers
as the Function Navigator, so their wording and documentation destination stay
consistent before and after placement.

The first version recognizes widget terminals, native numeric functions, and
diagram comments. Per-port required/recommended/optional markers, wire types,
coercions, and broken-wire diagnostics remain later extensions.

## Keep One Object Visible

Press `Ctrl+Shift+L`, or choose **Help > Lock Context Help**, to freeze the
current object. Locking is useful when the pointer must leave the object to
resize the window or open its **Detailed help** link. Repeat the command to
resume live updates.

## Built-In And External Documentation

Graiphic Studio ships built-in help for standard widgets and native functions
in the visible UTF-8 file `config/context-help.ini` beside the Windows
executable.

Document-owned widgets can override that catalog through the common `.frog`
properties `documentation.description` and `documentation.url`. Diagram nodes
can provide a structured `doc` member containing `summary` and `url`. This
allows an external function to explain itself and link to its own published
documentation without changing its execution semantics.

Only `http://` and `https://` detailed-help links are opened by the Studio.

## What Is Saved

Descriptions and documentation URLs attached to source objects round-trip in
the `.frog` document. Whether the Context Help window is open or locked is an
editor workspace concern and does not alter the program.
