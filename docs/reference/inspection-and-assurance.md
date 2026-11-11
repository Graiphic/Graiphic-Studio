# Inspection, execution and evidence

**Supporting guide · reviewed 11 November 2026**

The [product philosophy](product-philosophy.md) explains why Studio connects visual programming with execution and change. This page helps you interpret the information from its views and checks.

| View or check | What it tells you |
| --- | --- |
| Diagram and Source | The represented logic, connections and document structure you can inspect and edit. |
| Language validation | Whether the document satisfies its applicable structural and semantic rules. |
| Target admission | Whether the selected backend and providers support the complete program. |
| Run and Highlight | What happened during the identified execution and the values observed under its conditions. |
| Tests | Whether stated expectations were met for the tested inputs and conditions. |
| Build | Whether the captured program could be compiled and packaged for the chosen configuration. |

A useful investigation moves from an overview to relevant detail and checks the result of a change. Keep the program version, inputs, dependencies and configuration connected to the observations. Earlier results can guide an investigation; a relevant modification may require a new check.

## Coverage and claims

Selected functions and profiles have normal Run, Highlight and native LLVM paths on Windows/x86-64. Use [current capabilities](development-checkpoint.md), the relevant function documentation and Run/Build diagnostics to establish the supported scope. A visible palette entry alone does not qualify execution on a target.

Readable graphs support understanding. A successful build establishes packaging, and a successful run establishes behavior under its conditions. A claim of faster diagnosis or easier maintenance should be assessed through actual tasks and valid results. A compact picture alone is not a comparative study.

Some applications may benefit from an additional verification tool for a stated guarantee. Such an integration would have its own supported semantics, assumptions and checked artifact; this page introduces no verifier command or required execution mode. General product development continues through the existing authoring, Run/Highlight and Build workflows.

- [Product philosophy](product-philosophy.md)
- [Run and Highlight](../interface/run-and-highlight.md)
- [Build](../interface/build.md)
- [Document model](document-model.md)
- [FROG inspection and evidence guide](https://github.com/Graiphic/FROG/blob/main/Strategy/Inspection-and-Assurance.md)

Published checkpoints retain their own dates and scope. This documentation update announces no new binary release and does not rerun those tests.
