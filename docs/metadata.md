# Metadata

For pid4cat handles metadata are stored directly in the handle record. In this respect, pid4cat-handles are similar to [ePIC](http://www.pidconsortium.net/)-handles which also use the handle record to store metadata. The DOI-system is, however, different: Its metadata are managed by the DOI-providers like DataCite in separate data systems.

The metadata for pid4cat mainly include data about the PID and its relation to other PIDs. The relation information should relate the new PID to relevant existing PIDs. pid4cat allows, but does not mandate, that PIDs are updated with new relations that come into existence only later, after the PID assignment to a resource.

The metadata schema for pid4cat is defined as a Linked Data Modeling Language (LinkML) schema. From this LinkML schema various representations can be created.

The schema is documented under [overview](./elements/overview.md).

The Python package derived from the schema is described in the section [Tools and Services](./tools.md).

## Core Metadata Elements

pid4cat requires a set of core metadata elements for each identifier:

| Element            | Description                                                           | Required |
| ------------------ | --------------------------------------------------------------------- | -------- |
| `EMAIL`            | Contact email of PID curator in responsible SNAA.                     | Yes      |
| `STATUS`           | PID status information                                                | Yes      |
| `SCHEMA_VER`       | The version of the pid4cat metadata model                             | Yes      |
| `METADATA_LICENSE` | SPDX license specifier "CC0-1.0"                                      | Yes      |
| `RESOURCE`         | Information about the resource and its representation (json)          | Yes      |
| `RELATED`          | Information about related identifiers and the type of relation (json) | No       |
| `CHANGES`          | Structured change log for the PID record (json)                       | Yes      |

These metadata elements are stored in the handle records of pid4cat PIDs.

## Metadata Schema

The pid4cat metadata schema is defined using LinkML, which allows for:

- Clear definition of metadata elements
- Validation of metadata values
- Generation of various schema representations (JSON Schema, SHACL, etc.)
- Integration with semantic web technologies

The complete schema is available in the [pid4cat-model repository](https://github.com/nfdi4cat/pid4cat-model).

## Permanent URIs for the metadata schema

All elements in the schema (classes, slots, enums) have [w3id.org](https://w3id.org/)-URIs.
These point to the latest schema version released.<BR>For example: [https://w3id.org/nfdi4cat/pid4cat-model/class/HandleRecord](https://w3id.org/nfdi4cat/pid4cat-model/class/HandleRecord) is redirected to  <BR> [https://nfdi4cat.github.io/pid4cat-model/latest/elements/classes/HandleRecord/](https://nfdi4cat.github.io/pid4cat-model/latest/elements/classes/HandleRecord/).

Schema elements from older releases can also be referenced via permanent URIs. For example, to reference the same class but from Release 0.4.0, just insert the release tag into the URI:<BR>
[https://w3id.org/nfdi4cat/pid4cat-model/**v0.4.0**/class/HandleRecord](https://w3id.org/nfdi4cat/pid4cat-model/v0.4.0/class/HandleRecord)

The full LinkML schema in YAML format can be downloaded from [https://w3id.org/nfdi4cat/pid4cat-model/](https://w3id.org/nfdi4cat/pid4cat-model/) when specifying the media type `application/yaml`.

Example download command for [httpie](https://httpie.io/docs/cli):

```bash
http -o pid4cat_model.yaml --download https://w3id.org/nfdi4cat/pid4cat-model Accept:"application/yaml"
```

for [curl](https://curl.se/):

```bash
curl -o pid4cat_model.yaml -L -H "accept:application/yaml" https://w3id.org/nfdi4cat/pid4cat-model
```

## Metadata Validation

All metadata submitted to pid4cat is validated against the pid4cat-model schema. This ensures:

- Required fields are present
- Field values conform to expected formats
- Structural integrity of the metadata

Validation failures result in rejection of the current operation (create or update), with detailed error messages to assist in their correction.

## Metadata Access

pid4cat metadata can be accessed using the following methods:

- Direct API access
- Handle record retrieval
- Metadata dumps (for bulk analysis)

All metadata is provided under a CC0 1.0 Universal Public Domain Dedication license, enabling unrestricted reuse.
