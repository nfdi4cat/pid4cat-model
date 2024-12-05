-- # Class: "PID4CatRecord" Description: "Represents a PID4CatRecord"
--     * Slot: id Description: A unique identifier for a thing.
--     * Slot: landing_page_url Description: The URL of the landing page for the resource.
--     * Slot: status Description: The status of the PID4CatRecord.
--     * Slot: pid_schema_version Description: The version of the PID4Cat schema used for the PID4CatRecord.
--     * Slot: license Description: The license for the metadata contained in the PID4Cat record.
--     * Slot: curation_contact_email Description: The email address of a person or institution currently responsible for the curation of the PID record.
--     * Slot: Container_id Description: Autocreated FK slot
--     * Slot: resource_info_id Description: Information about the resource.
-- # Class: "PID4CatRelation" Description: "A relation between PID4CatRecords or between a PID4CatRecord and other resources with a PID."
--     * Slot: id Description: 
--     * Slot: related_identifier Description: Related identifiers for the resource.
--     * Slot: datetime_log Description: The date and time of a log record.
--     * Slot: has_agent_id Description: The person who registered the resource.
-- # Class: "ResourceInfo" Description: "Data object to hold information about the resource and its representation."
--     * Slot: id Description: 
--     * Slot: label Description: A human-readable name for a resource.
--     * Slot: description Description: A human-readable description for a resource.
--     * Slot: resource_category Description: The category of the resource.
--     * Slot: rdf_url Description: The URI of the rdf representation of the resource.
--     * Slot: rdf_type Description: The format of the rdf representation of the resource (xml, turtle, json-ld, ...).
--     * Slot: schema_url Description: The URI of the schema to which the resource conforms. Same property as in DataCite:schemeURI.
--     * Slot: schema_type Description: The type of the schema to which the resource conforms. Examples: XSD, DDT, SHACL Same property as in DataCite:schemeType.
-- # Class: "LogRecord" Description: "A log record for changes made on a PID4CatRecord starting from registration."
--     * Slot: id Description: 
--     * Slot: datetime_log Description: The date and time of a log record.
--     * Slot: changed_field Description: The field that was changed
--     * Slot: description Description: A human-readable description for a resource.
--     * Slot: has_agent_id Description: The person who registered the resource.
-- # Class: "Agent" Description: "Person who plays a role relative to PID creation or curation."
--     * Slot: id Description: 
--     * Slot: name Description: The name of the agent that created or modified the PID record.
--     * Slot: email Description: Email address of the agent that created or modified the PID record.
--     * Slot: orcid Description: The ORCID of the person
--     * Slot: affiliation_ror Description: The ROR of the agent's affiliation.
--     * Slot: role Description: The role of the agent relative to the resource
-- # Class: "Container" Description: "A container for all PID4Cat instances."
--     * Slot: id Description: 
-- # Class: "PID4CatRecord_related_identifiers" Description: ""
--     * Slot: PID4CatRecord_id Description: Autocreated FK slot
--     * Slot: related_identifiers_id Description: Relations of the resource to other identifiers.
-- # Class: "PID4CatRecord_change_log" Description: ""
--     * Slot: PID4CatRecord_id Description: Autocreated FK slot
--     * Slot: change_log_id Description: Change log of PID4Cat record.
-- # Class: "PID4CatRelation_relation_type" Description: ""
--     * Slot: PID4CatRelation_id Description: Autocreated FK slot
--     * Slot: relation_type Description: Relation type between the resources.

CREATE TABLE "ResourceInfo" (
	id INTEGER NOT NULL, 
	label TEXT, 
	description TEXT, 
	resource_category VARCHAR(12), 
	rdf_url TEXT, 
	rdf_type TEXT, 
	schema_url TEXT, 
	schema_type TEXT, 
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
CREATE TABLE "Container" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "PID4CatRecord" (
	id TEXT NOT NULL, 
	landing_page_url TEXT, 
	status VARCHAR(10), 
	pid_schema_version TEXT, 
	license TEXT, 
	curation_contact_email TEXT, 
	"Container_id" INTEGER, 
	resource_info_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Container_id") REFERENCES "Container" (id), 
	FOREIGN KEY(resource_info_id) REFERENCES "ResourceInfo" (id)
);
CREATE TABLE "PID4CatRelation" (
	id INTEGER NOT NULL, 
	related_identifier TEXT, 
	datetime_log TEXT, 
	has_agent_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_agent_id) REFERENCES "Agent" (id)
);
CREATE TABLE "LogRecord" (
	id INTEGER NOT NULL, 
	datetime_log TEXT, 
	changed_field VARCHAR(13), 
	description TEXT, 
	has_agent_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_agent_id) REFERENCES "Agent" (id)
);
CREATE TABLE "PID4CatRecord_related_identifiers" (
	"PID4CatRecord_id" TEXT, 
	related_identifiers_id INTEGER, 
	PRIMARY KEY ("PID4CatRecord_id", related_identifiers_id), 
	FOREIGN KEY("PID4CatRecord_id") REFERENCES "PID4CatRecord" (id), 
	FOREIGN KEY(related_identifiers_id) REFERENCES "PID4CatRelation" (id)
);
CREATE TABLE "PID4CatRecord_change_log" (
	"PID4CatRecord_id" TEXT, 
	change_log_id INTEGER NOT NULL, 
	PRIMARY KEY ("PID4CatRecord_id", change_log_id), 
	FOREIGN KEY("PID4CatRecord_id") REFERENCES "PID4CatRecord" (id), 
	FOREIGN KEY(change_log_id) REFERENCES "LogRecord" (id)
);
CREATE TABLE "PID4CatRelation_relation_type" (
	"PID4CatRelation_id" INTEGER, 
	relation_type VARCHAR(22), 
	PRIMARY KEY ("PID4CatRelation_id", relation_type), 
	FOREIGN KEY("PID4CatRelation_id") REFERENCES "PID4CatRelation" (id)
);