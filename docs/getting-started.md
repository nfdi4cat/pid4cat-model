# Getting Started

## Registration

To use pid4cat services, an organization applies to [HLRS](mailto:handles@hlrs.de) to become a Sub-Name Assigning Authority (SNAA).
The requirements are listed in [Registration as SNAA](./policies.md#registration-as-snaa).

Upon approval, the organization will receive:

- A unique namespace suffix (`<ns-suffix>`)
- An API key for the [pid4cat registry API](./apis.md#pid4cat-registry-api)
- Documentation and support for the integration into SNAA-operated services

## Structure of pid4cat handles

A pid4cat handle has the form `<prefix>/4cat/<ns-suffix>/<id-suffix>`, for example
`21.11165/4cat/d4y/sample-001`:

- `<prefix>`: the Handle prefix.
- `4cat`: a fixed segment that marks pid4cat handles.
- `<ns-suffix>`: the namespace of one SNAA, assigned at registration.
  It has three lower-case characters from the [Crockford Base32](https://www.crockford.com/base32.html)
  alphabet (digits and letters without i, l, o and u): a letter, a digit, then a letter or digit, for example `d4y`.
  Some combinations are reserved and never assigned.
  Test namespaces have the form `test-<ns-suffix>`.
- `<id-suffix>`: the identifier within the namespace.
  It has 1 to 36 characters from `a-z`, `0-9`, `.` and `-`.
  It contains no `/`, so every pid4cat handle has exactly four segments.

Handles resolve case-insensitively.
Lower case in `<ns-suffix>` and `<id-suffix>` gives each handle a single spelling.

## Creating and updating identifiers

SNAAs create and update PIDs with the [pid4cat registry API](./apis.md#pid4cat-registry-api).
The SNAA chooses the `<id-suffix>` of each PID following its own naming conventions.
A PID is created with a `POST` request to its path, for example:

```http
POST https://pid.nfdi4cat.org/api/v1/pids/21.11165/4cat/d4y/sample-001
```

The request body contains the landing page URL and the metadata required by the [pid4cat-model](./metadata.md).
Later requests can change the landing page URL and the metadata, but not the `<id-suffix>`.
The test namespace `test-<ns-suffix>` allows trying this out without creating real PIDs.

## Resolving identifiers

pid4cat identifiers can be resolved using:

1. **Direct resolution**: `https://hdl.handle.net/<prefix>/4cat/<ns-suffix>/<id-suffix>`
2. **pid4cat resolver**: `https://pid.nfdi4cat.org/<prefix>/4cat/<ns-suffix>/<id-suffix>`
3. **pid4cat resolver**: `https://handle.nfdi4cat.org/<prefix>/4cat/<ns-suffix>/<id-suffix>`
4. **DOI proxy**: `https://doi.org/<prefix>/4cat/<ns-suffix>/<id-suffix>`; the DOI resolver also resolves handles other than DOIs.

Resolution redirects to the landing page of the identified resource, which the responsible SNAA maintains.
