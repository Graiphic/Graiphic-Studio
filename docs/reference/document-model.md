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

## Document Icon

The document icon is editable SVG-oriented data. Its layer metadata is retained
inside the icon SVG so Graiphic Studio can reopen it. The 40 x 40 chrome square
is only a preview target.

## Media

Imported media should remain an explicit document asset relationship. Before a
document has a permanent location, Graiphic Studio may stage temporary assets;
saving transfers them into the document's managed location.

## Runtime Boundary

The Diagram remains the authoritative executable graph. Runtime execution must
consume explicit source and compiled artifacts, never Studio-only selection or
window state.
