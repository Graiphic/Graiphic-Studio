# Build a standalone application

Use the **hammer** button to open Build. Review the destination and presentation,
then choose **Build**. Run, Highlight and a standalone executable use the native
program path for admitted graphs; the chosen target must support the actual
types, operations and required providers.

## Destination and options

- A saved document defaults to `build/<document>/<document>.exe` beside its source.
- An unsaved document receives a unique destination under the Windows Desktop's
  `Temp` folder. Building does not save that document as your working source.
- Choose **Automatic**, **With Front Panel** or **Console** for the produced
  application's presentation. These choices do not change the calculation.
- The current admitted target is **Windows x64**, with **Standard (O2)**
  optimization. Unsupported optimization profiles are refused explicitly.

LLVM/clang is bundled with the Studio distribution. The Microsoft link
components remain a separately detected prerequisite. A toolchain failure is
different from an invalid graph; read the Build diagnostic for the missing step.

## Follow the build

The progress bar follows eight actual stages. It reports work completed, not a
prediction of remaining time. Closing the panel and cancelling compilation are
different actions. Open-folder and Launch actions use a completed, verified
result rather than a partly written executable.

Preserve the relative layout of dependencies when moving the output. Relative
native-library calls use the captured project context and verified dependencies;
the process's current directory does not substitute for that context.

## Supported scope

The dated Build checks constructed, relocated and ran real applications,
including exact I64 arithmetic, String, Cluster, native DLL and selected Event
and synchronization cases. Admission of the example corpus is broader than
the set of executables actually built: it is not proof of one EXE per example.

Front Panel capture does not admit every widget or decoration. Console avoids
capturing a Front Panel but retains the target's program-capability checks.
The graphical host uses the captured DPI; rebuild after changing that DPI.
Escape inside an editor of a generated graphical application remains a known
editing limitation in the recorded Build checkpoint.

[Run and Highlight](run-and-highlight.md) · [Examples](../examples/index.md) ·
[Current capabilities and evidence](../reference/development-checkpoint.md)
