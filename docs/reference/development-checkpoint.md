# Current capabilities and limits

**Documentation checkpoint: 15 October 2026.** The latest recorded local
Windows delivery is signed **0.0.5.332**, including the updated Detailed Help routes. This page describes product scope;
local delivery, source publication, targeted verification, and a complete
application qualification are separate states.

## Choose the right capability

| Capability | Current scope |
| --- | --- |
| Front Panel authoring | Typed controls/indicators, labels, Arrays and Clusters, visual editing, Interface Map, icon editing |
| Block Diagram authoring | Functions, typed ports/wires, structures, constants, container editing, reference menus, and object-specific context actions |
| Private local Run/Highlight | Admitted simulation graphs; normal Run can start with Highlight off; supported Controls stay interactive and Indicators stay read-only |
| Queue | Eight private local Run/Highlight functions; no public Source, lowering, or target-runtime contract |
| Public native execution | A narrow Numeric F64/Add corridor; not general execution of every authored graph |
| Public Event/Unbundle integration | Separately admitted records and SDK provider; no general LLVM Record or arbitrary aggregate transport implied |
| Generic Property/Invoke execution | Authoring menus/types/services exist; generic execution of these graph nodes is unavailable |
| Advanced Events and .NET | Limited, operation-specific integration; general provider/runtime coverage remains incomplete |
| Public FROG Source | Separate public reader/writer and admitted profiles; draft authoring, full editor projection, validation, lowering, and execution are distinct |

## Recent visible behavior

- Run and Highlight share the same private simulation session. Toggling Highlight
  changes its display, and Stop restores normal editing.
- Recursive container editing routes a value to the addressed field/cell while
  design changes apply to the shared template. Cluster **None** preserves manual
  bounds; **Size to Fit** follows child growth and shrinkage.
- Numeric and Enum text fitting, String/Path sizing, typed reference placement,
  and reference wiring have scoped improvements and verification.
- Queue operations use FIFO semantics, cooperative waits, named accesses, and
  cleanup. Queue references remain distinct from ordinary message values.
- Enum, Ring, and Dropdown String menus expose one **Create Constant / Control /
  Indicator** trio. Creation preserves the original object and its configuration;
  it is separate from changing its role. These latest menu changes are compiled
  in 0.0.5.331, with their added regression cases **not yet executed**.

## Verification limits that matter

Targeted passes support their tested feature and version; they do not qualify
the entire current application. A fresh successful complete gate is not claimed.

The Queue/reference campaign passed **13/14** targeted owners. Its Clipboard
owner failed; the separate retry passed **0/1**. The observed failure was
Windows denying Clipboard opening. Its exact cause remains unestablished.
Copy publication, paste, and Undo/Redo of that Queue copy therefore remain
**unqualified**, even though the six Queue rendering/wiring sub-scenarios passed.
The later menu compilation does not resolve that failure.

Native qualification for that work is scoped to **96 DPI**. Other Windows
display scales, the remaining Adapter workflow, general runtime support,
advanced Events/.NET, and global qualification remain open. The standing
regression pause remains in effect except for separately authorized targeted work.

## File and type boundaries

Studio's readable authoring envelope is `frog.document.draft` revision 2;
Automatic/Compact numeric storage uses private revision 3. Public FROG source
uses `spec_version` and its own published contract. A `.frog` extension or a
successful editor save does not make these envelopes interchangeable.

Array/Cluster rendering does not establish support for every nested runtime
type. Queue values in Front Panel source/indicator widgets and collections of
Matrix values are unavailable at runtime in this checkpoint.

## Read next

[Run and Highlight](../interface/run-and-highlight.md) ·
[Functions reference](../functions/index.md) ·
[Document model](document-model.md) ·
[FROG specification](https://graiphic.github.io/FROG/)
