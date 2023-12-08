# Enum: RelationTypes




_The type of the relation between the resources_



URI: [RelationTypes](RelationTypes.md)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| IS_CITED_BY | None | The resource is cited by another resource |
| CITES | None | The resource cites another resource |
| IS_SUPPLEMENT_TO | None | The resource is supplemented by another resource |
| IS_SUPPLEMENTED_BY | None | The resource supplements another resource |
| IS_CONTINUED_BY | None | The resource is continued by another resource |
| CONTINUES | None | The resource continues another resource |
| HAS_METADATA | None | The resource has metadata |
| IS_METADATA_FOR | None | The resource is metadata for |
| HAS_VERSION | dct:hasVersion | The resource has a version |
| IS_VERSION_OF | dct:isVersionOf | The resource is a version of |
| IS_NEW_VERSION_OF | None | The resource is a new version of |
| IS_PREVIOUS_VERSION_OF | None | The resource is a previous version of |
| IS_PART_OF | dct:isPartOf | The resource is part of another resource |
| HAS_PART | dct:hasPart | The resource has part another resource |
| IS_DESCRIBED_BY | None | The resource is documented by another resource |
| DESCRIBES | None | The resource documents another resource |
| IS_PUBLISHED_IN | None | The resource is published in another resource |
| IS_REFERENCED_BY | dct:isReferencedBy | The resource is referenced by another resource |
| REFERENCES | None | The resource references another resource |
| IS_DOCUMENTED_BY | None | The resource is documented by another resource |
| DOCUMENTS | None | The resource documents another resource |
| IS_COMPILED_BY | None | The resource is compiled by another resource |
| COMPILES | None | The resource compiles another resource |
| IS_VARIANT_FORM_OF | None | The resource is variant form of another resource |
| IS_ORIGINAL_FORM_OF | None | The resource is original form of another resource |
| IS_IDENTICAL_TO | None | The resource is identical to another resource |
| IS_DERIVED_FROM | None | The resource is derived from another resource |
| IS_SOURCE_OF | None | The resource is source of another resource |
| IS_REQUIRED_BY | dct:isRequiredBy | The resource is required by another resource |
| REQUIRES | dct:requires | The resource requires another resource |
| IS_OBSOLETED_BY | None | The resource or PID4Cat is obsoleted by another resource or PID4Cat |
| OBSOLETES | None | The resource or PID4Cat obsoletes another resource or PID4Cat |




## Slots

| Name | Description |
| ---  | --- |
| [relation_type](relation_type.md) | Relation type between the resources |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nfdi4cat/pid4cat-model




## LinkML Source

<details>
```yaml
name: RelationTypes
description: The type of the relation between the resources
from_schema: https://w3id.org/nfdi4cat/pid4cat-model
rank: 1000
permissible_values:
  IS_CITED_BY:
    text: IS_CITED_BY
    description: The resource is cited by another resource.
  CITES:
    text: CITES
    description: The resource cites another resource.
  IS_SUPPLEMENT_TO:
    text: IS_SUPPLEMENT_TO
    description: The resource is supplemented by another resource.
  IS_SUPPLEMENTED_BY:
    text: IS_SUPPLEMENTED_BY
    description: The resource supplements another resource.
  IS_CONTINUED_BY:
    text: IS_CONTINUED_BY
    description: The resource is continued by another resource.
  CONTINUES:
    text: CONTINUES
    description: The resource continues another resource.
  HAS_METADATA:
    text: HAS_METADATA
    description: The resource has metadata.
  IS_METADATA_FOR:
    text: IS_METADATA_FOR
    description: The resource is metadata for.
  HAS_VERSION:
    text: HAS_VERSION
    description: The resource has a version.
    meaning: dct:hasVersion
  IS_VERSION_OF:
    text: IS_VERSION_OF
    description: The resource is a version of.
    meaning: dct:isVersionOf
  IS_NEW_VERSION_OF:
    text: IS_NEW_VERSION_OF
    description: The resource is a new version of.
  IS_PREVIOUS_VERSION_OF:
    text: IS_PREVIOUS_VERSION_OF
    description: The resource is a previous version of.
  IS_PART_OF:
    text: IS_PART_OF
    description: The resource is part of another resource.
    meaning: dct:isPartOf
  HAS_PART:
    text: HAS_PART
    description: The resource has part another resource.
    meaning: dct:hasPart
  IS_DESCRIBED_BY:
    text: IS_DESCRIBED_BY
    description: The resource is documented by another resource.
  DESCRIBES:
    text: DESCRIBES
    description: The resource documents another resource.
  IS_PUBLISHED_IN:
    text: IS_PUBLISHED_IN
    description: The resource is published in another resource.
  IS_REFERENCED_BY:
    text: IS_REFERENCED_BY
    description: The resource is referenced by another resource.
    meaning: dct:isReferencedBy
  REFERENCES:
    text: REFERENCES
    description: The resource references another resource.
  IS_DOCUMENTED_BY:
    text: IS_DOCUMENTED_BY
    description: The resource is documented by another resource.
  DOCUMENTS:
    text: DOCUMENTS
    description: The resource documents another resource.
  IS_COMPILED_BY:
    text: IS_COMPILED_BY
    description: The resource is compiled by another resource.
  COMPILES:
    text: COMPILES
    description: The resource compiles another resource.
  IS_VARIANT_FORM_OF:
    text: IS_VARIANT_FORM_OF
    description: The resource is variant form of another resource.
  IS_ORIGINAL_FORM_OF:
    text: IS_ORIGINAL_FORM_OF
    description: The resource is original form of another resource.
  IS_IDENTICAL_TO:
    text: IS_IDENTICAL_TO
    description: The resource is identical to another resource.
  IS_DERIVED_FROM:
    text: IS_DERIVED_FROM
    description: The resource is derived from another resource.
  IS_SOURCE_OF:
    text: IS_SOURCE_OF
    description: The resource is source of another resource.
  IS_REQUIRED_BY:
    text: IS_REQUIRED_BY
    description: The resource is required by another resource.
    meaning: dct:isRequiredBy
  REQUIRES:
    text: REQUIRES
    description: The resource requires another resource.
    meaning: dct:requires
  IS_OBSOLETED_BY:
    text: IS_OBSOLETED_BY
    description: The resource or PID4Cat is obsoleted by another resource or PID4Cat.
  OBSOLETES:
    text: OBSOLETES
    description: The resource or PID4Cat obsoletes another resource or PID4Cat.

```
</details>
