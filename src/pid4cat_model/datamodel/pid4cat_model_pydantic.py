from __future__ import annotations
from datetime import datetime, date
from enum import Enum
from typing import List, Dict, Optional, Any, Union
from pydantic import BaseModel as BaseModel, ConfigDict, Field
import sys
if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


metamodel_version = "None"
version = "None"

class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        validate_assignment=True,
        validate_default=True,
        extra='forbid',
        arbitrary_types_allowed=True,
        use_enum_values = True)


class ResourceCategory(str, Enum):
    """
    The category of the resource
    """
    # A collection is described as a group; its parts may also be separately described.
    COLLECTION = "COLLECTION"
    # A representative part of an entity of interest on which observations may be made.
    SAMPLE = "SAMPLE"
    # A material used in the research process (except samples).
    MATERIAL = "MATERIAL"
    # A device used in the catalysis research process.
    DEVICE = "DEVICE"
    # A data object might be a data file, a data set, a data collection, or a data service.
    DATAOBJECT = "DATAOBJECT"
    
    

class RelationType(str, Enum):
    """
    The type of the relation between the resources
    """
    # The resource is cited by another resource.
    IS_CITED_BY = "IS_CITED_BY"
    # The resource cites another resource.
    CITES = "CITES"
    # The resource is supplemented by another resource.
    IS_SUPPLEMENT_TO = "IS_SUPPLEMENT_TO"
    # The resource supplements another resource.
    IS_SUPPLEMENTED_BY = "IS_SUPPLEMENTED_BY"
    # The resource is continued by another resource.
    IS_CONTINUED_BY = "IS_CONTINUED_BY"
    # The resource continues another resource.
    CONTINUES = "CONTINUES"
    # The resource has metadata.
    HAS_METADATA = "HAS_METADATA"
    # The resource is metadata for.
    IS_METADATA_FOR = "IS_METADATA_FOR"
    # The resource has a version.
    HAS_VERSION = "HAS_VERSION"
    # The resource is a version of.
    IS_VERSION_OF = "IS_VERSION_OF"
    # The resource is a new version of.
    IS_NEW_VERSION_OF = "IS_NEW_VERSION_OF"
    # The resource is a previous version of.
    IS_PREVIOUS_VERSION_OF = "IS_PREVIOUS_VERSION_OF"
    # The resource is part of another resource.
    IS_PART_OF = "IS_PART_OF"
    # The resource has part another resource.
    HAS_PART = "HAS_PART"
    # The resource is documented by another resource.
    IS_DESCRIBED_BY = "IS_DESCRIBED_BY"
    # The resource documents another resource.
    DESCRIBES = "DESCRIBES"
    # The resource is published in another resource.
    IS_PUBLISHED_IN = "IS_PUBLISHED_IN"
    # The resource is referenced by another resource.
    IS_REFERENCED_BY = "IS_REFERENCED_BY"
    # The resource references another resource.
    REFERENCES = "REFERENCES"
    # The resource is documented by another resource.
    IS_DOCUMENTED_BY = "IS_DOCUMENTED_BY"
    # The resource documents another resource.
    DOCUMENTS = "DOCUMENTS"
    # The resource is compiled by another resource.
    IS_COMPILED_BY = "IS_COMPILED_BY"
    # The resource compiles another resource.
    COMPILES = "COMPILES"
    # The resource is variant form of another resource.
    IS_VARIANT_FORM_OF = "IS_VARIANT_FORM_OF"
    # The resource is original form of another resource.
    IS_ORIGINAL_FORM_OF = "IS_ORIGINAL_FORM_OF"
    # The resource is identical to another resource.
    IS_IDENTICAL_TO = "IS_IDENTICAL_TO"
    # The resource is derived from another resource.
    IS_DERIVED_FROM = "IS_DERIVED_FROM"
    # The resource is source of another resource.
    IS_SOURCE_OF = "IS_SOURCE_OF"
    # The resource is collected by another resource.
    IS_COLLECTED_BY = "IS_COLLECTED_BY"
    # The resource collects another resource.
    COLLECTS = "COLLECTS"
    # The resource is required by another resource.
    IS_REQUIRED_BY = "IS_REQUIRED_BY"
    # The resource requires another resource.
    REQUIRES = "REQUIRES"
    # The resource or PID4Cat is obsoleted by another resource or PID4Cat.
    IS_OBSOLETED_BY = "IS_OBSOLETED_BY"
    # The resource or PID4Cat obsoletes another resource or PID4Cat.
    OBSOLETES = "OBSOLETES"
    
    

class PID4CatStatus(str, Enum):
    """
    The status of the PID4CatRecord.
    """
    # The PID4CatRecord is reserved but the resource is not yet linked.
    SUBMITTED = "SUBMITTED"
    # The PID4CatRecord links to a concrete ressource.
    REGISTERED = "REGISTERED"
    # The PID4CatRecord is obsolete, e.g. because the resource is referenced by another PID4Cat.
    OBSOLETED = "OBSOLETED"
    # The PID4CatRecord is deprecated, e.g. because the resource can no longer be found.
    DEPRECATED = "DEPRECATED"
    
    

class PID4CatAgentRole(str, Enum):
    """
    The role of an agent relative to the resource.
    """
    # The agent is the trustee of the resource.
    TRUSTEE = "TRUSTEE"
    # The agent is the owner of the resource.
    OWNER = "OWNER"
    
    

class ChangeLogField(str, Enum):
    """
    The field of the PID4Catrecord that was changed.
    """
    # The status of the PID4CatRecord was changed.
    STATUS = "STATUS"
    # The resource info of the PID4CatRecord was changed.
    RESOURCE_INFO = "RESOURCE_INFO"
    # The related identifiers of the PID4CatRecord were changed.
    RELATED_IDS = "RELATED_IDS"
    # The contact information of the PID4CatRecord was changed.
    CONTACT = "CONTACT"
    # The rights of the PID4CatRecord were changed.
    RIGHTS = "RIGHTS"
    
    

class PID4CatRecord(ConfiguredBaseModel):
    """
    Represents a PID4CatRecord
    """
    id: str = Field(..., description="""A unique identifier for a thing""")
    landing_page_url: Optional[str] = Field(None, description="""The URL of the landing page for the resource""")
    status: Optional[PID4CatStatus] = Field(None, description="""The status of the PID4CatRecord.""")
    record_version: Optional[str] = Field(None, description="""Date-based version string of the PID4CatRecord (e.g. 20240219v0, 20240219v1, ...). The version should be incremented with every change of the PID4CatRecord.""")
    pid_schema_version: Optional[str] = Field(None, description="""The version of the PID4Cat schema used for the PID4CatRecord.""")
    dc_rights: Optional[str] = Field(None, description="""The license for the metadata contained in the PID4Cat record.""")
    curation_contact: Optional[str] = Field(None, description="""The email address of a person or institution responsible for curation of the resource.""")
    resource_info: Optional[ResourceInfo] = Field(None, description="""Information about the resource.""")
    related_identifiers: Optional[List[str]] = Field(default_factory=list, description="""Alternate identifiers for the resource""")
    change_log: List[LogRecord] = Field(default_factory=list, description="""Change log of PID4Cat record""")
    

class PID4CatRelation(ConfiguredBaseModel):
    """
    A relation between PID4CatRecords or between a PID4CatRecord and other resources with a PID.
    """
    relation_type: Optional[List[RelationType]] = Field(default_factory=list, description="""Relation type between the resources""")
    related_identifier: Optional[str] = Field(None, description="""Related identifiers for the resource""")
    datetime_log: Optional[str] = Field(None, description="""The date and time of a log record""")
    has_agent: Optional[Agent] = Field(None, description="""The person who registered the resource""")
    

class ResourceInfo(ConfiguredBaseModel):
    """
    Data object to hold information about the resource and its representation.
    """
    label: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""")
    resource_category: Optional[ResourceCategory] = Field(None, description="""The category of the resource""")
    rdf_url: Optional[str] = Field(None, description="""The URI of the rdf represenation of the resource.""")
    rdf_type: Optional[str] = Field(None, description="""The format of the rdf representation of the resource (xml, turlte, json-ld, ...).""")
    schema_url: Optional[str] = Field(None, description="""The URI of the schema used to describe the resource. Same property as in DataCite:schemeURI.""")
    schema_type: Optional[str] = Field(None, description="""The type of the scheme used to describe the resource. Examples: XSD, DDT, Turtle Same property as in DataCite:schemeType.""")
    

class LogRecord(ConfiguredBaseModel):
    """
    A log record for changes made on a PID4CatRecord starting from registration.
    """
    datetime_log: Optional[str] = Field(None, description="""The date and time of a log record""")
    has_agent: Optional[Agent] = Field(None, description="""The person who registered the resource""")
    changed_field: Optional[ChangeLogField] = Field(None, description="""The field that was changed""")
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""")
    

class Agent(ConfiguredBaseModel):
    """
    Person who plays a role relative to PID creation or curation.
    """
    name: Optional[str] = Field(None, description="""The name of the agent""")
    contact_information: Optional[str] = Field(None, description="""Identification of the agent that registered the PID, with contact information. Should include person name and affiliation, or position name and affiliation, or just organization name. e-mail address is preferred contact information.""")
    person_orcid: Optional[str] = Field(None, description="""The ORCID of the person""")
    affiliation_ror: Optional[str] = Field(None, description="""The ROR of the affiliation""")
    role: Optional[PID4CatAgentRole] = Field(None, description="""The role of the agent relative to the resource""")
    

class Container(ConfiguredBaseModel):
    """
    A container for all PID4Cat instances.
    """
    contains_pids: Optional[List[PID4CatRecord]] = Field(default_factory=list, description="""The PID4CatRecords contained in the container.""")
    


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
PID4CatRecord.model_rebuild()
PID4CatRelation.model_rebuild()
ResourceInfo.model_rebuild()
LogRecord.model_rebuild()
Agent.model_rebuild()
Container.model_rebuild()

