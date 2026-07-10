# Screenshot Guide

Screenshots are part of the public Graiphic Studio documentation.

## Storage

Store screenshots under:

```text
assets/screenshots/
```

Recommended folders:

```text
assets/screenshots/front-panel/
assets/screenshots/widget-navigator/
assets/screenshots/interface-map/
assets/screenshots/icon-editor/
assets/screenshots/widgets/
```

## Naming

Use stable, descriptive names:

```text
front-panel-empty-dark.png
widget-navigator-string-path.png
interface-map-bound-slots.png
icon-editor-layers.png
```

## Rules

- Capture real Studio UI.
- Prefer stable, visually validated states.
- Avoid screenshots with transient mouse artifacts unless documenting cursor
  behavior.
- Keep screenshots focused on the feature being explained.
- Update screenshots when the UI contract changes.
- Capture from the canonical signed native executable.
- Verify text, active states, disabled states, and popup bounds at 100%.
- Do not publish a screenshot from an unfinished visual experiment.

## Documentation Pattern

Introduce a screenshot with one sentence that tells the reader what to look
for. Follow it with the workflow or rule the image demonstrates. Alt text must
name the visible feature rather than repeat the file name.

Screenshots document appearance; prose documents behavior. A page should not
rely on color or an image alone to explain a required action.
