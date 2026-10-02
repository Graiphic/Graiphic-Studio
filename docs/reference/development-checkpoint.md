# Development checkpoint — 2 October 2026

The current local Graiphic Studio delivery is **0.0.4.061**. Its executable was
compiled, signed and checked against the Desktop shortcut. Studio `main` is
published at `0734b4a046d08e99486f6360ef6402f4fb6a4acf` (2 October), verified
against the remote. It contains the accumulated editor and contour corrections
and the binding context-menu, invariant function-icon, compact structure-label
For Loop frame contrast and initial Wire Label text selection corrections.

Regression tests remain paused. The last complete attempt failed on **0.0.3.935**:
**300/403 passed, 103 failed**. Recent behavior below is implemented and published;
compilation and publication do not establish completed functional or visual qualification.
Existing screenshots belong to their dated captures, not a new UI review.

## Aggregates and text

Subdiagram Labels use the compact 11 pt default across creation, show and
typography refresh. Explicit sizes/styles remain preserved, including an
explicit 15 pt. Display and editing share the stored font.

Cluster **None** keeps manual dimensions when children change size. **Size to Fit**
follows the content bounds during enlargement and reduction. Copying retains the
mode and recalculates layout. Vertical/horizontal layout follows the logical
field order after insertion or Reorder Controls in Cluster, with values retained.
Constant conversion reuses the constant creation rules rather than retaining
control-only decoration. Boolean/error constants use compact bounds.

Arrays have **Add Element Gap / Remove Element Gap** and **Size to Widest Element**.
Widest is a one-shot action with a small margin; repeat it after content changes.
Nested arrays inside clusters in an array of clusters retain cell editing and
update the selected parent element.

Changing font, size or style fits targeted text in both dimensions. Rename editing
supports word selection/deletion and ordered Undo without duplicate text.
Comment main Enter inserts a newline; keypad Enter or click-away commits.
Waveform X/Y bound editing aligns with the value, commits with Enter/click-away,
cancels with Escape and retains the last valid bound when input is invalid.

Color Box is a fixed-size colored square on both canvases and during placement.
Converting it to U32 selects hexadecimal and shows the radix. Radix changes the
display base without changing the value or numeric representation.

## Diagram and selection

Creating a Wire Label immediately selects the whole displayed hint for
replacement. The hint stays transient; untouched validation stores no text,
Escape cancels and one committed edit is one Undo action. Existing labels
also open with their complete text selected.

For Loop frame/default inner frame use dark #575756 in Light and off-white
#F8FAFC in Dark, including the folded corner and rear sheet outlines. Existing
body tint/opacity and explicit saved body/inner-frame colors remain preserved.
The native renderer and placement preview reuse the same resolved geometry.

Function artwork is identical in Light and Dark UI themes: the same canonical
SVG, body, border, symbols and internal text across palette, help, placement
preview and Diagram. The theme-dependent yellow function fallback is superseded.

All function selection follows the actual visible contour with zero geometry
offset, including intrinsic SVGs, extended functions, Array/Matrix and Cluster
functions, and Frog calls. Normal and locked selection share the geometry.
Widget placement bands remain a separate contract. This supersedes the former
external function-selection gap from 2 October 2026.

Right-clicking a binding opens its menu without adding selection or an aura.
The existing left-button selection is retained. Connection points remain visible
while the binding menu is open, then return to ordinary hover behavior on close.

Wire context creation offers nested and direct Constant/Control/Indicator actions.
It carries the complete type and owning sub-diagram, preserves existing connections
and never adds a second source. Constant/Control may be created unwired when
automatic connection is impossible; an indicator can branch from the source.

Enum connections compare their ordered definitions. Moving an object preserves
valid semantic connections while updating geometry. Bundle By Name insertion
uses the dedicated cluster input; its output preserves the complete input cluster.
Shift-register inference prefers the exterior input source, then the interior
output source. Downstream indicators adapt or report incompatibility.

Structure selection includes nested contents. Rectangle overlap can select visible
iterator/conditional terminals. Multiple Delete uses one logical Undo action.
Selection/drop aura follows zoom and the actual valid drop target. Color and
context tools prioritize the contained object under the pointer.

Large Diagram navigation uses visible rendering; moving a large selection uses
a lightweight preview before the final commit. This is an implementation strategy,
not a measured claim of LabVIEW-equivalent performance.

## Interface and windows

Custom pattern menus use **Create... / Modify...** and **Saved Pattern**.
**Save** writes the pattern and keeps Custom Pattern open without applying it.
**Save Apply** writes, applies and closes. Failed saving/validation keeps the dialog
open. Saving and applying remain distinct actions.

Options Large and navigation typography have stable layouts and margins intended
to keep descenders visible. Highlight Execution, speed and Step keep their icons
stable while clicked. `Ctrl+R` opens broken-Run diagnostics when compilation fails;
it currently has no action for a compilable document with the runtime absent.

Window minimize/restore/open transitions last about 200 ms and respect the system's
reduced-animation preference. Rapid requests reverse or cancel the current effect;
the minimize transition finishes before the real window is hidden.

## Source and runtime limits

The [Document Model](document-model.md) distinguishes Studio authoring drafts from
public canonical `.frog` source. Public read/preserve/edit, migration, semantic
validation, lowering and execution are separate capabilities. Runtime POC is OFF
in this delivery. The public specification owns portable syntax and semantics;
these editor changes do not introduce a new source version or certify all targets.
