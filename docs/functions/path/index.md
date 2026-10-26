# Path functions

[All functions](../index.md)

23 operations or editor elements; 0 palette folders. Open a page to inspect its exact connector, typing rules and execution limits.

## Operations and editor elements

| Entry | Purpose |
| --- | --- |
| [Application Directory](application_directory.md) | Context constant returning the directory of the compiled FROG executable associated with this execution. A deployed program uses the executable actually launched, including after relocation. This is not the GS installation directory (Default Directory). In Studio, an absent associated compiled application reports an explicit unavailable-context diagnostic; it does not fall back to GS or the containing document. |
| [Compare Paths](compare.md) | Compares two paths. |
| [Compose Path](compose.md) | Builds a path from path components. |
| [Current Frog Path](current_frog_path.md) | Context constant returning the full Path of the containing .frog file, including its filename. Resolution follows that document, not the selected window or its caller; later evaluations follow Rename or Save As. An unsaved document or unavailable deployed source path reports an explicit unavailable-context diagnostic. It never substitutes a directory, current process directory or development-machine path. |
| [Decompose Path](decompose.md) | Separates a path into its components. |
| [Default Directory](default_directory.md) | Context constant returning the installation directory containing the Graiphic Studio executable. This is distinct from Application Directory, the project, Documents and the process working directory. Deployment without a known GS installation reports an explicit unavailable-context diagnostic. |
| [Empty String/Path?](empty_string_or_path.md) | Tests whether a string or path is empty. |
| [Generate Temporary File Path](generate_temporary_file.md) | Generates a path for a temporary file. |
| [Get Common/Relative Paths](common_relative.md) | Computes the common base and relative paths. |
| [Get Component Directory](get_component_directory.md) | Returns the directory that contains the current component. |
| [Get File Extension](get_file_extension.md) | Returns the file extension from a path. |
| [Get System Directory](get_system_directory.md) | Returns a selected system directory. |
| [Is Path Not Empty](is_not_empty.md) | Tests whether a path contains at least one component. |
| [Not A Refnum Constant](not_a_refnum_constant.md) | Provides the invalid reference constant. |
| [Path Constant](constant.md) | Places a path constant on the diagram. |
| [Path Terminal](terminal.md) | Places a path terminal on the diagram. |
| [Path To String](to_string.md) | Converts a path to its string representation. |
| [Path To String Array](to_string_array.md) | Converts a path to an array of components. |
| [Path Type](type.md) | Identifies the kind of a path. |
| [Replace File Extension](replace_file_extension.md) | Replaces the file extension in a path. |
| [String Array To Path](from_string_array.md) | Builds a path from an array of components. |
| [String To Path](from_string.md) | Converts a string to a path. |
| [Temporary Directory](temporary_directory.md) | Context constant returning the existing temporary directory supplied by the current execution environment through its system service. It does not create a file or a fresh subdirectory. Failure to obtain a valid directory reports an explicit diagnostic. |
