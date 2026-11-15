# Tools and Services

## pid4cat-model Python package

[pid4cat-model](https://pypi.org/project/pid4cat-model/) is a Python package for

- reading pid4cat records from the [Handle.net API](./apis.md#handlenet-api) (module `pid4cat_model.handle_api`).
- validating pid4cat metadata against the pid4cat-model schema.
- calculating and validating ISO 7064 checksums which may be used in local identifier schemes.

[ISO/IEC 7064](https://www.iso.org/standard/31531.html) describes eight generic check digit (character) systems for numeric, alphabetic, and alphanumeric strings.
It specifies two types of systems that use the same algorithm with different parameters:
Pure systems and Hybrid systems.

| Algorithm               | Function name | Input string          | Check character(s)                  |
| ------------------------- | ----------- | --------------------- | ----------------------------------- |
| ***Pure***                |             |                       |                                     |
| ISO/IEC 7064, MOD 11-2    | mod11_2     | Numeric (0-9)         | 1 digit or 'x' (0-9x)               |
| ISO/IEC 7064, MOD 37-2    | mod37_2     | Alphanumeric (0-9a-z) | 1 digit, letter, or '\*' (0-9a-z\*) |
| ISO/IEC 7064, MOD 97-10   | mod97_10    | Numeric (0-9)         | 2 digits (0-9)                      |
| ISO/IEC 7064, MOD 661-26  | mod661_26   | Alphabetic (a-z)      | 2 letters (a-z)                     |
| ISO/IEC 7064, MOD 1271-36 | mod1271_36  | Alphanumeric (0-9a-z) | 2 digits or letters (0-9a-z)        |
| ***Hybrid***              |             |                       |                                     |
| ISO/IEC 7064, MOD 11,10   | mod11_10    | Numeric (0-9)         | 1 digit (0-9)                       |
| ISO/IEC 7064, MOD 27,26   | mod27_26    | Alphabetic (a-z)      | 1 letter (a-z)                      |
| ISO/IEC 7064, MOD 37,36   | mod37_36    | Alphanumeric (0-9a-z) | 1 digit or letter (0-9a-z)          |

The pid4cat_model.iso7064 module contains implementations of all algorithms in the table.
They accept letters in either case and return check characters in lower case.

## pid4cat registry

The pid4cat registry is the service with which SNAAs create and manage the PIDs in their namespaces.
It authenticates the SNAAs, validates PIDs and their metadata against the pid4cat-model, and registers the PIDs on the Handle server.
Its main features are:

- Create, read, update and state changes of PIDs in the SNAA's namespaces
- Test namespaces on a separate test Handle server
- Search across the PIDs a user can access
- Periodic checks that landing pages and representation variants are reachable
- A [status dashboard](https://pid.nfdi4cat.org/dashboard)

The source code is not yet published. It will be released in 2027 under Apache 2.0 licence.
For usage, see [pid4cat registry API](./apis.md#pid4cat-registry-api).

## pid4cat in Django

A Django application [django-pid](https://gitlab.com/opensourcelab/scientificdata/pid/django-pid) to integrate pid4cat in django-based ELNs/LIMS solutions is in development (pre-alpha state).

## Schema representations

Through LinkML generators we provide other schema representations that are automatically derived from the pid4cat-model.
These are available in the repository under [/project](https://github.com/nfdi4cat/pid4cat-model/tree/main/project), and are, for example JSON-schema, SHACL shapes, SQL.

## Integration Libraries

Through LinkML generators, pid4cat provides integration code for some programming languages other than Python, see [generated model artifacts](https://github.com/nfdi4cat/pid4cat-model/tree/main/project).
