# Current capabilities and limits

**Documentation reconciliation: 26 October 2026.** See the [refresh and evidence boundaries](documentation-refresh-2026-10-26.md) for current guides, retained declarations and icon provenance.

**Runtime measurement: 25 October 2026.** The shared corpus contains
**625 actual `.frog` documents**. A local Windows x64 run of the rebuilt
example runner recorded **1,219 successful example/backend checks**. This is
a dated measurement of those files and modes, not certification of every
catalogue function, a new signed Studio release, or a complete application gate.

[Browse the examples](../examples/index.md) ·
[Understand their document profiles](studio-draft-examples.md) ·
<a href="../../assets/examples/validation-2026-10-25.json" download>Download the dated validation results</a>

## What was actually measured

The 625 documents declare 610 execution scenarios, eight expected diagnostics,
three expected stops, and four persistence scenarios. Some documents are
checked on two backends; this is why the check count exceeds the document count.

| Backend or mode | Successful checks |
| --- | ---: |
| Native Fast | 594 |
| Native Debug | 594 |
| Explicit private Simulation | 27 |
| Persistence only | 4 |
| **Total** | **1,219** |

Across those checks, 1,194 compare execution outputs with declared oracles,
15 verify an expected diagnostic, six verify a requested stop, and four verify
saved data. There were no failed, skipped, unsupported or blocked results in
this corpus run. A successful refusal or stop is not a newly supported
calculation. Persistence does not establish execution support.

The execution path for native cases is the actual document through Source,
FIR, LLVM and ProgramSession. The reviewed local Studio Run path selects Native;
Simulation remains an explicitly declared mode, with no silent fallback to
make a native example pass. These local profiles are distinct from a promise
of general public Source or cross-platform execution.

The snapshot records each example ID, relative file path, profile, mode,
backend, status and document hash. It also records the hashes of the 18 original
family reports and the runner. Its common identifiers are:

- Canonical index SHA-256: `4d70d9b7bc7b8da45d42d191542c2ad0cbda7528323510fbef44608754ef3e1e`.
- Runner SHA-256: `3dc9a136ecfdffccdb81581679053dc76811ad243d79a5e98213e03ac0b13dee`.

The index describes intended examples and expected outputs. The downloadable
validation snapshot records a past run. Neither is a second function-contract
registry or a live status monitor.

## Capability boundaries

| Area | Scope established by this corpus |
| --- | --- |
| Arithmetic, Boolean, comparison and Mathematics | Named scalar and aggregate profiles, Formula and selected existing math providers; exact integers, floating-point comparators and exceptional cases are scenario-specific. Add retains FROG's 2–16 input left fold. |
| String | Explicit byte lengths/offsets, selected transformations, ASCII case conversion and literal UTF-8 search. Raw-byte and UTF-8-checked profiles remain distinct. Unicode case-folding is not silently approximated. |
| Array | Bounded packed F64 operations and seven generic owned-value operations, with exact types, ranks and schemas. They do not provide every authoring option of every Array node. |
| Cluster and Variant | Bundle construction/update, schema-driven Unbundle, selected named fields, exact Variant payloads and ordinary mismatch errors. Variant attributes, flattening and type-analysis nodes are not thereby implemented. |
| Collection | Seventeen Map/Set operations with invariant schemas, typed defaults, comparison order and owned lifetimes. The examples do not test all possible composite keys or resource sizes. |
| Structures and synchronization | Selected For, While, Case, Sequence, In Place, Event timeout, Semaphore, Rendezvous and Occurrence scenarios, including explicit refusal, stop and restart cases. Timed/disabled structures with persistence-only examples are not claimed as fully executable. |
| Object references and errors | Selected real-target Value/Property/Invoke operations and complete Error records. Generic host actions, every method/property and interactive error dialogs remain separate capabilities. |
| Native C calls | Windows x64 scalar5 by-value I32/U32/I64/U64/F64 with a real example DLL. Visual order is separate from ABI order. Pointer/buffer/callback/array/string signatures are not covered by this profile. |
| File and dynamic events | The named examples exercise real providers in explicit Simulation. They are not compiled-native coverage for those families. |

The original audit includes **761 IDs**. After the requested retirement of
ActiveX, Database, DataFinder and Web Services, **678 contracts remain active**
and **83 are withdrawn**. The measured corpus cites 273 active IDs; evidence
for each is partial. The other 405 active IDs have no measured execution in
this snapshot. Being visible in a palette or having a type resolver does not
establish a complete runtime provider.

Remaining gaps include many formatting/scanning/regex operations, Variant
attributes and introspection, calendar/clock functions, some numeric and
aggregate representations, ODE/DAE/PDE and complex/fixed-point profiles.
The .NET bridge is not a general native-runner implementation. File examples
do not qualify every I/O effect or format. See each function's current
contract and backend requirements before using it.

## Files, dependencies and memory

All 625 documents in this snapshot retain their actual **Studio Draft**
envelope. Copying them into this public documentation does not convert them
into public FROG Source 0.1. Draft revision, application version and Source
compatibility version remain distinct.

The C example library is accompanied by its source, header, build recipe and
the <a href="../../assets/examples/LICENSE" download>corpus license</a>.
Its ABI is described in the
<a href="../../assets/examples/Native/lib/README.md" download>library README</a>.
The public download contains no private preparation archive, developer SDK
or application binary. Rebuilding portable C code does not establish a
Studio provider for another operating system.

Generic owned values are subject to their declared payload, schema, depth and
shape budgets. A U32 dimension or an exact I64 value does not promise an
allocation of that size. The known 16,000,000-byte conservative owned-value
budget is not a process-memory measurement. Records and the selected profiles
retain their individual arity/type restrictions.

## What this checkpoint does not certify

The global regression suite remains paused. The result above does not qualify
all editor interactions, Dark/Light rendering, every zoom/DPI, every nested
widget, a clean end-user installation, signing, or the final distributed
executable. Those checks need their own versioned evidence.

The [15 October checkpoint](development-checkpoint-2026-10-15.md) is retained
as historical context. This example campaign does not resolve unrelated
earlier Clipboard or UI issues merely by passing execution tests. No public
push or site deployment is claimed by this local documentation update.

[Functions reference](../functions/index.md) ·
[Example profiles](studio-draft-examples.md) ·
[Document model](document-model.md) ·
[FROG specification](https://graiphic.github.io/FROG/)
