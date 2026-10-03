# Archived development checkpoint

Historical evidence; see [current checkpoint](development-checkpoint.md).

# Development checkpoint — 3 October 2026

The current local Graiphic Studio delivery is **0.0.4.231**. Its executable was
compiled, signed and checked against the Desktop shortcut. Studio `main` is
published at `0734b4a046d08e99486f6360ef6402f4fb6a4acf` (2 October), verified
against the remote. It contains the accumulated editor and contour corrections
and the binding context-menu, invariant function-icon, compact structure-label
For Loop frame contrast and initial Wire Label text selection corrections.
The subsequent toolbar contrast, For layers/background, Boolean selection,
recursive containers, per-terminal unconnected circles and Reorder toolbar corrections
are delivered locally and not yet published. The For body stays close to the
general Diagram with separate rear-sheet traces; True/False selection follows
the authored rounded border, including fields in nested Clusters.

Regression tests remain paused. The last complete attempt failed on **0.0.3.935**:
**300/403 passed, 103 failed**. The earlier behavior below was published at that
checkpoint; the subsequent corrections remain local. The explicitly requested
systematic container checks passed four native owners on 0.0.4.137. Later port
Reorder, numeric type conversion and Highlight speed coverage is compiled but
not run under the pause. The Options scrollbar owner is registered and unrun;
numeric value conversion still depends on the absent runtime. See the
[ordered queue](../../../FROG-Context/Current/studio-request-queue-2026-10-02.md)
and its dated receipts for exact results and pending scope.
Compilation and publication do not establish completed functional or visual qualification.
Bundle/Unbundle By Name now lists duplicate occurrences by ordinal/full path,
uses stable IDs after reorder and offers top resize with exact cancellation.
Its two registered owners compile but are not executed under the pause.
Moving a wired node across graph boundaries now creates type-preserving Last
Value tunnels using the common mouse/keyboard move transaction and automatic
route planner. Its two registered owners compile without execution under the pause.
Existing screenshots belong to their dated captures, not a new UI review.

Scalar Numeric Diagram constants now use permanent measured text fitting in
both directions, default 11 pt, with no manual resize. Highlight For supports
per-invocation shift registers and an indexed input without N. Their owner
coverage is compiled, not executed while paused. While/Feedback remain explicit
simulation limitations. These local corrections have dated delivery receipts.

Custom binding authoring offers a + outside a free edge position with a 30%
ghost, preserves existing binding identities and positions, and reuses disabled
slots. Reset now has the shared action-button hand cursor, including capture
and disabled-state handling. These owners are compiled, not run under the pause.
Options now handles a double-click's second press as a normal button press.
Templates uses full themed rows, a flat border and buffered drawing. Its two
Light/Dark UI owners are registered, not run under the pause. Controlled
performance measurements now pass seven controlled scenes through 5,000 objects,
including exact Undo/Redo after a paste to 10,000. Mixed paste improves from
18.7 s to 281 ms, keyboard movement from 11.3 s to 69 ms, and cold validation
from 340 to 79 ms. The 64 MiB history budget remains unchanged. Exact raster
parity passes 3,072 cases, and diagnostic-location parity passes 416 cases.
Native Windows clipboard publication remains unverified. See the
[performance receipt](../../../FROG-STUDIO/native-portable-engine/docs/reponses/2026-10-03-performances-diagrammes-charges.md).
The ordered queue continues at Bundle/Unbundle By Name, item 18.

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

For Loop front frame/default inner frame and folded corner use #575756 on a
light Diagram and #F8FAFC on a dark Diagram. Rear/middle sheet traces use
#374151 on a dark Diagram and #575756 on light. Default body uses #C4D9E8 at
10% over the actual general Diagram background, including document overrides.
Explicit saved body/inner-frame colors, opacity and transparency remain preserved.
The native renderer and placement preview share this rule in Direct2D and GDI
with the same geometry. This latest appearance correction remains local.

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
Custom Pattern now has a single content page with title close, **OK** and
**Cancel**. **OK** validates, saves and applies; Cancel/close discard the draft.
Authoring dimensions are 32–128 px. Larger legacy descriptors remain readable
and are preserved on cancellation. Failed saving/validation keeps the draft
open. This replaces the previous Save/Save Apply footer and category navigation.
During a binding drag, its associated rectangle uses the theme selection fill;
the boundaries follow the current accepted pattern geometry and revert when
the drag ends. This coverage is compiled, not executed while paused.

Options Large and navigation typography have stable layouts and margins intended
to keep descenders visible. Highlight Execution, speed and Step keep their icons
stable while clicked. `Ctrl+R` opens broken-Run diagnostics when compilation fails.
Since local 0.0.4.160 it starts the document simulation when compilation passes
and Highlight is armed. Repeated presses during play/pause preserve the active
session. Without Highlight, the absent runtime still prevents execution.
The shortcut coverage is compiled, not executed under the pause.
Local 0.0.4.162 removes the dotted focus rectangle from Highlight, speed and
Step while retaining native keyboard activation and accessibility. Its focused
rendering coverage is compiled, not executed under the pause.

Highlight/Step monochrome ink follows the toolbar theme and button state,
including disabled state, using the same SVG geometry. The lit bulb uses
#8B5A00 on light surfaces and #FFD050 on dark to keep its active signal legible.
This latest toolbar contrast correction remains local and compiled; tests are
paused, so visual and functional acceptance is still pending.

Window minimize/restore/open transitions last about 200 ms and respect the system's
reduced-animation preference. Rapid requests reverse or cancel the current effect;
the minimize transition finishes before the real window is hidden.

## Source and runtime limits

The [Document Model](document-model.md) distinguishes Studio authoring drafts from
public canonical `.frog` source. Public read/preserve/edit, migration, semantic
validation, lowering and execution are separate capabilities. Runtime POC is OFF
in this delivery. The public specification owns portable syntax and semantics;
these editor changes do not introduce a new source version or certify all targets.

Storage lot 20 is locally delivered in 0.0.4.206 with three document modes. Private revision 3 describes opt-in numeric chunks; Readable remains revision 2 and public 0.1 is unchanged. Exact numeric text, dimensions and indices survive conversion; corrupt codecs/records reject loading. Three native owners compile and keyboard coverage is extended, unrun under the pause. This reduces saved size without claiming lazy loading or working-memory gains. [Storage profile](../../../FROG/docs/studio-array-storage-v1.md). Queue now continues at 21; cadence 75.

Enum sizing lot 21 is locally delivered in 0.0.4.210: current item and real typography determine growth/shrink with fixed padding and complete arrows. Repeated cells share their current extent and clusters retain their authored sizing policy. Two registered owners compile, unexecuted under the pause. Queue continues at 22, cadence 76.

Lot 22 is locally delivered in 0.0.4.213: the axis editor grows before native painting and settles its text viewport after actual keystrokes; endpoint/tick formatting and measured margins are shared while plot geometry stays stable during editing. Three registered owners compile, without test execution under the pause. [Receipt](../../../FROG-STUDIO/native-portable-engine/docs/reponses/2026-10-03-waveform-bornes-saisie-largeur.md). Cadence 77 at this closure; continue at 23.

Lot 23 is locally delivered in 0.0.4.216: Front Panel release transfers the complete selection into its nested target; Diagram constants use the same whole-group preflight and ordered insertion, retaining values and free-placement offsets in one drag transaction. Two registered owners compile, without test execution under the pause. [Receipt](../../../FROG-STUDIO/native-portable-engine/docs/reponses/2026-10-03-ajout-groupe-cluster-glisser-deposer.md). Cadence 78 at this closure; continue at 24.

Lot 24 is locally delivered in 0.0.4.222: rename rendering tracks root/field/cell identity through projected values, keeps mutation and geometry in one redraw cycle, seeds editable DirectWrite text with the current backdrop and invalidates both old and new footprints. Two registered owners compile, without test execution under the pause. [Receipt](../../../FROG-STUDIO/native-portable-engine/docs/reponses/2026-10-03-renommage-rendu-sans-residus.md). Cadence 79 at this closure; continue at 25.

Lot 25 is locally delivered in 0.0.4.226: CTest-only number/name badges on both canvases; all 417 generated number mappings checked in declaration order. Two registered owners compile, without test execution under the pause. [Receipt](../../../FROG-STUDIO/native-portable-engine/docs/reponses/2026-10-03-identification-visuelle-ctest.md). Cadence 80 at this closure; continue at 26.

Lot 26 is locally delivered in 0.0.4.231: incident wire geometry captured once per gesture; compact simple paths, stable remote junctions, continuous connected-selection movement and exact cancellation. Two registered owners compile, without test execution under the pause. [Receipt](../../../FROG-STUDIO/native-portable-engine/docs/reponses/2026-10-03-fils-adaptation-deplacement.md). Cadence 81 at this closure; continue at 27.
