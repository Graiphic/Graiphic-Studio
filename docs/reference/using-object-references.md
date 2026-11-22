# Working with object references

A reference identifies an object in a document. To read a button, change its appearance or call one of its methods, create a reference to that button and wire it to the reference input. Two buttons with the same label retain separate identities. The reference output lets the next node act on the same object.

## Find the member you need

1. Wire the reference and open **Select Property** or the method menu. The class of the target determines the choices. For a Property Node with a bound target the reference input is absent.
2. Choose a property and its direction. **Read** produces the typed value at that row's output. **Write** takes it at the input. Each row keeps its own ID and connection when other rows are added.
3. For a method, select the signature and wire its required inputs. An output parameter or result appears on the output side. A method returning `void` has no result port.
4. Wire the error terminals when ordering dependent operations. Check the error output, particularly when the target document has closed or the operation requires a host service.

The [class index](object-members/index.md) lists the menu paths, types, inputs, results and declared access of each class. **Editor** indicates that the descriptor advertises an authoring operation. **Run advertised** is the descriptor's separate runtime flag. Some runtime operations have a separately registered provider. A list entry alone does not establish execution on every target. A reason in the last column identifies a service or permission restriction.

### Boolean appearance

On a Boolean reference, choose **Colors[4]**. A read returns an array of clusters with **Foreground Color** and **Background Color**, both unsigned 32-bit colors. The first four pairs describe False, True, True to False and False to True. Styles with mouse-over colors can expose two additional pairs. A write accepts 1, 2 or 4 pairs, or 6 on styles that support them. Use **Create Constant** on the write input to get the typed array. Reading back the same target lets you inspect the resulting colors. Writing colors leaves the Boolean value, text, and Value Change events untouched. [Boolean members](object-members/frog.widgets.boolean_control.md)

### Value and Value (Signaling)

Use **Value** for ordinary typed access. **Value (Signaling)** is write-only. On a supported target it queues a Value Change event even for a write of the current value. A latch Boolean rejects a signaling write. An Array Element reference addresses the shared element presentation. To operate on a particular reference held in an array, wire the array to **Index Array** and wire the selected reference to the Property Node. [Array members](object-members/frog.widgets.array_control.md)

### Methods and strict types

For a String target, **Get Nth Line** exposes its declared line index and output parameters. For a Front Panel reference, **Find Child** receives a path and returns a Control reference. Its class determines which properties are available downstream. A strict reference also carries the target's value schema, which determines Value, array rank and cluster fields. Closing a borrowed reference preserves the object and its other aliases. [String methods](object-members/frog.widgets.string_control.md) · [Front Panel methods](object-members/frog.front_panel.md)

## Updating this index

The documentation tool `tools/export_reference_help.cpp` consumes the public Frontend member catalogue. Build it as a C++20 executable against the matching Frontend production and core libraries, then pass `docs/reference/object-members` as its output directory. Run the function help exporter on the same source snapshot. The class index counts inherited members for each class that exposes them.
