# File functions

[All functions](../index.md)

32 operations or editor elements; 5 palette folders. Open a page to inspect its exact connector, typing rules and execution limits.

## Operations and editor elements

| Entry | Purpose |
| --- | --- |
| [Check if File or Folder Exists](exists.md) | Tests file/folder existence. On Windows an empty path represents the drive list and returns true. Existence does not guarantee access. |
| [Close File](close.md) | Auxiliary Close File node releases a typed live file reference; reuse of a closed reference reports an error. |
| [Copy](copy.md) | Copies a file or recursive folder and preserves its source; overwrite defaults to false. Existing destination folders receive the source name. |
| [Create File with Incrementing Suffix](create_incrementing.md) | Atomically creates and opens a free filename, inserting default suffix (%d) before the extension starting at 1. The caller must close the returned reference. |
| [Create Folder](create_folder.md) | Creates an absolute folder path and missing parents; an already existing target is an error. |
| [Delete](delete.md) | Deletes a file or folder. Recursive removal requires entire hierarchy; confirm defaults to false. Errors are never success. |
| [Deny Access](deny_access.md) | Changes live file sharing: deny read/write, deny write, or deny none. These temporary restrictions are distinct from permissions. |
| [File/Directory Info](info.md) | Returns file/directory metadata. File size is bytes; directory size is its immediate entry count. Modified time is a timestamp. |
| [Flatten To XML](flatten_to_xml.md) | Serializes a supported typed value in memory using the NI LabVIEW XML schema subset; no file is created. Unsupported schemas report an error. |
| [Flush File](flush.md) | Flushes the live file to disk without closing its reference. |
| [Get File Position](get_position.md) | Returns a live file reference's current byte position without moving it. |
| [Get File Size](get_size.md) | Returns file length in bytes, independently of its current position. A path and an open file reference are distinct input variants. |
| [Get Permissions](get_permissions.md) | Returns the NI-style permission mask. On Windows owner and group are empty; this is not an NTFS ACL query. |
| [Get Type and Creator](get_type_creator.md) | Returns historical four-character type/creator codes for recognized extensions; unknown codes are ????; creator is not the Windows user. |
| [Get Volume Info](volume_info.md) | Returns containing volume, total/free bytes and sector size; it does not reserve storage. |
| [List Folder](list_folder.md) | Lists sorted immediate file/folder names using * and ? wildcards; returns names, not full paths, and does not recurse. |
| [Move](move.md) | Moves/renames a file or recursive folder to its destination; overwrite defaults to false. Existing destination folders receive the source name. |
| [Open/Create/Replace File](open.md) | Auxiliary Open/Create/Replace File node establishes a typed live file reference. Explicit operation, access and share mode control resource creation and lifetime. |
| [Preallocated Read from Binary File](binary_read_preallocated.md) | Reads into a preallocated numeric array at the live file position; output capacity is retained and count identifies the initialized prefix. String elements are unsupported. |
| [Read Delimited Spreadsheet](spreadsheet_read.md) | Reads 2D DBL, I64 or String data from a byte offset; count -1 reads the remainder; first row, resulting byte position and EOF are returned. |
| [Read from Text File](text_read.md) | Reads bytes or lines; Read Lines changes the output type when count is connected. Convert EOL defaults to true. A path opens read-only; wiring refnum out retains it. |
| [Read From XML File](read_xml.md) | Reads a LabVIEW XML document and returns its content fragment or top-level fragments; it does not deserialize the final typed data. |
| [Recursive File List](recursive_list.md) | Recursively lists full file/folder paths; exclusions are case-insensitive, wildcards filter files, errors stop by default. LLB content is unsupported by the Studio host provider. |
| [Set File Position](set_position.md) | Moves a live file position by a signed 64-bit byte offset relative to start, end or current position. |
| [Set File Size](set_size.md) | Changes file length in bytes. A smaller size truncates data; zero preserves the empty file. An open reference retains its lifetime. |
| [Set Permissions](set_permissions.md) | Changes the exposed permission mask. Windows applies only user-write bit 7 and ignores owner/group; this does not edit ACLs or file sharing. |
| [Set Type and Creator](set_type_creator.md) | Changes historical four-character codes on supported macOS targets only. Windows reports unsupported; it never simulates success. |
| [Show in File System](show_in_file_system.md) | Shows a path in the platform file manager; it does not read data or open a file reference. |
| [Unflatten From XML](unflatten_from_xml.md) | Parses a supported LabVIEW XML value against the complete connected type specimen. Invalid XML or mismatched schemas report an error. |
| [Write Delimited Spreadsheet](spreadsheet_write.md) | Writes 1D/2D DBL, I64 or String arrays as delimited text; default tab, numeric format %.3f, overwrite unless append is true. |
| [Write to Text File](text_write.md) | Writes a String or String array. A path replaces the file; a live reference writes at its current byte position. Wiring refnum out retains an automatically opened reference. |
| [Write to XML File](write_xml.md) | Wraps supplied XML fragment(s) in a LabVIEW XML document and writes an .xml file. UTF-8 encoding is the supported Studio adaptation; standalone defaults to true. |

## Palette folders

| Entry | Purpose |
| --- | --- |
| [CSV](csv.md) | Delimited spreadsheet file operations. Moving them here does not change their separator or format options. |
| [Operation](operation.md) | Other existing File operations, including opening and closing typed file references. Their operator identities and saved nodes are unchanged. |
| [Path](path.md) | Second access to the complete shared Path palette. Both locations use the same operations, constants, resources and types. |
| [Text](text.md) | Existing text-file read and write operations, with unchanged connectors and behavior. |
| [XML](xml.md) | Existing XML flattening, unflattening, file write and file read operations. |
