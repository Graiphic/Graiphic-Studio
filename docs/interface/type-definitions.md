# Share a standard Type Def

A **Type Def** shares a data schema between linked controls, indicators and
constants. Each instance retains its own value. A link is neither a Refnum nor
a global shared value.

## Create and reuse a definition

1. Create the Numeric, Boolean, String, Enum, Cluster or typed Array to share.
2. Use **Make Type Def.** and save the definition as a native **`.ftype`** file.
3. Use **Open Type Def.** to edit its root and the existing Icon Editor to
   customize its shared SVG artwork.
4. Use **Link to Type Def.** or **Place Type Def…** to reuse it in another `.frog`.
   **Open…** also opens the definition file directly.

The definition editor has one root control and no executable Block Diagram.
**Locate Type Def.** finds its source; **Disconnect from Type Def.** makes an
instance independent. Saving a definition under another source with Save As
creates an independent definition with a new identity.

## Apply a saved change

A successful Save publishes the definition. Open consumers reconcile against
their current in-memory document, preserving other unsaved edits. Closed files
resolve their definition at their next open or execution preparation; saving
the definition does not rewrite every closed consumer.

Existing values and local defaults remain separate from the definition's
initial values. Surviving Cluster fields and Enum items follow stable identities.
If a change is destructive or ambiguous, Studio retains the old data and reports
a diagnostic. Use **Review and Update from Type Def.** on the affected instance
before running it. Do not resolve the diagnostic by assuming a similarly named
new field has the old field's identity.

Label, position, text appearance and other local presentation stay with the
instance. Newly added content may require enough room to remain accessible.
Save a definition before durably saving a linked consumer, and keep dependency
paths valid when moving files. Structural publication is guarded while affected
consumers are preparing or executing.

## V1 scope

This is the standard Type Def V1, including definitions nested in definitions.
Strict Type Def and LabVIEW `.ctl` import/export are outside this version.
Propagation inside one Studio process and resolution of closed files are
distinct from refreshing another process that still holds an older snapshot.
The recorded tests cover migration, persistence, real native/FIR resolution and
authoring; they do not certify every possible Array publication gesture or
every legacy document.

[Document model](../reference/document-model.md) · [Cluster](../widgets/cluster.md) ·
[Current capabilities](../reference/development-checkpoint.md)
