# Slot: datetime_log


_The date and time of a log record_



URI: [schema:DateTime](http://schema.org/DateTime)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[PID4CatRelation](PID4CatRelation.md) | A relation between PID4CatRecords or between a PID4CatRecord and other resour... |  no  |
[LogRecord](LogRecord.md) | A log record for changes made on a PID4CatRecord starting from registration |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nfdi4cat/pid4cat-model




## LinkML Source

<details>
```yaml
name: datetime_log
description: The date and time of a log record
from_schema: https://w3id.org/nfdi4cat/pid4cat-model
rank: 1000
slot_uri: schema:DateTime
alias: datetime_log
domain_of:
- PID4CatRelation
- LogRecord
range: string

```
</details>