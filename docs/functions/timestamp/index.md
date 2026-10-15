# Timestamp functions

[All functions](../index.md)

8 operations or editor elements; 0 palette folders. Open a page to inspect its exact connector, typing rules and execution limits.

## Operations and editor elements

| Entry | Purpose |
| --- | --- |
| [Date/Time To Timestamp](from_date_time.md) | A date/time Cluster (fractional second F64 and nine I32 fields) and optional UTC flag produce a Timestamp. Day-of-week and day-of-year fields do not determine the instant. Runtime support depends on the selected execution target. |
| [Format Date/Time String](format_date_time.md) | Optional time format String (%c), scalar Timestamp or real number (current time if omitted) and UTC flag produce a formatted date/time String. Runtime support depends on the selected execution target. |
| [Get Current Time](get_current_time.md) | No input; current UTC time as Timestamp, in seconds since 1904-01-01. Runtime support depends on the selected execution target. |
| [Get Date/Time String](get_date_time_string.md) | Optional scalar Timestamp or real number (current time if omitted), date format and seconds flag produce date and time Strings in the computer time zone. Runtime support depends on the selected execution target. |
| [Timestamp Constant](constant.md) | Editor-managed Timestamp constant. Uses the existing UTC date/time editor and seconds-since-1904 double storage, not NI 128-bit timestamp precision. Runtime support depends on the selected execution target. |
| [Timestamp Terminal](terminal.md) | Editor-managed Timestamp Front Panel control/indicator and linked Diagram terminal; direction follows control versus indicator. Runtime support depends on the selected execution target. |
| [Timestamp To Date/Time](to_date_time.md) | Optional scalar Timestamp or real number and UTC flag produce a Cluster: fractional second F64; second, minute, hour, day of month, month, year, day of week, day of year and DST I32. Runtime support depends on the selected execution target. |
| [To Timestamp](to_timestamp.md) | Real numeric scalar, array or Cluster of real numbers converts to Timestamp leaves, preserving array ranks and Cluster field identity. Complex and nonnumeric leaves are rejected. Runtime support depends on the selected execution target. |
