# Documentation reconciliation — 26 October 2026

This is a documentation checkpoint, not a new Studio release or complete
application qualification. It separates published source, local delivery,
historical runtime measurements and the current reference export.

## Evidence retained

- FROG public source and the 625-document corpus were published on 26 October.
  The reference checks and Pages deployment completed successfully.
- The published Studio implementation checkpoint is the 26 October source
  commit `764900606ee56a757492be25005f3ada0aa3eca7`. Later local corrections
  do not become published implementation merely because this documentation
  describes their recorded behavior.
- The example run measured on 25 October retains its **1,219 successful checks**
  and backend limits. No example execution was performed by this documentation
  refresh. The global application regression suite remains paused.

The regenerated reference projects **678 active function contracts**, 64 palette
folders and 18 families. ActiveX, Database, DataFinder and Web Services were
withdrawn from this product surface; old declarations and historical snapshots
are not new palette availability.

## Example icons and historic hashes

Before this refresh, every one of the 625 documentation downloads differed from
the current canonical document. Comparing parsed JSON showed that **all 625
differences were confined to `icon`**, with no graph or value difference. The
current corpus uses the existing Studio diagram SVG resources.

The refresh restores exact canonical file copies. The index remains unchanged,
SHA-256 `4d70d9b7bc7b8da45d42d191542c2ad0cbda7528323510fbef44608754ef3e1e`.
The [25 October validation snapshot](../../assets/examples/validation-2026-10-25.json)
keeps the hashes of documents actually measured then. Icon replacement changes
file hashes; the historical snapshot is not rewritten to claim that those new
bytes were executed. The [icon comparison record](../../assets/examples/icon-refresh-2026-10-26.json)
records the old and current document hashes and the narrowly compared boundary.

## Reading older declarations

Some retained authoring contracts and help descriptions lag the native product
profiles. For example, Sequence's older binding text says execution is not
implemented, while its indexed examples exercise selected Flat and Stacked
native profiles, including early publication and rejection of a circular
dependency. Neither text makes a claim of universal public Source lowering.

Function pages keep the original contract text identifiable and direct readers
to the native examples and this reconciliation. The target's actual admission,
types and provider diagnostics decide whether a specific graph can run.

## Guides brought forward

See [Run and Highlight](../interface/run-and-highlight.md), [Build](../interface/build.md),
[Type Def V1](../interface/type-definitions.md), [Tab Controls](../widgets/tab-controls.md)
and [attached comments](../interface/attached-comments.md). String display and
numeric base-entry guidance are updated separately from their stored values.

Outstanding acceptance work remains visible: complete Tab editor reception,
some Numeric radix editor contexts and the neighboring PublicBinding property
test have incomplete or failed evidence in their recorded campaigns. A new
documentation page does not close those tests or the work still in progress
in the implementation chat.
