# FROG Properties

FROG Properties contains settings belonging to the current document. The
**Storage** category offers three choices for numeric array values:

| Mode | Saved representation |
| --- | --- |
| Readable | Ordinary editable JSON; the default. |
| Automatic | Keeps small arrays readable and uses embedded compressed chunks only when the complete encoded representation is smaller. |
| Compact standalone | Requests embedded binary chunks, without an external companion file. |

Metadata, identities, types, dimensions and field order remain readable and
unchanged. Compression preserves numeric authoring text exactly; it is not
encryption. Switching to Readable before saving expands the supported compact
values, subject to existing document limits. Apply changes the document option;
the next save writes the selected representation. Cancel discards the preview.

Automatic and Compact use the private Studio draft revision 3. They do not
change the public FROG 0.1 source schema. Current loading expands these values
into the existing editing model, so compact files do not promise lower working
memory or lazy loading. The
[storage profile](https://github.com/Graiphic/FROG/blob/main/docs/studio-array-storage-v1.md)
defines the exact representation and reader limits; the
[development checkpoint](../reference/development-checkpoint.md) distinguishes
compiled support from functional qualification, which is pending under the
test pause.
