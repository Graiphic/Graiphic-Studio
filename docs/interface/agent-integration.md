# Work with an external agent

**Tools → Agent Integration…** is the entry point for Studio's local agent
service. An external agent can inspect an open document and propose a limited
set of edits for review in Studio. This command shows local session information
or the pending proposal review; it does not start a model or sign you into one.

## Connect to the right document

The connection uses three parts: a compatible Studio session, its MCP adapter,
and an external client configured to use that adapter. The client supplies its
own model access. The adapter must match the Studio service; this guide does
not imply that every standard installation includes the adapter or its setup.
Context requested by the client can be sent to its configured model provider.

Once connected, the client discovers Studio sessions and their open documents.
Choose the intended document explicitly. Its session and document identities,
revision and capabilities determine what the agent can access. A file name
alone does not identify the active document, which may contain unsaved edits.

The agent can request the current selection, document context and operator
contracts, including resolved ports and types. It should use those contracts
rather than guess connections from an icon or a function name.

## Review a proposed edit

The existing editing profile supports changes to selected, existing nodes:

- Change the value of an admitted numeric constant.
- Change a node's label.
- Move a node.

The proposal is prepared separately from the active document. Validation and
the proposal preview let you inspect the result before applying it. Open
**Tools → Agent Integration…** to review a pending proposal, then choose
**Accept Proposal** or **Reject Proposal**. Acceptance applies the reviewed
proposal as one undoable transaction. Use the normal Undo and Redo commands
to revert or restore it.

If the document revision or exact Source changes, obtain fresh context
and prepare a new proposal. Unapplied Source edits and unsupported changes
are refused rather than silently replaced. Rejection leaves the active
document unchanged.

## Understand the execution boundary

The agent's `run_tests` tool is a bounded numeric test on an admitted graph or
proposal. It uses native operators, but it is a separate execution profile
with resource and type limits. A passing result does not qualify ordinary
Run, Highlight, hardware access, Build or an exported executable.

Use [Run and Highlight](run-and-highlight.md) for the normal interactive
execution workflow and [Build](build.md) for standalone applications.

## Scope and availability

The connected session's reported capabilities are the authority for an
individual request. This guide describes the existing bounded integration;
it does not advertise arbitrary program creation, rewiring, new Front Panel
widgets or an integrated chat as available through these editing operations.

Studio Draft documents and public FROG Source have different owners and
admission rules. Inspecting public Source through the service does not grant
the Studio Draft editing or execution capabilities to that format. See
[the document model](../reference/document-model.md).

Keep the Studio product version, adapter version, execution profile and
document revision with any test result. Earlier qualification applies to
the artifacts actually tested; this documentation update is not a fresh
interactive or model-assisted test. New assistant interfaces require their
own delivery and validation.
