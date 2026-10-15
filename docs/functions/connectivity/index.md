# Connectivity functions

[All functions](../index.md)

130 operations or editor elements; 20 palette folders. Open a page to inspect its exact connector, typing rules and execution limits.

## Operations and editor elements

| Entry | Purpose |
| --- | --- |
| [.NET Object To Variant.vi](dotnet/object_to_variant.md) | Converts a .NET Framework object reference to a LabVIEW variant while retaining the error connector. |
| [.NET Reference](../dotnet/reference.md) | Authors a typed null .NET reference constant. The selected CLR class is resolved from the saved configuration and inspected assembly metadata; this constant does not construct an instance. |
| [Acquire Input Data.vi](input_device/acquire_input_data.md) | Acquires joystick, keyboard or mouse state using the instance selected by the initialized device reference. |
| [Automation Open](activex/automation_open.md) | Creates or obtains an automation reference for the selected creatable ActiveX class and optional remote computer. |
| [Call Library Function Node](libraries/call_library_function.md) | Calls an explicitly configured native C function. Each node embeds its library path policy, exact export and typed ABI signature. Parameter rows may be reordered visually without changing ABI argument order. Configure by double-clicking its fixed header. Local Windows/x64 execution uses the libffi adapter; advanced representations require their own marshalling and lifetime capability. |
| [Check If Session Exists.vi](web_services/application/sessions/exists.md) | Checks whether the current HTTP request has an associated HTTP session. |
| [Close Input Device.vi](input_device/close_input_device.md) | Closes the initialized joystick, keyboard or mouse reference using the corresponding instance. |
| [Close Python Session](python/close_session.md) | Closes a Python session, including when a previous node has returned an error. |
| [Close Reference](activex/close_reference.md) | Closes an ActiveX automation reference or a one-dimensional array of automation references. |
| [Close Reference](dotnet/close_reference.md) | Closes a .NET object reference or a one-dimensional array of .NET references. |
| [Close Reference.vi](datafinder/close_reference.md) | Closes a DataFinder connection, a reference to a query, or references to search results. To select the polymorphic instance, connect data to the appropriate input or select the instance manually. |
| [Close Registry Key.vi](registry/close_key.md) | Closes the open Windows registry key; it still performs cleanup when an incoming error exists. |
| [Constructor Node](dotnet/constructor.md) | Selects a documented .NET constructor and exposes its initialization parameters and constructed class reference. |
| [Create Index Job File.vi](datafinder/create_index_job_file.md) | Creates a job file for indexing certain files or folders from the search areas of a DataFinder server. |
| [Create Query.vi](datafinder/create_query.md) | Creates a query. You can search for text, paths, numeric values, and time/date values. Use the instance Order by only to sort search results according to a property without searching for this particular property. Use the Merge Queries VI to query conditions to each other. Use the Execute Query VI to execute a query that consists of one or more search conditions. To select the polymorphic instance, connect data to the appropriate input or select the instance manually. |
| [Create Registry Key.vi](registry/create_key.md) | Creates or opens a Windows registry key and reports whether a new key was created or an existing one opened. |
| [Create Session.vi](web_services/application/sessions/create.md) | Creates an HTTP session for the current HTTP request. |
| [Database Variant To Data](database/variant_to_data.md) | Converts a database variant to the LabVIEW data type specified in type so you can use the data in another function or subVI. |
| [DataFinder Property Node.vi](datafinder/property_node.md) | Provides properties that you use to configure the DataFinder. |
| [DB Tools Close Connection.vi](database/close_connection.md) | Closes a database connection by destroying its associated connection reference . |
| [DB Tools Create Parameterized Query.vi](database/create_parameterized_query.md) | Creates a parameterized SQL query and returns a command reference that you must free eventually. Unless you are detecting the parameters automatically, the number of elements in the parameters array must match the number of parameters you specify in SQL query . For stored procedures, set stored procedure to TRUE and SQL query to the name of the procedure you want to execute. |
| [DB Tools Create Table.vi](database/create_table.md) | Creates a new table in the database identified by connection reference . The table and column information inputs describe the name of the table and the properties of each column in the table, respectively. |
| [DB Tools Database Transaction.vi](database/transaction.md) | Begins, commits, or rolls back a transaction for any type of reference. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance. |
| [DB Tools Delete Data.vi](database/delete_data.md) | Deletes data from a database identified by connection reference . |
| [DB Tools Drop Table.vi](database/drop_table.md) | Deletes the specified table from the database identified by connection reference . |
| [DB Tools Execute Query.vi](database/execute_query.md) | Executes an SQL query and returns a recordset reference that you must eventually free with the DB Tools Free Object VI. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance. |
| [DB Tools Fetch Element Data.vi](database/fetch_element_data.md) | Retrieves the data located at the column index of the current record in the recordset identified by the recordset reference . The column index can be either the zero-indexed position of the column in the recordset or the name of the column. Wire data to the type input to determine the polymorphic instance to use or manually select the instance. |
| [DB Tools Fetch Next Recordset.vi](database/fetch_next_recordset.md) | Retrieves the next recordset in a multi-recordset query identified by recordset reference . When the current recordset is no longer available, the recordset reference is redirected to the new recordset. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance. |
| [DB Tools Fetch Recordset Data.vi](database/fetch_recordset_data.md) | Retrieves the data in the recordset identified by the recordset reference input. You can convert each element in the array to its native LabVIEW data type using the Database Variant To Data function. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance. |
| [DB Tools Format Datetime String.vi](database/format_datetime_string.md) | Returns a string containing the formatted date and time, and identifies the string as a date/time string so other VIs can interpret this string. Wire data to the input of this VI to determine the polymorphic instance to use or manually select the instance. |
| [DB Tools Free Object.vi](database/free_object.md) | Frees an object by destroying its associated reference and returns a different reference object. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance. |
| [DB Tools Get Parameter Value.vi](database/get_parameter_value.md) | Retrieves the value of the parameter specified by the parameter index input in the command or command-recordset. The parameter index can be either the zero-indexed position of the parameter in the command or the name of the parameter. Wire data to the type input to determine the polymorphic instance to use or manually select the instance. |
| [DB Tools Get Properties.vi](database/get_properties.md) | Gets properties of the object as determined by the inputs. This VI works for connections, commands, recordsets, columns, and parameters. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance. |
| [DB Tools Insert Data.vi](database/insert_data.md) | Inserts a new row into the table in the database identified by the connection reference . |
| [DB Tools List Columns.vi](database/list_columns.md) | Lists the columns present in table . The column information includes the name, the data type, and the defined size of the column. |
| [DB Tools List Tables.vi](database/list_tables.md) | Lists the tables in the database identified by connection reference . |
| [DB Tools Load Recordset From File.vi](database/load_recordset_from_file.md) | Loads a recordset from a file and returns a recordset reference that identifies this recordset. You can retrieve data from this recordset like any other recordset, but some properties might not be available on this recordset. |
| [DB Tools Move To Next Record.vi](database/move_to_next_record.md) | Moves the cursor to point to the next record in the recordset identified by the reference. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance. |
| [DB Tools Move To Previous Record.vi](database/move_to_previous_record.md) | Moves the cursor to point to the previous record in the recordset. You cannot use this VI with a forward-only cursor. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance. |
| [DB Tools Move To Record N.vi](database/move_to_record_n.md) | Moves the cursor to point to record n in the recordset. To move the cursor to the last record, set n to -1. You cannot use this VI with a forward-only cursor. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance. |
| [DB Tools NULL.vi](database/null.md) | Returns a database variant that contains a NULL value. |
| [DB Tools Open Connection.vi](database/open_connection.md) | Opens a database connection using the connection information path and returns a connection reference. If prompt? is set to TRUE, LabVIEW displays a dialog box to set up the connection. Wire data to the connection information input to determine the polymorphic instance to use or manually select the instance. |
| [DB Tools Save Recordset To File.vi](database/save_recordset_to_file.md) | Saves the recordset identified by the recordset reference to either an XML or ADTG file. The ADTG file format is a proprietary format that only the LabVIEW Database Connectivity Toolkit can interpret. The ADTG format results in a smaller file than the XML format. You can reload both formats into LabVIEW using the DB Tools Load Recordset From File VI. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance. |
| [DB Tools Select Data.vi](database/select_data.md) | Selects data from the table in the database identified by connection reference using the columns supplied in the columns array. This VI returns the data as a 2D array of variants. You can convert each element in the array to its native LabVIEW data type using the Database Variant To Data function. |
| [DB Tools Set Parameter Value.vi](database/set_parameter_value.md) | Sets the value of the parameter at parameter index in the command or command-recordset. The parameter index can be either the zero-indexed position of the parameter in the command or the name of the parameter. Wire data to the reference input to determine the polymorphic instance to use or manually select the instance. |
| [DB Tools Set Properties.vi](database/set_properties.md) | Sets properties on the object as determined by the inputs. Wire data to the reference and properties inputs to determine the polymorphic instance to use or manually select the instance. |
| [DB Tools Update Data.vi](database/update_data.md) | Updates the data in a database identified by connection reference . |
| [Decrypt.vi](web_services/application/security/decrypt.md) | Decrypts data using the key associated with the current HTTP request. |
| [Delete Registry Key.vi](registry/delete_key.md) | Deletes the named child registry key in the selected registry view while forwarding the parent key reference. |
| [Delete Registry Value.vi](registry/delete_value.md) | Deletes the named value under the open registry key and forwards that key reference. |
| [Delete Session Variable.vi](web_services/application/sessions/delete_variable.md) | Deletes the named variable from the current HTTP session. |
| [Destroy Session.vi](web_services/application/sessions/destroy.md) | Destroys the HTTP session associated with the current request. |
| [Encrypt.vi](web_services/application/security/encrypt.md) | Encrypts request data using the key associated with the current HTTP request. |
| [Enum Registry Keys.vi](registry/enum_keys.md) | Enumerates child key names using the subkey counts and maximum name lengths from Query Registry Key Info. |
| [Enum Registry Values Simple.vi](registry/enum_values_simple.md) | Enumerates registry value names and simplified types, optionally retrieving distinct U32 DWORD and string/binary arrays. |
| [Escape HTTP URL.vi](web_services/conversion/escape_url.md) | Replaces special URL characters with percent-encoded escape sequences. |
| [Execute Query Ex.vi](datafinder/execute_query.md) | Uses the DataFinder to search the specified properties of the indexed data. |
| [Flush Output.vi](web_services/output/flush_output.md) | Sends buffered HTTP response data to the socket. |
| [Get Auth Details for NI Web Server.vi](web_services/ni_web_server/get_auth_details.md) | Reads NI Web Server user identity and request privileges. |
| [Get Auth Details.vi](web_services/application/security/get_auth_details.md) | Reads Application Web Server username, groups, permissions and login-session key. |
| [Get Indexed Properties.vi](datafinder/get_indexed_properties.md) | Determines for files, groups, or channels, the list of all the indexed properties in which you can execute a search with the DataFinder. |
| [Get Indexed Value Limits.vi](datafinder/get_indexed_value_limits.md) | Returns the minimum indexed value and the maximum indexed value of the given numeric or date/time property. If a query is provided, the minimum and maximum values are restricted to the given query conditions. |
| [Get Indexed Value List.vi](datafinder/get_indexed_value_list.md) | Returns a list of strings which contains all indexed values for the specified string property. You can restrict the list of values by setting a prefix. The list is also restricted by the given query. |
| [Get Property Values.vi](datafinder/get_property_values.md) | Determines from the result references the values of one or more properties that are the same data type. To select the polymorphic instance, connect data to the Data Type input or to the Property input or select the instance manually. |
| [Get Session ID Cookie.vi](web_services/application/sessions/get_id_cookie.md) | Reads the cookie identifying the HTTP session for this client. |
| [Get Web Service Status.vi](web_services/service/get_status.md) | Reports whether the current LabVIEW Web service is stopping. |
| [Initialize Joystick.vi](input_device/initialize_joystick.md) | Initializes the joystick selected by its signed I32 device index and returns its input-device DLL refnum. |
| [Initialize Keyboard.vi](input_device/initialize_keyboard.md) | Initializes the computer keyboard and returns the device reference used by keyboard acquisition. |
| [Initialize Mouse.vi](input_device/initialize_mouse.md) | Initializes the computer mouse and returns the device reference used by mouse acquisition. |
| [Invoke Node (.NET)](dotnet/invoke_node.md) | Invokes a selected .NET method overload with its exact input, output, bidirectional and return-value parameters. |
| [Invoke Node (ActiveX)](activex/invoke_node.md) | Invokes a configured ActiveX method with the exact parameters from the selected type-library member. |
| [LV Image to PNG Data.vi](web_services/conversion/image_to_png.md) | Encodes the LabVIEW image data cluster as a binary PNG buffer. |
| [Merge Queries.vi](datafinder/merge_queries.md) | Uses an operator to combine several queries into one query. For example, you can generate queries as "C1 AND C2 AND C3", "(C1 AND C2) OR C3", or "(C1 AND C2) OR (C3 AND C4). |
| [Open Python Session](python/open_session.md) | Opens a Python session for the specified version so multiple Python Nodes can share that process. |
| [Open Registry Key.vi](registry/open_key.md) | Opens a Windows registry key with the selected root, access rights, remote computer and registry view. |
| [Open Server.vi](datafinder/open_server.md) | Connects a DataFinder or a DataFinder federation with the specified connection parameters. |
| [PNG Data to LV Image.vi](web_services/conversion/png_to_image.md) | Converts a binary PNG buffer into the LabVIEW image data cluster. |
| [Property Node (.NET)](dotnet/property_node.md) | Reads or writes selected properties of a .NET object, with one typed terminal per configured property row. |
| [Property Node (ActiveX)](activex/property_node.md) | Reads or writes configured ActiveX properties using their documented types and access permissions. |
| [Python Node](python/node.md) | Calls a configured Python function with extensible typed arguments and a return value determined by return type. |
| [Query Input Devices.vi](input_device/query_input_devices.md) | Enumerates joystick, keyboard and mouse information as separate one-dimensional arrays of documented clusters. |
| [Query Registry Key Info.vi](registry/query_key_info.md) | Returns the key class and separate I32 value-information and subkey-information clusters. |
| [Read All Form Data.vi](web_services/read_all_form_data.md) | Reads all multipart form fields into parallel one-dimensional key, value and MIME type arrays. |
| [Read All Request Variables.vi](web_services/read_all_request_variables.md) | Reads the current HTTP request variables as parallel key and value arrays. |
| [Read All Session Variables.vi](web_services/application/sessions/read_all_variables.md) | Reads HTTP session variables as parallel key and value arrays. |
| [Read Form Data.vi](web_services/read_form_data.md) | Reads one multipart form field value and its MIME type from the current HTTP request. |
| [Read Postdata.vi](web_services/read_postdata.md) | Reads the POST body associated with the current HTTP request. |
| [Read Registry Value Simple.vi](registry/read_value_simple.md) | Reads string/binary or U32 registry data, selecting the instance from default data and returning that default on a missing value. |
| [Read Request Variable.vi](web_services/read_request_variable.md) | Reads a named server or HTTP request variable. |
| [Read Service Attribute.vi](web_services/service/read_attribute.md) | Reads a named attribute of the current LabVIEW Web service. |
| [Read Session Variable.vi](web_services/application/sessions/read_variable.md) | Reads the string value of a named HTTP session variable. |
| [Read Uploaded Files Info.vi](web_services/read_uploaded_files_info.md) | Reads temporary paths, client filenames, content types and sizes of uploaded request files. |
| [Register Event Callback](activex/register_event_callback.md) | Registers extensible event-source, strict callback-reference and user-data groups for local ActiveX objects. |
| [Register Event Callback](dotnet/register_event_callback.md) | Registers one or more strict callback references for documented events of local .NET objects. |
| [Render ESP Template.vi](web_services/application/output/render_esp_template.md) | Renders the named ESP scripting template for the current HTTP request. |
| [Results to Waveforms.vi](datafinder/results_to_waveforms.md) | Extracts the signals from the results of a DataFinder search. To select the polymorphic instance, connect data to the Data type input or select the instance manually. |
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
| [Search Text Ex.vi](datafinder/search_text.md) | Uses the DataFinder to search in all of the text properties of the indexed files. |
| [Set ESP Variable.vi](web_services/application/output/set_esp_variable.md) | Assigns one or more typed values to variables available in an ESP scripting template. |
| [Set HTTP Header.vi](web_services/output/set_header.md) | Assigns a header field in the current streaming HTTP response. |
| [Set HTTP Redirect.vi](web_services/output/set_redirect.md) | Sets an HTTP redirect for the current streaming response. |
| [Set HTTP Response Code.vi](web_services/output/set_http_code.md) | Sets the HTTP status code returned to the client. |
| [Set HTTP Response MIME Type.vi](web_services/output/set_mime_type.md) | Sets the MIME type of the current HTTP response. |
| [Static VI Reference](activex/static_vi_reference.md) | References a selected document with generic or strict connector typing, matching Static VI Reference in the ActiveX palette. |
| [Static VI Reference](dotnet/static_vi_reference.md) | Maintains a static reference to a selected document with either a generic reference or its exact strict connector schema. |
| [System Exec.vi](system_exec.md) | Runs a system command or executable and returns its standard streams and exit code. |
| [To .NET Object.vi](dotnet/to_dotnet_object.md) | Converts supported numeric, string, Boolean, timestamp, path, .NET reference and array data to a .NET Framework object. |
| [To More Generic Class](dotnet/to_more_generic_class.md) | Upcasts a .NET reference to the configured ancestor class without adding error terminals. |
| [To More Specific Class](dotnet/to_more_specific_class.md) | Downcasts a .NET reference to the configured descendant class and reports an invalid cast through the error cluster. |
| [To Variant](activex/to_variant.md) | Encapsulates typed LabVIEW or ActiveX data as a variant; this conversion has no error terminals. |
| [Unescape HTTP URL.vi](web_services/conversion/unescape_url.md) | Converts percent-encoded URL escape sequences back into characters. |
| [Unregister For Events](activex/unregister_for_events.md) | Unregisters the events associated with an ActiveX callback registration reference. |
| [Unregister For Events](dotnet/unregister_for_events.md) | Unregisters the events associated with a .NET callback registration reference. |
| [Variant To Data](activex/variant_to_data.md) | Extracts typed data or an ActiveX interface from a variant using the complete schema wired to type. |
| [Write Registry Value Simple.vi](registry/write_value_simple.md) | Writes string/binary or U32 DWORD data to a named registry value using the verified write connector. |
| [Write Response.vi](web_services/output/write_response.md) | Writes response text for an HTTP method configured to stream its output. |
| [Write Session Variable.vi](web_services/application/sessions/write_variable.md) | Creates or replaces typed session variables and returns their previous string values. |

## Palette folders

| Entry | Purpose |
| --- | --- |
| [.NET](dotnet.md) | Author .NET references, constructors, properties, methods, class conversions and callbacks. Connector types come from declared metadata; authoring does not activate objects. |
| [ActiveX](activex.md) | Author ActiveX automation references, properties, methods, class conversions and callbacks from declared metadata without activating COM objects. |
| [Advanced](database/advanced.md) | Author database command, parameter, recordset and cursor operations using distinct nominal references. |
| [Application Web Server](web_services/application_web_server.md) | Author Application Web Server response, session and security operations. This context is distinct from the NI Web Server. |
| [Conversion](web_services/conversion.md) | Author conversion of Web Service text or request data to the explicitly declared result type. |
| [Database](database.md) | Author typed database connections, queries, recordsets and conversions, with separate utility and advanced operations. |
| [DataFinder](datafinder.md) | Author DataFinder server, query, result and indexing operations. Signatures that require unavailable metadata remain explicitly unresolved. |
| [Input Device Control](input_device.md) | Author joystick, keyboard and mouse device operations. Device and result schemas are explicit and distinct. |
| [Libraries &amp; Executables](libraries.md) | Author external executable calls and static references to FROG documents. Call Library Function Node is intentionally excluded. |
| [NI Web Server](web_services/ni_web_server.md) | Author status requests for the NI Web Server. Runtime execution requires an explicit compatible provider. |
| [Output](web_services/application_web_server/output.md) | Author Web Service response bodies, headers, cookies and output stream operations with their declared data types. |
| [Output](web_services/output.md) | Author Web Service response bodies, headers, cookies and output stream operations with their declared data types. |
| [Python](python.md) | Author Python sessions and extensible Python Node signatures. The return type controls the result connector; no Python code is executed while editing. |
| [Security](web_services/application_web_server/security.md) | Author Web Service authentication and security checks using the relevant request or service reference. |
| [Service](web_services/service.md) | Author operations on the Web Service itself, using a service reference rather than a request value. |
| [Sessions](web_services/application_web_server/sessions.md) | Author creation, lookup, update and deletion of Web Service sessions and their named values. |
| [Source Control](source_control.md) | Author source-control configuration, file status, checkout, check-in and repository operations. The connector declares its provider-specific types. |
| [Utility](database/utility.md) | Author database transaction, error, variant and formatting utilities, retaining their actual types and connector defaults. |
| [Web Services](web_services.md) | Author typed Web Service request handling, request data, responses and service status. Browse the specialized output, conversion and server palettes. |
| [Windows Registry Access VIs](registry.md) | Author typed Windows Registry access, key creation, enumeration and value operations. No registry operation is executed while editing. |
