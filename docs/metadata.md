# Metadata

For pid4cat handles metadata are stored directly in the handle record in contrast to the DOI-system where metadata are hosted by the DOI-providers like DataCite.

The metadata for pid4cat include mainly data about the PID and its relation to other PIDs. The relation information should be relate the new PID to relevant existing PIDs. pid4cat allows but does not mandate that PIDs are updated with new relations that come into existence only later after the PID assignment to a resource.

The metadata schema for pid4cat is defined as a LinkML schema. From this LinkML schema various representations can be created.

The schema is documented under [overview](/overview).

The Python package derived from the schema is described in the section [Tools and Services](#tools-and-services) below.

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

The pid4cat metadata schema is defined using LinkML (Linked Data Modeling Language), which allows for:

- Clear definition of metadata elements
- Validation of metadata values
- Generation of various schema representations (JSON Schema, SHACL, etc.)
- Integration with semantic web technologies

The complete schema is available in the [pid4cat-model repository](https://github.com/nfdi4cat/pid4cat-model).

## Metadata Validation

All metadata submitted to pid4cat is validated against the pid4cat-model schema. This ensures:

- Required fields are present
- Field values conform to expected formats
- Structural integrity of the metadata

Validation failures result in rejection of the create or update operation, with detailed error messages to assist in correction.

## Metadata Access

pid4cat metadata can be accessed through multiple methods:

- Direct API access
- Handle record retrieval
- Metadata dumps (for bulk analysis)

All metadata is provided under a CC0 1.0 Universal Public Domain Dedication license, enabling unrestricted reuse.
