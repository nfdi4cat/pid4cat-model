from __future__ import annotations 

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal 
from enum import Enum 
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    field_validator
)


metamodel_version = "None"
version = "None"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )
    pass




class LinkMLMeta(RootModel):
    root: Dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'default_prefix': 'pid4cat_model',
     'default_range': 'string',
     'description': 'A LinkML model for PIDs for resources in catalysis (PID4Cat). '
                    'PID4Cat is a handle system based persistent identifier (PID) '
                    'for digital or physical resources used in the catalysis '
                    'research process. The handle record is used to store '
                    'additional metadata about the PID besides the obligatory '
                    'landing page URL.\n'
                    'The model describes metadata for the PID itself and how to '
                    'access the identified resource. It does not describe the '
                    'resource itself with the exception of the resource category, '
                    'which is a high-level description of what is identified by '
                    'the PID4Cat handle, e.g. a sample or a device.',
     'id': 'https://w3id.org/nfdi4cat/pid4cat-model',
     'imports': ['linkml:types'],
     'license': 'MIT',
     'name': 'pid4cat-model',
     'prefixes': {'DCAT': {'prefix_prefix': 'DCAT',
                           'prefix_reference': 'http://www.w3.org/ns/dcat#'},
                  'DataCite': {'prefix_prefix': 'DataCite',
                               'prefix_reference': 'http://purl.org/spar/datacite/'},
                  'dcterms': {'prefix_prefix': 'dcterms',
                              'prefix_reference': 'http://purl.org/dc/terms/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'pid4cat_model': {'prefix_prefix': 'pid4cat_model',
                                    'prefix_reference': 'https://w3id.org/nfdi4cat/pid4cat-model/'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'}},
     'see_also': ['https://nfdi4cat.github.io/pid4cat-model'],
     'source_file': 'src/pid4cat_model/schema/pid4cat_model.yaml',
     'title': 'pid4cat-model',
     'todos': ['Refine slots in slot_usage of class instead of globally in slot '
               'definitions',
               'Check and add mappings to other ontologies. (classes, slots, '
               'enums)',
               'Add ranges (types information) to slots']} )

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
    # The URL of the landing page in the PID4CatRecord was changed.
    LANDING_PAGE = "LANDING_PAGE"
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
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/nfdi4cat/pid4cat-model',
         'slot_usage': {'curation_contact_email': {'name': 'curation_contact_email',
                                                   'pattern': '^\\S+@[\\S+\\.]+\\S+'}}})

    id: str = Field(..., description="""A unique identifier for a thing.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['PID4CatRecord'], 'slot_uri': 'schema:identifier'} })
    landing_page_url: Optional[str] = Field(None, description="""The URL of the landing page for the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'landing_page_url',
         'domain_of': ['PID4CatRecord'],
         'rank': 10,
         'slot_uri': 'schema:url'} })
    status: Optional[PID4CatStatus] = Field(None, description="""The status of the PID4CatRecord.""", json_schema_extra = { "linkml_meta": {'alias': 'status', 'domain_of': ['PID4CatRecord']} })
    pid_schema_version: Optional[str] = Field(None, description="""The version of the PID4Cat schema used for the PID4CatRecord.""", json_schema_extra = { "linkml_meta": {'alias': 'pid_schema_version',
         'domain_of': ['PID4CatRecord'],
         'slot_uri': 'schema:identifier'} })
    license: Optional[str] = Field(None, description="""The license for the metadata contained in the PID4Cat record.""", json_schema_extra = { "linkml_meta": {'alias': 'license',
         'domain_of': ['PID4CatRecord'],
         'slot_uri': 'schema:license'} })
    curation_contact_email: Optional[str] = Field(None, description="""The email address of a person or institution currently responsible for the curation of the PID record.""", json_schema_extra = { "linkml_meta": {'alias': 'curation_contact_email',
         'domain_of': ['PID4CatRecord'],
         'slot_uri': 'schema:email'} })
    resource_info: Optional[ResourceInfo] = Field(None, description="""Information about the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'resource_info', 'domain_of': ['PID4CatRecord']} })
    related_identifiers: Optional[List[PID4CatRelation]] = Field(None, description="""Relations of the resource to other identifiers.""", json_schema_extra = { "linkml_meta": {'alias': 'related_identifiers',
         'domain_of': ['PID4CatRecord'],
         'slot_uri': 'schema:identifier'} })
    change_log: List[LogRecord] = Field(..., description="""Change log of PID4Cat record.""", json_schema_extra = { "linkml_meta": {'alias': 'change_log',
         'domain_of': ['PID4CatRecord'],
         'slot_uri': 'schema:identifier'} })

    @field_validator('curation_contact_email')
    def pattern_curation_contact_email(cls, v):
        pattern=re.compile(r"^\S+@[\S+\.]+\S+")
        if isinstance(v,list):
            for element in v:
                if isinstance(v, str) and not pattern.match(element):
                    raise ValueError(f"Invalid curation_contact_email format: {element}")
        elif isinstance(v,str):
            if not pattern.match(v):
                raise ValueError(f"Invalid curation_contact_email format: {v}")
        return v


class PID4CatRelation(ConfiguredBaseModel):
    """
    A relation between PID4CatRecords or between a PID4CatRecord and other resources with a PID.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/nfdi4cat/pid4cat-model'})

    relation_type: Optional[RelationType] = Field(None, description="""Relation type between the resources.""", json_schema_extra = { "linkml_meta": {'alias': 'relation_type',
         'domain_of': ['PID4CatRelation'],
         'slot_uri': 'schema:identifier'} })
    related_identifier: Optional[str] = Field(None, description="""Related identifiers for the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'related_identifier',
         'domain_of': ['PID4CatRelation'],
         'slot_uri': 'schema:identifier'} })
    datetime_log: Optional[str] = Field(None, description="""The date and time of a log record.""", json_schema_extra = { "linkml_meta": {'alias': 'datetime_log',
         'domain_of': ['PID4CatRelation', 'LogRecord'],
         'slot_uri': 'schema:DateTime'} })


class ResourceInfo(ConfiguredBaseModel):
    """
    Data object to hold information about the resource and its representation.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/nfdi4cat/pid4cat-model'})

    label: Optional[str] = Field(None, description="""A human-readable name for a resource.""", json_schema_extra = { "linkml_meta": {'alias': 'label', 'domain_of': ['ResourceInfo'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(None, description="""A human-readable description for a resource.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['ResourceInfo', 'LogRecord'],
         'slot_uri': 'schema:description'} })
    resource_category: Optional[ResourceCategory] = Field(None, description="""The category of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'resource_category',
         'domain_of': ['ResourceInfo'],
         'slot_uri': 'schema:additionalType'} })
    representation_variants: Optional[List[RepresentationVariant]] = Field(None, description="""The representations of the resource in other media types than text/html.""", json_schema_extra = { "linkml_meta": {'alias': 'representation_variants', 'domain_of': ['ResourceInfo']} })


class LogRecord(ConfiguredBaseModel):
    """
    A log record for changes made on a PID4CatRecord starting from registration.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/nfdi4cat/pid4cat-model'})

    datetime_log: Optional[str] = Field(None, description="""The date and time of a log record.""", json_schema_extra = { "linkml_meta": {'alias': 'datetime_log',
         'domain_of': ['PID4CatRelation', 'LogRecord'],
         'slot_uri': 'schema:DateTime'} })
    has_agent: Optional[Agent] = Field(None, description="""The person who registered or modified the PID record.""", json_schema_extra = { "linkml_meta": {'alias': 'has_agent', 'domain_of': ['LogRecord'], 'slot_uri': 'schema:Agent'} })
    changed_field: Optional[ChangeLogField] = Field(None, description="""The field that was changed""", json_schema_extra = { "linkml_meta": {'alias': 'changed_field',
         'domain_of': ['LogRecord'],
         'slot_uri': 'schema:identifier'} })
    description: Optional[str] = Field(None, description="""A human-readable description for a resource.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['ResourceInfo', 'LogRecord'],
         'slot_uri': 'schema:description'} })


class Agent(ConfiguredBaseModel):
    """
    Person who plays a role relative to PID creation or curation.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/nfdi4cat/pid4cat-model',
         'slot_usage': {'email': {'name': 'email', 'pattern': '^\\S+@[\\S+\\.]+\\S+'}}})

    name: Optional[str] = Field(None, description="""The name of the agent that created or modified the PID record.""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['Agent'], 'slot_uri': 'schema:name'} })
    email: Optional[str] = Field(None, description="""Email address of the agent that created or modified the PID record.""", json_schema_extra = { "linkml_meta": {'alias': 'email', 'domain_of': ['Agent'], 'slot_uri': 'schema:email'} })
    orcid: Optional[str] = Field(None, description="""The ORCID of the person""", json_schema_extra = { "linkml_meta": {'alias': 'orcid', 'domain_of': ['Agent'], 'slot_uri': 'schema:identifier'} })
    affiliation_ror: Optional[str] = Field(None, description="""The ROR of the agent's affiliation.""", json_schema_extra = { "linkml_meta": {'alias': 'affiliation_ror',
         'domain_of': ['Agent'],
         'slot_uri': 'schema:identifier'} })
    role: Optional[PID4CatAgentRole] = Field(None, description="""The role of the agent relative to the resource""", json_schema_extra = { "linkml_meta": {'alias': 'role', 'domain_of': ['Agent'], 'slot_uri': 'schema:identifier'} })

    @field_validator('email')
    def pattern_email(cls, v):
        pattern=re.compile(r"^\S+@[\S+\.]+\S+")
        if isinstance(v,list):
            for element in v:
                if isinstance(v, str) and not pattern.match(element):
                    raise ValueError(f"Invalid email format: {element}")
        elif isinstance(v,str):
            if not pattern.match(v):
                raise ValueError(f"Invalid email format: {v}")
        return v


class RepresentationVariant(ConfiguredBaseModel):
    """
    A representation of the resource in other media types than text/html which is the default for landing_page_url.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/nfdi4cat/pid4cat-model'})

    url: Optional[str] = Field(None, description="""The URL of the representation.""", json_schema_extra = { "linkml_meta": {'alias': 'url',
         'domain_of': ['RepresentationVariant'],
         'slot_uri': 'schema:URL'} })
    media_type: Optional[str] = Field(None, description="""The media type of the representation as defined by [IANA](https://www.iana.org/assignments/media-types/media-types.xhtml)""", json_schema_extra = { "linkml_meta": {'alias': 'media_type',
         'domain_of': ['RepresentationVariant'],
         'slot_uri': 'schema:encodingFormat'} })
    encoding_format: Optional[str] = Field(None, description="""The encoding of the representation. https://encoding.spec.whatwg.org/#names-and-labels""", json_schema_extra = { "linkml_meta": {'alias': 'encoding_format', 'domain_of': ['RepresentationVariant']} })
    size: Optional[int] = Field(None, description="""The size of the representation in bytes.""", ge=0, json_schema_extra = { "linkml_meta": {'alias': 'size',
         'domain_of': ['RepresentationVariant'],
         'slot_uri': 'schema:fileSize'} })


class Container(ConfiguredBaseModel):
    """
    A container for all PID4Cat instances.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/nfdi4cat/pid4cat-model', 'tree_root': True})

    contains_pids: Optional[List[PID4CatRecord]] = Field(None, description="""The PID4CatRecords contained in the container.""", json_schema_extra = { "linkml_meta": {'alias': 'contains_pids', 'domain_of': ['Container']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
PID4CatRecord.model_rebuild()
PID4CatRelation.model_rebuild()
ResourceInfo.model_rebuild()
LogRecord.model_rebuild()
Agent.model_rebuild()
RepresentationVariant.model_rebuild()
Container.model_rebuild()

