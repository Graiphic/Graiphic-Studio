# The `.frog` document model

A `.frog` document records the authored program: widgets, values, labels,
bindings, Diagram objects, connections, and visual layout. Studio's three views
show different parts of that document.

## Know the format before exchanging a file

| Format | Envelope | Purpose |
| --- | --- | --- |
| Studio Readable draft | `format: "frog.document.draft"`, `draft_revision`, `frontPanel` | Product authoring representation; revision depends on the features used |
| Studio Automatic/Compact draft | Private numeric-storage revision | Opt-in compact numeric Array storage |
| Public FROG Source | `spec_version`, optional `front_panel` | Published language contract and admitted profiles |

The shared extension does not make these formats interchangeable. Studio has a
separate public-source reader and preservation/transaction writer. Reading and
preserving a file do not imply complete visual editing, semantic validation,
lowering, or runtime support for its entire graph.

Revision 2 describes the older readable baseline, not every current document.
The example index includes revisions 2, 4, 6 and 7; linked standard Type Def
documents use revision 8. Application version, draft revision and public Source
version are different identities. Preserve the actual envelope rather than
rewriting its revision to match an older documentation snapshot.

The [FROG source guide](https://github.com/Graiphic/FROG/blob/main/Expression/Frog%20source%20guide.md)
and [compatibility reference](https://github.com/Graiphic/FROG/blob/main/Expression/Source%20compatibility%20and%20profiles.md)
define the public source boundary. See [current capabilities](development-checkpoint.md)
for the Studio checkpoint.

## What each part owns

| Part | Authored data |
| --- | --- |
| Front Panel | Widget instances, initial values, geometry, labels, visibility, lock state, groups, order, and appearance overrides |
| Public interface | Typed input/output declarations and explicit widget associations |
| Interface Map | Visual slot pattern and binding placement |
| Block Diagram | Nodes, typed ports, edges, structures, constants, annotations, and layout |
| Icon and media | Explicit artwork and asset relationships |

The public interface can exist independently of a Front Panel in the language.
Studio's draft writer currently derives its saved interface from bound widgets.
An Interface Map slot alone does not declare or execute a function.

Diagram objects carry explicit identities and saved configuration. Public
primitive types such as `frog.core.add` retain their published contracts;
editor-managed and private functions retain their separate support boundaries.
Geometry, SVG artwork, and selection never substitute for an execution contract.

## Values, design, and view state

Array cells keep distinct values while sharing an element design. Cluster fields
keep stable identities and order even when their labels or positions change.
This distinction lets a value edit affect one addressed cell without rewriting
the shared layout or another row.

The document can preserve zoom, viewport origin, canvas dimensions, and useful
window reopen hints. Unavailable monitor positions are clamped when reopening.
Those view details do not change the graph's meaning.

Theme, interface language, navigation size, and local glyph-folder locations are
Studio preferences. Hover, selection, open menus, and temporary runtime inputs
are workspace/session state. They do not become executable data.

## Icon and custom bindings

The icon retains editable SVG-oriented data and layer metadata. The toolbar
preview is independent of the logical icon dimensions. Custom layout descriptors
preserve slot identities, dimensions, explicit positions, and disabled slots;
see [Custom bindings](custom-bindings.md).

## Documentation metadata

A widget may carry `documentation.description` and `documentation.url`.
A Diagram node may carry a `doc` object with `summary` and `url`. These describe
the existing object and do not alter its type or ports.

## Execution boundary

Private Studio Run/Highlight, public-source compilation, and target runtime
execution have separate admission rules. A document that can be saved or drawn
is not automatically executable. Read [Run and Highlight](../interface/run-and-highlight.md)
and the relevant [function reference](../functions/index.md).
