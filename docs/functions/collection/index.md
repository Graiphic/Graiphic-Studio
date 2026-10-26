# Collection functions

[All functions](../index.md)

22 operations or editor elements; 2 palette folders. Open a page to inspect its exact connector, typing rules and execution limits.

## Operations and editor elements

| Entry | Purpose |
| --- | --- |
| [Build Map](map/build.md) | Builds Map&lt;K,V&gt; from stable key/value rows, evaluated in logical row order; the last duplicate key wins. An empty Build retains its resolved type. |
| [Build Set](set/build.md) | Builds set&lt;T&gt; from stable element rows using the common comparison policy. Duplicate values occur once. An Array as T remains one complete element. |
| [Collection Size](size.md) | Counts Map entries or distinct Set elements, as i32. Counts neither nested contents nor allocated capacity. Map and Set palettes access the same operation. |
| [Convert Map To Array](map/to_array.md) | Places an editable For with AtomicElements indexing and a real internal wire. Map iteration supplies a typed (key,value) cluster in key order; output is a 1D Array of these complete entries. Nested Arrays are not flattened. |
| [Convert Set To Array](set/to_array.md) | Places an editable For with AtomicElements indexing and its internal wire. Each ordered element T produces one output Array element, even when T is itself an Array. Empty Sets retain the output element schema. |
| [Element of Set?](set/contains.md) | found? is true when the complete element belongs to the Set, false when absent or empty. The Set is unchanged. |
| [Empty Collection?](empty.md) | True only for a collection with zero entries/elements. A stored zero, False or empty string is still an element. This read-only test never empties the collection. |
| [In Place Map Access](map/in_place_access.md) | Places the common IPE with one Map Get/Replace pair. Action 0 modifies only if found; 1 adds or modifies; 2 deletes. Both absence flags describe the original lookup, including after insertion. Other value branches remain independent. |
| [Insert Into Map](map/insert.md) | Inserts or replaces a key. key already included? describes the input. FROG: value unchanged? is true only for an existing key and equivalent value. Other branches retain their input value. |
| [Insert Into Set](set/insert.md) | Adds an absent element. already included? reports membership before insertion and is true for an existing element; no duplicate is created. |
| [Look In Map](map/look.md) | Reads a value without insertion. key not found? distinguishes a missing key from a stored default-valued entry. The optional default preserves full V; unwired uses its typed default. |
| [Map Constant](map/constant.md) | A Map type model and complete value. Setting K and V creates no entries. Copy Data and Paste Data transfer compatible complete typed data. Unconfigured constants remain editable but cannot run. |
| [Read Map Max &amp; Min Keys](map/extrema.md) | Returns extreme keys, not extreme values, using the common ordering policy. FROG: an empty Map returns the typed K defaults; use Empty Collection? to detect emptiness. |
| [Read Set Max &amp; Min](set/extrema.md) | Returns extreme elements using the common ordering policy. FROG: an empty Set returns typed T defaults; Empty Collection? distinguishes this case. |
| [Remove From Map](map/remove.md) | Removes only the requested key and returns its value. key not found? is true when absent. FROG: an absent value returns the typed V default and leaves the Map unchanged. |
| [Remove From Set](set/remove.md) | Removes the complete requested value, not an Array index. not included? is true if absent. Removing the last element preserves a typed empty Set. |
| [Set Cartesian Product](set/cartesian_product.md) | Forms set&lt;cluster&lt;first:A,second:B&gt;&gt; for every pair from the two Sets. Fields preserve input order and full types. Capacity is bounded and cancellation is supported. Search also accepts Set Cartesian Product.vim. |
| [Set Constant](set/constant.md) | A Set element type model and complete value. Defining T inserts no default element. Copy Data and Paste Data transfer the complete typed Set, including an empty Set. |
| [Set Difference](set/difference.md) | Returns elements in set_a that are not in set_b. The operation is directional and preserves the complete element schema. Search also accepts Set Difference.vim. |
| [Set Intersection](set/intersection.md) | Returns values present in both Sets of the same complete element type. Empty/disjoint inputs produce a typed empty Set. Search also accepts Set Intersection.vim. |
| [Set Symmetric Difference](set/symmetric_difference.md) | Returns values present in exactly one input Set. Equal inputs produce a typed empty Set. Search also accepts Set Symmetric Difference.vim. |
| [Set Union](set/union.md) | Returns values in either Set, once each, with the same complete element type and common order. Search also accepts Set Union.vim; no .vim loader is used. |

## Palette folders

| Entry | Purpose |
| --- | --- |
| [Map](map.md) | Ordered typed associations with unique keys. Maps have value semantics; their key and value models do not insert entries. |
| [Set](set.md) | Ordered typed unique elements, independent from Arrays and references. |
