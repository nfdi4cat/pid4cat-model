# Getting Started

## Registration

To use pid4cat services, organizations must apply to become a Sub-Name Assigning Authority (SNAA). The application process involves:

1. Submitting an application form to the pid4cat core organization (TODO add contact info)
2. Agreeing to the pid4cat policies (detailed in section [Policies](./policies.md))
3. Demonstrating the capability to maintain the identified resources
4. Designating a technical and administrative contact

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

Resolution will typically redirect to the landing page for the identified resource, which should be maintained by the responsible SNAA.
