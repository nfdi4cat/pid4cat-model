# Versioning of the pid4cat-model

The versioning of the pid4cat-model is following the **SchemaVer** scheme proposed in a [snowplow blog post](https://snowplow.io/blog/introducing-schemaver-for-semantic-versioning-of-schemas). The same principles are applied for the [HCA schema versioning](https://github.com/HumanCellAtlas/metadata-schema/blob/master/docs/evolution.md#schema-versioning). SchemaVer is also adapted by [openlineage](https://github.com/OpenLineage/OpenLineage/blob/main/spec/Versioning.md).

**SchemaVer**: Given a version number MODEL.REVISION.ADDITION, increment the

- MODEL when you make a breaking schema change which will prevent interaction with any historical data
- REVISION when you make a schema change which may prevent interaction with some historical data
- ADDITION when you make a schema change that is compatible with all historical data

## Schema version and package version

The schema version is set in the `version` of the schema file `pid4cat_model.yaml` and changes only when the schema changes.
pid4cat records state the schema version they follow in `schema_version` (handle record type `SCHEMA_VER`) with a leading "v", for example "v0.4.3".
The Python package provides it as `pid4cat_model.SCHEMA_VERSION`.

The version of the Python package `pid4cat-model` has four parts, MODEL.REVISION.ADDITION.N (PEP 440):
the first three parts are the schema version, and N counts releases of code, dependencies or documentation for the same schema.
The first release of a schema version has no fourth part.
For example, package 0.4.3.2 is the second release after 0.4.3 that leaves schema version 0.4.3 unchanged.

Releases 0.4.0 to 0.4.2 used a three-part package version for code-only changes; their schema is the same as schema version 0.4.3.

The Python classes in `pid4cat_model.datamodel` are generated from the schema with LinkML.
The LinkML version used for a release is pinned in `uv.lock` at its tag.

## Releases and documentation

The versions are tagged in git (for example "v1.2.3" or "v1.2.3.1").
Based on the tags we also create GitHub releases to provide easy access to all versions and to document the changes between versions.
The release workflows refuse a tag that does not start with the schema version.

Each release gets its own documentation, named with all four parts ("v1.2.3.0" for the tag "v1.2.3").
The schema version ("v1.2.3") is an alias of the documentation of its newest release, and the [w3id.org](https://w3id.org/nfdi4cat/pid4cat-model) URIs of a schema version redirect to it.
Pre-releases do not get this alias.
A pre-release of a new schema version has three parts and a suffix ("v1.3.0rc1"), a pre-release of a code-only release has four ("v1.2.3.1rc1").
