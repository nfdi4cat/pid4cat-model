-- # Class: "HandleAPIRecord" Description: "A handle record for a PID4CatRecord."
--     * Slot: id Description: 
--     * Slot: responseCode Description: The response code of the handle API.
--     * Slot: handle Description: The handle of the PID4CatRecord.
--     * Slot: HandleRecordContainer_id Description: Autocreated FK slot
-- # Class: "HandleRecord" Description: "A handle record for a PID4CatRecord."
--     * Slot: id Description: 
--     * Slot: index Description: The index of the handle record.
--     * Slot: type Description: The type of the handle record.
--     * Slot: ttl Description: A time to live in seconds for the handle record. Typically: 86400 => 1 dayTODO: Research details of ttl meaning for handle API.
--     * Slot: timestamp Description: The iso datetime for the last update of the handle data.
--     * Slot: data_id Description: The meta data stored in PID4CatRecord.
-- # Class: "HandleData" Description: "The data element in the handle API."
--     * Slot: id Description: 
--     * Slot: format Description: The format of the handle data.
--     * Slot: value Description: The value of the handle data.
-- # Class: "HandleRecordContainer" Description: "A container for all HandleRecords."
--     * Slot: id Description: 
-- # Class: "PID4CatRelation" Description: "A relation between PID4CatRecords or between a PID4CatRecord and other resources with a PID."
--     * Slot: id Description: 
--     * Slot: relation_type Description: Relation type between the resources.
--     * Slot: related_identifier Description: Related identifiers for the resource.
--     * Slot: datetime_log Description: The date and time of a log record.
-- # Class: "ResourceInfo" Description: "Data object to hold information about the resource and its representation."
--     * Slot: id Description: 
--     * Slot: label Description: A human-readable name for a resource.
--     * Slot: description Description: A human-readable description for a resource.
--     * Slot: resource_category Description: The category of the resource.
-- # Class: "LogRecord" Description: "A log record for changes made on a PID4CatRecord starting from registration."
--     * Slot: id Description: 
--     * Slot: datetime_log Description: The date and time of a log record.
--     * Slot: changed_field Description: The field that was changed
--     * Slot: description Description: A human-readable description for a resource.
--     * Slot: has_agent_id Description: The person who registered or modified the PID record.
-- # Class: "Agent" Description: "Person who plays a role relative to PID creation or curation."
--     * Slot: id Description: 
--     * Slot: name Description: The name of the agent that created or modified the PID record.
--     * Slot: email Description: Email address of the agent that created or modified the PID record.
--     * Slot: orcid Description: The ORCID of the person
--     * Slot: affiliation_ror Description: The ROR of the agent's affiliation.
--     * Slot: role Description: The role of the agent relative to the resource
-- # Class: "RepresentationVariant" Description: "A representation of the resource in other media types than text/html which is the default for landing_page_url."
--     * Slot: id Description: 
--     * Slot: url Description: The URL of the representation.
--     * Slot: media_type Description: The media type of the representation as defined by [IANA](https://www.iana.org/assignments/media-types/media-types.xhtml)
--     * Slot: encoding_format Description: The encoding of the representation. https://encoding.spec.whatwg.org/#names-and-labels
--     * Slot: size Description: The size of the representation in bytes.
-- # Class: "HandleAPIRecord_values" Description: ""
--     * Slot: HandleAPIRecord_id Description: Autocreated FK slot
--     * Slot: values_id Description: The values of the PID4CatRecord.
-- # Class: "ResourceInfo_representation_variants" Description: ""
--     * Slot: ResourceInfo_id Description: Autocreated FK slot
--     * Slot: representation_variants_id Description: The representations of the resource in other media types than text/html.

CREATE TABLE "HandleData" (
	id INTEGER NOT NULL, 
	format TEXT, 
	value TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "HandleRecordContainer" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "PID4CatRelation" (
	id INTEGER NOT NULL, 
	relation_type VARCHAR(22), 
	related_identifier TEXT, 
	datetime_log DATETIME, 
	PRIMARY KEY (id)
);
CREATE TABLE "ResourceInfo" (
	id INTEGER NOT NULL, 
	label TEXT, 
	description TEXT, 
	resource_category VARCHAR(12), 
	PRIMARY KEY (id)
);
CREATE TABLE "Agent" (
	id INTEGER NOT NULL, 
	name TEXT, 
	email TEXT, 
	orcid TEXT, 
	affiliation_ror TEXT, 
	role VARCHAR(7), 
	PRIMARY KEY (id)
);
CREATE TABLE "RepresentationVariant" (
	id INTEGER NOT NULL, 
	url TEXT, 
	media_type VARCHAR(84), 
	encoding_format TEXT, 
	size INTEGER, 
	PRIMARY KEY (id)
);
CREATE TABLE "HandleAPIRecord" (
	id INTEGER NOT NULL, 
	"responseCode" INTEGER, 
	handle TEXT, 
	"HandleRecordContainer_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("HandleRecordContainer_id") REFERENCES "HandleRecordContainer" (id)
);
CREATE TABLE "HandleRecord" (
	id INTEGER NOT NULL, 
	"index" INTEGER, 
	type VARCHAR(13), 
	ttl INTEGER, 
	timestamp DATETIME, 
	data_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(data_id) REFERENCES "HandleData" (id)
);
CREATE TABLE "LogRecord" (
	id INTEGER NOT NULL, 
	datetime_log DATETIME, 
	changed_field VARCHAR(13), 
	description TEXT, 
	has_agent_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_agent_id) REFERENCES "Agent" (id)
);
CREATE TABLE "ResourceInfo_representation_variants" (
	"ResourceInfo_id" INTEGER, 
	representation_variants_id INTEGER, 
	PRIMARY KEY ("ResourceInfo_id", representation_variants_id), 
	FOREIGN KEY("ResourceInfo_id") REFERENCES "ResourceInfo" (id), 
	FOREIGN KEY(representation_variants_id) REFERENCES "RepresentationVariant" (id)
);
CREATE TABLE "HandleAPIRecord_values" (
	"HandleAPIRecord_id" INTEGER, 
	values_id INTEGER, 
	PRIMARY KEY ("HandleAPIRecord_id", values_id), 
	FOREIGN KEY("HandleAPIRecord_id") REFERENCES "HandleAPIRecord" (id), 
	FOREIGN KEY(values_id) REFERENCES "HandleRecord" (id)
);