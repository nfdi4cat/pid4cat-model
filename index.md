# pid4cat-model

LinkML model for Catalyst Resource Identifier (PID4Cat). PID4Cat is handle system based persistent identifier (PID) for digital or physical resources used in the catalysis research process. The handle record is used to store metadata about the PID besides the obligatory landing page URL.
The model describes metadata for the PID itself and how to access the  identified resource. It does not describe the resource itself with the exception of the resource category, which is a high-level description of  what is identified by the PID4Cat handle, e.g. a sample or a device.

URI: https://w3id.org/nfdi4cat/pid4cat-model

Name: pid4cat-model



## Classes

| Class | Description |
| --- | --- |
| [Agent](Agent.md) | Person who plays a role relative to PID creation or curation. |
| [Container](Container.md) | A container for all PID4Cat instances. |
| [LogRecord](LogRecord.md) | A log record for changes made on a PID4CatRecord starting from registration. |
| [PID4CatRecord](PID4CatRecord.md) | Represents a PID4CatRecord |
| [PID4CatRelation](PID4CatRelation.md) | A relation between PID4CatRecords or between a PID4CatRecord and other resources with a PID. |
| [ResourceInfo](ResourceInfo.md) | Data object to hold information about the resource and its representation. |



## Slots

| Slot | Description |
| --- | --- |
| [affiliation_ror](affiliation_ror.md) | The ROR of the affiliation |
| [change_log](change_log.md) | Change log of PID4Cat record |
| [changed_field](changed_field.md) | The field that was changed |
| [contact_information](contact_information.md) | Identification of the agent that registered the PID, with contact information |
| [curation_contact](curation_contact.md) | The email address of a person or institution responsible for curation of the ... |
| [datetime_log](datetime_log.md) | The date and time of a log record |
| [dc_rights](dc_rights.md) | The license for the metadata contained in the PID4Cat record |
| [description](description.md) | A human-readable description for a thing |
| [has_agent](has_agent.md) | The person who registered the resource |
| [has_pids](has_pids.md) | The PID4CatRecords contained in the container |
| [id](id.md) | A unique identifier for a thing |
| [label](label.md) | A human-readable name for a thing |
| [landing_page_url](landing_page_url.md) | The URL of the landing page for the resource |
| [name](name.md) | The name of the agent |
| [person_orcid](person_orcid.md) | The ORCID of the person |
| [rdf_type](rdf_type.md) | The format of the rdf representation of the resource (xml, turlte, json-ld,  |
| [rdf_url](rdf_url.md) | The URI of the rdf represenation of the resource |
| [related_identifier](related_identifier.md) | Related identifiers for the resource |
| [related_identifiers](related_identifiers.md) | Alternate identifiers for the resource |
| [relation_type](relation_type.md) | Relation type between the resources |
| [resource_category](resource_category.md) | The category of the resource |
| [resource_info](resource_info.md) | Information about the resource |
| [role](role.md) | The role of the agent relative to the resource |
| [schema_type](schema_type.md) | The type of the scheme used to describe the resource |
| [schema_url](schema_url.md) | The URI of the schema used to describe the resource |
| [status](status.md) | The status of the PID4CatRecord |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [ChangeLogFields](ChangeLogFields.md) | The field of the PID4Catrecord that was changed |
| [PID4CatAgentRoles](PID4CatAgentRoles.md) | The role of an agent relative to the resource |
| [PID4CatStatus](PID4CatStatus.md) | The status of the PID4CatRecord |
| [RelationTypes](RelationTypes.md) | The type of the relation between the resources |
| [ResourceCategories](ResourceCategories.md) | The category of the resource |


## Types

| Type | Description |
| --- | --- |
| [Boolean](Boolean.md) | A binary (true or false) value |
| [Curie](Curie.md) | a compact URI |
| [Date](Date.md) | a date (year, month and day) in an idealized calendar |
| [DateOrDatetime](DateOrDatetime.md) | Either a date or a datetime |
| [Datetime](Datetime.md) | The combination of a date and time |
| [Decimal](Decimal.md) | A real number with arbitrary precision that conforms to the xsd:decimal speci... |
| [Double](Double.md) | A real number that conforms to the xsd:double specification |
| [Float](Float.md) | A real number that conforms to the xsd:float specification |
| [Integer](Integer.md) | An integer |
| [Jsonpath](Jsonpath.md) | A string encoding a JSON Path |
| [Jsonpointer](Jsonpointer.md) | A string encoding a JSON Pointer |
| [Ncname](Ncname.md) | Prefix part of CURIE |
| [Nodeidentifier](Nodeidentifier.md) | A URI, CURIE or BNODE that represents a node in a model |
| [Objectidentifier](Objectidentifier.md) | A URI or CURIE that represents an object in the model |
| [Sparqlpath](Sparqlpath.md) | A string encoding a SPARQL Property Path |
| [String](String.md) | A character string |
| [Time](Time.md) | A time object represents a (local) time of day, independent of any particular... |
| [Uri](Uri.md) | a complete URI |
| [Uriorcurie](Uriorcurie.md) | a URI or a CURIE |


## Subsets

| Subset | Description |
| --- | --- |
