

CREATE TABLE "Agent" (
	name TEXT, 
	contact_information TEXT, 
	person_orcid TEXT, 
	affiliation_ror TEXT, 
	role VARCHAR(7), 
	PRIMARY KEY (name, contact_information, person_orcid, affiliation_ror, role)
);

CREATE TABLE "Container" (
	contains_pids TEXT, 
	PRIMARY KEY (contains_pids)
);

CREATE TABLE "PID4CatRecord" (
	id TEXT NOT NULL, 
	landing_page_url TEXT, 
	status VARCHAR(10), 
	record_version TEXT, 
	pid_schema_version TEXT, 
	dc_rights TEXT, 
	curation_contact TEXT, 
	resource_info TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "PID4CatRelation" (
	relation_type VARCHAR(22), 
	related_identifier TEXT, 
	datetime_log TEXT, 
	has_agent TEXT, 
	PRIMARY KEY (relation_type, related_identifier, datetime_log, has_agent)
);

CREATE TABLE "ResourceInfo" (
	label TEXT, 
	description TEXT, 
	resource_category VARCHAR(10), 
	rdf_url TEXT, 
	rdf_type TEXT, 
	schema_url TEXT, 
	schema_type TEXT, 
	PRIMARY KEY (label, description, resource_category, rdf_url, rdf_type, schema_url, schema_type)
);

CREATE TABLE "LogRecord" (
	datetime_log TEXT, 
	has_agent TEXT, 
	changed_field VARCHAR(13), 
	description TEXT, 
	"PID4CatRecord_id" TEXT, 
	PRIMARY KEY (datetime_log, has_agent, changed_field, description, "PID4CatRecord_id"), 
	FOREIGN KEY("PID4CatRecord_id") REFERENCES "PID4CatRecord" (id)
);

CREATE TABLE "PID4CatRecord_related_identifiers" (
	backref_id TEXT, 
	related_identifiers TEXT, 
	PRIMARY KEY (backref_id, related_identifiers), 
	FOREIGN KEY(backref_id) REFERENCES "PID4CatRecord" (id)
);
