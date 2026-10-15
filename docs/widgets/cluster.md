# Cluster

A Cluster combines fields of different types into one ordered value and one
Diagram terminal. Use it for related values such as a state, a measurement, and
a status. An [Array](array-container.md) instead repeats one element type.

## Create and populate

Place a Cluster Control or Indicator from **Data Containers** in the Widget
Navigator. Drag supported widgets into the container to add fields. Select a
child to edit that field; select the enclosing frame to move or resize the
Cluster.

You can transfer a contained element directly to another compatible container.
The destination displays an acceptance aura while the pointer is in its valid
visible region. Release commits the transfer; `Escape` cancels it. A supported
group insertion preserves relative positions and is one Undo action.

## Field order and identity

Field identity and order define the composite value. A field's label is display
text: renaming or moving it does not replace its technical identity.
Use **Reorder Controls in Cluster** to preview an order, then Accept or Cancel.
Functions such as Bundle/Unbundle By Name address stable field identities even
when two displayed labels happen to be equal.

## AutoSizing

| Mode | Result |
| --- | --- |
| None | Keep manual Cluster bounds |
| Size to Fit | Fit the enclosure to child bounds, following both growth and shrinkage |
| Arrange Horizontally | Arrange fields in a horizontal layout and size the enclosure |
| Arrange Vertically | Arrange fields in a vertical layout and size the enclosure |

These are continuing layout modes. They differ from an Array's one-shot
**Size to Widest Element** command. A child resize previews the result and
commits one Undo action on release.

Nested children retain their own dimensions and local positions when a parent
changes size. In an Array of Clusters, design edits apply to the shared template;
a value edit applies to the addressed element, preserving other rows' values.

## Diagram and runtime

The Diagram terminal carries the complete ordered field type. Cluster constants
have their own compact Diagram presentation, editable fields, and AutoSizing
modes. The [Error Cluster](error-cluster.md) is a preset with ordinary Boolean,
I32, and String fields.

See [Cluster functions](../functions/cluster/index.md) for Bundle, Unbundle, and
related operations. Editor support and runtime aggregate support are separate;
[current capabilities](../reference/development-checkpoint.md) records their limits.
