# Tools and Services

## pid4cat-model Python package

[pid4cat-model](https://pypi.org/project/pid4cat-model/) is a Python package for

- interacting with the pid4cat API to create, read and update pid4cat identifiers and their metadata.
- validating pid4cat metadata against the pid4cat-model schema.
- calculating and validating ISO 7064 checksums which may be used in local identifier schemes.

[ISO/IEC 7064](https://www.iso.org/standard/31531.html) describes eight generic check digit (character) systems for numeric, alphabetic, and alphanumeric strings.
It specifies two types of systems that use the same algorithm with different parameters:
Pure systems and Hybrid systems.

| Algorithm               | Function name | Input string          | Check character(s)                  |
| ------------------------- | ----------- | --------------------- | ----------------------------------- |
| ***Pure***                |             |                       |                                     |
| ISO/IEC 7064, MOD 11-2    | mod11_2     | Numeric (0-9)         | 1 digit or 'X' (0-9X)               |
| ISO/IEC 7064, MOD 37-2    | mod37_2     | Alphanumeric (0-9A-Z) | 1 digit, letter, or '\*' (0-9A-Z\*) |
| ISO/IEC 7064, MOD 97-10   | mod97_10    | Numeric (0-9)         | 2 digits (0-9)                      |
| ISO/IEC 7064, MOD 661-26  | mod661_26   | Alphabetic (A-Z)      | 2 letters (A-Z)                     |
| ISO/IEC 7064, MOD 1271-36 | mod1271_36  | Alphanumeric (0-9A-Z) | 2 digits or letters (0-9A-Z)        |
| ***Hybrid***              |             |                       |                                     |
| ISO/IEC 7064, MOD 11,10   | mod11_10    | Numeric (0-9)         | 1 digit (0-9)                       |
| ISO/IEC 7064, MOD 27,26   | mod27_26    | Alphabetic (A-Z)      | 1 letter (A-Z)                      |
| ISO/IEC 7064, MOD 37,36   | mod37_36    | Alphanumeric (0-9A-Z) | 1 digit or letter (0-9A-Z)          |

The pid4cat_model.iso7064 module contains implementations of all algorithms in the table.

## pid4cat API

A REST API server that provides the endpoints to create, read and update pid4cat identifiers. It handles authentication of the SNAAs and SNAA-related validation.

The source code of the software is not yet available as open source but there are plans to release it in the future.

For usage instructions, see [pid4cat API](#pid4cat-api).

### Features

- Sub-namespace management
- Create, read, update operation on single pid4cat handles
- Bulk operations (future)
- Reporting (future)
- Monitoring (future)

### Access

The pid4cat-admin tool is available only to the core organization and authorized administrators.

Integration with NFDI Base4IAM is ongoing in order to use NFDI identification and authorisation services for access control to the pid4cat API gateway.

## pid4cat in Django

A Django application [django-pid](https://gitlab.com/opensourcelab/scientificdata/pid/django-pid) to integrate pid4cat in django-based ELNs/LIMS solutions is in development (pre-alpha state).

## Schema representations

Through LinkML generators we provide other schema representations that are automatically derived from the pid4cat-model.
These are available in the repository under [/project](https://github.com/nfdi4cat/pid4cat-model/tree/main/project), and are, for example JSON-schema, SHACL shapes, SQL.

## Integration Libraries

Through LinkML generators, pid4cat provides integration code for some programming languages other than Python, see [generated model artifacts](https://github.com/nfdi4cat/pid4cat-model/tree/main/project).
