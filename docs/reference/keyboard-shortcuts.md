# Keyboard Shortcuts

## Documents

| Shortcut | Action |
| --- | --- |
| `Ctrl+N` | New document |
| `Ctrl+O` | Open document |
| `Ctrl+S` | Save |
| `Ctrl+Shift+S` | Save As |
| `Ctrl+W` | Close |
| `Ctrl+Q` | Exit |

## Windows And Views

| Shortcut | Action |
| --- | --- |
| `Ctrl+E` | Raise the companion Front Panel or Block Diagram without moving or resizing either window |
| `Ctrl+Shift+E` | Open or raise the live Source view |
| `Ctrl+T` | Tile the Front Panel and Block Diagram |
| `Ctrl+H` | Show or hide Context Help |
| `Ctrl+Shift+L` | Lock or unlock Context Help on its current object |

## Editing

| Shortcut | Action |
| --- | --- |
| `Ctrl+Z` | Undo |
| `Ctrl+Shift+Z` | Redo |
| `Ctrl+C` | Copy selected content |
| `Ctrl+V` | Paste |
| `Ctrl+A` | Select all editable objects in the active Front Panel or Diagram |
| `Delete` or `Backspace` | Delete selection |
| Arrow keys | Nudge selection by one grid unit |
| `Shift` + arrow | Nudge by a larger step |
| `Escape` | Cancel the active mode or tool |

## Pointer Modifiers

| Modifier | Action |
| --- | --- |
| `Shift` while moving | Lock to the first horizontal or vertical axis |
| `Ctrl` while moving | Drag a duplicate while held |
| `Shift` while resizing | Preserve proportions |
| `Shift` while selecting | Add or remove objects from a multi-selection |
| Middle mouse drag | Pan the Front Panel, Block Diagram, or Icon Editor |

## Text And Icon Editing

| Shortcut | Action |
| --- | --- |
| Main `Enter` while editing a Diagram comment | Insert a line break |
| Keypad `Enter` or click outside a Diagram comment | Commit the comment and leave editing |
| `Enter` in a single-line name/value field | Commit when that editor supports it |
| `Escape` in a name/value field | Cancel the active edit |
| `Ctrl+Backspace` / `Ctrl+Delete` while editing text | Delete the preceding / following word |
| `Ctrl+Shift+Delete` | Clear all Icon Editor layers |
| `Ctrl++` / `Ctrl+-` | Increase or decrease the selected text font; otherwise zoom the active canvas within its allowed range |

Some commands are context-sensitive. Text and embedded Array-widget selection
take priority over canvas zoom, so `Ctrl++` and `Ctrl+-` change the selected
font instead of the view in those contexts. The Block Diagram zoom range is
`60%` to `150%`. A shortcut has no effect when the current selection cannot
perform the operation.

`Ctrl+R` opens the same compilation diagnostics as clicking a broken Run icon
when the document has compilation errors. For a compilable document it currently
does nothing; runtime execution is a separate delivery. Recent editing changes
are recorded in the [development checkpoint](development-checkpoint.md), with
their remaining qualification limits.
