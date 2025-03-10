## HandleAPIRecord-001
### Input
```yaml
handle: 21.T12995/lik-2
responseCode: 1
values:
- data:
    format: string
    value: https://pid4cat.example.org/lik-2
  index: 1
  timestamp: '2024-05-15T15:51:15Z'
  ttl: 86400
  type: URL
- data:
    format: string
    value: datafuzzi@example.org
  index: 10
  timestamp: '2024-05-15T15:51:15Z'
  ttl: 86400
  type: EMAIL
- data:
    format: string
    value: REGISTERED
  index: 11
  timestamp: '2024-05-15T15:51:15Z'
  ttl: 86400
  type: STATUS
- data:
    format: string
    value: v0.1.0
  index: 12
  timestamp: '2024-05-15T15:51:15Z'
  ttl: 86400
  type: SCHEMA_VER
- data:
    format: string
    value: CC0-1.0
  index: 13
  timestamp: '2024-05-15T15:51:15Z'
  ttl: 86400
  type: METADATA_LICENSE
- data:
    format: string
    value:
      description: Resource description
      label: Resource label
      representation_variants:
      - encoding_format: UTF-8
        media_type: text/turtle
        size: 12345
        variant_url: https://example.org/resource
      resource_category: SAMPLE
  index: 14
  timestamp: '2024-05-15T15:51:15Z'
  ttl: 86400
  type: RESOURCE
- data:
    format: string
    value:
    - datetime_log: '2024-02-19T00:00:00Z'
      related_identifier:
        identifier: 10.5281/zenodo.8313340
        resolving_url: https://doi.org/10.5281/zenodo.8313340
        type: DoiIdentifier
      relation_type: IS_PART_OF
    - datetime_log: '2024-02-19T00:00:00Z'
      related_identifier:
        identifier: ex:ref123
        resolving_url: https://example.org/ref123
        type: ExampleIdentifier
      relation_type: IS_REFERENCED_BY
  index: 15
  timestamp: '2024-05-15T15:51:15Z'
  ttl: 86400
  type: RELATED
- data:
    format: string
    value:
    - changed_field: STATUS
      datetime_log: '2024-02-19T00:00:00Z'
      description: 'as requested in issue #123'
      has_agent:
        affiliation_ror: https://ror.org/029hg0311
        email_address: datafuzzi@example.org
        name: Data Fuzzi
        orcid: 0000-0000-0000-0000
        role: TRUSTEE
  index: 16
  timestamp: '2024-05-15T15:51:15Z'
  ttl: 86400
  type: CHANGES

```
## HandleRecordContainer-001
### Input
```yaml
contains_pids:
- handle: 21.T12995/lik-1
  responseCode: 1
  values:
  - data:
      format: string
      value: https://pid4cat.example.org/lik-1
    index: 1
    timestamp: '2024-05-15T15:51:15Z'
    ttl: 86400
    type: URL
  - data:
      format: string
      value: datafuzzi@example.org
    index: 10
    timestamp: '2024-05-15T15:51:15Z'
    ttl: 86400
    type: EMAIL
  - data:
      format: string
      value: REGISTERED
    index: 11
    timestamp: '2024-05-15T15:51:15Z'
    ttl: 86400
    type: STATUS
  - data:
      format: string
      value: v0.1.0
    index: 12
    timestamp: '2024-05-15T15:51:15Z'
    ttl: 86400
    type: SCHEMA_VER
  - data:
      format: string
      value: CC0-1.0
    index: 13
    timestamp: '2024-05-15T15:51:15Z'
    ttl: 86400
    type: METADATA_LICENSE
  - data:
      format: string
      value:
        description: Resource description
        label: Resource label
        representation_variants:
        - encoding_format: UTF-8
          media_type: text/turtle
          size: 12345
          variant_url: https://example.org/resource
        resource_category: SAMPLE
    index: 14
    timestamp: '2024-05-15T15:51:15Z'
    ttl: 86400
    type: RESOURCE
  - data:
      format: string
      value:
      - datetime_log: '2024-02-19T00:00:00Z'
        related_identifier:
          identifier: 10.5281/zenodo.8313340
          resolving_url: https://doi.org/10.5281/zenodo.8313340
          type: DoiIdentifier
        relation_type: IS_PART_OF
      - datetime_log: '2024-02-19T00:00:00Z'
        related_identifier:
          identifier: ex:ref123
          resolving_url: https://example.org/ref123
          type: ExampleIdentifier
        relation_type: IS_REFERENCED_BY
    index: 15
    timestamp: '2024-05-15T15:51:15Z'
    ttl: 86400
    type: RELATED
  - data:
      format: string
      value:
      - changed_field: STATUS
        datetime_log: '2024-02-19T00:00:00Z'
        description: 'as requested in issue #123'
        has_agent:
          affiliation_ror: https://ror.org/029hg0311
          email_address: datafuzzi@example.org
          name: Data Fuzzi
          orcid: 0000-0000-0000-0000
          role: TRUSTEE
    index: 16
    timestamp: '2024-05-15T15:51:15Z'
    ttl: 86400
    type: CHANGES

```
