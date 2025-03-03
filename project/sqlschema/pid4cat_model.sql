-- # Class: "HandleAPIRecord" Description: "A class representing a handle record query response of the REST (json) API of a handle server."
--     * Slot: responseCode Description: The response code of the handle API.
--     * Slot: handle Description: The handle of the pid4cat record.
--     * Slot: HandleRecordContainer_id Description: Autocreated FK slot
-- # Class: "HandleRecord" Description: "A base class for handle-data classes that represent a handle record in the same way as in the REST (json) API of a handle server."
--     * Slot: id Description:
--     * Slot: timestamp Description: The iso datetime for the last update of the handle data.
--     * Slot: ttl Description: A time to live in seconds for the handle record. Typically: 86400 => 1 day
--     * Slot: type Description: The type of handledata stored in the handle record.
-- # Class: "URL" Description: "The data element in the handle API for the landing page URL."
--     * Slot: id Description:
--     * Slot: index Description: The index of the handle record.
--     * Slot: timestamp Description: The iso datetime for the last update of the handle data.
--     * Slot: ttl Description: A time to live in seconds for the handle record. Typically: 86400 => 1 day
--     * Slot: type Description: The type of handledata stored in the handle record.
--     * Slot: data_id Description: The data in the handle record.
-- # Class: "HdlDataUrl" Description: "The data class for the redirect url."
--     * Slot: id Description:
--     * Slot: format Description: The format of the handle data.
--     * Slot: value Description: The value of the handle data.
-- # Class: "STATUS" Description: "The data element in the handle API for the PID status information."
--     * Slot: id Description:
--     * Slot: index Description: The index of the handle record.
--     * Slot: timestamp Description: The iso datetime for the last update of the handle data.
--     * Slot: ttl Description: A time to live in seconds for the handle record. Typically: 86400 => 1 day
--     * Slot: type Description: The type of handledata stored in the handle record.
--     * Slot: data_id Description: The data in the handle record.
-- # Class: "HdlDataStatus" Description: "The data class for the PID status information."
--     * Slot: id Description:
--     * Slot: format Description: The format of the handle data.
--     * Slot: value Description: The value of the handle data.
-- # Class: "SCHEMA_VER" Description: "The data element in the handle API for the schema version."
--     * Slot: id Description:
--     * Slot: index Description: The index of the handle record.
--     * Slot: timestamp Description: The iso datetime for the last update of the handle data.
--     * Slot: ttl Description: A time to live in seconds for the handle record. Typically: 86400 => 1 day
--     * Slot: type Description: The type of handledata stored in the handle record.
--     * Slot: data_id Description: The data in the handle record.
-- # Class: "HdlDataSchemaVer" Description: "The data class for the schema version."
--     * Slot: id Description:
--     * Slot: format Description: The format of the handle data.
--     * Slot: value Description: The value of the handle data.
-- # Class: "LICENSE" Description: "The data element in the handle API for the PID metadata license."
--     * Slot: id Description:
--     * Slot: index Description: The index of the handle record.
--     * Slot: timestamp Description: The iso datetime for the last update of the handle data.
--     * Slot: ttl Description: A time to live in seconds for the handle record. Typically: 86400 => 1 day
--     * Slot: type Description: The type of handledata stored in the handle record.
--     * Slot: data_id Description: The data in the handle record.
-- # Class: "HdlDataLicense" Description: "The data class for the PID metadata license."
--     * Slot: id Description:
--     * Slot: format Description: The format of the handle data.
--     * Slot: value Description: The value of the handle data.
-- # Class: "EMAIL" Description: "The data element in the handle API for the contact email."
--     * Slot: id Description:
--     * Slot: index Description: The index of the handle record.
--     * Slot: timestamp Description: The iso datetime for the last update of the handle data.
--     * Slot: ttl Description: A time to live in seconds for the handle record. Typically: 86400 => 1 day
--     * Slot: type Description: The type of handledata stored in the handle record.
--     * Slot: data_id Description: The data in the handle record.
-- # Class: "HdlDataContact" Description: "The data class for the handle-record contact email."
--     * Slot: id Description:
--     * Slot: format Description: The format of the handle data.
--     * Slot: value Description: The value of the handle data.
-- # Class: "RESOURCE_INFO" Description: "The data element in the handle API for the resource info."
--     * Slot: id Description:
--     * Slot: index Description: The index of the handle record.
--     * Slot: timestamp Description: The iso datetime for the last update of the handle data.
--     * Slot: ttl Description: A time to live in seconds for the handle record. Typically: 86400 => 1 day
--     * Slot: type Description: The type of handledata stored in the handle record.
--     * Slot: data_id Description: The data in the handle record.
-- # Class: "HdlDataResourceInfo" Description: "The data class for the resource info."
--     * Slot: id Description:
--     * Slot: format Description: The format of the handle data.
--     * Slot: value_id Description: The value of the handle data.
-- # Class: "RELATED" Description: "The data element in the handle API for related identifiers."
--     * Slot: id Description:
--     * Slot: index Description: The index of the handle record.
--     * Slot: timestamp Description: The iso datetime for the last update of the handle data.
--     * Slot: ttl Description: A time to live in seconds for the handle record. Typically: 86400 => 1 day
--     * Slot: type Description: The type of handledata stored in the handle record.
--     * Slot: data_id Description: The data in the handle record.
-- # Class: "HdlDataRelated" Description: "The data class for related identifiers."
--     * Slot: id Description:
--     * Slot: format Description: The format of the handle data.
-- # Class: "LOG" Description: "The data element in the handle API for the change log."
--     * Slot: id Description:
--     * Slot: index Description: The index of the handle record.
--     * Slot: timestamp Description: The iso datetime for the last update of the handle data.
--     * Slot: ttl Description: A time to live in seconds for the handle record. Typically: 86400 => 1 day
--     * Slot: type Description: The type of handledata stored in the handle record.
--     * Slot: data_id Description: The data in the handle record.
-- # Class: "HdlDataLog" Description: "The data class for the change log."
--     * Slot: id Description:
--     * Slot: format Description: The format of the handle data.
-- # Class: "HandleRecordContainer" Description: "A container for all HandleRecords."
--     * Slot: id Description:
-- # Class: "Pid4CatRelation" Description: "Data class for a relation to another resource identified by a pid4cat handle or another PID type."
--     * Slot: id Description:
--     * Slot: relation_type Description: Relation type between the resources.
--     * Slot: datetime_log Description: The date and time of a log record.
--     * Slot: related_identifier_id Description: The related identifier.
-- # Class: "ResourceInfo" Description: "Data class to hold information about the resource and its representation."
--     * Slot: id Description:
--     * Slot: label Description: A human-readable name for a resource.
--     * Slot: description Description: A human-readable description for a resource.
--     * Slot: resource_category Description: The category of the resource.
-- # Class: "LogRecord" Description: "Data class for a change log of modification made on a pid4cat handle record starting from its registration."
--     * Slot: id Description:
--     * Slot: datetime_log Description: The date and time of a log record.
--     * Slot: changed_field Description: The field that was changed.
--     * Slot: description Description: A human-readable description for a resource.
--     * Slot: has_agent_id Description: The person who registered or modified the PID record.
-- # Class: "Agent" Description: "Data class for a person who plays a role relative to PID creation or curation."
--     * Slot: id Description:
--     * Slot: name Description: The name of the agent that created or modified the PID record.
--     * Slot: email Description: Email address of the agent that created or modified the PID record.
--     * Slot: orcid Description: The ORCID of the person
--     * Slot: affiliation_ror Description: The ROR of the agent's affiliation.
--     * Slot: role Description: The role of the agent relative to the resource
-- # Class: "RepresentationVariant" Description: "Data class for representations of the resource in other media types than text/html which is the default for landing_page_url."
--     * Slot: id Description:
--     * Slot: url Description: The URL of the representation.
--     * Slot: media_type Description: The media type of the representation as defined by [IANA](https://www.iana.org/assignments/media-types/media-types.xhtml)
--     * Slot: encoding_format Description: The encoding of the representation. https://encoding.spec.whatwg.org/#names-and-labels
--     * Slot: size Description: The size of the representation in bytes.
-- # Class: "RelatedIdentifier" Description: "A base class for all types of related identifiers."
--     * Slot: id Description:
--     * Slot: type Description: The type of the identifier.
-- # Class: "PurlIdentifier" Description: "A PURL (permanent uniform resource locator)."
--     * Slot: id Description:
--     * Slot: resolving_url Description: The URL that resolves the identifier.
--     * Slot: type Description: The type of the identifier.
-- # Class: "DoiIdentifier" Description: "A digital object identifier (DOI)."
--     * Slot: id Description:
--     * Slot: resolving_url Description: The URL that resolves the identifier.
--     * Slot: identifier Description: The identifier in recommended notation.
--     * Slot: type Description: The type of the identifier.
-- # Class: "HandleIdentifier" Description: "A handle identifier."
--     * Slot: id Description:
--     * Slot: resolving_url Description: The URL that resolves the identifier.
--     * Slot: identifier Description: The identifier in recommended notation.
--     * Slot: type Description: The type of the identifier.
-- # Class: "ArkIdentifier" Description: "An ARK (Archival Resource Key)."
--     * Slot: id Description:
--     * Slot: identifier Description: The identifier in recommended notation.
--     * Slot: resolving_url Description: The URL that resolves the identifier.
--     * Slot: type Description: The type of the identifier.
-- # Class: "UrnIdentifier" Description: "A URN (Uniform Resource Name)."
--     * Slot: id Description:
--     * Slot: identifier Description: The identifier in recommended notation.
--     * Slot: type Description: The type of the identifier.
-- # Class: "GtinIdentifier" Description: "A Global Trade Item Number (GTIN) previously called European Article Number (EAN) often encoded as EAN13 barcode. The identifier is used to identify products. GTINs don't have a resolvable URL."
--     * Slot: id Description:
--     * Slot: identifier Description: The identifier in recommended notation.
--     * Slot: type Description: The type of the identifier.
-- # Class: "ExampleIdentifier" Description: "An example.org test identifier."
--     * Slot: id Description:
--     * Slot: identifier Description: The identifier in recommended notation.
--     * Slot: resolving_url Description: The URL that resolves the identifier.
--     * Slot: type Description: The type of the identifier.
-- # Class: "HandleAPIRecord_values" Description: ""
--     * Slot: HandleAPIRecord_handle Description: Autocreated FK slot
--     * Slot: values_id Description: The values of the pid4cat record.
-- # Class: "HdlDataRelated_value" Description: ""
--     * Slot: HdlDataRelated_id Description: Autocreated FK slot
--     * Slot: value_id Description: The value of the handle data.
-- # Class: "HdlDataLog_value" Description: ""
--     * Slot: HdlDataLog_id Description: Autocreated FK slot
--     * Slot: value_id Description: The value of the handle data.
-- # Class: "ResourceInfo_representation_variants" Description: ""
--     * Slot: ResourceInfo_id Description: Autocreated FK slot
--     * Slot: representation_variants_id Description: The representations of the resource in other media types than text/html.

CREATE TABLE "HandleRecord" (
	id INTEGER NOT NULL,
	timestamp DATETIME NOT NULL,
	ttl INTEGER,
	type TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE TABLE "HdlDataUrl" (
	id INTEGER NOT NULL,
	format TEXT,
	value TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE TABLE "HdlDataStatus" (
	id INTEGER NOT NULL,
	format TEXT,
	value VARCHAR(10) NOT NULL,
	PRIMARY KEY (id)
);
CREATE TABLE "HdlDataSchemaVer" (
	id INTEGER NOT NULL,
	format TEXT,
	value TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE TABLE "HdlDataLicense" (
	id INTEGER NOT NULL,
	format TEXT,
	value TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE TABLE "HdlDataContact" (
	id INTEGER NOT NULL,
	format TEXT,
	value TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE TABLE "HdlDataRelated" (
	id INTEGER NOT NULL,
	format TEXT,
	PRIMARY KEY (id)
);
CREATE TABLE "HdlDataLog" (
	id INTEGER NOT NULL,
	format TEXT,
	PRIMARY KEY (id)
);
CREATE TABLE "HandleRecordContainer" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE TABLE "ResourceInfo" (
	id INTEGER NOT NULL,
	label TEXT,
	description TEXT,
	resource_category VARCHAR(12) NOT NULL,
	PRIMARY KEY (id)
);
CREATE TABLE "Agent" (
	id INTEGER NOT NULL,
	name TEXT NOT NULL,
	email TEXT NOT NULL,
	orcid TEXT,
	affiliation_ror TEXT,
	role VARCHAR(7) NOT NULL,
	PRIMARY KEY (id)
);
CREATE TABLE "RepresentationVariant" (
	id INTEGER NOT NULL,
	url TEXT,
	media_type VARCHAR(73),
	encoding_format TEXT,
	size INTEGER,
	PRIMARY KEY (id)
);
CREATE TABLE "RelatedIdentifier" (
	id INTEGER NOT NULL,
	type TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE TABLE "PurlIdentifier" (
	id INTEGER NOT NULL,
	resolving_url TEXT NOT NULL,
	type TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE TABLE "DoiIdentifier" (
	id INTEGER NOT NULL,
	resolving_url TEXT NOT NULL,
	identifier TEXT,
	type TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE TABLE "HandleIdentifier" (
	id INTEGER NOT NULL,
	resolving_url TEXT NOT NULL,
	identifier TEXT,
	type TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE TABLE "ArkIdentifier" (
	id INTEGER NOT NULL,
	identifier TEXT,
	resolving_url TEXT NOT NULL,
	type TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE TABLE "UrnIdentifier" (
	id INTEGER NOT NULL,
	identifier TEXT NOT NULL,
	type TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE TABLE "GtinIdentifier" (
	id INTEGER NOT NULL,
	identifier TEXT NOT NULL,
	type TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE TABLE "ExampleIdentifier" (
	id INTEGER NOT NULL,
	identifier TEXT,
	resolving_url TEXT,
	type TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE TABLE "HandleAPIRecord" (
	"responseCode" INTEGER,
	handle TEXT NOT NULL,
	"HandleRecordContainer_id" INTEGER,
	PRIMARY KEY (handle),
	FOREIGN KEY("HandleRecordContainer_id") REFERENCES "HandleRecordContainer" (id)
);
CREATE TABLE "URL" (
	id INTEGER NOT NULL,
	"index" INTEGER NOT NULL,
	timestamp DATETIME NOT NULL,
	ttl INTEGER,
	type TEXT NOT NULL,
	data_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(data_id) REFERENCES "HdlDataUrl" (id)
);
CREATE TABLE "STATUS" (
	id INTEGER NOT NULL,
	"index" INTEGER NOT NULL,
	timestamp DATETIME NOT NULL,
	ttl INTEGER,
	type TEXT NOT NULL,
	data_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(data_id) REFERENCES "HdlDataStatus" (id)
);
CREATE TABLE "SCHEMA_VER" (
	id INTEGER NOT NULL,
	"index" INTEGER NOT NULL,
	timestamp DATETIME NOT NULL,
	ttl INTEGER,
	type TEXT NOT NULL,
	data_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(data_id) REFERENCES "HdlDataSchemaVer" (id)
);
CREATE TABLE "LICENSE" (
	id INTEGER NOT NULL,
	"index" INTEGER NOT NULL,
	timestamp DATETIME NOT NULL,
	ttl INTEGER,
	type TEXT NOT NULL,
	data_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(data_id) REFERENCES "HdlDataLicense" (id)
);
CREATE TABLE "EMAIL" (
	id INTEGER NOT NULL,
	"index" INTEGER NOT NULL,
	timestamp DATETIME NOT NULL,
	ttl INTEGER,
	type TEXT NOT NULL,
	data_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(data_id) REFERENCES "HdlDataContact" (id)
);
CREATE TABLE "HdlDataResourceInfo" (
	id INTEGER NOT NULL,
	format TEXT,
	value_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(value_id) REFERENCES "ResourceInfo" (id)
);
CREATE TABLE "RELATED" (
	id INTEGER NOT NULL,
	"index" INTEGER NOT NULL,
	timestamp DATETIME NOT NULL,
	ttl INTEGER,
	type TEXT NOT NULL,
	data_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(data_id) REFERENCES "HdlDataRelated" (id)
);
CREATE TABLE "LOG" (
	id INTEGER NOT NULL,
	"index" INTEGER NOT NULL,
	timestamp DATETIME NOT NULL,
	ttl INTEGER,
	type TEXT NOT NULL,
	data_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(data_id) REFERENCES "HdlDataLog" (id)
);
CREATE TABLE "Pid4CatRelation" (
	id INTEGER NOT NULL,
	relation_type VARCHAR(22),
	datetime_log DATETIME,
	related_identifier_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(related_identifier_id) REFERENCES "RelatedIdentifier" (id)
);
CREATE TABLE "LogRecord" (
	id INTEGER NOT NULL,
	datetime_log DATETIME NOT NULL,
	changed_field VARCHAR(13) NOT NULL,
	description TEXT,
	has_agent_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(has_agent_id) REFERENCES "Agent" (id)
);
CREATE TABLE "ResourceInfo_representation_variants" (
	"ResourceInfo_id" INTEGER,
	representation_variants_id INTEGER NOT NULL,
	PRIMARY KEY ("ResourceInfo_id", representation_variants_id),
	FOREIGN KEY("ResourceInfo_id") REFERENCES "ResourceInfo" (id),
	FOREIGN KEY(representation_variants_id) REFERENCES "RepresentationVariant" (id)
);
CREATE TABLE "RESOURCE_INFO" (
	id INTEGER NOT NULL,
	"index" INTEGER NOT NULL,
	timestamp DATETIME NOT NULL,
	ttl INTEGER,
	type TEXT NOT NULL,
	data_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(data_id) REFERENCES "HdlDataResourceInfo" (id)
);
CREATE TABLE "HandleAPIRecord_values" (
	"HandleAPIRecord_handle" TEXT,
	values_id INTEGER NOT NULL,
	PRIMARY KEY ("HandleAPIRecord_handle", values_id),
	FOREIGN KEY("HandleAPIRecord_handle") REFERENCES "HandleAPIRecord" (handle),
	FOREIGN KEY(values_id) REFERENCES "HandleRecord" (id)
);
CREATE TABLE "HdlDataRelated_value" (
	"HdlDataRelated_id" INTEGER,
	value_id INTEGER,
	PRIMARY KEY ("HdlDataRelated_id", value_id),
	FOREIGN KEY("HdlDataRelated_id") REFERENCES "HdlDataRelated" (id),
	FOREIGN KEY(value_id) REFERENCES "Pid4CatRelation" (id)
);
CREATE TABLE "HdlDataLog_value" (
	"HdlDataLog_id" INTEGER,
	value_id INTEGER NOT NULL,
	PRIMARY KEY ("HdlDataLog_id", value_id),
	FOREIGN KEY("HdlDataLog_id") REFERENCES "HdlDataLog" (id),
	FOREIGN KEY(value_id) REFERENCES "LogRecord" (id)
);
