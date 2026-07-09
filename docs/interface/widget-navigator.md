# Widget Navigator

The Widget Navigator is used to browse widget families and place widgets on the
Front Panel.

## Families

Current families:

- Numeric
- Boolean
- String and Path
- Ring and Enum

The navigator groups widgets by user meaning, not by internal implementation.
For example, Boolean contains both LED-style boolean widgets and text buttons.

## Folder Behavior

Clicking a family folder opens its widget choices. When a direct folder click is
used as a placement action, the first standard widget in that family is used.

This keeps the navigator predictable:

- Numeric opens or places Numeric Control.
- Boolean opens or places Text Button as the first standard button-style entry.
- String and Path opens or places String Control.

## Screenshots

Screenshots for this page belong in:

```text
assets/screenshots/widget-navigator/
```
