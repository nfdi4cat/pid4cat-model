# Tools and Services

## pid4cat Python package

pid4cat is a Python package for

- interacting with the pid4cat API to create, read and update  pid4cat identifiers and their metadata.
- validating pid4cat metadata against the pid4cat-model schema.

## pid4cat gateway API

A REST API server that provides the endpoints to create, read and update pid4cat identifiers. It handles authentication of the sub name assigning authorities (SNAAs) and related validation.

The source code of the software is not yet available as open source put there are plans to releasing it in the future.

For usage instructions, see [pid4cat API](#pid4cat-api).

### Features

- Sub-namespace management
- Create, read, update operation on single pid4cat handles
- Bulk operations (future)
- Reporting (future)
- Monitoring (future)

### Access

The pid4cat-admin tool is available only to the Core Organization and authorized administrators.

Integration with NFDI Base4IAM is ongoing.

## pid4cat in Django

A Django application [django-pid](https://gitlab.com/opensourcelab/scientificdata/pid/django-pid) to integrate pid4cat in django-based ELNs/LIMS solutions is in development (pre-alpha state).

## Schema representations

Through LinkML generators we provide other schema representation that are automatically derived from the pid4cat-model.
These are available in the repository under [/project](https://github.com/nfdi4cat/pid4cat-model/tree/main/project),for example JSON-schema, SHACL shapes, SQL.

## Integration Libraries

Through LinkML generators pid4cat provides integration code for some programming languages other than Python, see [generated model artifacts](https://github.com/nfdi4cat/pid4cat-model/tree/main/project).
