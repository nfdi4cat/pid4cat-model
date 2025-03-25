# REST APIs

HLRS API (create, read, update)

## pid4cat API

The pid4cat API provides a RESTful interface for creating, reading, and updating pid4cat identifiers and their associated metadata.

### Base URL

```ascii
https://api.nfdi4cat.org/pid/v2/
```

### Authentication

The API uses API key authentication. Each SNAA is issued a unique API key that must be included in all requests:

```http
Authorization: Bearer <api-key>
```

### Endpoints

The endpoint are described in that auto-generated [API documentation](https://api.nfdi4cat.org/testpid/v2/index.html).

A demo showing how to access all available API endpoints from Python is provided in the [Jupyter](https://jupyter.org/) notebook [examples/api-v2-demo.ipynb](https://github.com/nfdi4cat/pid4cat-model/blob/main/examples/api-v2-demo.ipynb).

## Handle.net API

In addition to the pid4cat API, identifiers and there metadata can also be accessed through the API of the [HDL.NET Proxy Server System](https://www.handle.net/proxy_servlet.html).

### Base URL

```http
https://hdl.handle.net/api/handles/
```

### Request full handle metadata

```http
GET  https://hdl.handle.net/api/handles/<prefix>/4cat/<ns-suffix>/<id-suffix>
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

Tip: To request a tabular HTML view of all data in the pid4cat record you can attach the query parameter `noredirect` to the PID URL, for example

- [https://hdl.handle.net/21.T11978/test/C9K6-C6K9?noredirect](https://hdl.handle.net/21.T11978/test/C9K6-C6K9?noredirect)

### Limitations

The Handle.net API provides read-only access to pid4cat identifiers. To create or update identifiers, the pid4cat API must be used.
