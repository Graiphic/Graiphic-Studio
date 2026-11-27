# Context Help

Open Context Help, point at an object, and read what it does before acting on
it. The resizable help window stays open while you use the editor.

## Open, inspect, and lock

1. Press `Ctrl+H`, or choose **Help > Context Help**.
2. Hover a widget, function tile, Diagram function, terminal, wire, or supported
   interface control.
3. Press `Ctrl+Shift+L` to freeze the current object while you move the pointer.
4. Choose **Detailed help** for its documentation. Unlock to resume live updates.

Closing Context Help leaves the document open. The open/locked state belongs
to the workspace rather than the program.

## Widgets and terminals

Widget help identifies the object's name, purpose, Control/Indicator role,
value type, and visible label where available. A Control supplies values;
an Indicator displays them. An Array includes its contained type.

Free labels and Diagram comments are documentation objects. They do not
participate in dataflow.

## Function connectors

Function help uses the same catalog identity and icon as the Function Navigator.
The connector view identifies inputs and outputs and distinguishes **required**,
**recommended**, and **optional** terminals when declared by the function.

The description gives the function's quick purpose. **Terminal Data Types**
still describes its terminals, and **Examples** keeps the related examples.
Choose **Detailed help** for the full **Types and Compatibility** reference,
including accepted types, conversions, shape rules and declared limits.

For a placed object, connected types can refine the declared terminal type.
Inspect the type detail when working with nested Arrays or Clusters; a color
alone cannot tell you the complete type. Coercion information is shown where
available. Hover a wire to inspect the data type it carries.

The [Functions reference](../functions/index.md) provides a page for each
catalog entry, with its purpose, connector reference, types, and current
execution limits. Connector schematics on those pages describe declarations;
they are not captures of a particular wired graph.

## Find Examples

Choose **Help > Find Examples** and select an example. **Example documentation**
opens the installed `Readme.md` in the system viewer or shows it in Studio’s
details pane when the viewer is unavailable. If the example has no installed
readme, the button opens its page in the [online examples catalog](../examples/index.md).
The page includes the `.frog` file, its dependencies, expected results and
related functions.

**Function help** opens the relevant reference or lists the available references
when the example declares several. Choose **Open in Studio** to edit a working copy.

## Interface assistance

Options, Navigator controls, and other supported interactive controls use the
navigation helper's short explanations. With Context Help open, those
explanations are centralized in this window. Configure delayed interactive
hints under **Tools > Options... > Assistance**.

## Detailed help destinations

Built-in objects use known documentation destinations. Function entries open
their corresponding reference page; unrecognized built-in identities return
to the documentation home. A help description or a visible catalog tile does
not establish target-runtime support.

Document-owned widgets can carry `documentation.description` and
`documentation.url`; Diagram nodes can carry `doc.summary` and `doc.url`.
These fields document the object without changing its ports, type, or execution.
Only HTTP and HTTPS external documentation links are accepted.

## If help seems unexpected

- Check whether help is locked; unlock it to follow the pointer again.
- Hover the actual child field or cell when inspecting a nested container.
- Read [current capabilities](../reference/development-checkpoint.md) when a
  function is described but cannot run on the selected execution path.

## Property Nodes, methods and references

Use Detailed Help on a Property Node or an Invoke Node to reach its function page. Follow the [reference guide](../reference/using-object-references.md) for wiring, or choose the target class in the [property and method index](../reference/object-members/index.md) for member types, access and method parameters.
