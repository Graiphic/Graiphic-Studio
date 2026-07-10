# Studio Options

Open **Tools > Options...** to configure Graiphic Studio without changing the
execution meaning of the current `.frog` document.

The Options window is divided into three categories: Appearance, Front Panel,
and Icon Editor. Changes are applied only after pressing **OK**. **Cancel** and
the close button leave the current settings unchanged.

## Appearance

Appearance selects the interface theme. The current release provides **Dark**
and **Light** profiles. Selecting a profile updates the preview immediately so
you can inspect the title area, menus, toolbar, Front Panel, widget selection,
grid, and status bar before applying it.

![Light theme preview](../../assets/screenshots/options/appearance-light-preview.png)

Theme colors are profile-based rather than embedded in individual windows.
This keeps the shell, menus, popups, palettes, editors, text, icons, and
interaction states on one shared visual system. Additional profiles can be
added without redefining `.frog` source semantics.

## Front Panel

Front Panel options configure the editing grid:

- **Show front panel grid** controls grid visibility.
- **Default grid size** sets the grid pitch in pixels.
- **Enable grid alignment** enables snap-to-grid placement.
- **Grid draw style** selects **Lines**, **Dots**, or **Graph Paper**.

![Front Panel grid options](../../assets/screenshots/options/front-panel-grid.png)

Pressing **OK** applies these values to the current Front Panel and stores them
as defaults for a new document. Grid appearance and snapping are editing
preferences; widget placement stored in a saved `.frog` document remains
explicit source-owned layout.

## Icon Editor

The Icon Editor category manages folders that contain reusable SVG glyphs.

- **Add Folder...** selects a folder containing SVG assets.
- Selecting a listed path enables **Remove**.
- **Remove** forgets the folder from the local profile; it does not delete the
  folder or any SVG file from disk.

Configured folders are available again the next time Graiphic Studio starts.
If the Icon Editor is already open, applying Options refreshes its glyph
library immediately.

## Preference Storage

Studio preferences are stored in the local user profile:

```text
%APPDATA%\Graiphic\Frog Engine 1.0\frog-studio.ini
```

The selected theme, Front Panel grid defaults, and glyph-folder list are
Studio preferences. They do not become hidden runtime behavior and do not
replace source-owned `.frog` document properties.
