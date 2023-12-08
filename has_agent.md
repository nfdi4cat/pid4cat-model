# Slot: has_agent


_The person who registered the resource_



URI: [schema:Agent](http://schema.org/Agent)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[PID4CatRelation](PID4CatRelation.md) | A relation between PID4CatRecords or between a PID4CatRecord and other resour... |  no  |
[LogRecord](LogRecord.md) | A log record for changes made on a PID4CatRecord starting from registration |  no  |







## Properties

* Range: [Agent](Agent.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nfdi4cat/pid4cat-model




## LinkML Source

<details>
```yaml
name: has_agent
description: The person who registered the resource
from_schema: https://w3id.org/nfdi4cat/pid4cat-model
rank: 1000
slot_uri: schema:Agent
alias: has_agent
domain_of:
- PID4CatRelation
- LogRecord
range: Agent

```
</details>