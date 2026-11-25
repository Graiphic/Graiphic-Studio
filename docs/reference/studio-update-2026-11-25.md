# November Studio update

The build numbers below identify the Studio version in which each workflow was exercised.

| Workflow | How to use it | Studio build |
| --- | --- | --- |
| Branch an error wire | Connect the same error to a loop condition and a Variant field. Read both complete messages back from a queue. [Walk through the example](../interface/error-variant-loop.md). | 0.0.9.781 |
| Browse properties | Open **Browse Properties** on a Property Node. Enlarging the window gives the property table more rows. Expanding **Technical details** uses table space while the description and bottom buttons stay in place. [Work with object references](using-object-references.md). | 0.0.9.779 |
| Share a nested cluster | Select the enclosing cluster by field path to create a Type Def containing its children and their image catalogues. Linked controls keep their usual appearance on the Front Panel. [Create and reuse Type Definitions](../interface/type-definitions.md). | 0.0.9.751 for nested creation, 0.0.9.778 for the diagram badge |
| Set or display a numeric value | Choose a Knob, Meter, Gauge, Tank, or a single- or two-handle slider. Use **Visible Items → Cursor** on a single-handle slider to hide its thumb. [Numeric instruments](../widgets/numeric.md#instruments-and-sliders). | 0.0.9.731 for instruments, 0.0.9.776 for single-handle sliders |
| Pick an image inside a cluster | Click a Picture Ring to choose a thumbnail. A ring inside a nested cluster updates its own field. The arrow is optional, and resizing the frame clips the original image. [Picture Ring](../widgets/ring-and-enum.md#picture-ring). | 0.0.9.734 for resizing, 0.0.9.739 for nested selection |
| Inspect probes | The execution probe window shows the short document name and one row per probe and value. Select a row to copy its value or locate its wire. [Run and Highlight](../interface/run-and-highlight.md). | 0.0.9.675 |

## Receive and reuse a user event

Connect the reference from **Create User Event** to **Register For Events**.
Wire the resulting registration to the dynamic terminal of the Event Structure.
Before Run, open **Edit Events**, expand **Dynamic** and select the event and
the case that will handle it. Inside that case, select **UsrEvtRef** on a row
of the Event Data Node. Drag the node's lower handle to show the payload on a
second row. For a cluster payload, select its named fields individually.

For example, create a Boolean event named `stop` and generate `True`. Its
case receives `True`. Wire the **UsrEvtRef** output to **Generate User Event**
and send `False` once. The second invocation of the same case receives `False`.
This two-reception sequence was exercised in Studio 0.0.9.722.
[Register For Events](../functions/dialog/events/register_for_events.md) · [Event Structure](../functions/structures/event_structure.md) · [Generate User Event](../functions/dialog/events/generate_user_event.md).

## Create a project class and use its accessors

In Project Explorer, open the creation menu on an auto-populated folder. For a
new class, the proposed destination is a subfolder with its class name. Expand
the class to edit its private data, choose a field's type and default, then
generate read and write accessors for the field. Call the writer, wire its class
output to the reader, and display the result. A numeric field written as `37`
was read back as `37` after reopening the project in Studio 0.0.9.715.
