# DialogUserInterface functions

[All functions](../index.md)

6 operations or editor elements; 1 palette folders. Open a page to inspect its exact connector, typing rules and execution limits.

## Operations and editor elements

| Entry | Purpose |
| --- | --- |
| [Create User Event](../dialog/events/create_user_event.md) | Creates a new source UserEvent&lt;T&gt; from the complete type of the data specimen. The specimen value is not emitted. Distinct calls create distinct identities even with the same label and schema. Arrays, cluster field identities, Enums and embedded reference metadata remain part of T. Resources are local to this application execution instance; a saved document contains only the declaration. |
| [Destroy User Event](../dialog/events/destroy_user_event.md) | Invalidates the user event source for future generation. Already published occurrences retain their exact schema and data until consumed, flushed or abandoned by Unregister. Does not globally flush or unregister consumers. Cleanup executes even with an incoming error and preserves that original error. There is no output user-event reference. |
| [Flush Event Queue](../dialog/events/flush_event_queue.md) | Atomically removes eligible pending notifications while retaining the subscription. Returns the registration and a u32 removal count, never the removed payloads. Stops before a filter event. Time and keep-most-recent protections accumulate; the retained quantity is global across targeted queues. Unwired options differ from explicit zero. Static-queue inclusion requires the actual enclosing Event case and defaults according to that context. Ordinary Queue&lt;T&gt; references are incompatible. |
| [Generate User Event](../dialog/events/generate_user_event.md) | Publishes an immutable semantic snapshot of the supplied T to current subscribers, without recursively executing a consumer. Embedded references retain identity. Priority 0 is high and 1 is normal (default); equal-priority order is stable. Without a current registration, the emission is not retained for future subscribers. Returns the same UserEvent&lt;T&gt;. Invalid, foreign or destroyed references and incompatible data produce errors. |
| [Register For Events](../dialog/events/register_for_events.md) | Creates a dynamic subscription, or updates the supplied registration without creating another queue. Each stable row associates a typed source with a compatible event from the common catalog. A UserEvent&lt;T&gt;, an EventRegistration&lt;S&gt; and the payload T are different values. Wire the resulting registration to the existing Event Structure and choose its Dynamic event case. Sharing the same registration between consumers shares its queue; create independent registrations for broadcast delivery. None, null and unwired inputs follow the documented FROG adapter contract, not a measured NI compatibility claim. |
| [Unregister For Events](../dialog/events/unregister_for_events.md) | Destroys this registration and discards its pending occurrences. Observed controls, user event sources and independent registrations remain intact. Cleanup executes even with an incoming error and preserves that original error. No valid registration is returned. Expired references are diagnosed and affected waits are cancelled explicitly. |

## Palette folders

| Entry | Purpose |
| --- | --- |
| [Events](../dialog/events.md) | Typed event sources and dynamic subscriptions. Event Structure is another access to the existing structure. Independent registrations each receive a copy; sharing a registration shares one queue. Local Studio execution resources are not persisted as live handles. |
