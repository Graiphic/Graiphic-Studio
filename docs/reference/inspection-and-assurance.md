# Inspection, execution and evidence

**Supporting guide · reviewed 11 November 2026**

The [product philosophy](product-philosophy.md) focuses on human understanding and acceptance as machine generation grows. Studio's graphical projection helps investigate a FROG model serialized in `.frog`; execution and compilation are distinct operations on the supported program.

| View or check | What it tells you |
| --- | --- |
| Diagram and Source | Represented logic and document structure, with visual cues and hierarchy for navigation. |
| Conversion evidence | Whether a declared input subset preserves relevant behavior in the FROG model; serialization alone is insufficient. |
| Change information | Which revision and meaningful differences are under review; broad change-review support remains a design goal. |
| Language validation | Whether the document satisfies the applicable structural and semantic rules. |
| Target admission | Whether the selected backend and providers support the complete program. |
| Run and Highlight | What happened during an identified execution and which values were observed. |
| Review and tests | Whether relevant expectations were met for the behavior, inputs and revision actually checked. |
| Build | Which captured program, dependencies and configuration were compiled and packaged. |

Human acceptance should remain connected to the version that runs. A generated edit can invalidate a previous conclusion about affected behavior. Source associations and fingerprints help identify revisions; they do not alone establish a faithful translation or a successful result.

## Coverage and claims

Selected functions and profiles have normal Run, Highlight and native LLVM paths on Windows/x86-64. Use [current capabilities](development-checkpoint.md), function documentation and diagnostics to establish support. General language imports and complete change-review workflows are not announced by this update.

The calculator's roughly 1,000-line C comparison illustrates an architecture accessible through a graphical page and its underlying cases. Evaluate correct understanding, diagnosis and valid changes rather than infer a review-speed result from screen area alone.

FIR/IR and compiler infrastructure provide a path to machine efficiency. Performance comparisons must also account for algorithms, semantics, runtime services, data and target configuration. A successful build establishes packaging; behavior must be checked through the relevant execution and tests.

Specialized verification tools may address guarantees needed by a particular collaboration. They retain their own semantics, assumptions and checked artifacts and do not become a required Studio mode through this page.

- [Product philosophy](product-philosophy.md)
- [Run and Highlight](../interface/run-and-highlight.md)
- [Build](../interface/build.md)
- [Document model](document-model.md)
- [FROG inspection and evidence guide](https://github.com/Graiphic/FROG/blob/main/Strategy/Inspection-and-Assurance.md)

Published checkpoints retain their dates and scope. This editorial update introduces no binary release and reruns none of their tests.
