# Enum: ResourceCategories




_The category of the resource_



URI: [ResourceCategories](ResourceCategories.md)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| COLLECTION | http://purl.org/dc/dcmitype/Collection | A collection is described as a group; its parts may also be separately descri... |
| CATALYST | None | A physical entity meant to be applied as catalyst |
| MATERIAL | None | A material used in the catalysis research process (except the catalyst itself... |
| DEVICE | None | A device used in the catalysis research process |
| DATAOBJECT | None | A data object might be a data file, a data set, a data collection, or a data ... |




## Slots

| Name | Description |
| ---  | --- |
| [resource_category](resource_category.md) | The category of the resource |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nfdi4cat/pid4cat-model




## LinkML Source

<details>
```yaml
name: ResourceCategories
description: The category of the resource
from_schema: https://w3id.org/nfdi4cat/pid4cat-model
rank: 1000
permissible_values:
  COLLECTION:
    text: COLLECTION
    description: A collection is described as a group; its parts may also be separately
      described.
    meaning: http://purl.org/dc/dcmitype/Collection
  CATALYST:
    text: CATALYST
    description: A physical entity meant to be applied as catalyst.
    todos:
    - map this to an ontology
  MATERIAL:
    text: MATERIAL
    description: A material used in the catalysis research process (except the catalyst
      itself).
    todos:
    - map this to an ontology
  DEVICE:
    text: DEVICE
    description: A device used in the catalysis research process.
    todos:
    - map this to an ontology
  DATAOBJECT:
    text: DATAOBJECT
    description: A data object might be a data file, a data set, a data collection,
      or a data service.
    todos:
    - map this to an ontology

```
</details>
