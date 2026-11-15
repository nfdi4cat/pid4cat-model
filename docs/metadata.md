# Metadata

pid4cat handles store their metadata directly in the handle record, as [ePIC](http://www.pidconsortium.net/) handles do.
DOI metadata, in contrast, are managed by DOI providers such as DataCite in separate systems.

The metadata describe the PID and its relations to other PIDs.
Relations to relevant existing PIDs should be given when the PID is created; relations that come into existence later may be added, but this is not required.

The metadata schema is defined in the Linked Data Modeling Language (LinkML) and documented in [Schema](./elements/overview.md).
The Python package derived from the schema is described in [Tools and Services](./tools.md).

## Core Metadata Elements

pid4cat requires a set of core metadata elements for each identifier:

| Element            | Description                                                           | Required |
| ------------------ | --------------------------------------------------------------------- | -------- |
| `URL`              | Landing page URL                                                      | Yes      |
| `EMAIL`            | Contact email of PID curator in responsible SNAA                      | Yes      |
| `STATUS`           | PID status information                                                | Yes      |
| `SCHEMA_VER`       | The version of the pid4cat metadata model                             | Yes      |
| `METADATA_LICENSE` | SPDX license specifier "CC0-1.0"                                      | Yes      |
| `RESOURCE`         | Information about the resource and its representation (json)          | Yes      |
| `RELATED`          | Information about related identifiers and the type of relation (json) | No       |
| `CHANGES`          | Structured change log for the PID record (json)                       | Yes      |

These metadata elements are stored in the handle records of pid4cat PIDs.

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

The pid4cat registry validates all metadata against the pid4cat-model schema.
A request with invalid metadata is rejected with an error message for each problem.

## Metadata Access

pid4cat metadata can be read with the [pid4cat registry API](./apis.md#pid4cat-registry-api) and, for PIDs on the Handle server, publicly with the [Handle.net API](./apis.md#handlenet-api).
All metadata is provided under the CC0 1.0 Universal Public Domain Dedication, enabling unrestricted reuse.
