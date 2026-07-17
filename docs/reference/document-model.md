# The `.frog` Document Model

A `.frog` file is the source of truth for a Graiphic Studio project. Studio
windows edit explicit document data rather than keeping hidden runtime state.

## Front Panel

The Front Panel owns widget instances, object geometry, labels, initial values,
visibility, lock state, groups, z-order, colors, and instance-level overrides.

## Public Interface

The public interface exists independently from the Front Panel. Interface Map
patterns arrange public ports visually. Front Panel bindings explicitly connect
widget value properties to those ports.

Controls bind toward public inputs. Indicators bind from public outputs. The
Diagram will project these as `interface_input` and `interface_output` nodes;
the Interface Map itself does not execute code.

## Diagram

The Diagram owns the executable dataflow graph. Operations placed from the
Function Navigator become explicit entries in `diagram.nodes`; a primitive
node uses `kind = "primitive"` and a published namespaced `type`, such as
`frog.core.add` or `frog.math.sqrt`.

Studio also records the authored Diagram `layout` for each placed node. Layout
controls where the node reappears when the document is reopened, but it does
not replace dataflow semantics. Execution will be determined by the node type,
typed ports, and explicit connections in `diagram.edges`.

Catalog entries without a published primitive contract are not serialized as
executable nodes. This keeps the `.frog` document valid while the Function
Navigator can still preview future operation families.

## Authoring View State

The document may preserve enough non-executable state to reopen the authored
workspace faithfully:

- `front_panel.canvas.width` and `front_panel.canvas.height` describe the useful
  Front Panel client surface;
- `ide.front_panel.zoom_percent` and `viewport_origin` restore the Front Panel
  view;
- the Diagram records its own zoom and viewport origin and always uses a solid
  editing background;
- `ide.workflow.views` may carry useful client width and height for the Front
  Panel, Diagram, and Source windows, plus recoverable position, visibility, or
  maximized hints.

Window positions are clamped to the monitors available when reopening. Native
window chrome, monitor identity, theme, language, navigation font size, and
local glyph-folder paths remain local Studio preferences. They are not program
semantics.

## Document Icon

The document icon is editable SVG-oriented data. Its layer metadata is retained
inside the icon SVG so Graiphic Studio can reopen it. The 40 x 40 chrome square
is only a preview target.

Imported SVG content may be normalized into independently editable visible
regions. This authoring segmentation remains presentation metadata; runtimes
consume the final SVG visual rather than Icon Editor selection state.

## Media

Imported media should remain an explicit document asset relationship. Before a
document has a permanent location, Graiphic Studio may stage temporary assets;
saving transfers them into the document's managed location.

## Runtime Boundary

The Diagram remains the authoritative executable graph. Runtime execution must
consume explicit source and compiled artifacts, never Studio-only selection or
window state.
