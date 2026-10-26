# Variant functions

[All functions](../index.md)

23 operations or editor elements; 1 palette folders. Open a page to inspect its exact connector, typing rules and execution limits.

## Operations and editor elements

| Entry | Purpose |
| --- | --- |
| [Delete Variant Attribute](delete_attribute.md) | Diagram node for Delete Variant Attribute. Ports are available for authoring; execution requires target support. |
| [Disconnect G Types](data_type_analysis/disconnect_g_types.md) | Data Type Analysis palette entry. Artwork is available; ports and execution are not defined yet. |
| [Find Contained Data Types](data_type_analysis/find_contained_data_types.md) | Data Type Analysis palette entry. Artwork is available; ports and execution are not defined yet. |
| [Flattened Bytes To Variant](from_flattened_bytes.md) | Diagram node for Flattened Bytes To Variant. Ports are available for authoring; execution requires target support. |
| [Get Array Information](data_type_analysis/get_array_info.md) | Data Type Analysis palette entry. Artwork is available; ports and execution are not defined yet. |
| [Get Cluster Information](data_type_analysis/get_cluster_info.md) | Data Type Analysis palette entry. Artwork is available; ports and execution are not defined yet. |
| [Get Fixed-Point Information](data_type_analysis/get_fixed_point_info.md) | Data Type Analysis palette entry. Artwork is available; ports and execution are not defined yet. |
| [Get Hardware Reference Type Information](data_type_analysis/get_hardware_reference_info.md) | Data Type Analysis palette entry. Artwork is available; ports and execution are not defined yet. |
| [Get Numeric Information](data_type_analysis/get_numeric_info.md) | Data Type Analysis palette entry. Artwork is available; ports and execution are not defined yet. |
| [Get Refnum Information](data_type_analysis/get_refnum_info.md) | Data Type Analysis palette entry. Artwork is available; ports and execution are not defined yet. |
| [Get Type Information](data_type_analysis/get_type_info.md) | Data Type Analysis palette entry. Artwork is available; ports and execution are not defined yet. |
| [Get User-Defined Hardware Reference Type Information](data_type_analysis/get_user_defined_hardware_reference_info.md) | Data Type Analysis palette entry. Artwork is available; ports and execution are not defined yet. |
| [Get User-Defined Refnum Information](data_type_analysis/get_user_defined_refnum_info.md) | Data Type Analysis palette entry. Artwork is available; ports and execution are not defined yet. |
| [Get Variant Attribute](get_attribute.md) | Diagram node for Get Variant Attribute. Ports are available for authoring; execution requires target support. |
| [Get Waveform Information](data_type_analysis/get_waveform_info.md) | Data Type Analysis palette entry. Artwork is available; ports and execution are not defined yet. |
| [Is Error Cluster](data_type_analysis/is_error_cluster.md) | Data Type Analysis palette entry. Artwork is available; ports and execution are not defined yet. |
| [Is Or Contains G Type](data_type_analysis/is_or_contains_g_type.md) | Data Type Analysis palette entry. Artwork is available; ports and execution are not defined yet. |
| [Set Variant Attribute](set_attribute.md) | Diagram node for Set Variant Attribute. Ports are available for authoring; execution requires target support. |
| [To Variant](to_variant.md) | Local Studio Play/Highlight wraps one immutable exact typed value in a Variant envelope. Arrays retain rank and dimensions, clusters retain field identities, and I128/U128 lexical payloads remain exact; there is no conversion to the ODE f64 state profile. Boxing a Variant deliberately adds one nesting level. Common value placement limits remain active. No external Variant backend, attributes or serialization are implied. Public FROG/LLVM target support is not declared. |
| [Variant Constant](constant.md) | Diagram node for Variant Constant. Ports are available for authoring; execution requires target support. |
| [Variant Terminal](terminal.md) | Diagram node for Variant Terminal. Ports are available for authoring; execution requires target support. |
| [Variant To Data](to_data.md) | Local Studio Play/Highlight removes exactly one immutable Variant envelope when its child type exactly matches both the actual wired type specimen and the compiled data output. No implicit numeric conversion: exact integer lexical payloads, array rank/dimensions, ordered cluster fields and immutable ownership survive. The specimen is a type, not an arbitrary fallback value. A neutral or historical text Variant remains opaque: return the requested typed default and error 8051 VARIANT_NO_CONCRETE_PAYLOAD. A wrong payload type/rank gives 8051 VARIANT_TYPE_MISMATCH. Incoming active error is preserved with a typed default. Double boxing requires unboxing Variant first, then its child. Public FROG/LLVM target support is not declared. |
| [Variant To Flattened Bytes](to_flattened_bytes.md) | Diagram node for Variant To Flattened Bytes. Ports are available for authoring; execution requires target support. |

## Palette folders

| Entry | Purpose |
| --- | --- |
| [Data Type Analysis](data_type_analysis.md) | Opens the 14-entry Variant data type analysis repository, ordered as in the NXG reference. |
