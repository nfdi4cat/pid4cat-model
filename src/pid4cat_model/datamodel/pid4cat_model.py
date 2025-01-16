# Auto generated from pid4cat_model.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-01-16T23:37:49
# Schema: pid4cat-model
#
# id: https://w3id.org/nfdi4cat/pid4cat-model
# description: A LinkML model for PIDs for resources in catalysis (PID4Cat). PID4Cat is a handle system based persistent identifier (PID) for digital or physical resources used in the catalysis research process. The handle record is used to store additional metadata about the PID besides the obligatory landing page URL.
#   The model describes metadata for the PID itself and how to access the identified resource. It does not describe the resource itself with the exception of the resource category, which is a high-level description of what is identified by the PID4Cat handle, e.g. a sample or a device.
# license: MIT

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Datetime, Integer, String, Uri, Uriorcurie
from linkml_runtime.utils.metamodelcore import URI, URIorCURIE, XSDDateTime

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
DATACITE = CurieNamespace('DataCite', 'https://purl.org/spar/datacite/')
DCAT = CurieNamespace('dcat', 'https://www.w3.org/ns/dcat#')
DCTERMS = CurieNamespace('dcterms', 'https://purl.org/dc/terms/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
PID4CAT_MODEL = CurieNamespace('pid4cat_model', 'https://w3id.org/nfdi4cat/pid4cat-model/')
PROV = CurieNamespace('prov', 'https://www.w3.org/ns/prov#')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = PID4CAT_MODEL


# Types

# Class references



@dataclass(repr=False)
class HandleAPIRecord(YAMLRoot):
    """
    A handle record for a PID4CatRecord.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PID4CAT_MODEL["HandleAPIRecord"]
    class_class_curie: ClassVar[str] = "pid4cat_model:HandleAPIRecord"
    class_name: ClassVar[str] = "HandleAPIRecord"
    class_model_uri: ClassVar[URIRef] = PID4CAT_MODEL.HandleAPIRecord

    responseCode: Optional[int] = None
    handle: Optional[str] = None
    values: Optional[Union[Union[dict, "HandleRecord"], List[Union[dict, "HandleRecord"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.responseCode is not None and not isinstance(self.responseCode, int):
            self.responseCode = int(self.responseCode)

        if self.handle is not None and not isinstance(self.handle, str):
            self.handle = str(self.handle)

        if not isinstance(self.values, list):
            self.values = [self.values] if self.values is not None else []
        self.values = [v if isinstance(v, HandleRecord) else HandleRecord(**as_dict(v)) for v in self.values]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HandleRecord(YAMLRoot):
    """
    A handle record for a PID4CatRecord.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PID4CAT_MODEL["HandleRecord"]
    class_class_curie: ClassVar[str] = "pid4cat_model:HandleRecord"
    class_name: ClassVar[str] = "HandleRecord"
    class_model_uri: ClassVar[URIRef] = PID4CAT_MODEL.HandleRecord

    index: Optional[int] = None
    type: Optional[Union[str, "HandleDataType"]] = None
    data: Optional[Union[dict, "HandleData"]] = None
    ttl: Optional[int] = None
    timestamp: Optional[Union[str, XSDDateTime]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.index is not None and not isinstance(self.index, int):
            self.index = int(self.index)

        if self.type is not None and not isinstance(self.type, HandleDataType):
            self.type = HandleDataType(self.type)

        if self.data is not None and not isinstance(self.data, HandleData):
            self.data = HandleData(**as_dict(self.data))

        if self.ttl is not None and not isinstance(self.ttl, int):
            self.ttl = int(self.ttl)

        if self.timestamp is not None and not isinstance(self.timestamp, XSDDateTime):
            self.timestamp = XSDDateTime(self.timestamp)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HandleData(YAMLRoot):
    """
    The data element in the handle API.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PID4CAT_MODEL["HandleData"]
    class_class_curie: ClassVar[str] = "pid4cat_model:HandleData"
    class_name: ClassVar[str] = "HandleData"
    class_model_uri: ClassVar[URIRef] = PID4CAT_MODEL.HandleData

    format: Optional[str] = None
    value: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.format is not None and not isinstance(self.format, str):
            self.format = str(self.format)

        if self.value is not None and not isinstance(self.value, str):
            self.value = str(self.value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HandleRecordContainer(YAMLRoot):
    """
    A container for all HandleRecords.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PID4CAT_MODEL["HandleRecordContainer"]
    class_class_curie: ClassVar[str] = "pid4cat_model:HandleRecordContainer"
    class_name: ClassVar[str] = "HandleRecordContainer"
    class_model_uri: ClassVar[URIRef] = PID4CAT_MODEL.HandleRecordContainer

    contains_pids: Optional[Union[Union[dict, HandleAPIRecord], List[Union[dict, HandleAPIRecord]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.contains_pids, list):
            self.contains_pids = [self.contains_pids] if self.contains_pids is not None else []
        self.contains_pids = [v if isinstance(v, HandleAPIRecord) else HandleAPIRecord(**as_dict(v)) for v in self.contains_pids]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PID4CatRelation(YAMLRoot):
    """
    A relation between PID4CatRecords or between a PID4CatRecord and other resources with a PID.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PID4CAT_MODEL["PID4CatRelation"]
    class_class_curie: ClassVar[str] = "pid4cat_model:PID4CatRelation"
    class_name: ClassVar[str] = "PID4CatRelation"
    class_model_uri: ClassVar[URIRef] = PID4CAT_MODEL.PID4CatRelation

    relation_type: Optional[Union[str, "RelationType"]] = None
    related_identifier: Optional[Union[str, URI]] = None
    datetime_log: Optional[Union[str, XSDDateTime]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.relation_type is not None and not isinstance(self.relation_type, RelationType):
            self.relation_type = RelationType(self.relation_type)

        if self.related_identifier is not None and not isinstance(self.related_identifier, URI):
            self.related_identifier = URI(self.related_identifier)

        if self.datetime_log is not None and not isinstance(self.datetime_log, XSDDateTime):
            self.datetime_log = XSDDateTime(self.datetime_log)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ResourceInfo(YAMLRoot):
    """
    Data object to hold information about the resource and its representation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PID4CAT_MODEL["ResourceInfo"]
    class_class_curie: ClassVar[str] = "pid4cat_model:ResourceInfo"
    class_name: ClassVar[str] = "ResourceInfo"
    class_model_uri: ClassVar[URIRef] = PID4CAT_MODEL.ResourceInfo

    label: Optional[str] = None
    description: Optional[str] = None
    resource_category: Optional[Union[str, "ResourceCategory"]] = None
    representation_variants: Optional[Union[Union[dict, "RepresentationVariant"], List[Union[dict, "RepresentationVariant"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.resource_category is not None and not isinstance(self.resource_category, ResourceCategory):
            self.resource_category = ResourceCategory(self.resource_category)

        if not isinstance(self.representation_variants, list):
            self.representation_variants = [self.representation_variants] if self.representation_variants is not None else []
        self.representation_variants = [v if isinstance(v, RepresentationVariant) else RepresentationVariant(**as_dict(v)) for v in self.representation_variants]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LogRecord(YAMLRoot):
    """
    A log record for changes made on a PID4CatRecord starting from registration.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PID4CAT_MODEL["LogRecord"]
    class_class_curie: ClassVar[str] = "pid4cat_model:LogRecord"
    class_name: ClassVar[str] = "LogRecord"
    class_model_uri: ClassVar[URIRef] = PID4CAT_MODEL.LogRecord

    datetime_log: Optional[Union[str, XSDDateTime]] = None
    has_agent: Optional[Union[dict, "Agent"]] = None
    changed_field: Optional[Union[str, "ChangeLogField"]] = None
    description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.datetime_log is not None and not isinstance(self.datetime_log, XSDDateTime):
            self.datetime_log = XSDDateTime(self.datetime_log)

        if self.has_agent is not None and not isinstance(self.has_agent, Agent):
            self.has_agent = Agent(**as_dict(self.has_agent))

        if self.changed_field is not None and not isinstance(self.changed_field, ChangeLogField):
            self.changed_field = ChangeLogField(self.changed_field)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Agent(YAMLRoot):
    """
    Person who plays a role relative to PID creation or curation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV["Agent"]
    class_class_curie: ClassVar[str] = "prov:Agent"
    class_name: ClassVar[str] = "Agent"
    class_model_uri: ClassVar[URIRef] = PID4CAT_MODEL.Agent

    name: Optional[str] = None
    email: Optional[str] = None
    orcid: Optional[str] = None
    affiliation_ror: Optional[Union[str, URI]] = None
    role: Optional[Union[str, "PID4CatAgentRole"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.email is not None and not isinstance(self.email, str):
            self.email = str(self.email)

        if self.orcid is not None and not isinstance(self.orcid, str):
            self.orcid = str(self.orcid)

        if self.affiliation_ror is not None and not isinstance(self.affiliation_ror, URI):
            self.affiliation_ror = URI(self.affiliation_ror)

        if self.role is not None and not isinstance(self.role, PID4CatAgentRole):
            self.role = PID4CatAgentRole(self.role)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RepresentationVariant(YAMLRoot):
    """
    A representation of the resource in other media types than text/html which is the default for landing_page_url.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PID4CAT_MODEL["RepresentationVariant"]
    class_class_curie: ClassVar[str] = "pid4cat_model:RepresentationVariant"
    class_name: ClassVar[str] = "RepresentationVariant"
    class_model_uri: ClassVar[URIRef] = PID4CAT_MODEL.RepresentationVariant

    url: Optional[Union[str, URI]] = None
    media_type: Optional[str] = None
    encoding_format: Optional[str] = None
    size: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.url is not None and not isinstance(self.url, URI):
            self.url = URI(self.url)

        if self.media_type is not None and not isinstance(self.media_type, str):
            self.media_type = str(self.media_type)

        if self.encoding_format is not None and not isinstance(self.encoding_format, str):
            self.encoding_format = str(self.encoding_format)

        if self.size is not None and not isinstance(self.size, int):
            self.size = int(self.size)

        super().__post_init__(**kwargs)


# Enumerations
class ResourceCategory(EnumDefinitionImpl):
    """
    The category of the resource
    """
    COLLECTION = PermissibleValue(
        text="COLLECTION",
        description="A collection is a group of resources and/or other collections.",
        meaning=None)
    SAMPLE = PermissibleValue(
        text="SAMPLE",
        description="A representative part of an entity of interest on which observations may be made.",
        meaning=None)
    MATERIAL = PermissibleValue(
        text="MATERIAL",
        description="A material used in the research process (except samples).")
    DEVICE = PermissibleValue(
        text="DEVICE",
        description="A physical device used in the research process.")
    DATA_OBJECT = PermissibleValue(
        text="DATA_OBJECT",
        description="""A collection of data available for access or download. A data set might be a data file, a data set, a data collection.""",
        meaning=DCAT["dataset"])
    DATA_SERVICE = PermissibleValue(
        text="DATA_SERVICE",
        description="""An organized system of operations that provide data processing functions or access to datasets.""",
        meaning=DCAT["DataService"])

    _defn = EnumDefinition(
        name="ResourceCategory",
        description="The category of the resource",
    )

class RelationType(EnumDefinitionImpl):
    """
    The type of the relation between the resources
    """
    IS_CITED_BY = PermissibleValue(
        text="IS_CITED_BY",
        description="The resource is cited by another resource.")
    CITES = PermissibleValue(
        text="CITES",
        description="The resource cites another resource.")
    IS_SUPPLEMENT_TO = PermissibleValue(
        text="IS_SUPPLEMENT_TO",
        description="The resource is supplemented by another resource.")
    IS_SUPPLEMENTED_BY = PermissibleValue(
        text="IS_SUPPLEMENTED_BY",
        description="The resource supplements another resource.")
    IS_CONTINUED_BY = PermissibleValue(
        text="IS_CONTINUED_BY",
        description="The resource is continued by another resource.")
    CONTINUES = PermissibleValue(
        text="CONTINUES",
        description="The resource continues another resource.")
    HAS_METADATA = PermissibleValue(
        text="HAS_METADATA",
        description="The resource has metadata in another resource.")
    IS_METADATA_FOR = PermissibleValue(
        text="IS_METADATA_FOR",
        description="The resource is metadata for another resource.")
    HAS_VERSION = PermissibleValue(
        text="HAS_VERSION",
        description="The resource has a version.",
        meaning=DCTERMS["hasVersion"])
    IS_VERSION_OF = PermissibleValue(
        text="IS_VERSION_OF",
        description="""The resource is a version of another resource. This is useful to refer to an abstract resource that has different versions, for example, \"Python 3.12 is a version of Python\".""",
        meaning=DCTERMS["isVersionOf"])
    IS_NEW_VERSION_OF = PermissibleValue(
        text="IS_NEW_VERSION_OF",
        description="The resource is a new version of.")
    IS_PREVIOUS_VERSION_OF = PermissibleValue(
        text="IS_PREVIOUS_VERSION_OF",
        description="The resource is a previous version of.")
    IS_PART_OF = PermissibleValue(
        text="IS_PART_OF",
        description="The resource is part of another resource.",
        meaning=DCTERMS["isPartOf"])
    HAS_PART = PermissibleValue(
        text="HAS_PART",
        description="The resource has part another resource.",
        meaning=DCTERMS["hasPart"])
    IS_DESCRIBED_BY = PermissibleValue(
        text="IS_DESCRIBED_BY",
        description="The resource is documented by another resource.")
    DESCRIBES = PermissibleValue(
        text="DESCRIBES",
        description="The resource documents another resource.")
    IS_PUBLISHED_IN = PermissibleValue(
        text="IS_PUBLISHED_IN",
        description="The resource is published in another resource.")
    IS_REFERENCED_BY = PermissibleValue(
        text="IS_REFERENCED_BY",
        description="The resource is referenced by another resource.",
        meaning=DCTERMS["isReferencedBy"])
    REFERENCES = PermissibleValue(
        text="REFERENCES",
        description="The resource references another resource.")
    IS_DOCUMENTED_BY = PermissibleValue(
        text="IS_DOCUMENTED_BY",
        description="The resource is documented by another resource.")
    DOCUMENTS = PermissibleValue(
        text="DOCUMENTS",
        description="The resource documents another resource.")
    IS_COMPILED_BY = PermissibleValue(
        text="IS_COMPILED_BY",
        description="The resource is compiled by another resource.")
    COMPILES = PermissibleValue(
        text="COMPILES",
        description="The resource compiles another resource.")
    IS_VARIANT_FORM_OF = PermissibleValue(
        text="IS_VARIANT_FORM_OF",
        description="The resource is variant form of another resource.")
    IS_ORIGINAL_FORM_OF = PermissibleValue(
        text="IS_ORIGINAL_FORM_OF",
        description="The resource is original form of another resource.")
    IS_IDENTICAL_TO = PermissibleValue(
        text="IS_IDENTICAL_TO",
        description="The resource is identical to another resource.")
    IS_DERIVED_FROM = PermissibleValue(
        text="IS_DERIVED_FROM",
        description="The resource is derived from another resource.")
    IS_SOURCE_OF = PermissibleValue(
        text="IS_SOURCE_OF",
        description="The resource is source of another resource.")
    IS_COLLECTED_BY = PermissibleValue(
        text="IS_COLLECTED_BY",
        description="The resource is collected by another resource.")
    COLLECTS = PermissibleValue(
        text="COLLECTS",
        description="The resource collects another resource.")
    IS_REQUIRED_BY = PermissibleValue(
        text="IS_REQUIRED_BY",
        description="The resource is required by another resource.",
        meaning=DCTERMS["isRequiredBy"])
    REQUIRES = PermissibleValue(
        text="REQUIRES",
        description="The resource requires another resource.",
        meaning=DCTERMS["requires"])
    IS_OBSOLETED_BY = PermissibleValue(
        text="IS_OBSOLETED_BY",
        description="The resource or PID4Cat is obsoleted by another resource or PID4Cat.")
    OBSOLETES = PermissibleValue(
        text="OBSOLETES",
        description="The resource or PID4Cat obsoletes another resource or PID4Cat.")

    _defn = EnumDefinition(
        name="RelationType",
        description="The type of the relation between the resources",
    )

class PID4CatStatus(EnumDefinitionImpl):
    """
    The status of the PID4CatRecord.
    """
    SUBMITTED = PermissibleValue(
        text="SUBMITTED",
        description="The PID4CatRecord is reserved but the resource is not yet linked.")
    REGISTERED = PermissibleValue(
        text="REGISTERED",
        description="The PID4CatRecord links to a concrete resource.")
    OBSOLETED = PermissibleValue(
        text="OBSOLETED",
        description="The PID4CatRecord is obsolete, e.g. because the resource is referenced by another PID4Cat.")
    DEPRECATED = PermissibleValue(
        text="DEPRECATED",
        description="The PID4CatRecord is deprecated, e.g. because the resource can no longer be found.")

    _defn = EnumDefinition(
        name="PID4CatStatus",
        description="The status of the PID4CatRecord.",
    )

class PID4CatAgentRole(EnumDefinitionImpl):
    """
    The role of an agent relative to the resource.
    """
    TRUSTEE = PermissibleValue(
        text="TRUSTEE",
        description="The agent is the trustee of the resource.")
    OWNER = PermissibleValue(
        text="OWNER",
        description="The agent is the owner of the resource.")

    _defn = EnumDefinition(
        name="PID4CatAgentRole",
        description="The role of an agent relative to the resource.",
    )

class ChangeLogField(EnumDefinitionImpl):
    """
    The field of the PID4Catrecord that was changed.
    """
    STATUS = PermissibleValue(
        text="STATUS",
        description="The status of the PID4CatRecord was changed.")
    LANDING_PAGE = PermissibleValue(
        text="LANDING_PAGE",
        description="The URL of the landing page in the PID4CatRecord was changed.")
    RESOURCE_INFO = PermissibleValue(
        text="RESOURCE_INFO",
        description="The resource info of the PID4CatRecord was changed.")
    RELATED_IDS = PermissibleValue(
        text="RELATED_IDS",
        description="The related identifiers of the PID4CatRecord were changed.")
    CONTACT = PermissibleValue(
        text="CONTACT",
        description="The contact information of the PID4CatRecord was changed.")
    LICENSE = PermissibleValue(
        text="LICENSE",
        description="The license of the PID4CatRecord was changed.")

    _defn = EnumDefinition(
        name="ChangeLogField",
        description="The field of the PID4Catrecord that was changed.",
    )

class HandleDataType(EnumDefinitionImpl):
    """
    The type of the handle record element.
    """
    URL = PermissibleValue(
        text="URL",
        description="The handle record element is of type URL.")
    STATUS = PermissibleValue(
        text="STATUS",
        description="The handle record element is of custom type STATUS.")
    SCHEMA_VER = PermissibleValue(
        text="SCHEMA_VER",
        description="The handle record element is of type SCHEMA_VER.")
    LICENSE = PermissibleValue(
        text="LICENSE",
        description="The handle record element is of type LICENSE.")
    EMAIL = PermissibleValue(
        text="EMAIL",
        description="The handle record element is of type EMAIL.")
    RESOURCE_INFO = PermissibleValue(
        text="RESOURCE_INFO",
        description="The handle record element is of custom type JSON.")
    RELATED = PermissibleValue(
        text="RELATED",
        description="The handle record element is of custom type JSON.")
    LOG = PermissibleValue(
        text="LOG",
        description="The handle record element is of custom type JSON.")

    _defn = EnumDefinition(
        name="HandleDataType",
        description="The type of the handle record element.",
    )

# Slots
class slots:
    pass

slots.response_code = Slot(uri=PID4CAT_MODEL.responseCode, name="response_code", curie=PID4CAT_MODEL.curie('responseCode'),
                   model_uri=PID4CAT_MODEL.response_code, domain=None, range=Optional[int])

slots.handle = Slot(uri=PID4CAT_MODEL.handle, name="handle", curie=PID4CAT_MODEL.curie('handle'),
                   model_uri=PID4CAT_MODEL.handle, domain=None, range=Optional[str])

slots.values = Slot(uri=PID4CAT_MODEL.values, name="values", curie=PID4CAT_MODEL.curie('values'),
                   model_uri=PID4CAT_MODEL.values, domain=None, range=Optional[Union[Union[dict, HandleRecord], List[Union[dict, HandleRecord]]]])

slots.index = Slot(uri=PID4CAT_MODEL.index, name="index", curie=PID4CAT_MODEL.curie('index'),
                   model_uri=PID4CAT_MODEL.index, domain=None, range=Optional[int])

slots.type = Slot(uri=PID4CAT_MODEL.type, name="type", curie=PID4CAT_MODEL.curie('type'),
                   model_uri=PID4CAT_MODEL.type, domain=None, range=Optional[Union[str, "HandleDataType"]])

slots.data = Slot(uri=PID4CAT_MODEL.data, name="data", curie=PID4CAT_MODEL.curie('data'),
                   model_uri=PID4CAT_MODEL.data, domain=None, range=Optional[Union[dict, HandleData]])

slots.ttl = Slot(uri=PID4CAT_MODEL.ttl, name="ttl", curie=PID4CAT_MODEL.curie('ttl'),
                   model_uri=PID4CAT_MODEL.ttl, domain=None, range=Optional[int])

slots.timestamp = Slot(uri=PID4CAT_MODEL.timestamp, name="timestamp", curie=PID4CAT_MODEL.curie('timestamp'),
                   model_uri=PID4CAT_MODEL.timestamp, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.format = Slot(uri=PID4CAT_MODEL.format, name="format", curie=PID4CAT_MODEL.curie('format'),
                   model_uri=PID4CAT_MODEL.format, domain=None, range=Optional[str])

slots.value = Slot(uri=PID4CAT_MODEL.value, name="value", curie=PID4CAT_MODEL.curie('value'),
                   model_uri=PID4CAT_MODEL.value, domain=None, range=Optional[str])

slots.id = Slot(uri=SCHEMA.identifier, name="id", curie=SCHEMA.curie('identifier'),
                   model_uri=PID4CAT_MODEL.id, domain=None, range=URIRef)

slots.landing_page_url = Slot(uri=SCHEMA.url, name="landing_page_url", curie=SCHEMA.curie('url'),
                   model_uri=PID4CAT_MODEL.landing_page_url, domain=None, range=Optional[Union[str, URI]])

slots.status = Slot(uri=PID4CAT_MODEL.status, name="status", curie=PID4CAT_MODEL.curie('status'),
                   model_uri=PID4CAT_MODEL.status, domain=None, range=Optional[Union[str, "PID4CatStatus"]])

slots.pid_schema_version = Slot(uri=PID4CAT_MODEL.pid_schema_version, name="pid_schema_version", curie=PID4CAT_MODEL.curie('pid_schema_version'),
                   model_uri=PID4CAT_MODEL.pid_schema_version, domain=None, range=Optional[str])

slots.resource_info = Slot(uri=PID4CAT_MODEL.resource_info, name="resource_info", curie=PID4CAT_MODEL.curie('resource_info'),
                   model_uri=PID4CAT_MODEL.resource_info, domain=None, range=Optional[Union[dict, ResourceInfo]])

slots.related_identifiers = Slot(uri=PID4CAT_MODEL.related_identifiers, name="related_identifiers", curie=PID4CAT_MODEL.curie('related_identifiers'),
                   model_uri=PID4CAT_MODEL.related_identifiers, domain=None, range=Optional[Union[Union[dict, PID4CatRelation], List[Union[dict, PID4CatRelation]]]])

slots.license = Slot(uri=PID4CAT_MODEL.license, name="license", curie=PID4CAT_MODEL.curie('license'),
                   model_uri=PID4CAT_MODEL.license, domain=None, range=Optional[str])

slots.curation_contact_email = Slot(uri=PID4CAT_MODEL.curation_contact_email, name="curation_contact_email", curie=PID4CAT_MODEL.curie('curation_contact_email'),
                   model_uri=PID4CAT_MODEL.curation_contact_email, domain=None, range=Optional[str])

slots.change_log = Slot(uri=PID4CAT_MODEL.change_log, name="change_log", curie=PID4CAT_MODEL.curie('change_log'),
                   model_uri=PID4CAT_MODEL.change_log, domain=None, range=Union[Union[dict, LogRecord], List[Union[dict, LogRecord]]])

slots.relation_type = Slot(uri=PID4CAT_MODEL.relation_type, name="relation_type", curie=PID4CAT_MODEL.curie('relation_type'),
                   model_uri=PID4CAT_MODEL.relation_type, domain=None, range=Optional[Union[str, "RelationType"]])

slots.related_identifier = Slot(uri=PID4CAT_MODEL.related_identifier, name="related_identifier", curie=PID4CAT_MODEL.curie('related_identifier'),
                   model_uri=PID4CAT_MODEL.related_identifier, domain=None, range=Optional[Union[str, URI]])

slots.datetime_log = Slot(uri=PID4CAT_MODEL.datetime_log, name="datetime_log", curie=PID4CAT_MODEL.curie('datetime_log'),
                   model_uri=PID4CAT_MODEL.datetime_log, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.label = Slot(uri=PID4CAT_MODEL.label, name="label", curie=PID4CAT_MODEL.curie('label'),
                   model_uri=PID4CAT_MODEL.label, domain=None, range=Optional[str])

slots.description = Slot(uri=PID4CAT_MODEL.description, name="description", curie=PID4CAT_MODEL.curie('description'),
                   model_uri=PID4CAT_MODEL.description, domain=None, range=Optional[str])

slots.resource_category = Slot(uri=PID4CAT_MODEL.resource_category, name="resource_category", curie=PID4CAT_MODEL.curie('resource_category'),
                   model_uri=PID4CAT_MODEL.resource_category, domain=None, range=Optional[Union[str, "ResourceCategory"]])

slots.representation_variants = Slot(uri=PID4CAT_MODEL.representation_variants, name="representation_variants", curie=PID4CAT_MODEL.curie('representation_variants'),
                   model_uri=PID4CAT_MODEL.representation_variants, domain=None, range=Optional[Union[Union[dict, RepresentationVariant], List[Union[dict, RepresentationVariant]]]])

slots.changed_field = Slot(uri=PID4CAT_MODEL.changed_field, name="changed_field", curie=PID4CAT_MODEL.curie('changed_field'),
                   model_uri=PID4CAT_MODEL.changed_field, domain=None, range=Optional[Union[str, "ChangeLogField"]])

slots.has_agent = Slot(uri=PID4CAT_MODEL.has_agent, name="has_agent", curie=PID4CAT_MODEL.curie('has_agent'),
                   model_uri=PID4CAT_MODEL.has_agent, domain=None, range=Optional[Union[dict, Agent]])

slots.name = Slot(uri=PID4CAT_MODEL.name, name="name", curie=PID4CAT_MODEL.curie('name'),
                   model_uri=PID4CAT_MODEL.name, domain=None, range=Optional[str])

slots.email = Slot(uri=PID4CAT_MODEL.email, name="email", curie=PID4CAT_MODEL.curie('email'),
                   model_uri=PID4CAT_MODEL.email, domain=None, range=Optional[str])

slots.orcid = Slot(uri=PID4CAT_MODEL.orcid, name="orcid", curie=PID4CAT_MODEL.curie('orcid'),
                   model_uri=PID4CAT_MODEL.orcid, domain=None, range=Optional[str])

slots.affiliation_ror = Slot(uri=PID4CAT_MODEL.affiliation_ror, name="affiliation_ror", curie=PID4CAT_MODEL.curie('affiliation_ror'),
                   model_uri=PID4CAT_MODEL.affiliation_ror, domain=None, range=Optional[Union[str, URI]])

slots.role = Slot(uri=PID4CAT_MODEL.role, name="role", curie=PID4CAT_MODEL.curie('role'),
                   model_uri=PID4CAT_MODEL.role, domain=None, range=Optional[Union[str, "PID4CatAgentRole"]])

slots.media_type = Slot(uri=PID4CAT_MODEL.media_type, name="media_type", curie=PID4CAT_MODEL.curie('media_type'),
                   model_uri=PID4CAT_MODEL.media_type, domain=None, range=Optional[str])

slots.encoding_format = Slot(uri=PID4CAT_MODEL.encoding_format, name="encoding_format", curie=PID4CAT_MODEL.curie('encoding_format'),
                   model_uri=PID4CAT_MODEL.encoding_format, domain=None, range=Optional[str])

slots.size = Slot(uri=PID4CAT_MODEL.size, name="size", curie=PID4CAT_MODEL.curie('size'),
                   model_uri=PID4CAT_MODEL.size, domain=None, range=Optional[int])

slots.url = Slot(uri=PID4CAT_MODEL.url, name="url", curie=PID4CAT_MODEL.curie('url'),
                   model_uri=PID4CAT_MODEL.url, domain=None, range=Optional[Union[str, URI]])

slots.handleRecordContainer__contains_pids = Slot(uri=PID4CAT_MODEL.contains_pids, name="handleRecordContainer__contains_pids", curie=PID4CAT_MODEL.curie('contains_pids'),
                   model_uri=PID4CAT_MODEL.handleRecordContainer__contains_pids, domain=None, range=Optional[Union[Union[dict, HandleAPIRecord], List[Union[dict, HandleAPIRecord]]]])

slots.Agent_email = Slot(uri=PID4CAT_MODEL.email, name="Agent_email", curie=PID4CAT_MODEL.curie('email'),
                   model_uri=PID4CAT_MODEL.Agent_email, domain=Agent, range=Optional[str],
                   pattern=re.compile(r'^\S+@[\S+\.]+\S+'))