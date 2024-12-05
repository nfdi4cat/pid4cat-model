from __future__ import annotations 
from datetime import (
    datetime,
    date
)
from decimal import Decimal 
from enum import Enum 
import re
import sys
from typing import (
    Any,
    List,
    Literal,
    Dict,
    Optional,
    Union
)
from pydantic.version import VERSION  as PYDANTIC_VERSION 
if int(PYDANTIC_VERSION[0])>=2:
    from pydantic import (
        BaseModel,
        ConfigDict,
        Field,
        field_validator
    )
else:
    from pydantic import (
        BaseModel,
        Field,
        validator
    )

metamodel_version = "None"
version = "None"


class WeakRefShimBaseModel(BaseModel):
    __slots__ = '__weakref__'

class ConfiguredBaseModel(WeakRefShimBaseModel,
                validate_assignment = True,
                validate_all = True,
                underscore_attrs_are_private = True,
                extra = "forbid",
                arbitrary_types_allowed = True,
                use_enum_values = True):
    pass


class ResourceCategory(str, Enum):
    """
    The category of the resource
    """
    # A collection is a group of resources and/or other collections.
    COLLECTION = "COLLECTION"
    # A representative part of an entity of interest on which observations may be made.
    SAMPLE = "SAMPLE"
    # A material used in the research process (except samples).
    MATERIAL = "MATERIAL"
    # A physical device used in the research process.
    DEVICE = "DEVICE"
    # A collection of data available for access or download. A data set might be a data file, a data set, a data collection.
    DATA_OBJECT = "DATA_OBJECT"
    # An organized system of operations that provide data processing functions or access to datasets.
    DATA_SERVICE = "DATA_SERVICE"


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
    # The resource has metadata in another resource.
    HAS_METADATA = "HAS_METADATA"
    # The resource is metadata for another resource.
    IS_METADATA_FOR = "IS_METADATA_FOR"
    # The resource has a version.
    HAS_VERSION = "HAS_VERSION"
    # The resource is a version of another resource. This is useful to refer to an abstract resource that has different versions, for example, "Python 3.12 is a version of Python".
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
    # The PID4CatRecord links to a concrete resource.
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
    # The license of the PID4CatRecord was changed.
    LICENSE = "LICENSE"


class PID4CatRecord(ConfiguredBaseModel):
    """
    Represents a PID4CatRecord
    """
    id: str = Field(..., description="""A unique identifier for a thing.""")
    landing_page_url: Optional[str] = Field(None, description="""The URL of the landing page for the resource.""")
    status: Optional[PID4CatStatus] = Field(None, description="""The status of the PID4CatRecord.""")
    pid_schema_version: Optional[str] = Field(None, description="""The version of the PID4Cat schema used for the PID4CatRecord.""")
    license: Optional[str] = Field(None, description="""The license for the metadata contained in the PID4Cat record.""")
    curation_contact_email: Optional[str] = Field(None, description="""The email address of a person or institution currently responsible for the curation of the PID record.""")
    resource_info: Optional[ResourceInfo] = Field(None, description="""Information about the resource.""")
    related_identifiers: Optional[List[PID4CatRelation]] = Field(default_factory=list, description="""Relations of the resource to other identifiers.""")
    change_log: List[LogRecord] = Field(default_factory=list, description="""Change log of PID4Cat record.""")

    @validator('curation_contact_email', allow_reuse=True)
    def pattern_curation_contact_email(cls, v):
        pattern=re.compile(r"^\S+@[\S+\.]+\S+")
        if isinstance(v,list):
            for element in v:
                if not pattern.match(element):
                    raise ValueError(f"Invalid curation_contact_email format: {element}")
        elif isinstance(v,str):
            if not pattern.match(v):
                raise ValueError(f"Invalid curation_contact_email format: {v}")
        return v


class PID4CatRelation(ConfiguredBaseModel):
    """
    A relation between PID4CatRecords or between a PID4CatRecord and other resources with a PID.
    """
    relation_type: Optional[List[RelationType]] = Field(default_factory=list, description="""Relation type between the resources.""")
    related_identifier: Optional[str] = Field(None, description="""Related identifiers for the resource.""")
    datetime_log: Optional[str] = Field(None, description="""The date and time of a log record.""")
    has_agent: Optional[Agent] = Field(None, description="""The person who registered the resource.""")


class ResourceInfo(ConfiguredBaseModel):
    """
    Data object to hold information about the resource and its representation.
    """
    label: Optional[str] = Field(None, description="""A human-readable name for a resource.""")
    description: Optional[str] = Field(None, description="""A human-readable description for a resource.""")
    resource_category: Optional[ResourceCategory] = Field(None, description="""The category of the resource.""")
    rdf_url: Optional[str] = Field(None, description="""The URI of the rdf representation of the resource.""")
    rdf_type: Optional[str] = Field(None, description="""The format of the rdf representation of the resource (xml, turtle, json-ld, ...).""")
    schema_url: Optional[str] = Field(None, description="""The URI of the schema to which the resource conforms. Same property as in DataCite:schemeURI.""")
    schema_type: Optional[str] = Field(None, description="""The type of the schema to which the resource conforms. Examples: XSD, DDT, SHACL Same property as in DataCite:schemeType.""")


class LogRecord(ConfiguredBaseModel):
    """
    A log record for changes made on a PID4CatRecord starting from registration.
    """
    datetime_log: Optional[str] = Field(None, description="""The date and time of a log record.""")
    has_agent: Optional[Agent] = Field(None, description="""The person who registered the resource.""")
    changed_field: Optional[ChangeLogField] = Field(None, description="""The field that was changed""")
    description: Optional[str] = Field(None, description="""A human-readable description for a resource.""")


class Agent(ConfiguredBaseModel):
    """
    Person who plays a role relative to PID creation or curation.
    """
    name: Optional[str] = Field(None, description="""The name of the agent that created or modified the PID record.""")
    email: Optional[str] = Field(None, description="""Email address of the agent that created or modified the PID record.""")
    orcid: Optional[str] = Field(None, description="""The ORCID of the person""")
    affiliation_ror: Optional[str] = Field(None, description="""The ROR of the agent's affiliation.""")
    role: Optional[PID4CatAgentRole] = Field(None, description="""The role of the agent relative to the resource""")

    @validator('email', allow_reuse=True)
    def pattern_email(cls, v):
        pattern=re.compile(r"^\S+@[\S+\.]+\S+")
        if isinstance(v,list):
            for element in v:
                if not pattern.match(element):
                    raise ValueError(f"Invalid email format: {element}")
        elif isinstance(v,str):
            if not pattern.match(v):
                raise ValueError(f"Invalid email format: {v}")
        return v


class Container(ConfiguredBaseModel):
    """
    A container for all PID4Cat instances.
    """
    contains_pids: Optional[List[PID4CatRecord]] = Field(default_factory=list, description="""The PID4CatRecords contained in the container.""")


# Update forward refs
# see https://pydantic-docs.helpmanual.io/usage/postponed_annotations/
PID4CatRecord.update_forward_refs()
PID4CatRelation.update_forward_refs()
ResourceInfo.update_forward_refs()
LogRecord.update_forward_refs()
Agent.update_forward_refs()
Container.update_forward_refs()

