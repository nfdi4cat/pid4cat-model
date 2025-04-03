## HandleAPIRecord-002
### Input
```yaml
handle: 21.T11978/test/km28-dk21
responseCode: 1
values:
- data:
    format: string
    value: http://mynewtest.com
  index: 1
  timestamp: '2025-03-10T14:39:04Z'
  ttl: 86400
  type: URL
- data:
    format: string
    value: mynewemail@test.com
  index: 10
  timestamp: '2025-03-10T14:40:24Z'
  ttl: 86400
  type: EMAIL
- data:
    format: string
    value: REGISTERED
  index: 11
  timestamp: '2025-03-10T15:09:16Z'
  ttl: 86400
  type: STATUS
- data:
    format: string
    value: v1.0.1
  index: 12
  timestamp: '2025-03-10T15:26:17Z'
  ttl: 86400
  type: SCHEMA_VER
- data:
    format: string
    value: CC0-1.0
  index: 13
  timestamp: '2025-03-10T14:41:29Z'
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
  timestamp: '2025-03-10T14:41:30Z'
  ttl: 86400
  type: RESOURCE
- data:
    format: string
    value:
    - datetime_log: '2024-02-19T00:00:00+00:00'
      related_identifier:
        identifier: ex:collection1
        resolving_url: https://example.org/collection1
        type: ExampleIdentifier
      relation_type: IS_PART_OF
    - datetime_log: '2024-02-19T00:00:00+00:00'
      related_identifier:
        identifier: ex:referenced1
        resolving_url: https://example.org/referenced1
        type: ExampleIdentifier
      relation_type: IS_REFERENCED_BY
  index: 15
  timestamp: '2025-03-10T15:01:37Z'
  ttl: 86400
  type: RELATED
- data:
    format: string
    value:
    - changed_field: STATUS
      datetime_log: '2024-02-19T00:00:00+00:00'
      description: Registration completed.
      has_agent:
        affiliation_ror: https://ror.org/029hg0311
        email_address: data.fuzzi@example.org
        name: Data Fuzzi
        orcid: 0000-0000-0000-0000
        role: TRUSTEE
    - changed_field: RESOURCE_INFO
      datetime_log: '2024-05-15T15:51:15+00:00'
      description: 'as requested in issue #234'
      has_agent:
        affiliation_ror: https://ror.org/029hg0311
        email_address: data.fuzzi@example.org
        name: Data Fuzzi
        orcid: 0000-0000-0000-0000
        role: TRUSTEE
  index: 16
  timestamp: '2025-03-10T15:02:58Z'
  ttl: 86400
  type: CHANGES

```
## HandleAPIRecord-003
### Input
```yaml
handle: 21.T11978/TEST/KBKA-BEM9
responseCode: 1
values:
- data:
    format: string
    value: http://Mytest2.com
  index: 1
  timestamp: '2025-03-11T09:43:14Z'
  ttl: 86400
  type: URL
- data:
    format: string
    value: abc@xyz.com
  index: 10
  timestamp: '2025-03-11T10:32:45Z'
  ttl: 86400
  type: EMAIL
- data:
    format: string
    value: REGISTERED
  index: 11
  timestamp: '2025-03-11T10:33:39Z'
  ttl: 86400
  type: STATUS
- data:
    format: string
    value: v1.0.1
  index: 12
  timestamp: '2025-03-11T10:34:03Z'
  ttl: 86400
  type: SCHEMA_VER
- data:
    format: string
    value: CC0-1.0
  index: 13
  timestamp: '2025-03-11T09:45:25Z'
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
  timestamp: '2025-03-11T09:45:26Z'
  ttl: 86400
  type: RESOURCE
- data:
    format: string
    value:
    - datetime_log: '2024-02-19T00:00:00+00:00'
      related_identifier:
        identifier: ex:collection1
        resolving_url: https://example.org/collection1
        type: ExampleIdentifier
      relation_type: IS_PART_OF
    - datetime_log: '2024-02-19T00:00:00+00:00'
      related_identifier:
        identifier: ex:referenced1
        resolving_url: https://example.org/referenced1
        type: ExampleIdentifier
      relation_type: IS_REFERENCED_BY
  index: 15
  timestamp: '2025-03-11T10:00:50Z'
  ttl: 86400
  type: RELATED
- data:
    format: string
    value:
    - changed_field: STATUS
      datetime_log: '2024-02-19T00:00:00+00:00'
      description: Registration completed.
      has_agent:
        affiliation_ror: https://ror.org/029hg0311
        email_address: data.fuzzi@example.org
        name: Data Fuzzi
        orcid: 0000-0000-0000-0000
        role: TRUSTEE
    - changed_field: RESOURCE_INFO
      datetime_log: '2024-05-15T15:51:15+00:00'
      description: 'as requested in issue #234'
      has_agent:
        affiliation_ror: https://ror.org/029hg0311
        email_address: data.fuzzi@example.org
        name: Data Fuzzi
        orcid: 0000-0000-0000-0000
        role: TRUSTEE
  index: 16
  timestamp: '2025-03-11T10:01:38Z'
  ttl: 86400
  type: CHANGES

```
## HandleAPIRecord-004
### Input
```yaml
handle: 21.T11978/TEST/KBKA-BEM9
responseCode: 1
values:
- data:
    format: string
    value: http://Mytest2.com
  index: 1
  timestamp: '2025-03-11T09:43:14Z'
  ttl: 86400
  type: URL
- data:
    format: string
    value: abc@xyz.com
  index: 10
  timestamp: '2025-03-11T10:32:45Z'
  ttl: 86400
  type: EMAIL
- data:
    format: string
    value: REGISTERED
  index: 11
  timestamp: '2025-03-11T10:33:39Z'
  ttl: 86400
  type: STATUS
- data:
    format: string
    value: v1.0.1
  index: 12
  timestamp: '2025-03-11T10:34:03Z'
  ttl: 86400
  type: SCHEMA_VER
- data:
    format: string
    value: CC0-1.0
  index: 13
  timestamp: '2025-03-11T09:45:25Z'
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
  timestamp: '2025-03-11T09:45:26Z'
  ttl: 86400
  type: RESOURCE
- data:
    format: string
    value: []
  index: 15
  timestamp: '2025-03-11T10:00:50Z'
  ttl: 86400
  type: RELATED
- data:
    format: string
    value:
    - changed_field: STATUS
      datetime_log: '2024-02-19T00:00:00+00:00'
      description: Registration completed.
      has_agent:
        affiliation_ror: https://ror.org/029hg0311
        email_address: data.fuzzi@example.org
        name: Data Fuzzi
        orcid: 0000-0000-0000-0000
        role: TRUSTEE
  index: 16
  timestamp: '2025-03-11T10:01:38Z'
  ttl: 86400
  type: CHANGES

```
## HandleAPIRecord-004
### Input
```yaml
handle: 21.T11978/test/b93k-bkc9
responseCode: 1
values:
- data:
    format: string
    value: http://mytest2.com
  index: 1
  timestamp: '2025-03-11T10:36:09Z'
  ttl: 86400
  type: URL
- data:
    format: string
    value: xzy@abc.com
  index: 10
  timestamp: '2025-03-11T10:38:14Z'
  ttl: 86400
  type: EMAIL
- data:
    format: string
    value: REGISTERED
  index: 11
  timestamp: '2025-03-11T10:37:49Z'
  ttl: 86400
  type: STATUS
- data:
    format: string
    value: v1.0.1
  index: 12
  timestamp: '2025-03-11T10:37:28Z'
  ttl: 86400
  type: SCHEMA_VER
- data:
    format: string
    value: CC0-1.0
  index: 13
  timestamp: '2025-03-11T10:39:21Z'
  ttl: 86400
  type: METADATA_LICENSE
- data:
    format: string
    value:
      resource_category: SAMPLE
  index: 14
  timestamp: '2025-03-11T10:50:40Z'
  ttl: 86400
  type: RESOURCE
- data:
    format: string
    value: []
  index: 15
  timestamp: '2025-03-11T10:39:47Z'
  ttl: 86400
  type: RELATED
- data:
    format: string
    value: []
  index: 16
  timestamp: '2025-03-11T10:40:08Z'
  ttl: 86400
  type: CHANGES

```
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
