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

For a placed object, connected types can refine the declared terminal type.
Inspect the type detail when working with nested Arrays or Clusters; a color
alone cannot tell you the complete type. Coercion information is shown where
available. Hover a wire to inspect the data type it carries.

The [Functions reference](../functions/index.md) provides a page for each
catalog entry, with its purpose, connector reference, types, and current
execution limits. Connector schematics on those pages describe declarations;
they are not captures of a particular wired graph.

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
