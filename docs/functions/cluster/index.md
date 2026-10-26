# Cluster functions

[All functions](../index.md)

11 operations or editor elements; 1 palette folders. Open a page to inspect its exact connector, typing rules and execution limits.

## Operations and editor elements

| Entry | Purpose |
| --- | --- |
| [Array To Cluster](conversion/array_to_cluster.md) | Diagram node for converting an array to a cluster. Ports are available for authoring; execution requires target support. |
| [Build Cluster](build.md) | Diagram node for building a cluster. Ports are available for authoring; execution requires target support. |
| [Build Cluster Array](build_array.md) | Diagram node for building an array of clusters. Ports are available for authoring; execution requires target support. |
| [Bundle](bundle.md) | Constructs an ordered heterogeneous Cluster, or replaces wired ordinal fields of the connected Cluster. References retain their complete type and target; this operation does not read Value. |
| [Bundle By Name](bundle_by_name.md) | Replace selected fields of an existing Cluster; preserve all other fields. Runtime requires aggregate target support. |
| [Cluster Constant](constant.md) | Diagram node for a cluster constant. Ports are available for authoring; execution requires target support. |
| [Cluster Properties](properties.md) | Diagram node for cluster properties. Ports are available for authoring; execution requires target support. |
| [Cluster To Array](conversion/cluster_to_array.md) | Diagram node for converting a cluster to an array. Ports are available for authoring; execution requires target support. |
| [Index &amp; Bundle Cluster Array](index_build_array.md) | Diagram node for indexing and building an array of clusters. Ports are available for authoring; execution requires target support. |
| [Unbundle](unbundle.md) | Extracts the ordered fields of a Cluster with their complete types. A reference remains a reference; use Property Value explicitly to read the referenced control. |
| [Unbundle By Name](unbundle_by_name.md) | Select a Cluster field in each extensible row. Missing names break validation. Runtime requires aggregate target support. |

## Palette folders

| Entry | Purpose |
| --- | --- |
| [Conversion](conversion.md) | Palette icons for Cluster To Array and Array To Cluster. |
