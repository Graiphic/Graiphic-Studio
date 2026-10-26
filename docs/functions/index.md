# Function reference

Browse every function, editor element and palette folder in the current Studio catalogue. Each operation has its own page with its purpose, IN/OUT connectors, type rules and execution limits. Authentic palette icons are shown wherever the catalogue declares an asset.

Use the documentation search for an English or French helper title, a catalogue ID, a connector name or a legacy identity. [Machine-readable catalogue](catalog.json).

| Family | Operations / editor elements | Folders |
| --- | --- | --- |
| [Application Control](applicationcontrol/index.md) | 4 | 0 |
| [Array](array/overview.md) | 58 | 4 |
| [Boolean](boolean/index.md) | 16 | 0 |
| [Cluster](cluster/index.md) | 11 | 1 |
| [Collection](collection/index.md) | 22 | 2 |
| [Comparison](comparison/index.md) | 19 | 0 |
| [Connectivity](connectivity/index.md) | 47 | 6 |
| [DialogUserInterface](dialoguserinterface/index.md) | 6 | 1 |
| [Error](error/index.md) | 24 | 0 |
| [File](file/index.md) | 32 | 5 |
| [Mathematics](mathematics/index.md) | 172 | 28 |
| [Numeric](numeric/index.md) | 106 | 5 |
| [Path](path/index.md) | 23 | 0 |
| [String](string/index.md) | 58 | 2 |
| [Structures](structures/index.md) | 16 | 3 |
| [Synchronization](synchronization/index.md) | 33 | 6 |
| [Timestamp](timestamp/index.md) | 8 | 0 |
| [Variant](variant/index.md) | 23 | 1 |

## Read a function page

**IN** terminals receive values and **OUT** terminals publish values. Required inputs must be connected for semantic readiness. Recommended and optional inputs keep their distinct Studio connection flags. A listed default is a value only when the reviewed metadata states one; the preview type is shown separately.

Authoring a node does not establish execution support. Each page names the public FROG / target Runtime declaration separately from private local Run/Highlight behavior when the source describes it. A partial or blocked authoring contract remains labelled as such.

Constants, terminals and structure containers are included. Their editor-managed values, dynamic boundaries and configured connectors must not be read as an ordinary fixed executable function signature.

## Provenance and notation

This deterministic export covers **742 catalogue entries**, **678 versioned function contracts** and **64 palette folders** across **18 families**. 689 entries carry an existing context-help section. The remaining purposes come from reviewed family metadata or the versioned authoring contract.

The English text follows Studio help. French summaries are reproduced only where the existing helper supplies them. Missing French text, defaults, requirements or capabilities are not translated or inferred.

The source snapshot combines the context-help catalogue, the four catalogue tables, v2 family binding manifests, reviewed Connectivity/Mathematics metadata, explicit File defaults, Queue contracts, shared displayed terminal labels and private evaluator dispatch sources. SHA-256 hashes for every consumed source file and copied icon are retained in the machine-readable catalogue. Private source filenames are provenance records, not public source links.

The SVG icons are copied byte for byte from Studio assets. They are reference icons, not screenshots of a running diagram. No screenshot or native execution result is synthesized. Three File reference entries declare no icon; their pages say so explicitly.

Type expressions preserve the contract notation: `T:` names a generic type constraint; `array<...>` includes rank/shape rules; `cluster<...>` preserves ordered fields; `ref<...>` is a nominal reference; `resolve:...` names a resolver; `unresolved:...` requires explicit configuration or metadata. `f64`, `i32` and `bool` are scalar types. Exact per-port connection policies and preview types are available in each page’s connector-details panel.

NI API links document reference semantics and connector evidence. They do not promise every NI overload or a compatible Studio execution provider. NI flags marked unverified stay unverified, even when Studio has an explicit authoring connection policy.

Regenerate with Python 3.11+: `python tools/export_studio_help.py --source ../FROG-STUDIO/native-portable-engine`; add `--check` for a read-only deterministic export check. This documentation check does not run application regression tests.

Source snapshot SHA-256: `5aacecb1be75a8e4dbbe99e9d280891e0c47d6f8736e100a82caf4993e09c0ea`.

## Actual example documents

[Browse the shared example index](../examples/index.md). Each example provides its actual `.frog`, explanation, expected results and explicit backend/profile requirements. These expectations do not certify a successful native run.
