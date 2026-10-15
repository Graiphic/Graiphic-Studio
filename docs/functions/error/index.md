# Error functions

[All functions](../index.md)

24 operations or editor elements; 0 palette folders. Open a page to inspect its exact connector, typing rules and execution limits.

## Operations and editor elements

| Entry | Purpose |
| --- | --- |
| [Build Error Cluster](build_cluster.md) | Creates a diagnostic from an I32 code, description and optional call chain. An incoming error or warning is preserved. |
| [Clear Error Cluster](clear_cluster.md) | Resets status to false, code to zero and source to an empty string. Clearing a diagnostic does not repair or retry the failed operation. |
| [Demultiplex Errors](demultiplex.md) | Extracts the diagnostics combined by Multiplex Errors into a 1D array of error clusters. |
| [Display Error](display.md) | Reports status, code, location and description; the selected dialog mode controls runtime presentation. Placing this node opens no dialog. |
| [Downgrade To Warning](downgrade_to_warning.md) | Changes an active error into a warning without treating the sign of the code as severity. |
| [Error Constant](constant.md) | Creates an editable status/code/source cluster with the initial no-error value false, zero and empty string. This value is not an exception. |
| [Error Terminal](terminal.md) | Creates an error-cluster control on the Front Panel and its linked diagram terminal. |
| [Filter Error Code](filter_code.md) | Accepts an I32 code or a 1D I32 array. Clears matching diagnostics, preserves others, and exposes codes cleared for the array overload. |
| [Generate Error Report](generate_report.md) | Formats a diagnostic into a multiline report string, optionally followed by a divider line. |
| [Is Error](is_error.md) | Tests the status field, not the sign of the error code. The output is one Boolean. |
| [Is Error Or Warning](is_error_or_warning.md) | Tests for an error or warning: status true or nonzero code. The output is one Boolean. |
| [Is Warning](is_warning.md) | Tests for status false with a nonzero code. The output is one Boolean. |
| [Multiplex Errors](multiplex.md) | Combines three individual diagnostics and a 1D diagnostic array into one multiplexed error cluster. Demultiplex Errors recovers the collection. |
| [Override Call Chain](override_call_chain.md) | Replaces the stored call chain with a location string; an empty string removes that location. |
| [Read Call Chain](read_call_chain.md) | Returns the call chain as a 1D string array and indicates whether an alternate location was stored. |
| [Read Description](read_description.md) | Reads the diagnostic description, optionally removing typeface formatting tags. |
| [Read Error Code](read_code.md) | Reads the signed 32-bit code without inferring severity from its sign. |
| [Read Location](read_location.md) | Reads the location or formats the call chain as a multiline string. |
| [Retain First Error](retain_first.md) | Expandable inputs are checked from top to bottom: first error, otherwise first warning, otherwise no error. This is not Multiplex Errors. |
| [Translate Error Code](translate_code.md) | Maps original codes to replacement codes supplied as two 1D I32 arrays; optionally updates the call chain. Array lengths are runtime values. |
| [Upgrade To Error](upgrade_to_error.md) | Changes a warning into an active error. |
| [Write Call Chain](write_call_chain.md) | Writes a 1D string array as the diagnostic call chain, including in an empty error cluster. |
| [Write Current Call Chain](write_current_call_chain.md) | Updates an error or warning with the current call chain, omitting the specified number of initial elements (default one). |
| [Write Error Code](write_code.md) | Replaces the signed 32-bit diagnostic code. |
