# Enum: PID4CatStatus




_The status of the PID4CatRecord._



URI: [PID4CatStatus](PID4CatStatus.md)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| SUBMITTED | None | The PID4CatRecord is reserved but the resource is not yet linked |
| REGISTERED | None | The PID4CatRecord links to a concrete ressource |
| OBSOLETED | None | The PID4CatRecord is obsolete, e |
| DEPRECATED | None | The PID4CatRecord is deprecated, e |




## Slots

| Name | Description |
| ---  | --- |
| [status](status.md) | The status of the PID4CatRecord |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nfdi4cat/pid4cat-model




## LinkML Source

<details>
```yaml
name: PID4CatStatus
description: The status of the PID4CatRecord.
from_schema: https://w3id.org/nfdi4cat/pid4cat-model
rank: 1000
permissible_values:
  SUBMITTED:
    text: SUBMITTED
    description: The PID4CatRecord is reserved but the resource is not yet linked.
  REGISTERED:
    text: REGISTERED
    description: The PID4CatRecord links to a concrete ressource.
  OBSOLETED:
    text: OBSOLETED
    description: The PID4CatRecord is obsolete, e.g. because the resource is referenced
      by another PID4Cat.
  DEPRECATED:
    text: DEPRECATED
    description: The PID4CatRecord is deprecated, e.g. because the resource can no
      longer be found.

```
</details>
