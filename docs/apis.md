# REST APIs

Two APIs give access to pid4cat handles:

- The **pid4cat registry API** creates and changes PIDs. Only namespace owners (SNAAs) can use it.
- The **Handle.net API** returns the current handle record of any PID. It is public and read-only.

## pid4cat registry API

!!! warning "The registry is in pre-production testing."

    URLs and behaviour may change until the service is launched.

The registry is the reference for its own API:
[Swagger UI](https://pid.nfdi4cat.org/docs) to try requests,
[ReDoc](https://pid.nfdi4cat.org/redoc) with full-text search,
and the OpenAPI specification as [YAML](https://pid.nfdi4cat.org/openapi.yaml) or [JSON](https://pid.nfdi4cat.org/openapi.json).
This section gives an overview.

The base URL is `https://pid.nfdi4cat.org/api/v1`.
A PID `<prefix>/4cat/<ns-suffix>/<id-suffix>` (see [Structure of pid4cat handles](./getting-started.md#structure-of-pid4cat-handles)) has the path

```http
https://pid.nfdi4cat.org/api/v1/pids/<prefix>/4cat/<ns-suffix>/<id-suffix>
```

### Authentication

Each namespace owner receives an API key from the pid4cat administrators.
The API key is exchanged for short-lived tokens:

1. `POST /api/v1/auth/login` with `{"api_key": "…"}` returns an `access_token`, a `refresh_token` and the lifetime of the access token in seconds (`expires_in`).
2. Every request sends the access token in the header `Authorization: Bearer <access_token>`.
3. `POST /api/v1/auth/refresh` with `{"refresh_token": "…"}` returns a new token pair.
   A refresh token works only once.

### Creating a PID

The namespace owner chooses the `<id-suffix>` and creates the PID with a `POST` to its path:

```http
POST https://pid.nfdi4cat.org/api/v1/pids/<prefix>/4cat/<ns-suffix>/<id-suffix>
Authorization: Bearer <access_token>
Content-Type: application/json

{
  "landing_page_url": "https://example.org/samples/s-001",
  "status": "REGISTERED",
  "curation_contact": "pid-curator@example.org",
  "resource_info": {
    "resource_category": "SAMPLE",
    "representation_variants": []
  }
}
```

The fields follow the [pid4cat metadata model](./metadata.md).
A PID that already exists gets the status 409.

### PID states

| State | Meaning | On the Handle server |
| ----- | ------- | -------------------- |
| SUBMITTED | Reserved; not yet linked to a resource | Not present |
| REGISTERED | Linked to a resource | Resolves to the landing page |
| DEPRECATED | Deprecated, for example because the resource can no longer be found | Kept, with status DEPRECATED |
| OBSOLETED | Obsolete, for example because another PID replaces it, or deleted | Kept if the PID was ever REGISTERED |

A new PID is SUBMITTED unless the request sets `"status": "REGISTERED"` and gives a landing page.
`POST …/activate` registers a SUBMITTED PID.
DEPRECATED and OBSOLETED are final.

### Changing a PID

Each part of the metadata has its own path below the PID, for example `…/landing-page`, `…/contact`, `…/resource-info` and `…/relations`.
`GET` reads the part, `PUT` replaces it, and `POST …/relations` adds one relation.
The `<id-suffix>` of a PID cannot be changed.

### Test namespaces

Each namespace `<ns-suffix>` has a test namespace `test-<ns-suffix>`.
Its PIDs are registered on a separate test Handle server, so an integration can be tried out without creating real PIDs.

## Handle.net API

The [HDL.NET Proxy Server System](https://www.handle.net/proxy_servlet.html) returns the handle record of every pid4cat PID on the Handle server.
It needs no authentication.

```http
GET https://hdl.handle.net/api/handles/<prefix>/4cat/<ns-suffix>/<id-suffix>
```

Response:

```json
{
  "responseCode": 1,
  "handle": "<prefix>/4cat/<ns-suffix>/<id-suffix>",
  "values": [
    {
      "index": 1,
      "type": "URL",
      "data": {
        "format": "string",
        "value": "https://example.org/resource"
      },
      "ttl": 86400,
      "timestamp": "2023-01-01T00:00:00Z"
    },
    // Additional handle values containing metadata
  ]
}
```

The query parameter `noredirect` shows the handle record as an HTML table, for example

- `https://hdl.handle.net/21.11165/4cat/d4y/sample-001?noredirect`

The Jupyter notebook [examples/hdl-net-api-demo.ipynb](https://github.com/nfdi4cat/pid4cat-model/blob/main/examples/hdl-net-api-demo.ipynb) reads pid4cat records with the `pid4cat_model.handle_api` module of the [pid4cat-model package](./tools.md#pid4cat-model-python-package).
