# Timestamp

Timestamp represents an instant. Its Front Panel Control/Indicator and linked
Diagram terminal keep the timestamp type separate from ordinary Numeric display
formatting.

## Edit and display

The Control uses the existing date/time editor. Indicators display the value
without accepting user input. The context menu provides **Two lines** and
**Single line** presentation. Label and clock visibility are presentation
settings; changing them does not change the instant.

Diagram Timestamp constants use the UTC date/time editor. The current Studio
storage is a double containing seconds since **1904-01-01**, rather than a
128-bit timestamp representation. Do not assume another tool's precision from
the similar appearance.

## Use in a graph

[Timestamp functions](../functions/timestamp/index.md) document current time,
formatting, and date/time conversion. Each page states the declared types and
execution boundary. A local timestamp editor does not establish execution of
every time operation on every target.
