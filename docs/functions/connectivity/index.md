# Connectivity functions

[All functions](../index.md)

35 operations or editor elements; 5 palette folders. Open a page to inspect its exact connector, typing rules and execution limits.

## Operations and editor elements

| Entry | Purpose |
| --- | --- |
| [Acquire Input Data.vi](input_device/acquire_input_data.md) | Acquires joystick, keyboard or mouse state using the instance selected by the initialized device reference. |
| [Call Library Function Node](libraries/call_library_function.md) | Calls an explicitly configured native C function. Each node embeds its library path policy, exact export and typed ABI signature. Parameter rows may be reordered visually without changing ABI argument order. Configure by double-clicking its fixed header. Local Windows/x64 execution uses the libffi adapter; advanced representations require their own marshalling and lifetime capability. |
| [Close Input Device.vi](input_device/close_input_device.md) | Closes the initialized joystick, keyboard or mouse reference using the corresponding instance. |
| [Close Python Session](python/close_session.md) | Closes a Python session, including when a previous node has returned an error. |
| [Close Registry Key.vi](registry/close_key.md) | Closes the open Windows registry key; it still performs cleanup when an incoming error exists. |
| [Create Registry Key.vi](registry/create_key.md) | Creates or opens a Windows registry key and reports whether a new key was created or an existing one opened. |
| [Delete Registry Key.vi](registry/delete_key.md) | Deletes the named child registry key in the selected registry view while forwarding the parent key reference. |
| [Delete Registry Value.vi](registry/delete_value.md) | Deletes the named value under the open registry key and forwards that key reference. |
| [Enum Registry Keys.vi](registry/enum_keys.md) | Enumerates child key names using the subkey counts and maximum name lengths from Query Registry Key Info. |
| [Enum Registry Values Simple.vi](registry/enum_values_simple.md) | Enumerates registry value names and simplified types, optionally retrieving distinct U32 DWORD and string/binary arrays. |
| [Initialize Joystick.vi](input_device/initialize_joystick.md) | Initializes the joystick selected by its signed I32 device index and returns its input-device DLL refnum. |
| [Initialize Keyboard.vi](input_device/initialize_keyboard.md) | Initializes the computer keyboard and returns the device reference used by keyboard acquisition. |
| [Initialize Mouse.vi](input_device/initialize_mouse.md) | Initializes the computer mouse and returns the device reference used by mouse acquisition. |
| [Open Python Session](python/open_session.md) | Opens a Python session for the specified version so multiple Python Nodes can share that process. |
| [Open Registry Key.vi](registry/open_key.md) | Opens a Windows registry key with the selected root, access rights, remote computer and registry view. |
| [Python Node](python/node.md) | Calls a configured Python function with extensible typed arguments and a return value determined by return type. |
| [Query Input Devices.vi](input_device/query_input_devices.md) | Enumerates joystick, keyboard and mouse information as separate one-dimensional arrays of documented clusters. |
| [Query Registry Key Info.vi](registry/query_key_info.md) | Returns the key class and separate I32 value-information and subkey-information clusters. |
| [Read Registry Value Simple.vi](registry/read_value_simple.md) | Reads string/binary or U32 registry data, selecting the instance from default data and returning that default on a missing value. |
| [SCC Add.vi](source_control/add.md) | Adds the selected files to source control. |
| [SCC Check In.vi](source_control/check_in.md) | Checks the selected files into source control and records a provider comment. |
| [SCC Check Out.vi](source_control/check_out.md) | Checks the selected files out of source control for editing. |
| [SCC Close SCC Project.vi](source_control/close_project.md) | Closes an existing source control reference. |
| [SCC Compare Files.vi](source_control/compare_files.md) | Compares a local file with its source controlled version using the selected comparison method. |
| [SCC Compare VIs.vi](source_control/compare_vis.md) | Compares a local VI with its source controlled version using LabVIEW VI comparison options. |
| [SCC File History.vi](source_control/file_history.md) | Reads provider history for selected source controlled files. |
| [SCC File Properties.vi](source_control/file_properties.md) | Displays provider properties for a selected source controlled file. |
| [SCC File Status.vi](source_control/file_status.md) | Reads source control status for each selected file and its provider status flags. |
| [SCC Get Latest Version.vi](source_control/get_latest_version.md) | Retrieves source controlled file versions into the configured local directory. |
| [SCC Not A Source Control Reference.vi](source_control/not_a_reference.md) | Checks whether a source control reference is invalid. |
| [SCC Open SCC Project.vi](source_control/open_project.md) | Creates a source control reference from the configured provider and optional LabVIEW project. |
| [SCC Remove.vi](source_control/remove.md) | Removes the selected files from source control. |
| [SCC Undo Check Out.vi](source_control/undo_check_out.md) | Cancels the source control check out for the selected files. |
| [System Exec.vi](system_exec.md) | Runs a system command or executable and returns its standard streams and exit code. |
| [Write Registry Value Simple.vi](registry/write_value_simple.md) | Writes string/binary or U32 DWORD data to a named registry value using the verified write connector. |

## Palette folders

| Entry | Purpose |
| --- | --- |
| [Input Device Control](input_device.md) | Author joystick, keyboard and mouse device operations. Device and result schemas are explicit and distinct. |
| [Libraries &amp; Executables](libraries.md) | Author external executable calls and static references to FROG documents. Call Library Function Node is intentionally excluded. |
| [Python](python.md) | Author Python sessions and extensible Python Node signatures. The return type controls the result connector; no Python code is executed while editing. |
| [Source Control](source_control.md) | Author source-control configuration, file status, checkout, check-in and repository operations. The connector declares its provider-specific types. |
| [Windows Registry Access VIs](registry.md) | Author typed Windows Registry access, key creation, enumeration and value operations. No registry operation is executed while editing. |
