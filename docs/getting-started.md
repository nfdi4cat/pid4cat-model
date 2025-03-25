# Getting Started

## Registration

To use pid4cat services, organizations must apply to become a Sub-Name Assigning Authority (SNAA). The application process involves:

1. Submitting an application form to the pid4cat Core Organization
2. Agreeing to the pid4cat policies (detailed in the Policies section)
3. Demonstrating the capability to maintain the identified resources
4. Designating a technical and administrative contact

Upon approval, the organization will receive:

- A unique namespace suffix (`<ns-suffix>`)
- API credentials for accessing the pid4cat API
- Documentation and support for implementation

## Creating identifiers

Identifiers can be created through the pid4cat API. Partner organizations (SNAAs) have two options:

1. **Opaque identifiers**: System-generated identifiers with no semantic meaning
2. **Semantic identifiers**: Custom identifiers created according to local naming conventions

To create an identifier:

```http
POST /api/v2/handles/<prefix>/<ns-suffix>/
```

With a payload containing:

- The local identifier (optional for opaque identifiers)
- The URL of the resource
- Required metadata according to the pid4cat-model

For detailed API documentation, see the [REST APIs](#rest-apis) section.

## Updating identifiers

Identifiers and their associated metadata can be updated through the pid4cat API:

```http
PUT /api/v2/handles/<prefix>/<ns-suffix>/<local-id>
```

Updates may include:

- Changes to the target URL
- Additions or modifications to metadata
- Changes in access controls

Note that the identifier itself cannot be changed once created. Only its associated metadata and target URL can be modified.

## Resolving identifiers

pid4cat identifiers can be resolved using:

1. **Direct resolution**: `https://hdl.handle.net/<prefix>/<ns-suffix>/<local-id>`
2. **pid4cat resolver**: `https://pid.nfdi4cat.org/<prefix>/<ns-suffix>/<local-id>`

Resolution will typically redirect to the landing page for the identified resource, which should be maintained by the responsible SNAA.
