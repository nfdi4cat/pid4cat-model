# Auto generated from pid4cat_model.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-01-24T13:12:01
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
VOC4CAT = CurieNamespace('voc4cat', 'https://w3id.org/nfdi4cat/voc4cat_')
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
    media_type: Optional[Union[str, "MEDIATypes"]] = None
    encoding_format: Optional[str] = None
    size: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.url is not None and not isinstance(self.url, URI):
            self.url = URI(self.url)

        if self.media_type is not None and not isinstance(self.media_type, MEDIATypes):
            self.media_type = MEDIATypes(self.media_type)

        if self.encoding_format is not None and not isinstance(self.encoding_format, str):
            self.encoding_format = str(self.encoding_format)

        if self.size is not None and not isinstance(self.size, int):
            self.size = int(self.size)

        super().__post_init__(**kwargs)


# Enumerations
class ResourceCategory(EnumDefinitionImpl):
    """
    The ResourceCategory expresses for which type of resource the PID is used, e.g. if the PID is for a sample or a
    device.
    """
    COLLECTION = PermissibleValue(
        text="COLLECTION",
        description="A collection is a group of resources and/or other collections.",
        meaning=VOC4CAT["0005012"])
    SAMPLE = PermissibleValue(
        text="SAMPLE",
        description="A representative part of a material of interest on which observations are made.",
        meaning=VOC4CAT["0005013"])
    MATERIAL = PermissibleValue(
        text="MATERIAL",
        description="A material used in the research process (except samples).",
        meaning=VOC4CAT["0005014"])
    DEVICE = PermissibleValue(
        text="DEVICE",
        description="A physical device used in a research or manufacturing process.",
        meaning=VOC4CAT["0005015"])
    DATA_OBJECT = PermissibleValue(
        text="DATA_OBJECT",
        description="""A collection of data available for access or download. A data object might be a data file, a data set, a data collection.""",
        meaning=VOC4CAT["0005016"])
    DATA_SERVICE = PermissibleValue(
        text="DATA_SERVICE",
        description="""An organized system of operations that provide data processing functions or access to datasets.""",
        meaning=VOC4CAT["0005017"])

    _defn = EnumDefinition(
        name="ResourceCategory",
        description="""The ResourceCategory expresses for which type of resource the PID is used, e.g. if the PID is for a sample or a device.""",
    )

class RelationType(EnumDefinitionImpl):
    """
    The type of relation between two resources referenced by their PIDs.
    """
    IS_CITED_BY = PermissibleValue(
        text="IS_CITED_BY",
        description="The resource is cited by another resource.",
        meaning=VOC4CAT["0005019"])
    CITES = PermissibleValue(
        text="CITES",
        description="The resource cites another resource.",
        meaning=VOC4CAT["0005020"])
    IS_SUPPLEMENT_TO = PermissibleValue(
        text="IS_SUPPLEMENT_TO",
        description="The resource is supplemented by another resource.",
        meaning=VOC4CAT["0005021"])
    IS_SUPPLEMENTED_BY = PermissibleValue(
        text="IS_SUPPLEMENTED_BY",
        description="The resource supplements another resource.",
        meaning=VOC4CAT["0005022"])
    IS_CONTINUED_BY = PermissibleValue(
        text="IS_CONTINUED_BY",
        description="The resource is continued by another resource.",
        meaning=VOC4CAT["0005023"])
    CONTINUES = PermissibleValue(
        text="CONTINUES",
        description="The resource continues another resource.",
        meaning=VOC4CAT["0005024"])
    HAS_METADATA = PermissibleValue(
        text="HAS_METADATA",
        description="The resource has metadata in another resource.",
        meaning=VOC4CAT["0005025"])
    IS_METADATA_FOR = PermissibleValue(
        text="IS_METADATA_FOR",
        description="The resource is metadata for another resource.",
        meaning=VOC4CAT["0005026"])
    HAS_VERSION = PermissibleValue(
        text="HAS_VERSION",
        description="The resource has a version.",
        meaning=VOC4CAT["0005027"])
    IS_VERSION_OF = PermissibleValue(
        text="IS_VERSION_OF",
        description="""The resource is a version of another resource. This is useful to refer to an abstract resource that has different versions, for example, \"Python 3.12 is a version of Python\".""",
        meaning=VOC4CAT["0005028"])
    IS_NEW_VERSION_OF = PermissibleValue(
        text="IS_NEW_VERSION_OF",
        description="The resource is a new version of another resource.",
        meaning=VOC4CAT["0005029"])
    IS_PREVIOUS_VERSION_OF = PermissibleValue(
        text="IS_PREVIOUS_VERSION_OF",
        description="The resource is a previous version of another resource.",
        meaning=VOC4CAT["0005030"])
    IS_PART_OF = PermissibleValue(
        text="IS_PART_OF",
        description="The resource is part of another resource.",
        meaning=VOC4CAT["0005031"])
    HAS_PART = PermissibleValue(
        text="HAS_PART",
        description="The resource has part another resource.",
        meaning=VOC4CAT["0005032"])
    IS_PUBLISHED_IN = PermissibleValue(
        text="IS_PUBLISHED_IN",
        description="The resource is published in another resource.",
        meaning=VOC4CAT["0005033"])
    IS_REFERENCED_BY = PermissibleValue(
        text="IS_REFERENCED_BY",
        description="The resource is referenced by another resource.",
        meaning=VOC4CAT["0005034"])
    REFERENCES = PermissibleValue(
        text="REFERENCES",
        description="The resource references another resource.",
        meaning=VOC4CAT["0005035"])
    IS_DOCUMENTED_BY = PermissibleValue(
        text="IS_DOCUMENTED_BY",
        description="The resource is documented by another resource.",
        meaning=VOC4CAT["0005036"])
    DOCUMENTS = PermissibleValue(
        text="DOCUMENTS",
        description="The resource documents another resource.",
        meaning=VOC4CAT["0005037"])
    IS_COMPILED_BY = PermissibleValue(
        text="IS_COMPILED_BY",
        description="The resource is compiled by another resource.",
        meaning=VOC4CAT["0005038"])
    COMPILES = PermissibleValue(
        text="COMPILES",
        description="The resource compiles another resource.",
        meaning=VOC4CAT["0005039"])
    IS_VARIANT_FORM_OF = PermissibleValue(
        text="IS_VARIANT_FORM_OF",
        description="The resource is variant form of another resource.",
        meaning=VOC4CAT["0005040"])
    IS_ORIGINAL_FORM_OF = PermissibleValue(
        text="IS_ORIGINAL_FORM_OF",
        description="The resource is original form of another resource.",
        meaning=VOC4CAT["0005041"])
    IS_IDENTICAL_TO = PermissibleValue(
        text="IS_IDENTICAL_TO",
        description="The resource is identical to another resource.",
        meaning=VOC4CAT["0005042"])
    IS_DERIVED_FROM = PermissibleValue(
        text="IS_DERIVED_FROM",
        description="The resource is derived from another resource.",
        meaning=VOC4CAT["0005043"])
    IS_SOURCE_OF = PermissibleValue(
        text="IS_SOURCE_OF",
        description="The resource is source of another resource.",
        meaning=VOC4CAT["0005044"])
    IS_COLLECTED_BY = PermissibleValue(
        text="IS_COLLECTED_BY",
        description="The resource is collected by another resource.",
        meaning=VOC4CAT["0005045"])
    COLLECTS = PermissibleValue(
        text="COLLECTS",
        description="The resource collects another resource.",
        meaning=VOC4CAT["0005046"])
    IS_REQUIRED_BY = PermissibleValue(
        text="IS_REQUIRED_BY",
        description="The resource is required by another resource.",
        meaning=VOC4CAT["0005047"])
    REQUIRES = PermissibleValue(
        text="REQUIRES",
        description="The resource requires another resource.",
        meaning=VOC4CAT["0005048"])
    IS_OBSOLETED_BY = PermissibleValue(
        text="IS_OBSOLETED_BY",
        description="The resource is obsoleted by another resource.",
        meaning=VOC4CAT["0005049"])
    OBSOLETES = PermissibleValue(
        text="OBSOLETES",
        description="The resource obsoletes another resource.",
        meaning=VOC4CAT["0005050"])

    _defn = EnumDefinition(
        name="RelationType",
        description="The type of relation between two resources referenced by their PIDs.",
    )

class PID4CatStatus(EnumDefinitionImpl):
    """
    The usage status of the PID4CatRecord.
    """
    SUBMITTED = PermissibleValue(
        text="SUBMITTED",
        description="The PID4CatRecord is reserved but the resource is not yet linked.",
        meaning=VOC4CAT["0005052"])
    REGISTERED = PermissibleValue(
        text="REGISTERED",
        description="The PID4CatRecord is linked to a concrete resource.",
        meaning=VOC4CAT["0005053"])
    OBSOLETED = PermissibleValue(
        text="OBSOLETED",
        description="The PID4CatRecord is obsolete, e.g. because the resource is referenced by another PID4Cat.",
        meaning=VOC4CAT["0005054"])
    DEPRECATED = PermissibleValue(
        text="DEPRECATED",
        description="The PID4CatRecord is deprecated, e.g. because the resource can no longer be found.",
        meaning=VOC4CAT["0005055"])

    _defn = EnumDefinition(
        name="PID4CatStatus",
        description="The usage status of the PID4CatRecord.",
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

class MEDIATypes(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="MEDIATypes",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "application/1d-interleaved-parityfec",
            PermissibleValue(text="application/1d-interleaved-parityfec"))
        setattr(cls, "application/3gpdash-qoe-report+xml",
            PermissibleValue(text="application/3gpdash-qoe-report+xml"))
        setattr(cls, "application/3gppHal+json",
            PermissibleValue(text="application/3gppHal+json"))
        setattr(cls, "application/3gppHalForms+json",
            PermissibleValue(text="application/3gppHalForms+json"))
        setattr(cls, "application/3gpp-ims+xml",
            PermissibleValue(text="application/3gpp-ims+xml"))
        setattr(cls, "application/A2L",
            PermissibleValue(text="application/A2L"))
        setattr(cls, "application/ace+cbor",
            PermissibleValue(text="application/ace+cbor"))
        setattr(cls, "application/ace+json",
            PermissibleValue(text="application/ace+json"))
        setattr(cls, "application/ace-groupcomm+cbor",
            PermissibleValue(text="application/ace-groupcomm+cbor"))
        setattr(cls, "application/ace-trl+cbor",
            PermissibleValue(text="application/ace-trl+cbor"))
        setattr(cls, "application/activemessage",
            PermissibleValue(text="application/activemessage"))
        setattr(cls, "application/activity+json",
            PermissibleValue(text="application/activity+json"))
        setattr(cls, "application/aif+cbor",
            PermissibleValue(text="application/aif+cbor"))
        setattr(cls, "application/aif+json",
            PermissibleValue(text="application/aif+json"))
        setattr(cls, "application/alto-cdni+json",
            PermissibleValue(text="application/alto-cdni+json"))
        setattr(cls, "application/alto-cdnifilter+json",
            PermissibleValue(text="application/alto-cdnifilter+json"))
        setattr(cls, "application/alto-costmap+json",
            PermissibleValue(text="application/alto-costmap+json"))
        setattr(cls, "application/alto-costmapfilter+json",
            PermissibleValue(text="application/alto-costmapfilter+json"))
        setattr(cls, "application/alto-directory+json",
            PermissibleValue(text="application/alto-directory+json"))
        setattr(cls, "application/alto-endpointcost+json",
            PermissibleValue(text="application/alto-endpointcost+json"))
        setattr(cls, "application/alto-endpointcostparams+json",
            PermissibleValue(text="application/alto-endpointcostparams+json"))
        setattr(cls, "application/alto-endpointprop+json",
            PermissibleValue(text="application/alto-endpointprop+json"))
        setattr(cls, "application/alto-endpointpropparams+json",
            PermissibleValue(text="application/alto-endpointpropparams+json"))
        setattr(cls, "application/alto-error+json",
            PermissibleValue(text="application/alto-error+json"))
        setattr(cls, "application/alto-networkmap+json",
            PermissibleValue(text="application/alto-networkmap+json"))
        setattr(cls, "application/alto-networkmapfilter+json",
            PermissibleValue(text="application/alto-networkmapfilter+json"))
        setattr(cls, "application/alto-propmap+json",
            PermissibleValue(text="application/alto-propmap+json"))
        setattr(cls, "application/alto-propmapparams+json",
            PermissibleValue(text="application/alto-propmapparams+json"))
        setattr(cls, "application/alto-tips+json",
            PermissibleValue(text="application/alto-tips+json"))
        setattr(cls, "application/alto-tipsparams+json",
            PermissibleValue(text="application/alto-tipsparams+json"))
        setattr(cls, "application/alto-updatestreamcontrol+json",
            PermissibleValue(text="application/alto-updatestreamcontrol+json"))
        setattr(cls, "application/alto-updatestreamparams+json",
            PermissibleValue(text="application/alto-updatestreamparams+json"))
        setattr(cls, "application/AML",
            PermissibleValue(text="application/AML"))
        setattr(cls, "application/andrew-inset",
            PermissibleValue(text="application/andrew-inset"))
        setattr(cls, "application/applefile",
            PermissibleValue(text="application/applefile"))
        setattr(cls, "application/at+jwt",
            PermissibleValue(text="application/at+jwt"))
        setattr(cls, "application/ATF",
            PermissibleValue(text="application/ATF"))
        setattr(cls, "application/ATFX",
            PermissibleValue(text="application/ATFX"))
        setattr(cls, "application/atom+xml",
            PermissibleValue(text="application/atom+xml"))
        setattr(cls, "application/atomcat+xml",
            PermissibleValue(text="application/atomcat+xml"))
        setattr(cls, "application/atomdeleted+xml",
            PermissibleValue(text="application/atomdeleted+xml"))
        setattr(cls, "application/atomicmail",
            PermissibleValue(text="application/atomicmail"))
        setattr(cls, "application/atomsvc+xml",
            PermissibleValue(text="application/atomsvc+xml"))
        setattr(cls, "application/atsc-dwd+xml",
            PermissibleValue(text="application/atsc-dwd+xml"))
        setattr(cls, "application/atsc-dynamic-event-message",
            PermissibleValue(text="application/atsc-dynamic-event-message"))
        setattr(cls, "application/atsc-held+xml",
            PermissibleValue(text="application/atsc-held+xml"))
        setattr(cls, "application/atsc-rdt+json",
            PermissibleValue(text="application/atsc-rdt+json"))
        setattr(cls, "application/atsc-rsat+xml",
            PermissibleValue(text="application/atsc-rsat+xml"))
        setattr(cls, "application/ATXML",
            PermissibleValue(text="application/ATXML"))
        setattr(cls, "application/auth-policy+xml",
            PermissibleValue(text="application/auth-policy+xml"))
        setattr(cls, "application/automationml-aml+xml",
            PermissibleValue(text="application/automationml-aml+xml"))
        setattr(cls, "application/automationml-amlx+zip",
            PermissibleValue(text="application/automationml-amlx+zip"))
        setattr(cls, "application/bacnet-xdd+zip",
            PermissibleValue(text="application/bacnet-xdd+zip"))
        setattr(cls, "application/batch-SMTP",
            PermissibleValue(text="application/batch-SMTP"))
        setattr(cls, "application/beep+xml",
            PermissibleValue(text="application/beep+xml"))
        setattr(cls, "application/bufr",
            PermissibleValue(text="application/bufr"))
        setattr(cls, "application/c2pa",
            PermissibleValue(text="application/c2pa"))
        setattr(cls, "application/calendar+json",
            PermissibleValue(text="application/calendar+json"))
        setattr(cls, "application/calendar+xml",
            PermissibleValue(text="application/calendar+xml"))
        setattr(cls, "application/call-completion",
            PermissibleValue(text="application/call-completion"))
        setattr(cls, "application/CALS-1840",
            PermissibleValue(text="application/CALS-1840"))
        setattr(cls, "application/captive+json",
            PermissibleValue(text="application/captive+json"))
        setattr(cls, "application/cbor",
            PermissibleValue(text="application/cbor"))
        setattr(cls, "application/cbor-seq",
            PermissibleValue(text="application/cbor-seq"))
        setattr(cls, "application/cccex",
            PermissibleValue(text="application/cccex"))
        setattr(cls, "application/ccmp+xml",
            PermissibleValue(text="application/ccmp+xml"))
        setattr(cls, "application/ccxml+xml",
            PermissibleValue(text="application/ccxml+xml"))
        setattr(cls, "application/cda+xml",
            PermissibleValue(text="application/cda+xml"))
        setattr(cls, "application/CDFX+XML",
            PermissibleValue(text="application/CDFX+XML"))
        setattr(cls, "application/cdmi-capability",
            PermissibleValue(text="application/cdmi-capability"))
        setattr(cls, "application/cdmi-container",
            PermissibleValue(text="application/cdmi-container"))
        setattr(cls, "application/cdmi-domain",
            PermissibleValue(text="application/cdmi-domain"))
        setattr(cls, "application/cdmi-object",
            PermissibleValue(text="application/cdmi-object"))
        setattr(cls, "application/cdmi-queue",
            PermissibleValue(text="application/cdmi-queue"))
        setattr(cls, "application/cdni",
            PermissibleValue(text="application/cdni"))
        setattr(cls, "application/ce+cbor",
            PermissibleValue(text="application/ce+cbor"))
        setattr(cls, "application/CEA",
            PermissibleValue(text="application/CEA"))
        setattr(cls, "application/cea-2018+xml",
            PermissibleValue(text="application/cea-2018+xml"))
        setattr(cls, "application/cellml+xml",
            PermissibleValue(text="application/cellml+xml"))
        setattr(cls, "application/cfw",
            PermissibleValue(text="application/cfw"))
        setattr(cls, "application/cid-edhoc+cbor-seq",
            PermissibleValue(text="application/cid-edhoc+cbor-seq"))
        setattr(cls, "application/city+json",
            PermissibleValue(text="application/city+json"))
        setattr(cls, "application/city+json-seq",
            PermissibleValue(text="application/city+json-seq"))
        setattr(cls, "application/clr",
            PermissibleValue(text="application/clr"))
        setattr(cls, "application/clue_info+xml",
            PermissibleValue(text="application/clue_info+xml"))
        setattr(cls, "application/clue+xml",
            PermissibleValue(text="application/clue+xml"))
        setattr(cls, "application/cms",
            PermissibleValue(text="application/cms"))
        setattr(cls, "application/cnrp+xml",
            PermissibleValue(text="application/cnrp+xml"))
        setattr(cls, "application/coap-group+json",
            PermissibleValue(text="application/coap-group+json"))
        setattr(cls, "application/coap-payload",
            PermissibleValue(text="application/coap-payload"))
        setattr(cls, "application/commonground",
            PermissibleValue(text="application/commonground"))
        setattr(cls, "application/concise-problem-details+cbor",
            PermissibleValue(text="application/concise-problem-details+cbor"))
        setattr(cls, "application/conference-info+xml",
            PermissibleValue(text="application/conference-info+xml"))
        setattr(cls, "application/cose",
            PermissibleValue(text="application/cose"))
        setattr(cls, "application/cose-key",
            PermissibleValue(text="application/cose-key"))
        setattr(cls, "application/cose-key-set",
            PermissibleValue(text="application/cose-key-set"))
        setattr(cls, "application/cose-x509",
            PermissibleValue(text="application/cose-x509"))
        setattr(cls, "application/cpl+xml",
            PermissibleValue(text="application/cpl+xml"))
        setattr(cls, "application/csrattrs",
            PermissibleValue(text="application/csrattrs"))
        setattr(cls, "application/csta+xml",
            PermissibleValue(text="application/csta+xml"))
        setattr(cls, "application/CSTAdata+xml",
            PermissibleValue(text="application/CSTAdata+xml"))
        setattr(cls, "application/csvm+json",
            PermissibleValue(text="application/csvm+json"))
        setattr(cls, "application/cwl",
            PermissibleValue(text="application/cwl"))
        setattr(cls, "application/cwl+json",
            PermissibleValue(text="application/cwl+json"))
        setattr(cls, "application/cwl+yaml",
            PermissibleValue(text="application/cwl+yaml"))
        setattr(cls, "application/cwt",
            PermissibleValue(text="application/cwt"))
        setattr(cls, "application/cybercash",
            PermissibleValue(text="application/cybercash"))
        setattr(cls, "application/dash+xml",
            PermissibleValue(text="application/dash+xml"))
        setattr(cls, "application/dashdelta",
            PermissibleValue(text="application/dashdelta"))
        setattr(cls, "application/dash-patch+xml",
            PermissibleValue(text="application/dash-patch+xml"))
        setattr(cls, "application/davmount+xml",
            PermissibleValue(text="application/davmount+xml"))
        setattr(cls, "application/dca-rft",
            PermissibleValue(text="application/dca-rft"))
        setattr(cls, "application/DCD",
            PermissibleValue(text="application/DCD"))
        setattr(cls, "application/dec-dx",
            PermissibleValue(text="application/dec-dx"))
        setattr(cls, "application/dialog-info+xml",
            PermissibleValue(text="application/dialog-info+xml"))
        setattr(cls, "application/dicom",
            PermissibleValue(text="application/dicom"))
        setattr(cls, "application/dicom+json",
            PermissibleValue(text="application/dicom+json"))
        setattr(cls, "application/dicom+xml",
            PermissibleValue(text="application/dicom+xml"))
        setattr(cls, "application/DII",
            PermissibleValue(text="application/DII"))
        setattr(cls, "application/DIT",
            PermissibleValue(text="application/DIT"))
        setattr(cls, "application/dns",
            PermissibleValue(text="application/dns"))
        setattr(cls, "application/dns+json",
            PermissibleValue(text="application/dns+json"))
        setattr(cls, "application/dns-message",
            PermissibleValue(text="application/dns-message"))
        setattr(cls, "application/dots+cbor",
            PermissibleValue(text="application/dots+cbor"))
        setattr(cls, "application/dpop+jwt",
            PermissibleValue(text="application/dpop+jwt"))
        setattr(cls, "application/dskpp+xml",
            PermissibleValue(text="application/dskpp+xml"))
        setattr(cls, "application/dssc+der",
            PermissibleValue(text="application/dssc+der"))
        setattr(cls, "application/dssc+xml",
            PermissibleValue(text="application/dssc+xml"))
        setattr(cls, "application/dvcs",
            PermissibleValue(text="application/dvcs"))
        setattr(cls, "application/eat+cwt",
            PermissibleValue(text="application/eat+cwt"))
        setattr(cls, "application/eat+jwt",
            PermissibleValue(text="application/eat+jwt"))
        setattr(cls, "application/eat-bun+cbor",
            PermissibleValue(text="application/eat-bun+cbor"))
        setattr(cls, "application/eat-bun+json",
            PermissibleValue(text="application/eat-bun+json"))
        setattr(cls, "application/eat-ucs+cbor",
            PermissibleValue(text="application/eat-ucs+cbor"))
        setattr(cls, "application/eat-ucs+json",
            PermissibleValue(text="application/eat-ucs+json"))
        setattr(cls, "application/ecmascript",
            PermissibleValue(text="application/ecmascript"))
        setattr(cls, "application/edhoc+cbor-seq",
            PermissibleValue(text="application/edhoc+cbor-seq"))
        setattr(cls, "application/EDI-consent",
            PermissibleValue(text="application/EDI-consent"))
        setattr(cls, "application/EDIFACT",
            PermissibleValue(text="application/EDIFACT"))
        setattr(cls, "application/EDI-X12",
            PermissibleValue(text="application/EDI-X12"))
        setattr(cls, "application/efi",
            PermissibleValue(text="application/efi"))
        setattr(cls, "application/elm+json",
            PermissibleValue(text="application/elm+json"))
        setattr(cls, "application/elm+xml",
            PermissibleValue(text="application/elm+xml"))
        setattr(cls, "application/EmergencyCallData.cap+xml",
            PermissibleValue(text="application/EmergencyCallData.cap+xml"))
        setattr(cls, "application/EmergencyCallData.Comment+xml",
            PermissibleValue(text="application/EmergencyCallData.Comment+xml"))
        setattr(cls, "application/EmergencyCallData.Control+xml",
            PermissibleValue(text="application/EmergencyCallData.Control+xml"))
        setattr(cls, "application/EmergencyCallData.DeviceInfo+xml",
            PermissibleValue(text="application/EmergencyCallData.DeviceInfo+xml"))
        setattr(cls, "application/EmergencyCallData.eCall.MSD",
            PermissibleValue(text="application/EmergencyCallData.eCall.MSD"))
        setattr(cls, "application/EmergencyCallData.LegacyESN+json",
            PermissibleValue(text="application/EmergencyCallData.LegacyESN+json"))
        setattr(cls, "application/EmergencyCallData.ProviderInfo+xml",
            PermissibleValue(text="application/EmergencyCallData.ProviderInfo+xml"))
        setattr(cls, "application/EmergencyCallData.ServiceInfo+xml",
            PermissibleValue(text="application/EmergencyCallData.ServiceInfo+xml"))
        setattr(cls, "application/EmergencyCallData.SubscriberInfo+xml",
            PermissibleValue(text="application/EmergencyCallData.SubscriberInfo+xml"))
        setattr(cls, "application/EmergencyCallData.VEDS+xml",
            PermissibleValue(text="application/EmergencyCallData.VEDS+xml"))
        setattr(cls, "application/emma+xml",
            PermissibleValue(text="application/emma+xml"))
        setattr(cls, "application/emotionml+xml",
            PermissibleValue(text="application/emotionml+xml"))
        setattr(cls, "application/encaprtp",
            PermissibleValue(text="application/encaprtp"))
        setattr(cls, "application/entity-statement+jwt",
            PermissibleValue(text="application/entity-statement+jwt"))
        setattr(cls, "application/epp+xml",
            PermissibleValue(text="application/epp+xml"))
        setattr(cls, "application/epub+zip",
            PermissibleValue(text="application/epub+zip"))
        setattr(cls, "application/eshop",
            PermissibleValue(text="application/eshop"))
        setattr(cls, "application/example",
            PermissibleValue(text="application/example"))
        setattr(cls, "application/exi",
            PermissibleValue(text="application/exi"))
        setattr(cls, "application/expect-ct-report+json",
            PermissibleValue(text="application/expect-ct-report+json"))
        setattr(cls, "application/express",
            PermissibleValue(text="application/express"))
        setattr(cls, "application/fastinfoset",
            PermissibleValue(text="application/fastinfoset"))
        setattr(cls, "application/fastsoap",
            PermissibleValue(text="application/fastsoap"))
        setattr(cls, "application/fdf",
            PermissibleValue(text="application/fdf"))
        setattr(cls, "application/fdt+xml",
            PermissibleValue(text="application/fdt+xml"))
        setattr(cls, "application/fhir+json",
            PermissibleValue(text="application/fhir+json"))
        setattr(cls, "application/fhir+xml",
            PermissibleValue(text="application/fhir+xml"))
        setattr(cls, "application/fits",
            PermissibleValue(text="application/fits"))
        setattr(cls, "application/flexfec",
            PermissibleValue(text="application/flexfec"))
        setattr(cls, "application/font-sfnt",
            PermissibleValue(text="application/font-sfnt"))
        setattr(cls, "application/font-tdpfr",
            PermissibleValue(text="application/font-tdpfr"))
        setattr(cls, "application/font-woff",
            PermissibleValue(text="application/font-woff"))
        setattr(cls, "application/framework-attributes+xml",
            PermissibleValue(text="application/framework-attributes+xml"))
        setattr(cls, "application/geo+json",
            PermissibleValue(text="application/geo+json"))
        setattr(cls, "application/geo+json-seq",
            PermissibleValue(text="application/geo+json-seq"))
        setattr(cls, "application/geopackage+sqlite3",
            PermissibleValue(text="application/geopackage+sqlite3"))
        setattr(cls, "application/geopose+json",
            PermissibleValue(text="application/geopose+json"))
        setattr(cls, "application/geoxacml+json",
            PermissibleValue(text="application/geoxacml+json"))
        setattr(cls, "application/geoxacml+xml",
            PermissibleValue(text="application/geoxacml+xml"))
        setattr(cls, "application/gltf-buffer",
            PermissibleValue(text="application/gltf-buffer"))
        setattr(cls, "application/gml+xml",
            PermissibleValue(text="application/gml+xml"))
        setattr(cls, "application/gnap-binding-jws",
            PermissibleValue(text="application/gnap-binding-jws"))
        setattr(cls, "application/gnap-binding-jwsd",
            PermissibleValue(text="application/gnap-binding-jwsd"))
        setattr(cls, "application/gnap-binding-rotation-jws",
            PermissibleValue(text="application/gnap-binding-rotation-jws"))
        setattr(cls, "application/gnap-binding-rotation-jwsd",
            PermissibleValue(text="application/gnap-binding-rotation-jwsd"))
        setattr(cls, "application/grib",
            PermissibleValue(text="application/grib"))
        setattr(cls, "application/gzip",
            PermissibleValue(text="application/gzip"))
        setattr(cls, "application/H224",
            PermissibleValue(text="application/H224"))
        setattr(cls, "application/held+xml",
            PermissibleValue(text="application/held+xml"))
        setattr(cls, "application/hl7v2+xml",
            PermissibleValue(text="application/hl7v2+xml"))
        setattr(cls, "application/http",
            PermissibleValue(text="application/http"))
        setattr(cls, "application/hyperstudio",
            PermissibleValue(text="application/hyperstudio"))
        setattr(cls, "application/ibe-key-request+xml",
            PermissibleValue(text="application/ibe-key-request+xml"))
        setattr(cls, "application/ibe-pkg-reply+xml",
            PermissibleValue(text="application/ibe-pkg-reply+xml"))
        setattr(cls, "application/ibe-pp-data",
            PermissibleValue(text="application/ibe-pp-data"))
        setattr(cls, "application/iges",
            PermissibleValue(text="application/iges"))
        setattr(cls, "application/im-iscomposing+xml",
            PermissibleValue(text="application/im-iscomposing+xml"))
        setattr(cls, "application/index",
            PermissibleValue(text="application/index"))
        setattr(cls, "application/index.cmd",
            PermissibleValue(text="application/index.cmd"))
        setattr(cls, "application/index.obj",
            PermissibleValue(text="application/index.obj"))
        setattr(cls, "application/index.response",
            PermissibleValue(text="application/index.response"))
        setattr(cls, "application/index.vnd",
            PermissibleValue(text="application/index.vnd"))
        setattr(cls, "application/inkml+xml",
            PermissibleValue(text="application/inkml+xml"))
        setattr(cls, "application/IOTP",
            PermissibleValue(text="application/IOTP"))
        setattr(cls, "application/ipfix",
            PermissibleValue(text="application/ipfix"))
        setattr(cls, "application/ipp",
            PermissibleValue(text="application/ipp"))
        setattr(cls, "application/ISUP",
            PermissibleValue(text="application/ISUP"))
        setattr(cls, "application/its+xml",
            PermissibleValue(text="application/its+xml"))
        setattr(cls, "application/java-archive",
            PermissibleValue(text="application/java-archive"))
        setattr(cls, "application/javascript",
            PermissibleValue(text="application/javascript"))
        setattr(cls, "application/jf2feed+json",
            PermissibleValue(text="application/jf2feed+json"))
        setattr(cls, "application/jose",
            PermissibleValue(text="application/jose"))
        setattr(cls, "application/jose+json",
            PermissibleValue(text="application/jose+json"))
        setattr(cls, "application/jrd+json",
            PermissibleValue(text="application/jrd+json"))
        setattr(cls, "application/jscalendar+json",
            PermissibleValue(text="application/jscalendar+json"))
        setattr(cls, "application/jscontact+json",
            PermissibleValue(text="application/jscontact+json"))
        setattr(cls, "application/json",
            PermissibleValue(text="application/json"))
        setattr(cls, "application/json-patch+json",
            PermissibleValue(text="application/json-patch+json"))
        setattr(cls, "application/jsonpath",
            PermissibleValue(text="application/jsonpath"))
        setattr(cls, "application/json-seq",
            PermissibleValue(text="application/json-seq"))
        setattr(cls, "application/jwk+json",
            PermissibleValue(text="application/jwk+json"))
        setattr(cls, "application/jwk-set+json",
            PermissibleValue(text="application/jwk-set+json"))
        setattr(cls, "application/jwk-set+jwt",
            PermissibleValue(text="application/jwk-set+jwt"))
        setattr(cls, "application/jwt",
            PermissibleValue(text="application/jwt"))
        setattr(cls, "application/kpml-request+xml",
            PermissibleValue(text="application/kpml-request+xml"))
        setattr(cls, "application/kpml-response+xml",
            PermissibleValue(text="application/kpml-response+xml"))
        setattr(cls, "application/ld+json",
            PermissibleValue(text="application/ld+json"))
        setattr(cls, "application/lgr+xml",
            PermissibleValue(text="application/lgr+xml"))
        setattr(cls, "application/link-format",
            PermissibleValue(text="application/link-format"))
        setattr(cls, "application/linkset",
            PermissibleValue(text="application/linkset"))
        setattr(cls, "application/linkset+json",
            PermissibleValue(text="application/linkset+json"))
        setattr(cls, "application/load-control+xml",
            PermissibleValue(text="application/load-control+xml"))
        setattr(cls, "application/logout+jwt",
            PermissibleValue(text="application/logout+jwt"))
        setattr(cls, "application/lost+xml",
            PermissibleValue(text="application/lost+xml"))
        setattr(cls, "application/lostsync+xml",
            PermissibleValue(text="application/lostsync+xml"))
        setattr(cls, "application/lpf+zip",
            PermissibleValue(text="application/lpf+zip"))
        setattr(cls, "application/LXF",
            PermissibleValue(text="application/LXF"))
        setattr(cls, "application/mac-binhex40",
            PermissibleValue(text="application/mac-binhex40"))
        setattr(cls, "application/macwriteii",
            PermissibleValue(text="application/macwriteii"))
        setattr(cls, "application/mads+xml",
            PermissibleValue(text="application/mads+xml"))
        setattr(cls, "application/manifest+json",
            PermissibleValue(text="application/manifest+json"))
        setattr(cls, "application/marc",
            PermissibleValue(text="application/marc"))
        setattr(cls, "application/marcxml+xml",
            PermissibleValue(text="application/marcxml+xml"))
        setattr(cls, "application/mathematica",
            PermissibleValue(text="application/mathematica"))
        setattr(cls, "application/mathml+xml",
            PermissibleValue(text="application/mathml+xml"))
        setattr(cls, "application/mathml-content+xml",
            PermissibleValue(text="application/mathml-content+xml"))
        setattr(cls, "application/mathml-presentation+xml",
            PermissibleValue(text="application/mathml-presentation+xml"))
        setattr(cls, "application/mbms-associated-procedure-description+xml",
            PermissibleValue(text="application/mbms-associated-procedure-description+xml"))
        setattr(cls, "application/mbms-deregister+xml",
            PermissibleValue(text="application/mbms-deregister+xml"))
        setattr(cls, "application/mbms-envelope+xml",
            PermissibleValue(text="application/mbms-envelope+xml"))
        setattr(cls, "application/mbms-msk+xml",
            PermissibleValue(text="application/mbms-msk+xml"))
        setattr(cls, "application/mbms-msk-response+xml",
            PermissibleValue(text="application/mbms-msk-response+xml"))
        setattr(cls, "application/mbms-protection-description+xml",
            PermissibleValue(text="application/mbms-protection-description+xml"))
        setattr(cls, "application/mbms-reception-report+xml",
            PermissibleValue(text="application/mbms-reception-report+xml"))
        setattr(cls, "application/mbms-register+xml",
            PermissibleValue(text="application/mbms-register+xml"))
        setattr(cls, "application/mbms-register-response+xml",
            PermissibleValue(text="application/mbms-register-response+xml"))
        setattr(cls, "application/mbms-schedule+xml",
            PermissibleValue(text="application/mbms-schedule+xml"))
        setattr(cls, "application/mbms-user-service-description+xml",
            PermissibleValue(text="application/mbms-user-service-description+xml"))
        setattr(cls, "application/mbox",
            PermissibleValue(text="application/mbox"))
        setattr(cls, "application/media_control+xml",
            PermissibleValue(text="application/media_control+xml"))
        setattr(cls, "application/media-policy-dataset+xml",
            PermissibleValue(text="application/media-policy-dataset+xml"))
        setattr(cls, "application/mediaservercontrol+xml",
            PermissibleValue(text="application/mediaservercontrol+xml"))
        setattr(cls, "application/merge-patch+json",
            PermissibleValue(text="application/merge-patch+json"))
        setattr(cls, "application/metalink4+xml",
            PermissibleValue(text="application/metalink4+xml"))
        setattr(cls, "application/mets+xml",
            PermissibleValue(text="application/mets+xml"))
        setattr(cls, "application/MF4",
            PermissibleValue(text="application/MF4"))
        setattr(cls, "application/mikey",
            PermissibleValue(text="application/mikey"))
        setattr(cls, "application/mipc",
            PermissibleValue(text="application/mipc"))
        setattr(cls, "application/missing-blocks+cbor-seq",
            PermissibleValue(text="application/missing-blocks+cbor-seq"))
        setattr(cls, "application/mmt-aei+xml",
            PermissibleValue(text="application/mmt-aei+xml"))
        setattr(cls, "application/mmt-usd+xml",
            PermissibleValue(text="application/mmt-usd+xml"))
        setattr(cls, "application/mods+xml",
            PermissibleValue(text="application/mods+xml"))
        setattr(cls, "application/mosskey-data",
            PermissibleValue(text="application/mosskey-data"))
        setattr(cls, "application/mosskey-request",
            PermissibleValue(text="application/mosskey-request"))
        setattr(cls, "application/moss-keys",
            PermissibleValue(text="application/moss-keys"))
        setattr(cls, "application/moss-signature",
            PermissibleValue(text="application/moss-signature"))
        setattr(cls, "application/mp21",
            PermissibleValue(text="application/mp21"))
        setattr(cls, "application/mp4",
            PermissibleValue(text="application/mp4"))
        setattr(cls, "application/mpeg4-generic",
            PermissibleValue(text="application/mpeg4-generic"))
        setattr(cls, "application/mpeg4-iod",
            PermissibleValue(text="application/mpeg4-iod"))
        setattr(cls, "application/mpeg4-iod-xmt",
            PermissibleValue(text="application/mpeg4-iod-xmt"))
        setattr(cls, "application/mrb-consumer+xml",
            PermissibleValue(text="application/mrb-consumer+xml"))
        setattr(cls, "application/mrb-publish+xml",
            PermissibleValue(text="application/mrb-publish+xml"))
        setattr(cls, "application/msc-ivr+xml",
            PermissibleValue(text="application/msc-ivr+xml"))
        setattr(cls, "application/msc-mixer+xml",
            PermissibleValue(text="application/msc-mixer+xml"))
        setattr(cls, "application/msword",
            PermissibleValue(text="application/msword"))
        setattr(cls, "application/mud+json",
            PermissibleValue(text="application/mud+json"))
        setattr(cls, "application/multipart-core",
            PermissibleValue(text="application/multipart-core"))
        setattr(cls, "application/mxf",
            PermissibleValue(text="application/mxf"))
        setattr(cls, "application/nasdata",
            PermissibleValue(text="application/nasdata"))
        setattr(cls, "application/news-checkgroups",
            PermissibleValue(text="application/news-checkgroups"))
        setattr(cls, "application/news-groupinfo",
            PermissibleValue(text="application/news-groupinfo"))
        setattr(cls, "application/news-transmission",
            PermissibleValue(text="application/news-transmission"))
        setattr(cls, "application/nlsml+xml",
            PermissibleValue(text="application/nlsml+xml"))
        setattr(cls, "application/node",
            PermissibleValue(text="application/node"))
        setattr(cls, "application/n-quads",
            PermissibleValue(text="application/n-quads"))
        setattr(cls, "application/nss",
            PermissibleValue(text="application/nss"))
        setattr(cls, "application/n-triples",
            PermissibleValue(text="application/n-triples"))
        setattr(cls, "application/oauth-authz-req+jwt",
            PermissibleValue(text="application/oauth-authz-req+jwt"))
        setattr(cls, "application/oblivious-dns-message",
            PermissibleValue(text="application/oblivious-dns-message"))
        setattr(cls, "application/ocsp-request",
            PermissibleValue(text="application/ocsp-request"))
        setattr(cls, "application/ocsp-response",
            PermissibleValue(text="application/ocsp-response"))
        setattr(cls, "application/octet-stream",
            PermissibleValue(text="application/octet-stream"))
        setattr(cls, "application/ODA",
            PermissibleValue(text="application/ODA"))
        setattr(cls, "application/odm+xml",
            PermissibleValue(text="application/odm+xml"))
        setattr(cls, "application/ODX",
            PermissibleValue(text="application/ODX"))
        setattr(cls, "application/oebps-package+xml",
            PermissibleValue(text="application/oebps-package+xml"))
        setattr(cls, "application/ogg",
            PermissibleValue(text="application/ogg"))
        setattr(cls, "application/ohttp-keys",
            PermissibleValue(text="application/ohttp-keys"))
        setattr(cls, "application/opc-nodeset+xml",
            PermissibleValue(text="application/opc-nodeset+xml"))
        setattr(cls, "application/oscore",
            PermissibleValue(text="application/oscore"))
        setattr(cls, "application/oxps",
            PermissibleValue(text="application/oxps"))
        setattr(cls, "application/p21",
            PermissibleValue(text="application/p21"))
        setattr(cls, "application/p21+zip",
            PermissibleValue(text="application/p21+zip"))
        setattr(cls, "application/p2p-overlay+xml",
            PermissibleValue(text="application/p2p-overlay+xml"))
        setattr(cls, "application/parityfec",
            PermissibleValue(text="application/parityfec"))
        setattr(cls, "application/passport",
            PermissibleValue(text="application/passport"))
        setattr(cls, "application/patch-ops-error+xml",
            PermissibleValue(text="application/patch-ops-error+xml"))
        setattr(cls, "application/pdf",
            PermissibleValue(text="application/pdf"))
        setattr(cls, "application/PDX",
            PermissibleValue(text="application/PDX"))
        setattr(cls, "application/pem-certificate-chain",
            PermissibleValue(text="application/pem-certificate-chain"))
        setattr(cls, "application/pgp-encrypted",
            PermissibleValue(text="application/pgp-encrypted"))
        setattr(cls, "application/pgp-keys",
            PermissibleValue(text="application/pgp-keys"))
        setattr(cls, "application/pgp-signature",
            PermissibleValue(text="application/pgp-signature"))
        setattr(cls, "application/pidf+xml",
            PermissibleValue(text="application/pidf+xml"))
        setattr(cls, "application/pidf-diff+xml",
            PermissibleValue(text="application/pidf-diff+xml"))
        setattr(cls, "application/pkcs10",
            PermissibleValue(text="application/pkcs10"))
        setattr(cls, "application/pkcs12",
            PermissibleValue(text="application/pkcs12"))
        setattr(cls, "application/pkcs7-mime",
            PermissibleValue(text="application/pkcs7-mime"))
        setattr(cls, "application/pkcs7-signature",
            PermissibleValue(text="application/pkcs7-signature"))
        setattr(cls, "application/pkcs8",
            PermissibleValue(text="application/pkcs8"))
        setattr(cls, "application/pkcs8-encrypted",
            PermissibleValue(text="application/pkcs8-encrypted"))
        setattr(cls, "application/pkix-attr-cert",
            PermissibleValue(text="application/pkix-attr-cert"))
        setattr(cls, "application/pkix-cert",
            PermissibleValue(text="application/pkix-cert"))
        setattr(cls, "application/pkixcmp",
            PermissibleValue(text="application/pkixcmp"))
        setattr(cls, "application/pkix-crl",
            PermissibleValue(text="application/pkix-crl"))
        setattr(cls, "application/pkix-pkipath",
            PermissibleValue(text="application/pkix-pkipath"))
        setattr(cls, "application/pls+xml",
            PermissibleValue(text="application/pls+xml"))
        setattr(cls, "application/poc-settings+xml",
            PermissibleValue(text="application/poc-settings+xml"))
        setattr(cls, "application/postscript",
            PermissibleValue(text="application/postscript"))
        setattr(cls, "application/ppsp-tracker+json",
            PermissibleValue(text="application/ppsp-tracker+json"))
        setattr(cls, "application/private-token-issuer-directory",
            PermissibleValue(text="application/private-token-issuer-directory"))
        setattr(cls, "application/private-token-request",
            PermissibleValue(text="application/private-token-request"))
        setattr(cls, "application/private-token-response",
            PermissibleValue(text="application/private-token-response"))
        setattr(cls, "application/problem+json",
            PermissibleValue(text="application/problem+json"))
        setattr(cls, "application/problem+xml",
            PermissibleValue(text="application/problem+xml"))
        setattr(cls, "application/provenance+xml",
            PermissibleValue(text="application/provenance+xml"))
        setattr(cls, "application/provided-claims+jwt",
            PermissibleValue(text="application/provided-claims+jwt"))
        setattr(cls, "application/prs.alvestrand.titrax-sheet",
            PermissibleValue(text="application/prs.alvestrand.titrax-sheet"))
        setattr(cls, "application/prs.cww",
            PermissibleValue(text="application/prs.cww"))
        setattr(cls, "application/prs.cyn",
            PermissibleValue(text="application/prs.cyn"))
        setattr(cls, "application/prs.hpub+zip",
            PermissibleValue(text="application/prs.hpub+zip"))
        setattr(cls, "application/prs.implied-document+xml",
            PermissibleValue(text="application/prs.implied-document+xml"))
        setattr(cls, "application/prs.implied-executable",
            PermissibleValue(text="application/prs.implied-executable"))
        setattr(cls, "application/prs.implied-object+json",
            PermissibleValue(text="application/prs.implied-object+json"))
        setattr(cls, "application/prs.implied-object+json-seq",
            PermissibleValue(text="application/prs.implied-object+json-seq"))
        setattr(cls, "application/prs.implied-object+yaml",
            PermissibleValue(text="application/prs.implied-object+yaml"))
        setattr(cls, "application/prs.implied-structure",
            PermissibleValue(text="application/prs.implied-structure"))
        setattr(cls, "application/prs.mayfile",
            PermissibleValue(text="application/prs.mayfile"))
        setattr(cls, "application/prs.nprend",
            PermissibleValue(text="application/prs.nprend"))
        setattr(cls, "application/prs.plucker",
            PermissibleValue(text="application/prs.plucker"))
        setattr(cls, "application/prs.rdf-xml-crypt",
            PermissibleValue(text="application/prs.rdf-xml-crypt"))
        setattr(cls, "application/prs.vcfbzip2",
            PermissibleValue(text="application/prs.vcfbzip2"))
        setattr(cls, "application/prs.xsf+xml",
            PermissibleValue(text="application/prs.xsf+xml"))
        setattr(cls, "application/pskc+xml",
            PermissibleValue(text="application/pskc+xml"))
        setattr(cls, "application/pvd+json",
            PermissibleValue(text="application/pvd+json"))
        setattr(cls, "application/QSIG",
            PermissibleValue(text="application/QSIG"))
        setattr(cls, "application/raptorfec",
            PermissibleValue(text="application/raptorfec"))
        setattr(cls, "application/rdap+json",
            PermissibleValue(text="application/rdap+json"))
        setattr(cls, "application/rdf+xml",
            PermissibleValue(text="application/rdf+xml"))
        setattr(cls, "application/reginfo+xml",
            PermissibleValue(text="application/reginfo+xml"))
        setattr(cls, "application/relax-ng-compact-syntax",
            PermissibleValue(text="application/relax-ng-compact-syntax"))
        setattr(cls, "application/remote-printing",
            PermissibleValue(text="application/remote-printing"))
        setattr(cls, "application/reputon+json",
            PermissibleValue(text="application/reputon+json"))
        setattr(cls, "application/resolve-response+jwt",
            PermissibleValue(text="application/resolve-response+jwt"))
        setattr(cls, "application/resource-lists+xml",
            PermissibleValue(text="application/resource-lists+xml"))
        setattr(cls, "application/resource-lists-diff+xml",
            PermissibleValue(text="application/resource-lists-diff+xml"))
        setattr(cls, "application/rfc+xml",
            PermissibleValue(text="application/rfc+xml"))
        setattr(cls, "application/riscos",
            PermissibleValue(text="application/riscos"))
        setattr(cls, "application/rlmi+xml",
            PermissibleValue(text="application/rlmi+xml"))
        setattr(cls, "application/rls-services+xml",
            PermissibleValue(text="application/rls-services+xml"))
        setattr(cls, "application/route-apd+xml",
            PermissibleValue(text="application/route-apd+xml"))
        setattr(cls, "application/route-s-tsid+xml",
            PermissibleValue(text="application/route-s-tsid+xml"))
        setattr(cls, "application/route-usd+xml",
            PermissibleValue(text="application/route-usd+xml"))
        setattr(cls, "application/rpki-checklist",
            PermissibleValue(text="application/rpki-checklist"))
        setattr(cls, "application/rpki-ghostbusters",
            PermissibleValue(text="application/rpki-ghostbusters"))
        setattr(cls, "application/rpki-manifest",
            PermissibleValue(text="application/rpki-manifest"))
        setattr(cls, "application/rpki-publication",
            PermissibleValue(text="application/rpki-publication"))
        setattr(cls, "application/rpki-roa",
            PermissibleValue(text="application/rpki-roa"))
        setattr(cls, "application/rpki-signed-tal",
            PermissibleValue(text="application/rpki-signed-tal"))
        setattr(cls, "application/rpki-updown",
            PermissibleValue(text="application/rpki-updown"))
        setattr(cls, "application/rtf",
            PermissibleValue(text="application/rtf"))
        setattr(cls, "application/rtploopback",
            PermissibleValue(text="application/rtploopback"))
        setattr(cls, "application/rtx",
            PermissibleValue(text="application/rtx"))
        setattr(cls, "application/samlassertion+xml",
            PermissibleValue(text="application/samlassertion+xml"))
        setattr(cls, "application/samlmetadata+xml",
            PermissibleValue(text="application/samlmetadata+xml"))
        setattr(cls, "application/sarif+json",
            PermissibleValue(text="application/sarif+json"))
        setattr(cls, "application/sarif-external-properties+json",
            PermissibleValue(text="application/sarif-external-properties+json"))
        setattr(cls, "application/sbe",
            PermissibleValue(text="application/sbe"))
        setattr(cls, "application/sbml+xml",
            PermissibleValue(text="application/sbml+xml"))
        setattr(cls, "application/scaip+xml",
            PermissibleValue(text="application/scaip+xml"))
        setattr(cls, "application/scim+json",
            PermissibleValue(text="application/scim+json"))
        setattr(cls, "application/scvp-cv-request",
            PermissibleValue(text="application/scvp-cv-request"))
        setattr(cls, "application/scvp-cv-response",
            PermissibleValue(text="application/scvp-cv-response"))
        setattr(cls, "application/scvp-vp-request",
            PermissibleValue(text="application/scvp-vp-request"))
        setattr(cls, "application/scvp-vp-response",
            PermissibleValue(text="application/scvp-vp-response"))
        setattr(cls, "application/sdp",
            PermissibleValue(text="application/sdp"))
        setattr(cls, "application/secevent+jwt",
            PermissibleValue(text="application/secevent+jwt"))
        setattr(cls, "application/senml+cbor",
            PermissibleValue(text="application/senml+cbor"))
        setattr(cls, "application/senml+json",
            PermissibleValue(text="application/senml+json"))
        setattr(cls, "application/senml+xml",
            PermissibleValue(text="application/senml+xml"))
        setattr(cls, "application/senml-etch+cbor",
            PermissibleValue(text="application/senml-etch+cbor"))
        setattr(cls, "application/senml-etch+json",
            PermissibleValue(text="application/senml-etch+json"))
        setattr(cls, "application/senml-exi",
            PermissibleValue(text="application/senml-exi"))
        setattr(cls, "application/sensml+cbor",
            PermissibleValue(text="application/sensml+cbor"))
        setattr(cls, "application/sensml+json",
            PermissibleValue(text="application/sensml+json"))
        setattr(cls, "application/sensml+xml",
            PermissibleValue(text="application/sensml+xml"))
        setattr(cls, "application/sensml-exi",
            PermissibleValue(text="application/sensml-exi"))
        setattr(cls, "application/sep+xml",
            PermissibleValue(text="application/sep+xml"))
        setattr(cls, "application/sep-exi",
            PermissibleValue(text="application/sep-exi"))
        setattr(cls, "application/session-info",
            PermissibleValue(text="application/session-info"))
        setattr(cls, "application/set-payment",
            PermissibleValue(text="application/set-payment"))
        setattr(cls, "application/set-payment-initiation",
            PermissibleValue(text="application/set-payment-initiation"))
        setattr(cls, "application/set-registration",
            PermissibleValue(text="application/set-registration"))
        setattr(cls, "application/set-registration-initiation",
            PermissibleValue(text="application/set-registration-initiation"))
        setattr(cls, "application/SGML",
            PermissibleValue(text="application/SGML"))
        setattr(cls, "application/sgml-open-catalog",
            PermissibleValue(text="application/sgml-open-catalog"))
        setattr(cls, "application/shf+xml",
            PermissibleValue(text="application/shf+xml"))
        setattr(cls, "application/sieve",
            PermissibleValue(text="application/sieve"))
        setattr(cls, "application/simple-filter+xml",
            PermissibleValue(text="application/simple-filter+xml"))
        setattr(cls, "application/simple-message-summary",
            PermissibleValue(text="application/simple-message-summary"))
        setattr(cls, "application/simpleSymbolContainer",
            PermissibleValue(text="application/simpleSymbolContainer"))
        setattr(cls, "application/sipc",
            PermissibleValue(text="application/sipc"))
        setattr(cls, "application/slate",
            PermissibleValue(text="application/slate"))
        setattr(cls, "application/smil",
            PermissibleValue(text="application/smil"))
        setattr(cls, "application/smil+xml",
            PermissibleValue(text="application/smil+xml"))
        setattr(cls, "application/smpte336m",
            PermissibleValue(text="application/smpte336m"))
        setattr(cls, "application/soap+fastinfoset",
            PermissibleValue(text="application/soap+fastinfoset"))
        setattr(cls, "application/soap+xml",
            PermissibleValue(text="application/soap+xml"))
        setattr(cls, "application/sparql-query",
            PermissibleValue(text="application/sparql-query"))
        setattr(cls, "application/sparql-results+xml",
            PermissibleValue(text="application/sparql-results+xml"))
        setattr(cls, "application/spdx+json",
            PermissibleValue(text="application/spdx+json"))
        setattr(cls, "application/spirits-event+xml",
            PermissibleValue(text="application/spirits-event+xml"))
        setattr(cls, "application/sql",
            PermissibleValue(text="application/sql"))
        setattr(cls, "application/srgs",
            PermissibleValue(text="application/srgs"))
        setattr(cls, "application/srgs+xml",
            PermissibleValue(text="application/srgs+xml"))
        setattr(cls, "application/sru+xml",
            PermissibleValue(text="application/sru+xml"))
        setattr(cls, "application/sslkeylogfile",
            PermissibleValue(text="application/sslkeylogfile"))
        setattr(cls, "application/ssml+xml",
            PermissibleValue(text="application/ssml+xml"))
        setattr(cls, "application/ST2110-41",
            PermissibleValue(text="application/ST2110-41"))
        setattr(cls, "application/stix+json",
            PermissibleValue(text="application/stix+json"))
        setattr(cls, "application/stratum",
            PermissibleValue(text="application/stratum"))
        setattr(cls, "application/swid+cbor",
            PermissibleValue(text="application/swid+cbor"))
        setattr(cls, "application/swid+xml",
            PermissibleValue(text="application/swid+xml"))
        setattr(cls, "application/tamp-apex-update",
            PermissibleValue(text="application/tamp-apex-update"))
        setattr(cls, "application/tamp-apex-update-confirm",
            PermissibleValue(text="application/tamp-apex-update-confirm"))
        setattr(cls, "application/tamp-community-update",
            PermissibleValue(text="application/tamp-community-update"))
        setattr(cls, "application/tamp-community-update-confirm",
            PermissibleValue(text="application/tamp-community-update-confirm"))
        setattr(cls, "application/tamp-error",
            PermissibleValue(text="application/tamp-error"))
        setattr(cls, "application/tamp-sequence-adjust",
            PermissibleValue(text="application/tamp-sequence-adjust"))
        setattr(cls, "application/tamp-sequence-adjust-confirm",
            PermissibleValue(text="application/tamp-sequence-adjust-confirm"))
        setattr(cls, "application/tamp-status-query",
            PermissibleValue(text="application/tamp-status-query"))
        setattr(cls, "application/tamp-status-response",
            PermissibleValue(text="application/tamp-status-response"))
        setattr(cls, "application/tamp-update",
            PermissibleValue(text="application/tamp-update"))
        setattr(cls, "application/tamp-update-confirm",
            PermissibleValue(text="application/tamp-update-confirm"))
        setattr(cls, "application/taxii+json",
            PermissibleValue(text="application/taxii+json"))
        setattr(cls, "application/td+json",
            PermissibleValue(text="application/td+json"))
        setattr(cls, "application/tei+xml",
            PermissibleValue(text="application/tei+xml"))
        setattr(cls, "application/TETRA_ISI",
            PermissibleValue(text="application/TETRA_ISI"))
        setattr(cls, "application/thraud+xml",
            PermissibleValue(text="application/thraud+xml"))
        setattr(cls, "application/timestamped-data",
            PermissibleValue(text="application/timestamped-data"))
        setattr(cls, "application/timestamp-query",
            PermissibleValue(text="application/timestamp-query"))
        setattr(cls, "application/timestamp-reply",
            PermissibleValue(text="application/timestamp-reply"))
        setattr(cls, "application/tlsrpt+gzip",
            PermissibleValue(text="application/tlsrpt+gzip"))
        setattr(cls, "application/tlsrpt+json",
            PermissibleValue(text="application/tlsrpt+json"))
        setattr(cls, "application/tm+json",
            PermissibleValue(text="application/tm+json"))
        setattr(cls, "application/tnauthlist",
            PermissibleValue(text="application/tnauthlist"))
        setattr(cls, "application/toc+cbor",
            PermissibleValue(text="application/toc+cbor"))
        setattr(cls, "application/token-introspection+jwt",
            PermissibleValue(text="application/token-introspection+jwt"))
        setattr(cls, "application/toml",
            PermissibleValue(text="application/toml"))
        setattr(cls, "application/trickle-ice-sdpfrag",
            PermissibleValue(text="application/trickle-ice-sdpfrag"))
        setattr(cls, "application/trig",
            PermissibleValue(text="application/trig"))
        setattr(cls, "application/trust-chain+json",
            PermissibleValue(text="application/trust-chain+json"))
        setattr(cls, "application/trust-mark+jwt",
            PermissibleValue(text="application/trust-mark+jwt"))
        setattr(cls, "application/trust-mark-delegation+jwt",
            PermissibleValue(text="application/trust-mark-delegation+jwt"))
        setattr(cls, "application/ttml+xml",
            PermissibleValue(text="application/ttml+xml"))
        setattr(cls, "application/tve-trigger",
            PermissibleValue(text="application/tve-trigger"))
        setattr(cls, "application/tzif",
            PermissibleValue(text="application/tzif"))
        setattr(cls, "application/tzif-leap",
            PermissibleValue(text="application/tzif-leap"))
        setattr(cls, "application/uccs+cbor",
            PermissibleValue(text="application/uccs+cbor"))
        setattr(cls, "application/ujcs+json",
            PermissibleValue(text="application/ujcs+json"))
        setattr(cls, "application/ulpfec",
            PermissibleValue(text="application/ulpfec"))
        setattr(cls, "application/urc-grpsheet+xml",
            PermissibleValue(text="application/urc-grpsheet+xml"))
        setattr(cls, "application/urc-ressheet+xml",
            PermissibleValue(text="application/urc-ressheet+xml"))
        setattr(cls, "application/urc-targetdesc+xml",
            PermissibleValue(text="application/urc-targetdesc+xml"))
        setattr(cls, "application/urc-uisocketdesc+xml",
            PermissibleValue(text="application/urc-uisocketdesc+xml"))
        setattr(cls, "application/vc",
            PermissibleValue(text="application/vc"))
        setattr(cls, "application/vc+cose",
            PermissibleValue(text="application/vc+cose"))
        setattr(cls, "application/vc+jwt",
            PermissibleValue(text="application/vc+jwt"))
        setattr(cls, "application/vcard+json",
            PermissibleValue(text="application/vcard+json"))
        setattr(cls, "application/vcard+xml",
            PermissibleValue(text="application/vcard+xml"))
        setattr(cls, "application/vemmi",
            PermissibleValue(text="application/vemmi"))
        setattr(cls, "application/vnd.1000minds.decision-model+xml",
            PermissibleValue(text="application/vnd.1000minds.decision-model+xml"))
        setattr(cls, "application/vnd.1ob",
            PermissibleValue(text="application/vnd.1ob"))
        setattr(cls, "application/vnd.3gpp.5gnas",
            PermissibleValue(text="application/vnd.3gpp.5gnas"))
        setattr(cls, "application/vnd.3gpp.5gsa2x",
            PermissibleValue(text="application/vnd.3gpp.5gsa2x"))
        setattr(cls, "application/vnd.3gpp.5gsa2x-local-service-information",
            PermissibleValue(text="application/vnd.3gpp.5gsa2x-local-service-information"))
        setattr(cls, "application/vnd.3gpp.5gsv2x",
            PermissibleValue(text="application/vnd.3gpp.5gsv2x"))
        setattr(cls, "application/vnd.3gpp.5gsv2x-local-service-information",
            PermissibleValue(text="application/vnd.3gpp.5gsv2x-local-service-information"))
        setattr(cls, "application/vnd.3gpp.access-transfer-events+xml",
            PermissibleValue(text="application/vnd.3gpp.access-transfer-events+xml"))
        setattr(cls, "application/vnd.3gpp.bsf+xml",
            PermissibleValue(text="application/vnd.3gpp.bsf+xml"))
        setattr(cls, "application/vnd.3gpp.crs+xml",
            PermissibleValue(text="application/vnd.3gpp.crs+xml"))
        setattr(cls, "application/vnd.3gpp.current-location-discovery+xml",
            PermissibleValue(text="application/vnd.3gpp.current-location-discovery+xml"))
        setattr(cls, "application/vnd.3gpp.GMOP+xml",
            PermissibleValue(text="application/vnd.3gpp.GMOP+xml"))
        setattr(cls, "application/vnd.3gpp.gtpc",
            PermissibleValue(text="application/vnd.3gpp.gtpc"))
        setattr(cls, "application/vnd.3gpp.interworking-data",
            PermissibleValue(text="application/vnd.3gpp.interworking-data"))
        setattr(cls, "application/vnd.3gpp.lpp",
            PermissibleValue(text="application/vnd.3gpp.lpp"))
        setattr(cls, "application/vnd.3gpp.mcdata-affiliation-command+xml",
            PermissibleValue(text="application/vnd.3gpp.mcdata-affiliation-command+xml"))
        setattr(cls, "application/vnd.3gpp.mcdata-info+xml",
            PermissibleValue(text="application/vnd.3gpp.mcdata-info+xml"))
        setattr(cls, "application/vnd.3gpp.mcdata-msgstore-ctrl-request+xml",
            PermissibleValue(text="application/vnd.3gpp.mcdata-msgstore-ctrl-request+xml"))
        setattr(cls, "application/vnd.3gpp.mcdata-payload",
            PermissibleValue(text="application/vnd.3gpp.mcdata-payload"))
        setattr(cls, "application/vnd.3gpp.mcdata-regroup+xml",
            PermissibleValue(text="application/vnd.3gpp.mcdata-regroup+xml"))
        setattr(cls, "application/vnd.3gpp.mcdata-service-config+xml",
            PermissibleValue(text="application/vnd.3gpp.mcdata-service-config+xml"))
        setattr(cls, "application/vnd.3gpp.mcdata-signalling",
            PermissibleValue(text="application/vnd.3gpp.mcdata-signalling"))
        setattr(cls, "application/vnd.3gpp.mcdata-ue-config+xml",
            PermissibleValue(text="application/vnd.3gpp.mcdata-ue-config+xml"))
        setattr(cls, "application/vnd.3gpp.mcdata-user-profile+xml",
            PermissibleValue(text="application/vnd.3gpp.mcdata-user-profile+xml"))
        setattr(cls, "application/vnd.3gpp.mcptt-affiliation-command+xml",
            PermissibleValue(text="application/vnd.3gpp.mcptt-affiliation-command+xml"))
        setattr(cls, "application/vnd.3gpp.mcptt-floor-request+xml",
            PermissibleValue(text="application/vnd.3gpp.mcptt-floor-request+xml"))
        setattr(cls, "application/vnd.3gpp.mcptt-info+xml",
            PermissibleValue(text="application/vnd.3gpp.mcptt-info+xml"))
        setattr(cls, "application/vnd.3gpp.mcptt-location-info+xml",
            PermissibleValue(text="application/vnd.3gpp.mcptt-location-info+xml"))
        setattr(cls, "application/vnd.3gpp.mcptt-mbms-usage-info+xml",
            PermissibleValue(text="application/vnd.3gpp.mcptt-mbms-usage-info+xml"))
        setattr(cls, "application/vnd.3gpp.mcptt-regroup+xml",
            PermissibleValue(text="application/vnd.3gpp.mcptt-regroup+xml"))
        setattr(cls, "application/vnd.3gpp.mcptt-service-config+xml",
            PermissibleValue(text="application/vnd.3gpp.mcptt-service-config+xml"))
        setattr(cls, "application/vnd.3gpp.mcptt-signed+xml",
            PermissibleValue(text="application/vnd.3gpp.mcptt-signed+xml"))
        setattr(cls, "application/vnd.3gpp.mcptt-ue-config+xml",
            PermissibleValue(text="application/vnd.3gpp.mcptt-ue-config+xml"))
        setattr(cls, "application/vnd.3gpp.mcptt-ue-init-config+xml",
            PermissibleValue(text="application/vnd.3gpp.mcptt-ue-init-config+xml"))
        setattr(cls, "application/vnd.3gpp.mcptt-user-profile+xml",
            PermissibleValue(text="application/vnd.3gpp.mcptt-user-profile+xml"))
        setattr(cls, "application/vnd.3gpp.mc-signalling-ear",
            PermissibleValue(text="application/vnd.3gpp.mc-signalling-ear"))
        setattr(cls, "application/vnd.3gpp.mcvideo-affiliation-command+xml",
            PermissibleValue(text="application/vnd.3gpp.mcvideo-affiliation-command+xml"))
        setattr(cls, "application/vnd.3gpp.mcvideo-affiliation-info+xml",
            PermissibleValue(text="application/vnd.3gpp.mcvideo-affiliation-info+xml"))
        setattr(cls, "application/vnd.3gpp.mcvideo-info+xml",
            PermissibleValue(text="application/vnd.3gpp.mcvideo-info+xml"))
        setattr(cls, "application/vnd.3gpp.mcvideo-location-info+xml",
            PermissibleValue(text="application/vnd.3gpp.mcvideo-location-info+xml"))
        setattr(cls, "application/vnd.3gpp.mcvideo-mbms-usage-info+xml",
            PermissibleValue(text="application/vnd.3gpp.mcvideo-mbms-usage-info+xml"))
        setattr(cls, "application/vnd.3gpp.mcvideo-regroup+xml",
            PermissibleValue(text="application/vnd.3gpp.mcvideo-regroup+xml"))
        setattr(cls, "application/vnd.3gpp.mcvideo-service-config+xml",
            PermissibleValue(text="application/vnd.3gpp.mcvideo-service-config+xml"))
        setattr(cls, "application/vnd.3gpp.mcvideo-transmission-request+xml",
            PermissibleValue(text="application/vnd.3gpp.mcvideo-transmission-request+xml"))
        setattr(cls, "application/vnd.3gpp.mcvideo-ue-config+xml",
            PermissibleValue(text="application/vnd.3gpp.mcvideo-ue-config+xml"))
        setattr(cls, "application/vnd.3gpp.mcvideo-user-profile+xml",
            PermissibleValue(text="application/vnd.3gpp.mcvideo-user-profile+xml"))
        setattr(cls, "application/vnd.3gpp.mid-call+xml",
            PermissibleValue(text="application/vnd.3gpp.mid-call+xml"))
        setattr(cls, "application/vnd.3gpp.ngap",
            PermissibleValue(text="application/vnd.3gpp.ngap"))
        setattr(cls, "application/vnd.3gpp.pfcp",
            PermissibleValue(text="application/vnd.3gpp.pfcp"))
        setattr(cls, "application/vnd.3gpp.pic-bw-large",
            PermissibleValue(text="application/vnd.3gpp.pic-bw-large"))
        setattr(cls, "application/vnd.3gpp.pic-bw-small",
            PermissibleValue(text="application/vnd.3gpp.pic-bw-small"))
        setattr(cls, "application/vnd.3gpp.pic-bw-var",
            PermissibleValue(text="application/vnd.3gpp.pic-bw-var"))
        setattr(cls, "application/vnd.3gpp.pinapp-info+xml",
            PermissibleValue(text="application/vnd.3gpp.pinapp-info+xml"))
        setattr(cls, "application/vnd.3gpp.s1ap",
            PermissibleValue(text="application/vnd.3gpp.s1ap"))
        setattr(cls, "application/vnd.3gpp.seal-group-doc+xml",
            PermissibleValue(text="application/vnd.3gpp.seal-group-doc+xml"))
        setattr(cls, "application/vnd.3gpp.seal-info+xml",
            PermissibleValue(text="application/vnd.3gpp.seal-info+xml"))
        setattr(cls, "application/vnd.3gpp.seal-location-info+xml",
            PermissibleValue(text="application/vnd.3gpp.seal-location-info+xml"))
        setattr(cls, "application/vnd.3gpp.seal-mbms-usage-info+xml",
            PermissibleValue(text="application/vnd.3gpp.seal-mbms-usage-info+xml"))
        setattr(cls, "application/vnd.3gpp.seal-network-QoS-management-info+xml",
            PermissibleValue(text="application/vnd.3gpp.seal-network-QoS-management-info+xml"))
        setattr(cls, "application/vnd.3gpp.seal-ue-config-info+xml",
            PermissibleValue(text="application/vnd.3gpp.seal-ue-config-info+xml"))
        setattr(cls, "application/vnd.3gpp.seal-unicast-info+xml",
            PermissibleValue(text="application/vnd.3gpp.seal-unicast-info+xml"))
        setattr(cls, "application/vnd.3gpp.seal-user-profile-info+xml",
            PermissibleValue(text="application/vnd.3gpp.seal-user-profile-info+xml"))
        setattr(cls, "application/vnd.3gpp.sms",
            PermissibleValue(text="application/vnd.3gpp.sms"))
        setattr(cls, "application/vnd.3gpp.sms+xml",
            PermissibleValue(text="application/vnd.3gpp.sms+xml"))
        setattr(cls, "application/vnd.3gpp.srvcc-ext+xml",
            PermissibleValue(text="application/vnd.3gpp.srvcc-ext+xml"))
        setattr(cls, "application/vnd.3gpp.SRVCC-info+xml",
            PermissibleValue(text="application/vnd.3gpp.SRVCC-info+xml"))
        setattr(cls, "application/vnd.3gpp.state-and-event-info+xml",
            PermissibleValue(text="application/vnd.3gpp.state-and-event-info+xml"))
        setattr(cls, "application/vnd.3gpp.ussd+xml",
            PermissibleValue(text="application/vnd.3gpp.ussd+xml"))
        setattr(cls, "application/vnd.3gpp.v2x",
            PermissibleValue(text="application/vnd.3gpp.v2x"))
        setattr(cls, "application/vnd.3gpp.vae-info+xml",
            PermissibleValue(text="application/vnd.3gpp.vae-info+xml"))
        setattr(cls, "application/vnd.3gpp2.bcmcsinfo+xml",
            PermissibleValue(text="application/vnd.3gpp2.bcmcsinfo+xml"))
        setattr(cls, "application/vnd.3gpp2.sms",
            PermissibleValue(text="application/vnd.3gpp2.sms"))
        setattr(cls, "application/vnd.3gpp2.tcap",
            PermissibleValue(text="application/vnd.3gpp2.tcap"))
        setattr(cls, "application/vnd.3gpp-prose+xml",
            PermissibleValue(text="application/vnd.3gpp-prose+xml"))
        setattr(cls, "application/vnd.3gpp-prose-pc3a+xml",
            PermissibleValue(text="application/vnd.3gpp-prose-pc3a+xml"))
        setattr(cls, "application/vnd.3gpp-prose-pc3ach+xml",
            PermissibleValue(text="application/vnd.3gpp-prose-pc3ach+xml"))
        setattr(cls, "application/vnd.3gpp-prose-pc3ch+xml",
            PermissibleValue(text="application/vnd.3gpp-prose-pc3ch+xml"))
        setattr(cls, "application/vnd.3gpp-prose-pc8+xml",
            PermissibleValue(text="application/vnd.3gpp-prose-pc8+xml"))
        setattr(cls, "application/vnd.3gpp-v2x-local-service-information",
            PermissibleValue(text="application/vnd.3gpp-v2x-local-service-information"))
        setattr(cls, "application/vnd.3lightssoftware.imagescal",
            PermissibleValue(text="application/vnd.3lightssoftware.imagescal"))
        setattr(cls, "application/vnd.3M.Post-it-Notes",
            PermissibleValue(text="application/vnd.3M.Post-it-Notes"))
        setattr(cls, "application/vnd.accpac.simply.aso",
            PermissibleValue(text="application/vnd.accpac.simply.aso"))
        setattr(cls, "application/vnd.accpac.simply.imp",
            PermissibleValue(text="application/vnd.accpac.simply.imp"))
        setattr(cls, "application/vnd.acm.addressxfer+json",
            PermissibleValue(text="application/vnd.acm.addressxfer+json"))
        setattr(cls, "application/vnd.acm.chatbot+json",
            PermissibleValue(text="application/vnd.acm.chatbot+json"))
        setattr(cls, "application/vnd.acucobol",
            PermissibleValue(text="application/vnd.acucobol"))
        setattr(cls, "application/vnd.acucorp",
            PermissibleValue(text="application/vnd.acucorp"))
        setattr(cls, "application/vnd.adobe.flash.movie",
            PermissibleValue(text="application/vnd.adobe.flash.movie"))
        setattr(cls, "application/vnd.adobe.formscentral.fcdt",
            PermissibleValue(text="application/vnd.adobe.formscentral.fcdt"))
        setattr(cls, "application/vnd.adobe.fxp",
            PermissibleValue(text="application/vnd.adobe.fxp"))
        setattr(cls, "application/vnd.adobe.partial-upload",
            PermissibleValue(text="application/vnd.adobe.partial-upload"))
        setattr(cls, "application/vnd.adobe.xdp+xml",
            PermissibleValue(text="application/vnd.adobe.xdp+xml"))
        setattr(cls, "application/vnd.aether.imp",
            PermissibleValue(text="application/vnd.aether.imp"))
        setattr(cls, "application/vnd.afpc.afplinedata",
            PermissibleValue(text="application/vnd.afpc.afplinedata"))
        setattr(cls, "application/vnd.afpc.afplinedata-pagedef",
            PermissibleValue(text="application/vnd.afpc.afplinedata-pagedef"))
        setattr(cls, "application/vnd.afpc.cmoca-cmresource",
            PermissibleValue(text="application/vnd.afpc.cmoca-cmresource"))
        setattr(cls, "application/vnd.afpc.foca-charset",
            PermissibleValue(text="application/vnd.afpc.foca-charset"))
        setattr(cls, "application/vnd.afpc.foca-codedfont",
            PermissibleValue(text="application/vnd.afpc.foca-codedfont"))
        setattr(cls, "application/vnd.afpc.foca-codepage",
            PermissibleValue(text="application/vnd.afpc.foca-codepage"))
        setattr(cls, "application/vnd.afpc.modca",
            PermissibleValue(text="application/vnd.afpc.modca"))
        setattr(cls, "application/vnd.afpc.modca-cmtable",
            PermissibleValue(text="application/vnd.afpc.modca-cmtable"))
        setattr(cls, "application/vnd.afpc.modca-formdef",
            PermissibleValue(text="application/vnd.afpc.modca-formdef"))
        setattr(cls, "application/vnd.afpc.modca-mediummap",
            PermissibleValue(text="application/vnd.afpc.modca-mediummap"))
        setattr(cls, "application/vnd.afpc.modca-objectcontainer",
            PermissibleValue(text="application/vnd.afpc.modca-objectcontainer"))
        setattr(cls, "application/vnd.afpc.modca-overlay",
            PermissibleValue(text="application/vnd.afpc.modca-overlay"))
        setattr(cls, "application/vnd.afpc.modca-pagesegment",
            PermissibleValue(text="application/vnd.afpc.modca-pagesegment"))
        setattr(cls, "application/vnd.age",
            PermissibleValue(text="application/vnd.age"))
        setattr(cls, "application/vnd.ah-barcode",
            PermissibleValue(text="application/vnd.ah-barcode"))
        setattr(cls, "application/vnd.ahead.space",
            PermissibleValue(text="application/vnd.ahead.space"))
        setattr(cls, "application/vnd.airzip.filesecure.azf",
            PermissibleValue(text="application/vnd.airzip.filesecure.azf"))
        setattr(cls, "application/vnd.airzip.filesecure.azs",
            PermissibleValue(text="application/vnd.airzip.filesecure.azs"))
        setattr(cls, "application/vnd.amadeus+json",
            PermissibleValue(text="application/vnd.amadeus+json"))
        setattr(cls, "application/vnd.amazon.mobi8-ebook",
            PermissibleValue(text="application/vnd.amazon.mobi8-ebook"))
        setattr(cls, "application/vnd.americandynamics.acc",
            PermissibleValue(text="application/vnd.americandynamics.acc"))
        setattr(cls, "application/vnd.amiga.ami",
            PermissibleValue(text="application/vnd.amiga.ami"))
        setattr(cls, "application/vnd.amundsen.maze+xml",
            PermissibleValue(text="application/vnd.amundsen.maze+xml"))
        setattr(cls, "application/vnd.android.ota",
            PermissibleValue(text="application/vnd.android.ota"))
        setattr(cls, "application/vnd.anki",
            PermissibleValue(text="application/vnd.anki"))
        setattr(cls, "application/vnd.anser-web-certificate-issue-initiation",
            PermissibleValue(text="application/vnd.anser-web-certificate-issue-initiation"))
        setattr(cls, "application/vnd.antix.game-component",
            PermissibleValue(text="application/vnd.antix.game-component"))
        setattr(cls, "application/vnd.apache.arrow.file",
            PermissibleValue(text="application/vnd.apache.arrow.file"))
        setattr(cls, "application/vnd.apache.arrow.stream",
            PermissibleValue(text="application/vnd.apache.arrow.stream"))
        setattr(cls, "application/vnd.apache.parquet",
            PermissibleValue(text="application/vnd.apache.parquet"))
        setattr(cls, "application/vnd.apache.thrift.binary",
            PermissibleValue(text="application/vnd.apache.thrift.binary"))
        setattr(cls, "application/vnd.apache.thrift.compact",
            PermissibleValue(text="application/vnd.apache.thrift.compact"))
        setattr(cls, "application/vnd.apache.thrift.json",
            PermissibleValue(text="application/vnd.apache.thrift.json"))
        setattr(cls, "application/vnd.apexlang",
            PermissibleValue(text="application/vnd.apexlang"))
        setattr(cls, "application/vnd.api+json",
            PermissibleValue(text="application/vnd.api+json"))
        setattr(cls, "application/vnd.aplextor.warrp+json",
            PermissibleValue(text="application/vnd.aplextor.warrp+json"))
        setattr(cls, "application/vnd.apothekende.reservation+json",
            PermissibleValue(text="application/vnd.apothekende.reservation+json"))
        setattr(cls, "application/vnd.apple.installer+xml",
            PermissibleValue(text="application/vnd.apple.installer+xml"))
        setattr(cls, "application/vnd.apple.keynote",
            PermissibleValue(text="application/vnd.apple.keynote"))
        setattr(cls, "application/vnd.apple.mpegurl",
            PermissibleValue(text="application/vnd.apple.mpegurl"))
        setattr(cls, "application/vnd.apple.numbers",
            PermissibleValue(text="application/vnd.apple.numbers"))
        setattr(cls, "application/vnd.apple.pages",
            PermissibleValue(text="application/vnd.apple.pages"))
        setattr(cls, "application/vnd.arastra.swi",
            PermissibleValue(text="application/vnd.arastra.swi"))
        setattr(cls, "application/vnd.aristanetworks.swi",
            PermissibleValue(text="application/vnd.aristanetworks.swi"))
        setattr(cls, "application/vnd.artisan+json",
            PermissibleValue(text="application/vnd.artisan+json"))
        setattr(cls, "application/vnd.artsquare",
            PermissibleValue(text="application/vnd.artsquare"))
        setattr(cls, "application/vnd.astraea-software.iota",
            PermissibleValue(text="application/vnd.astraea-software.iota"))
        setattr(cls, "application/vnd.audiograph",
            PermissibleValue(text="application/vnd.audiograph"))
        setattr(cls, "application/vnd.autopackage",
            PermissibleValue(text="application/vnd.autopackage"))
        setattr(cls, "application/vnd.avalon+json",
            PermissibleValue(text="application/vnd.avalon+json"))
        setattr(cls, "application/vnd.avistar+xml",
            PermissibleValue(text="application/vnd.avistar+xml"))
        setattr(cls, "application/vnd.balsamiq.bmml+xml",
            PermissibleValue(text="application/vnd.balsamiq.bmml+xml"))
        setattr(cls, "application/vnd.balsamiq.bmpr",
            PermissibleValue(text="application/vnd.balsamiq.bmpr"))
        setattr(cls, "application/vnd.banana-accounting",
            PermissibleValue(text="application/vnd.banana-accounting"))
        setattr(cls, "application/vnd.bbf.usp.error",
            PermissibleValue(text="application/vnd.bbf.usp.error"))
        setattr(cls, "application/vnd.bbf.usp.msg",
            PermissibleValue(text="application/vnd.bbf.usp.msg"))
        setattr(cls, "application/vnd.bbf.usp.msg+json",
            PermissibleValue(text="application/vnd.bbf.usp.msg+json"))
        setattr(cls, "application/vnd.bekitzur-stech+json",
            PermissibleValue(text="application/vnd.bekitzur-stech+json"))
        setattr(cls, "application/vnd.belightsoft.lhzd+zip",
            PermissibleValue(text="application/vnd.belightsoft.lhzd+zip"))
        setattr(cls, "application/vnd.belightsoft.lhzl+zip",
            PermissibleValue(text="application/vnd.belightsoft.lhzl+zip"))
        setattr(cls, "application/vnd.bint.med-content",
            PermissibleValue(text="application/vnd.bint.med-content"))
        setattr(cls, "application/vnd.biopax.rdf+xml",
            PermissibleValue(text="application/vnd.biopax.rdf+xml"))
        setattr(cls, "application/vnd.blink-idb-value-wrapper",
            PermissibleValue(text="application/vnd.blink-idb-value-wrapper"))
        setattr(cls, "application/vnd.blueice.multipass",
            PermissibleValue(text="application/vnd.blueice.multipass"))
        setattr(cls, "application/vnd.bluetooth.ep.oob",
            PermissibleValue(text="application/vnd.bluetooth.ep.oob"))
        setattr(cls, "application/vnd.bluetooth.le.oob",
            PermissibleValue(text="application/vnd.bluetooth.le.oob"))
        setattr(cls, "application/vnd.bmi",
            PermissibleValue(text="application/vnd.bmi"))
        setattr(cls, "application/vnd.bpf",
            PermissibleValue(text="application/vnd.bpf"))
        setattr(cls, "application/vnd.bpf3",
            PermissibleValue(text="application/vnd.bpf3"))
        setattr(cls, "application/vnd.businessobjects",
            PermissibleValue(text="application/vnd.businessobjects"))
        setattr(cls, "application/vnd.byu.uapi+json",
            PermissibleValue(text="application/vnd.byu.uapi+json"))
        setattr(cls, "application/vnd.bzip3",
            PermissibleValue(text="application/vnd.bzip3"))
        setattr(cls, "application/vnd.c3voc.schedule+xml",
            PermissibleValue(text="application/vnd.c3voc.schedule+xml"))
        setattr(cls, "application/vnd.cab-jscript",
            PermissibleValue(text="application/vnd.cab-jscript"))
        setattr(cls, "application/vnd.canon-cpdl",
            PermissibleValue(text="application/vnd.canon-cpdl"))
        setattr(cls, "application/vnd.canon-lips",
            PermissibleValue(text="application/vnd.canon-lips"))
        setattr(cls, "application/vnd.capasystems-pg+json",
            PermissibleValue(text="application/vnd.capasystems-pg+json"))
        setattr(cls, "application/vnd.cendio.thinlinc.clientconf",
            PermissibleValue(text="application/vnd.cendio.thinlinc.clientconf"))
        setattr(cls, "application/vnd.century-systems.tcp_stream",
            PermissibleValue(text="application/vnd.century-systems.tcp_stream"))
        setattr(cls, "application/vnd.chemdraw+xml",
            PermissibleValue(text="application/vnd.chemdraw+xml"))
        setattr(cls, "application/vnd.chess-pgn",
            PermissibleValue(text="application/vnd.chess-pgn"))
        setattr(cls, "application/vnd.chipnuts.karaoke-mmd",
            PermissibleValue(text="application/vnd.chipnuts.karaoke-mmd"))
        setattr(cls, "application/vnd.ciedi",
            PermissibleValue(text="application/vnd.ciedi"))
        setattr(cls, "application/vnd.cinderella",
            PermissibleValue(text="application/vnd.cinderella"))
        setattr(cls, "application/vnd.cirpack.isdn-ext",
            PermissibleValue(text="application/vnd.cirpack.isdn-ext"))
        setattr(cls, "application/vnd.citationstyles.style+xml",
            PermissibleValue(text="application/vnd.citationstyles.style+xml"))
        setattr(cls, "application/vnd.claymore",
            PermissibleValue(text="application/vnd.claymore"))
        setattr(cls, "application/vnd.cloanto.rp9",
            PermissibleValue(text="application/vnd.cloanto.rp9"))
        setattr(cls, "application/vnd.clonk.c4group",
            PermissibleValue(text="application/vnd.clonk.c4group"))
        setattr(cls, "application/vnd.cluetrust.cartomobile-config",
            PermissibleValue(text="application/vnd.cluetrust.cartomobile-config"))
        setattr(cls, "application/vnd.cluetrust.cartomobile-config-pkg",
            PermissibleValue(text="application/vnd.cluetrust.cartomobile-config-pkg"))
        setattr(cls, "application/vnd.cncf.helm.chart.content.v1.tar+gzip",
            PermissibleValue(text="application/vnd.cncf.helm.chart.content.v1.tar+gzip"))
        setattr(cls, "application/vnd.cncf.helm.chart.provenance.v1.prov",
            PermissibleValue(text="application/vnd.cncf.helm.chart.provenance.v1.prov"))
        setattr(cls, "application/vnd.cncf.helm.config.v1+json",
            PermissibleValue(text="application/vnd.cncf.helm.config.v1+json"))
        setattr(cls, "application/vnd.coffeescript",
            PermissibleValue(text="application/vnd.coffeescript"))
        setattr(cls, "application/vnd.collabio.xodocuments.document",
            PermissibleValue(text="application/vnd.collabio.xodocuments.document"))
        setattr(cls, "application/vnd.collabio.xodocuments.document-template",
            PermissibleValue(text="application/vnd.collabio.xodocuments.document-template"))
        setattr(cls, "application/vnd.collabio.xodocuments.presentation",
            PermissibleValue(text="application/vnd.collabio.xodocuments.presentation"))
        setattr(cls, "application/vnd.collabio.xodocuments.presentation-template",
            PermissibleValue(text="application/vnd.collabio.xodocuments.presentation-template"))
        setattr(cls, "application/vnd.collabio.xodocuments.spreadsheet",
            PermissibleValue(text="application/vnd.collabio.xodocuments.spreadsheet"))
        setattr(cls, "application/vnd.collabio.xodocuments.spreadsheet-template",
            PermissibleValue(text="application/vnd.collabio.xodocuments.spreadsheet-template"))
        setattr(cls, "application/vnd.collection.doc+json",
            PermissibleValue(text="application/vnd.collection.doc+json"))
        setattr(cls, "application/vnd.collection.next+json",
            PermissibleValue(text="application/vnd.collection.next+json"))
        setattr(cls, "application/vnd.collection+json",
            PermissibleValue(text="application/vnd.collection+json"))
        setattr(cls, "application/vnd.comicbook+zip",
            PermissibleValue(text="application/vnd.comicbook+zip"))
        setattr(cls, "application/vnd.comicbook-rar",
            PermissibleValue(text="application/vnd.comicbook-rar"))
        setattr(cls, "application/vnd.commerce-battelle",
            PermissibleValue(text="application/vnd.commerce-battelle"))
        setattr(cls, "application/vnd.commonspace",
            PermissibleValue(text="application/vnd.commonspace"))
        setattr(cls, "application/vnd.contact.cmsg",
            PermissibleValue(text="application/vnd.contact.cmsg"))
        setattr(cls, "application/vnd.coreos.ignition+json",
            PermissibleValue(text="application/vnd.coreos.ignition+json"))
        setattr(cls, "application/vnd.cosmocaller",
            PermissibleValue(text="application/vnd.cosmocaller"))
        setattr(cls, "application/vnd.crick.clicker",
            PermissibleValue(text="application/vnd.crick.clicker"))
        setattr(cls, "application/vnd.crick.clicker.keyboard",
            PermissibleValue(text="application/vnd.crick.clicker.keyboard"))
        setattr(cls, "application/vnd.crick.clicker.palette",
            PermissibleValue(text="application/vnd.crick.clicker.palette"))
        setattr(cls, "application/vnd.crick.clicker.template",
            PermissibleValue(text="application/vnd.crick.clicker.template"))
        setattr(cls, "application/vnd.crick.clicker.wordbank",
            PermissibleValue(text="application/vnd.crick.clicker.wordbank"))
        setattr(cls, "application/vnd.criticaltools.wbs+xml",
            PermissibleValue(text="application/vnd.criticaltools.wbs+xml"))
        setattr(cls, "application/vnd.cryptii.pipe+json",
            PermissibleValue(text="application/vnd.cryptii.pipe+json"))
        setattr(cls, "application/vnd.cryptomator.encrypted",
            PermissibleValue(text="application/vnd.cryptomator.encrypted"))
        setattr(cls, "application/vnd.cryptomator.vault",
            PermissibleValue(text="application/vnd.cryptomator.vault"))
        setattr(cls, "application/vnd.crypto-shade-file",
            PermissibleValue(text="application/vnd.crypto-shade-file"))
        setattr(cls, "application/vnd.ctc-posml",
            PermissibleValue(text="application/vnd.ctc-posml"))
        setattr(cls, "application/vnd.ctct.ws+xml",
            PermissibleValue(text="application/vnd.ctct.ws+xml"))
        setattr(cls, "application/vnd.cups-pdf",
            PermissibleValue(text="application/vnd.cups-pdf"))
        setattr(cls, "application/vnd.cups-postscript",
            PermissibleValue(text="application/vnd.cups-postscript"))
        setattr(cls, "application/vnd.cups-ppd",
            PermissibleValue(text="application/vnd.cups-ppd"))
        setattr(cls, "application/vnd.cups-raster",
            PermissibleValue(text="application/vnd.cups-raster"))
        setattr(cls, "application/vnd.cups-raw",
            PermissibleValue(text="application/vnd.cups-raw"))
        setattr(cls, "application/vnd.curl",
            PermissibleValue(text="application/vnd.curl"))
        setattr(cls, "application/vnd.cyan.dean.root+xml",
            PermissibleValue(text="application/vnd.cyan.dean.root+xml"))
        setattr(cls, "application/vnd.cybank",
            PermissibleValue(text="application/vnd.cybank"))
        setattr(cls, "application/vnd.cyclonedx+json",
            PermissibleValue(text="application/vnd.cyclonedx+json"))
        setattr(cls, "application/vnd.cyclonedx+xml",
            PermissibleValue(text="application/vnd.cyclonedx+xml"))
        setattr(cls, "application/vnd.d2l.coursepackage1p0+zip",
            PermissibleValue(text="application/vnd.d2l.coursepackage1p0+zip"))
        setattr(cls, "application/vnd.d3m-dataset",
            PermissibleValue(text="application/vnd.d3m-dataset"))
        setattr(cls, "application/vnd.d3m-problem",
            PermissibleValue(text="application/vnd.d3m-problem"))
        setattr(cls, "application/vnd.dart",
            PermissibleValue(text="application/vnd.dart"))
        setattr(cls, "application/vnd.datalog",
            PermissibleValue(text="application/vnd.datalog"))
        setattr(cls, "application/vnd.datapackage+json",
            PermissibleValue(text="application/vnd.datapackage+json"))
        setattr(cls, "application/vnd.dataresource+json",
            PermissibleValue(text="application/vnd.dataresource+json"))
        setattr(cls, "application/vnd.data-vision.rdz",
            PermissibleValue(text="application/vnd.data-vision.rdz"))
        setattr(cls, "application/vnd.dbf",
            PermissibleValue(text="application/vnd.dbf"))
        setattr(cls, "application/vnd.dcmp+xml",
            PermissibleValue(text="application/vnd.dcmp+xml"))
        setattr(cls, "application/vnd.debian.binary-package",
            PermissibleValue(text="application/vnd.debian.binary-package"))
        setattr(cls, "application/vnd.dece.data",
            PermissibleValue(text="application/vnd.dece.data"))
        setattr(cls, "application/vnd.dece.ttml+xml",
            PermissibleValue(text="application/vnd.dece.ttml+xml"))
        setattr(cls, "application/vnd.dece.unspecified",
            PermissibleValue(text="application/vnd.dece.unspecified"))
        setattr(cls, "application/vnd.dece.zip",
            PermissibleValue(text="application/vnd.dece.zip"))
        setattr(cls, "application/vnd.denovo.fcselayout-link",
            PermissibleValue(text="application/vnd.denovo.fcselayout-link"))
        setattr(cls, "application/vnd.desmume.movie",
            PermissibleValue(text="application/vnd.desmume.movie"))
        setattr(cls, "application/vnd.dir-bi.plate-dl-nosuffix",
            PermissibleValue(text="application/vnd.dir-bi.plate-dl-nosuffix"))
        setattr(cls, "application/vnd.dm.delegation+xml",
            PermissibleValue(text="application/vnd.dm.delegation+xml"))
        setattr(cls, "application/vnd.dna",
            PermissibleValue(text="application/vnd.dna"))
        setattr(cls, "application/vnd.document+json",
            PermissibleValue(text="application/vnd.document+json"))
        setattr(cls, "application/vnd.dolby.mobile.1",
            PermissibleValue(text="application/vnd.dolby.mobile.1"))
        setattr(cls, "application/vnd.dolby.mobile.2",
            PermissibleValue(text="application/vnd.dolby.mobile.2"))
        setattr(cls, "application/vnd.doremir.scorecloud-binary-document",
            PermissibleValue(text="application/vnd.doremir.scorecloud-binary-document"))
        setattr(cls, "application/vnd.dpgraph",
            PermissibleValue(text="application/vnd.dpgraph"))
        setattr(cls, "application/vnd.dreamfactory",
            PermissibleValue(text="application/vnd.dreamfactory"))
        setattr(cls, "application/vnd.drive+json",
            PermissibleValue(text="application/vnd.drive+json"))
        setattr(cls, "application/vnd.dtg.local",
            PermissibleValue(text="application/vnd.dtg.local"))
        setattr(cls, "application/vnd.dtg.local.flash",
            PermissibleValue(text="application/vnd.dtg.local.flash"))
        setattr(cls, "application/vnd.dtg.local.html",
            PermissibleValue(text="application/vnd.dtg.local.html"))
        setattr(cls, "application/vnd.dvb.ait",
            PermissibleValue(text="application/vnd.dvb.ait"))
        setattr(cls, "application/vnd.dvb.dvbisl+xml",
            PermissibleValue(text="application/vnd.dvb.dvbisl+xml"))
        setattr(cls, "application/vnd.dvb.dvbj",
            PermissibleValue(text="application/vnd.dvb.dvbj"))
        setattr(cls, "application/vnd.dvb.esgcontainer",
            PermissibleValue(text="application/vnd.dvb.esgcontainer"))
        setattr(cls, "application/vnd.dvb.ipdcdftnotifaccess",
            PermissibleValue(text="application/vnd.dvb.ipdcdftnotifaccess"))
        setattr(cls, "application/vnd.dvb.ipdcesgaccess",
            PermissibleValue(text="application/vnd.dvb.ipdcesgaccess"))
        setattr(cls, "application/vnd.dvb.ipdcesgaccess2",
            PermissibleValue(text="application/vnd.dvb.ipdcesgaccess2"))
        setattr(cls, "application/vnd.dvb.ipdcesgpdd",
            PermissibleValue(text="application/vnd.dvb.ipdcesgpdd"))
        setattr(cls, "application/vnd.dvb.ipdcroaming",
            PermissibleValue(text="application/vnd.dvb.ipdcroaming"))
        setattr(cls, "application/vnd.dvb.iptv.alfec-base",
            PermissibleValue(text="application/vnd.dvb.iptv.alfec-base"))
        setattr(cls, "application/vnd.dvb.iptv.alfec-enhancement",
            PermissibleValue(text="application/vnd.dvb.iptv.alfec-enhancement"))
        setattr(cls, "application/vnd.dvb.notif-aggregate-root+xml",
            PermissibleValue(text="application/vnd.dvb.notif-aggregate-root+xml"))
        setattr(cls, "application/vnd.dvb.notif-container+xml",
            PermissibleValue(text="application/vnd.dvb.notif-container+xml"))
        setattr(cls, "application/vnd.dvb.notif-generic+xml",
            PermissibleValue(text="application/vnd.dvb.notif-generic+xml"))
        setattr(cls, "application/vnd.dvb.notif-ia-msglist+xml",
            PermissibleValue(text="application/vnd.dvb.notif-ia-msglist+xml"))
        setattr(cls, "application/vnd.dvb.notif-ia-registration-request+xml",
            PermissibleValue(text="application/vnd.dvb.notif-ia-registration-request+xml"))
        setattr(cls, "application/vnd.dvb.notif-ia-registration-response+xml",
            PermissibleValue(text="application/vnd.dvb.notif-ia-registration-response+xml"))
        setattr(cls, "application/vnd.dvb.notif-init+xml",
            PermissibleValue(text="application/vnd.dvb.notif-init+xml"))
        setattr(cls, "application/vnd.dvb.pfr",
            PermissibleValue(text="application/vnd.dvb.pfr"))
        setattr(cls, "application/vnd.dvb.service",
            PermissibleValue(text="application/vnd.dvb.service"))
        setattr(cls, "application/vnd.dxr",
            PermissibleValue(text="application/vnd.dxr"))
        setattr(cls, "application/vnd.dynageo",
            PermissibleValue(text="application/vnd.dynageo"))
        setattr(cls, "application/vnd.dzr",
            PermissibleValue(text="application/vnd.dzr"))
        setattr(cls, "application/vnd.easykaraoke.cdgdownload",
            PermissibleValue(text="application/vnd.easykaraoke.cdgdownload"))
        setattr(cls, "application/vnd.ecdis-update",
            PermissibleValue(text="application/vnd.ecdis-update"))
        setattr(cls, "application/vnd.ecip.rlp",
            PermissibleValue(text="application/vnd.ecip.rlp"))
        setattr(cls, "application/vnd.eclipse.ditto+json",
            PermissibleValue(text="application/vnd.eclipse.ditto+json"))
        setattr(cls, "application/vnd.ecowin.chart",
            PermissibleValue(text="application/vnd.ecowin.chart"))
        setattr(cls, "application/vnd.ecowin.filerequest",
            PermissibleValue(text="application/vnd.ecowin.filerequest"))
        setattr(cls, "application/vnd.ecowin.fileupdate",
            PermissibleValue(text="application/vnd.ecowin.fileupdate"))
        setattr(cls, "application/vnd.ecowin.series",
            PermissibleValue(text="application/vnd.ecowin.series"))
        setattr(cls, "application/vnd.ecowin.seriesrequest",
            PermissibleValue(text="application/vnd.ecowin.seriesrequest"))
        setattr(cls, "application/vnd.ecowin.seriesupdate",
            PermissibleValue(text="application/vnd.ecowin.seriesupdate"))
        setattr(cls, "application/vnd.efi.img",
            PermissibleValue(text="application/vnd.efi.img"))
        setattr(cls, "application/vnd.efi.iso",
            PermissibleValue(text="application/vnd.efi.iso"))
        setattr(cls, "application/vnd.eln+zip",
            PermissibleValue(text="application/vnd.eln+zip"))
        setattr(cls, "application/vnd.emclient.accessrequest+xml",
            PermissibleValue(text="application/vnd.emclient.accessrequest+xml"))
        setattr(cls, "application/vnd.enliven",
            PermissibleValue(text="application/vnd.enliven"))
        setattr(cls, "application/vnd.enphase.envoy",
            PermissibleValue(text="application/vnd.enphase.envoy"))
        setattr(cls, "application/vnd.eprints.data+xml",
            PermissibleValue(text="application/vnd.eprints.data+xml"))
        setattr(cls, "application/vnd.epson.esf",
            PermissibleValue(text="application/vnd.epson.esf"))
        setattr(cls, "application/vnd.epson.msf",
            PermissibleValue(text="application/vnd.epson.msf"))
        setattr(cls, "application/vnd.epson.quickanime",
            PermissibleValue(text="application/vnd.epson.quickanime"))
        setattr(cls, "application/vnd.epson.salt",
            PermissibleValue(text="application/vnd.epson.salt"))
        setattr(cls, "application/vnd.epson.ssf",
            PermissibleValue(text="application/vnd.epson.ssf"))
        setattr(cls, "application/vnd.ericsson.quickcall",
            PermissibleValue(text="application/vnd.ericsson.quickcall"))
        setattr(cls, "application/vnd.erofs",
            PermissibleValue(text="application/vnd.erofs"))
        setattr(cls, "application/vnd.espass-espass+zip",
            PermissibleValue(text="application/vnd.espass-espass+zip"))
        setattr(cls, "application/vnd.eszigno3+xml",
            PermissibleValue(text="application/vnd.eszigno3+xml"))
        setattr(cls, "application/vnd.etsi.aoc+xml",
            PermissibleValue(text="application/vnd.etsi.aoc+xml"))
        setattr(cls, "application/vnd.etsi.asic-e+zip",
            PermissibleValue(text="application/vnd.etsi.asic-e+zip"))
        setattr(cls, "application/vnd.etsi.asic-s+zip",
            PermissibleValue(text="application/vnd.etsi.asic-s+zip"))
        setattr(cls, "application/vnd.etsi.cug+xml",
            PermissibleValue(text="application/vnd.etsi.cug+xml"))
        setattr(cls, "application/vnd.etsi.iptvcommand+xml",
            PermissibleValue(text="application/vnd.etsi.iptvcommand+xml"))
        setattr(cls, "application/vnd.etsi.iptvdiscovery+xml",
            PermissibleValue(text="application/vnd.etsi.iptvdiscovery+xml"))
        setattr(cls, "application/vnd.etsi.iptvprofile+xml",
            PermissibleValue(text="application/vnd.etsi.iptvprofile+xml"))
        setattr(cls, "application/vnd.etsi.iptvsad-bc+xml",
            PermissibleValue(text="application/vnd.etsi.iptvsad-bc+xml"))
        setattr(cls, "application/vnd.etsi.iptvsad-cod+xml",
            PermissibleValue(text="application/vnd.etsi.iptvsad-cod+xml"))
        setattr(cls, "application/vnd.etsi.iptvsad-npvr+xml",
            PermissibleValue(text="application/vnd.etsi.iptvsad-npvr+xml"))
        setattr(cls, "application/vnd.etsi.iptvservice+xml",
            PermissibleValue(text="application/vnd.etsi.iptvservice+xml"))
        setattr(cls, "application/vnd.etsi.iptvsync+xml",
            PermissibleValue(text="application/vnd.etsi.iptvsync+xml"))
        setattr(cls, "application/vnd.etsi.iptvueprofile+xml",
            PermissibleValue(text="application/vnd.etsi.iptvueprofile+xml"))
        setattr(cls, "application/vnd.etsi.mcid+xml",
            PermissibleValue(text="application/vnd.etsi.mcid+xml"))
        setattr(cls, "application/vnd.etsi.mheg5",
            PermissibleValue(text="application/vnd.etsi.mheg5"))
        setattr(cls, "application/vnd.etsi.overload-control-policy-dataset+xml",
            PermissibleValue(text="application/vnd.etsi.overload-control-policy-dataset+xml"))
        setattr(cls, "application/vnd.etsi.pstn+xml",
            PermissibleValue(text="application/vnd.etsi.pstn+xml"))
        setattr(cls, "application/vnd.etsi.sci+xml",
            PermissibleValue(text="application/vnd.etsi.sci+xml"))
        setattr(cls, "application/vnd.etsi.simservs+xml",
            PermissibleValue(text="application/vnd.etsi.simservs+xml"))
        setattr(cls, "application/vnd.etsi.timestamp-token",
            PermissibleValue(text="application/vnd.etsi.timestamp-token"))
        setattr(cls, "application/vnd.etsi.tsl.der",
            PermissibleValue(text="application/vnd.etsi.tsl.der"))
        setattr(cls, "application/vnd.etsi.tsl+xml",
            PermissibleValue(text="application/vnd.etsi.tsl+xml"))
        setattr(cls, "application/vnd.eu.kasparian.car+json",
            PermissibleValue(text="application/vnd.eu.kasparian.car+json"))
        setattr(cls, "application/vnd.eudora.data",
            PermissibleValue(text="application/vnd.eudora.data"))
        setattr(cls, "application/vnd.evolv.ecig.profile",
            PermissibleValue(text="application/vnd.evolv.ecig.profile"))
        setattr(cls, "application/vnd.evolv.ecig.settings",
            PermissibleValue(text="application/vnd.evolv.ecig.settings"))
        setattr(cls, "application/vnd.evolv.ecig.theme",
            PermissibleValue(text="application/vnd.evolv.ecig.theme"))
        setattr(cls, "application/vnd.exstream-empower+zip",
            PermissibleValue(text="application/vnd.exstream-empower+zip"))
        setattr(cls, "application/vnd.exstream-package",
            PermissibleValue(text="application/vnd.exstream-package"))
        setattr(cls, "application/vnd.ezpix-album",
            PermissibleValue(text="application/vnd.ezpix-album"))
        setattr(cls, "application/vnd.ezpix-package",
            PermissibleValue(text="application/vnd.ezpix-package"))
        setattr(cls, "application/vnd.familysearch.gedcom+zip",
            PermissibleValue(text="application/vnd.familysearch.gedcom+zip"))
        setattr(cls, "application/vnd.fastcopy-disk-image",
            PermissibleValue(text="application/vnd.fastcopy-disk-image"))
        setattr(cls, "application/vnd.fdsn.mseed",
            PermissibleValue(text="application/vnd.fdsn.mseed"))
        setattr(cls, "application/vnd.fdsn.seed",
            PermissibleValue(text="application/vnd.fdsn.seed"))
        setattr(cls, "application/vnd.fdsn.stationxml+xml",
            PermissibleValue(text="application/vnd.fdsn.stationxml+xml"))
        setattr(cls, "application/vnd.ffsns",
            PermissibleValue(text="application/vnd.ffsns"))
        setattr(cls, "application/vnd.ficlab.flb+zip",
            PermissibleValue(text="application/vnd.ficlab.flb+zip"))
        setattr(cls, "application/vnd.filmit.zfc",
            PermissibleValue(text="application/vnd.filmit.zfc"))
        setattr(cls, "application/vnd.fints",
            PermissibleValue(text="application/vnd.fints"))
        setattr(cls, "application/vnd.firemonkeys.cloudcell",
            PermissibleValue(text="application/vnd.firemonkeys.cloudcell"))
        setattr(cls, "application/vnd.FloGraphIt",
            PermissibleValue(text="application/vnd.FloGraphIt"))
        setattr(cls, "application/vnd.fluxtime.clip",
            PermissibleValue(text="application/vnd.fluxtime.clip"))
        setattr(cls, "application/vnd.font-fontforge-sfd",
            PermissibleValue(text="application/vnd.font-fontforge-sfd"))
        setattr(cls, "application/vnd.framemaker",
            PermissibleValue(text="application/vnd.framemaker"))
        setattr(cls, "application/vnd.freelog.comic",
            PermissibleValue(text="application/vnd.freelog.comic"))
        setattr(cls, "application/vnd.frogans.fnc",
            PermissibleValue(text="application/vnd.frogans.fnc"))
        setattr(cls, "application/vnd.frogans.ltf",
            PermissibleValue(text="application/vnd.frogans.ltf"))
        setattr(cls, "application/vnd.fsc.weblaunch",
            PermissibleValue(text="application/vnd.fsc.weblaunch"))
        setattr(cls, "application/vnd.f-secure.mobile",
            PermissibleValue(text="application/vnd.f-secure.mobile"))
        setattr(cls, "application/vnd.fujifilm.fb.docuworks",
            PermissibleValue(text="application/vnd.fujifilm.fb.docuworks"))
        setattr(cls, "application/vnd.fujifilm.fb.docuworks.binder",
            PermissibleValue(text="application/vnd.fujifilm.fb.docuworks.binder"))
        setattr(cls, "application/vnd.fujifilm.fb.docuworks.container",
            PermissibleValue(text="application/vnd.fujifilm.fb.docuworks.container"))
        setattr(cls, "application/vnd.fujifilm.fb.jfi+xml",
            PermissibleValue(text="application/vnd.fujifilm.fb.jfi+xml"))
        setattr(cls, "application/vnd.fujitsu.oasys",
            PermissibleValue(text="application/vnd.fujitsu.oasys"))
        setattr(cls, "application/vnd.fujitsu.oasys2",
            PermissibleValue(text="application/vnd.fujitsu.oasys2"))
        setattr(cls, "application/vnd.fujitsu.oasys3",
            PermissibleValue(text="application/vnd.fujitsu.oasys3"))
        setattr(cls, "application/vnd.fujitsu.oasysgp",
            PermissibleValue(text="application/vnd.fujitsu.oasysgp"))
        setattr(cls, "application/vnd.fujitsu.oasysprs",
            PermissibleValue(text="application/vnd.fujitsu.oasysprs"))
        setattr(cls, "application/vnd.fujixerox.ART4",
            PermissibleValue(text="application/vnd.fujixerox.ART4"))
        setattr(cls, "application/vnd.fujixerox.ART-EX",
            PermissibleValue(text="application/vnd.fujixerox.ART-EX"))
        setattr(cls, "application/vnd.fujixerox.ddd",
            PermissibleValue(text="application/vnd.fujixerox.ddd"))
        setattr(cls, "application/vnd.fujixerox.docuworks",
            PermissibleValue(text="application/vnd.fujixerox.docuworks"))
        setattr(cls, "application/vnd.fujixerox.docuworks.binder",
            PermissibleValue(text="application/vnd.fujixerox.docuworks.binder"))
        setattr(cls, "application/vnd.fujixerox.docuworks.container",
            PermissibleValue(text="application/vnd.fujixerox.docuworks.container"))
        setattr(cls, "application/vnd.fujixerox.HBPL",
            PermissibleValue(text="application/vnd.fujixerox.HBPL"))
        setattr(cls, "application/vnd.fut-misnet",
            PermissibleValue(text="application/vnd.fut-misnet"))
        setattr(cls, "application/vnd.futoin+cbor",
            PermissibleValue(text="application/vnd.futoin+cbor"))
        setattr(cls, "application/vnd.futoin+json",
            PermissibleValue(text="application/vnd.futoin+json"))
        setattr(cls, "application/vnd.fuzzysheet",
            PermissibleValue(text="application/vnd.fuzzysheet"))
        setattr(cls, "application/vnd.ga4gh.passport+jwt",
            PermissibleValue(text="application/vnd.ga4gh.passport+jwt"))
        setattr(cls, "application/vnd.genomatix.tuxedo",
            PermissibleValue(text="application/vnd.genomatix.tuxedo"))
        setattr(cls, "application/vnd.genozip",
            PermissibleValue(text="application/vnd.genozip"))
        setattr(cls, "application/vnd.gentics.grd+json",
            PermissibleValue(text="application/vnd.gentics.grd+json"))
        setattr(cls, "application/vnd.gentoo.catmetadata+xml",
            PermissibleValue(text="application/vnd.gentoo.catmetadata+xml"))
        setattr(cls, "application/vnd.gentoo.ebuild",
            PermissibleValue(text="application/vnd.gentoo.ebuild"))
        setattr(cls, "application/vnd.gentoo.eclass",
            PermissibleValue(text="application/vnd.gentoo.eclass"))
        setattr(cls, "application/vnd.gentoo.gpkg",
            PermissibleValue(text="application/vnd.gentoo.gpkg"))
        setattr(cls, "application/vnd.gentoo.manifest",
            PermissibleValue(text="application/vnd.gentoo.manifest"))
        setattr(cls, "application/vnd.gentoo.pkgmetadata+xml",
            PermissibleValue(text="application/vnd.gentoo.pkgmetadata+xml"))
        setattr(cls, "application/vnd.gentoo.xpak",
            PermissibleValue(text="application/vnd.gentoo.xpak"))
        setattr(cls, "application/vnd.geo+json",
            PermissibleValue(text="application/vnd.geo+json"))
        setattr(cls, "application/vnd.geocube+xml",
            PermissibleValue(text="application/vnd.geocube+xml"))
        setattr(cls, "application/vnd.geogebra.file",
            PermissibleValue(text="application/vnd.geogebra.file"))
        setattr(cls, "application/vnd.geogebra.pinboard",
            PermissibleValue(text="application/vnd.geogebra.pinboard"))
        setattr(cls, "application/vnd.geogebra.slides",
            PermissibleValue(text="application/vnd.geogebra.slides"))
        setattr(cls, "application/vnd.geogebra.tool",
            PermissibleValue(text="application/vnd.geogebra.tool"))
        setattr(cls, "application/vnd.geometry-explorer",
            PermissibleValue(text="application/vnd.geometry-explorer"))
        setattr(cls, "application/vnd.geonext",
            PermissibleValue(text="application/vnd.geonext"))
        setattr(cls, "application/vnd.geoplan",
            PermissibleValue(text="application/vnd.geoplan"))
        setattr(cls, "application/vnd.geospace",
            PermissibleValue(text="application/vnd.geospace"))
        setattr(cls, "application/vnd.gerber",
            PermissibleValue(text="application/vnd.gerber"))
        setattr(cls, "application/vnd.globalplatform.card-content-mgt",
            PermissibleValue(text="application/vnd.globalplatform.card-content-mgt"))
        setattr(cls, "application/vnd.globalplatform.card-content-mgt-response",
            PermissibleValue(text="application/vnd.globalplatform.card-content-mgt-response"))
        setattr(cls, "application/vnd.gmx",
            PermissibleValue(text="application/vnd.gmx"))
        setattr(cls, "application/vnd.gnu.taler.exchange+json",
            PermissibleValue(text="application/vnd.gnu.taler.exchange+json"))
        setattr(cls, "application/vnd.gnu.taler.merchant+json",
            PermissibleValue(text="application/vnd.gnu.taler.merchant+json"))
        setattr(cls, "application/vnd.google-earth.kml+xml",
            PermissibleValue(text="application/vnd.google-earth.kml+xml"))
        setattr(cls, "application/vnd.google-earth.kmz",
            PermissibleValue(text="application/vnd.google-earth.kmz"))
        setattr(cls, "application/vnd.gov.sk.e-form+xml",
            PermissibleValue(text="application/vnd.gov.sk.e-form+xml"))
        setattr(cls, "application/vnd.gov.sk.e-form+zip",
            PermissibleValue(text="application/vnd.gov.sk.e-form+zip"))
        setattr(cls, "application/vnd.gov.sk.xmldatacontainer+xml",
            PermissibleValue(text="application/vnd.gov.sk.xmldatacontainer+xml"))
        setattr(cls, "application/vnd.gpxsee.map+xml",
            PermissibleValue(text="application/vnd.gpxsee.map+xml"))
        setattr(cls, "application/vnd.grafeq",
            PermissibleValue(text="application/vnd.grafeq"))
        setattr(cls, "application/vnd.gridmp",
            PermissibleValue(text="application/vnd.gridmp"))
        setattr(cls, "application/vnd.groove-account",
            PermissibleValue(text="application/vnd.groove-account"))
        setattr(cls, "application/vnd.groove-help",
            PermissibleValue(text="application/vnd.groove-help"))
        setattr(cls, "application/vnd.groove-identity-message",
            PermissibleValue(text="application/vnd.groove-identity-message"))
        setattr(cls, "application/vnd.groove-injector",
            PermissibleValue(text="application/vnd.groove-injector"))
        setattr(cls, "application/vnd.groove-tool-message",
            PermissibleValue(text="application/vnd.groove-tool-message"))
        setattr(cls, "application/vnd.groove-tool-template",
            PermissibleValue(text="application/vnd.groove-tool-template"))
        setattr(cls, "application/vnd.groove-vcard",
            PermissibleValue(text="application/vnd.groove-vcard"))
        setattr(cls, "application/vnd.hal+json",
            PermissibleValue(text="application/vnd.hal+json"))
        setattr(cls, "application/vnd.hal+xml",
            PermissibleValue(text="application/vnd.hal+xml"))
        setattr(cls, "application/vnd.HandHeld-Entertainment+xml",
            PermissibleValue(text="application/vnd.HandHeld-Entertainment+xml"))
        setattr(cls, "application/vnd.hbci",
            PermissibleValue(text="application/vnd.hbci"))
        setattr(cls, "application/vnd.hc+json",
            PermissibleValue(text="application/vnd.hc+json"))
        setattr(cls, "application/vnd.hcl-bireports",
            PermissibleValue(text="application/vnd.hcl-bireports"))
        setattr(cls, "application/vnd.hdt",
            PermissibleValue(text="application/vnd.hdt"))
        setattr(cls, "application/vnd.heroku+json",
            PermissibleValue(text="application/vnd.heroku+json"))
        setattr(cls, "application/vnd.hhe.lesson-player",
            PermissibleValue(text="application/vnd.hhe.lesson-player"))
        setattr(cls, "application/vnd.hp-HPGL",
            PermissibleValue(text="application/vnd.hp-HPGL"))
        setattr(cls, "application/vnd.hp-hpid",
            PermissibleValue(text="application/vnd.hp-hpid"))
        setattr(cls, "application/vnd.hp-hps",
            PermissibleValue(text="application/vnd.hp-hps"))
        setattr(cls, "application/vnd.hp-jlyt",
            PermissibleValue(text="application/vnd.hp-jlyt"))
        setattr(cls, "application/vnd.hp-PCL",
            PermissibleValue(text="application/vnd.hp-PCL"))
        setattr(cls, "application/vnd.hp-PCLXL",
            PermissibleValue(text="application/vnd.hp-PCLXL"))
        setattr(cls, "application/vnd.hsl",
            PermissibleValue(text="application/vnd.hsl"))
        setattr(cls, "application/vnd.httphone",
            PermissibleValue(text="application/vnd.httphone"))
        setattr(cls, "application/vnd.hydrostatix.sof-data",
            PermissibleValue(text="application/vnd.hydrostatix.sof-data"))
        setattr(cls, "application/vnd.hyper+json",
            PermissibleValue(text="application/vnd.hyper+json"))
        setattr(cls, "application/vnd.hyperdrive+json",
            PermissibleValue(text="application/vnd.hyperdrive+json"))
        setattr(cls, "application/vnd.hyper-item+json",
            PermissibleValue(text="application/vnd.hyper-item+json"))
        setattr(cls, "application/vnd.hzn-3d-crossword",
            PermissibleValue(text="application/vnd.hzn-3d-crossword"))
        setattr(cls, "application/vnd.ibm.afplinedata",
            PermissibleValue(text="application/vnd.ibm.afplinedata"))
        setattr(cls, "application/vnd.ibm.electronic-media",
            PermissibleValue(text="application/vnd.ibm.electronic-media"))
        setattr(cls, "application/vnd.ibm.MiniPay",
            PermissibleValue(text="application/vnd.ibm.MiniPay"))
        setattr(cls, "application/vnd.ibm.modcap",
            PermissibleValue(text="application/vnd.ibm.modcap"))
        setattr(cls, "application/vnd.ibm.rights-management",
            PermissibleValue(text="application/vnd.ibm.rights-management"))
        setattr(cls, "application/vnd.ibm.secure-container",
            PermissibleValue(text="application/vnd.ibm.secure-container"))
        setattr(cls, "application/vnd.iccprofile",
            PermissibleValue(text="application/vnd.iccprofile"))
        setattr(cls, "application/vnd.ieee.1905",
            PermissibleValue(text="application/vnd.ieee.1905"))
        setattr(cls, "application/vnd.igloader",
            PermissibleValue(text="application/vnd.igloader"))
        setattr(cls, "application/vnd.imagemeter.folder+zip",
            PermissibleValue(text="application/vnd.imagemeter.folder+zip"))
        setattr(cls, "application/vnd.imagemeter.image+zip",
            PermissibleValue(text="application/vnd.imagemeter.image+zip"))
        setattr(cls, "application/vnd.immervision-ivp",
            PermissibleValue(text="application/vnd.immervision-ivp"))
        setattr(cls, "application/vnd.immervision-ivu",
            PermissibleValue(text="application/vnd.immervision-ivu"))
        setattr(cls, "application/vnd.ims.imsccv1p1",
            PermissibleValue(text="application/vnd.ims.imsccv1p1"))
        setattr(cls, "application/vnd.ims.imsccv1p2",
            PermissibleValue(text="application/vnd.ims.imsccv1p2"))
        setattr(cls, "application/vnd.ims.imsccv1p3",
            PermissibleValue(text="application/vnd.ims.imsccv1p3"))
        setattr(cls, "application/vnd.ims.lis.v2.result+json",
            PermissibleValue(text="application/vnd.ims.lis.v2.result+json"))
        setattr(cls, "application/vnd.ims.lti.v2.toolconsumerprofile+json",
            PermissibleValue(text="application/vnd.ims.lti.v2.toolconsumerprofile+json"))
        setattr(cls, "application/vnd.ims.lti.v2.toolproxy.id+json",
            PermissibleValue(text="application/vnd.ims.lti.v2.toolproxy.id+json"))
        setattr(cls, "application/vnd.ims.lti.v2.toolproxy+json",
            PermissibleValue(text="application/vnd.ims.lti.v2.toolproxy+json"))
        setattr(cls, "application/vnd.ims.lti.v2.toolsettings.simple+json",
            PermissibleValue(text="application/vnd.ims.lti.v2.toolsettings.simple+json"))
        setattr(cls, "application/vnd.ims.lti.v2.toolsettings+json",
            PermissibleValue(text="application/vnd.ims.lti.v2.toolsettings+json"))
        setattr(cls, "application/vnd.informedcontrol.rms+xml",
            PermissibleValue(text="application/vnd.informedcontrol.rms+xml"))
        setattr(cls, "application/vnd.informix-visionary",
            PermissibleValue(text="application/vnd.informix-visionary"))
        setattr(cls, "application/vnd.infotech.project",
            PermissibleValue(text="application/vnd.infotech.project"))
        setattr(cls, "application/vnd.infotech.project+xml",
            PermissibleValue(text="application/vnd.infotech.project+xml"))
        setattr(cls, "application/vnd.innopath.wamp.notification",
            PermissibleValue(text="application/vnd.innopath.wamp.notification"))
        setattr(cls, "application/vnd.insors.igm",
            PermissibleValue(text="application/vnd.insors.igm"))
        setattr(cls, "application/vnd.intercon.formnet",
            PermissibleValue(text="application/vnd.intercon.formnet"))
        setattr(cls, "application/vnd.intergeo",
            PermissibleValue(text="application/vnd.intergeo"))
        setattr(cls, "application/vnd.intertrust.digibox",
            PermissibleValue(text="application/vnd.intertrust.digibox"))
        setattr(cls, "application/vnd.intertrust.nncp",
            PermissibleValue(text="application/vnd.intertrust.nncp"))
        setattr(cls, "application/vnd.intu.qbo",
            PermissibleValue(text="application/vnd.intu.qbo"))
        setattr(cls, "application/vnd.intu.qfx",
            PermissibleValue(text="application/vnd.intu.qfx"))
        setattr(cls, "application/vnd.ipfs.ipns-record",
            PermissibleValue(text="application/vnd.ipfs.ipns-record"))
        setattr(cls, "application/vnd.ipld.car",
            PermissibleValue(text="application/vnd.ipld.car"))
        setattr(cls, "application/vnd.ipld.dag-cbor",
            PermissibleValue(text="application/vnd.ipld.dag-cbor"))
        setattr(cls, "application/vnd.ipld.dag-json",
            PermissibleValue(text="application/vnd.ipld.dag-json"))
        setattr(cls, "application/vnd.ipld.raw",
            PermissibleValue(text="application/vnd.ipld.raw"))
        setattr(cls, "application/vnd.iptc.g2.catalogitem+xml",
            PermissibleValue(text="application/vnd.iptc.g2.catalogitem+xml"))
        setattr(cls, "application/vnd.iptc.g2.conceptitem+xml",
            PermissibleValue(text="application/vnd.iptc.g2.conceptitem+xml"))
        setattr(cls, "application/vnd.iptc.g2.knowledgeitem+xml",
            PermissibleValue(text="application/vnd.iptc.g2.knowledgeitem+xml"))
        setattr(cls, "application/vnd.iptc.g2.newsitem+xml",
            PermissibleValue(text="application/vnd.iptc.g2.newsitem+xml"))
        setattr(cls, "application/vnd.iptc.g2.newsmessage+xml",
            PermissibleValue(text="application/vnd.iptc.g2.newsmessage+xml"))
        setattr(cls, "application/vnd.iptc.g2.packageitem+xml",
            PermissibleValue(text="application/vnd.iptc.g2.packageitem+xml"))
        setattr(cls, "application/vnd.iptc.g2.planningitem+xml",
            PermissibleValue(text="application/vnd.iptc.g2.planningitem+xml"))
        setattr(cls, "application/vnd.ipunplugged.rcprofile",
            PermissibleValue(text="application/vnd.ipunplugged.rcprofile"))
        setattr(cls, "application/vnd.irepository.package+xml",
            PermissibleValue(text="application/vnd.irepository.package+xml"))
        setattr(cls, "application/vnd.isac.fcs",
            PermissibleValue(text="application/vnd.isac.fcs"))
        setattr(cls, "application/vnd.iso11783-10+zip",
            PermissibleValue(text="application/vnd.iso11783-10+zip"))
        setattr(cls, "application/vnd.is-xpr",
            PermissibleValue(text="application/vnd.is-xpr"))
        setattr(cls, "application/vnd.jam",
            PermissibleValue(text="application/vnd.jam"))
        setattr(cls, "application/vnd.japannet-directory-service",
            PermissibleValue(text="application/vnd.japannet-directory-service"))
        setattr(cls, "application/vnd.japannet-jpnstore-wakeup",
            PermissibleValue(text="application/vnd.japannet-jpnstore-wakeup"))
        setattr(cls, "application/vnd.japannet-payment-wakeup",
            PermissibleValue(text="application/vnd.japannet-payment-wakeup"))
        setattr(cls, "application/vnd.japannet-registration",
            PermissibleValue(text="application/vnd.japannet-registration"))
        setattr(cls, "application/vnd.japannet-registration-wakeup",
            PermissibleValue(text="application/vnd.japannet-registration-wakeup"))
        setattr(cls, "application/vnd.japannet-setstore-wakeup",
            PermissibleValue(text="application/vnd.japannet-setstore-wakeup"))
        setattr(cls, "application/vnd.japannet-verification",
            PermissibleValue(text="application/vnd.japannet-verification"))
        setattr(cls, "application/vnd.japannet-verification-wakeup",
            PermissibleValue(text="application/vnd.japannet-verification-wakeup"))
        setattr(cls, "application/vnd.jcp.javame.midlet-rms",
            PermissibleValue(text="application/vnd.jcp.javame.midlet-rms"))
        setattr(cls, "application/vnd.jisp",
            PermissibleValue(text="application/vnd.jisp"))
        setattr(cls, "application/vnd.joost.joda-archive",
            PermissibleValue(text="application/vnd.joost.joda-archive"))
        setattr(cls, "application/vnd.jsk.isdn-ngn",
            PermissibleValue(text="application/vnd.jsk.isdn-ngn"))
        setattr(cls, "application/vnd.kahootz",
            PermissibleValue(text="application/vnd.kahootz"))
        setattr(cls, "application/vnd.kde.karbon",
            PermissibleValue(text="application/vnd.kde.karbon"))
        setattr(cls, "application/vnd.kde.kchart",
            PermissibleValue(text="application/vnd.kde.kchart"))
        setattr(cls, "application/vnd.kde.kformula",
            PermissibleValue(text="application/vnd.kde.kformula"))
        setattr(cls, "application/vnd.kde.kivio",
            PermissibleValue(text="application/vnd.kde.kivio"))
        setattr(cls, "application/vnd.kde.kontour",
            PermissibleValue(text="application/vnd.kde.kontour"))
        setattr(cls, "application/vnd.kde.kpresenter",
            PermissibleValue(text="application/vnd.kde.kpresenter"))
        setattr(cls, "application/vnd.kde.kspread",
            PermissibleValue(text="application/vnd.kde.kspread"))
        setattr(cls, "application/vnd.kde.kword",
            PermissibleValue(text="application/vnd.kde.kword"))
        setattr(cls, "application/vnd.kdl",
            PermissibleValue(text="application/vnd.kdl"))
        setattr(cls, "application/vnd.kenameaapp",
            PermissibleValue(text="application/vnd.kenameaapp"))
        setattr(cls, "application/vnd.keyman.kmp+zip",
            PermissibleValue(text="application/vnd.keyman.kmp+zip"))
        setattr(cls, "application/vnd.keyman.kmx",
            PermissibleValue(text="application/vnd.keyman.kmx"))
        setattr(cls, "application/vnd.kidspiration",
            PermissibleValue(text="application/vnd.kidspiration"))
        setattr(cls, "application/vnd.Kinar",
            PermissibleValue(text="application/vnd.Kinar"))
        setattr(cls, "application/vnd.koan",
            PermissibleValue(text="application/vnd.koan"))
        setattr(cls, "application/vnd.kodak-descriptor",
            PermissibleValue(text="application/vnd.kodak-descriptor"))
        setattr(cls, "application/vnd.las",
            PermissibleValue(text="application/vnd.las"))
        setattr(cls, "application/vnd.las.las+json",
            PermissibleValue(text="application/vnd.las.las+json"))
        setattr(cls, "application/vnd.las.las+xml",
            PermissibleValue(text="application/vnd.las.las+xml"))
        setattr(cls, "application/vnd.laszip",
            PermissibleValue(text="application/vnd.laszip"))
        setattr(cls, "application/vnd.ldev.productlicensing",
            PermissibleValue(text="application/vnd.ldev.productlicensing"))
        setattr(cls, "application/vnd.leap+json",
            PermissibleValue(text="application/vnd.leap+json"))
        setattr(cls, "application/vnd.liberty-request+xml",
            PermissibleValue(text="application/vnd.liberty-request+xml"))
        setattr(cls, "application/vnd.llamagraphics.life-balance.desktop",
            PermissibleValue(text="application/vnd.llamagraphics.life-balance.desktop"))
        setattr(cls, "application/vnd.llamagraphics.life-balance.exchange+xml",
            PermissibleValue(text="application/vnd.llamagraphics.life-balance.exchange+xml"))
        setattr(cls, "application/vnd.logipipe.circuit+zip",
            PermissibleValue(text="application/vnd.logipipe.circuit+zip"))
        setattr(cls, "application/vnd.loom",
            PermissibleValue(text="application/vnd.loom"))
        setattr(cls, "application/vnd.lotus-1-2-3",
            PermissibleValue(text="application/vnd.lotus-1-2-3"))
        setattr(cls, "application/vnd.lotus-approach",
            PermissibleValue(text="application/vnd.lotus-approach"))
        setattr(cls, "application/vnd.lotus-freelance",
            PermissibleValue(text="application/vnd.lotus-freelance"))
        setattr(cls, "application/vnd.lotus-notes",
            PermissibleValue(text="application/vnd.lotus-notes"))
        setattr(cls, "application/vnd.lotus-organizer",
            PermissibleValue(text="application/vnd.lotus-organizer"))
        setattr(cls, "application/vnd.lotus-screencam",
            PermissibleValue(text="application/vnd.lotus-screencam"))
        setattr(cls, "application/vnd.lotus-wordpro",
            PermissibleValue(text="application/vnd.lotus-wordpro"))
        setattr(cls, "application/vnd.macports.portpkg",
            PermissibleValue(text="application/vnd.macports.portpkg"))
        setattr(cls, "application/vnd.mapbox-vector-tile",
            PermissibleValue(text="application/vnd.mapbox-vector-tile"))
        setattr(cls, "application/vnd.marlin.drm.actiontoken+xml",
            PermissibleValue(text="application/vnd.marlin.drm.actiontoken+xml"))
        setattr(cls, "application/vnd.marlin.drm.conftoken+xml",
            PermissibleValue(text="application/vnd.marlin.drm.conftoken+xml"))
        setattr(cls, "application/vnd.marlin.drm.license+xml",
            PermissibleValue(text="application/vnd.marlin.drm.license+xml"))
        setattr(cls, "application/vnd.marlin.drm.mdcf",
            PermissibleValue(text="application/vnd.marlin.drm.mdcf"))
        setattr(cls, "application/vnd.mason+json",
            PermissibleValue(text="application/vnd.mason+json"))
        setattr(cls, "application/vnd.maxar.archive.3tz+zip",
            PermissibleValue(text="application/vnd.maxar.archive.3tz+zip"))
        setattr(cls, "application/vnd.maxmind.maxmind-db",
            PermissibleValue(text="application/vnd.maxmind.maxmind-db"))
        setattr(cls, "application/vnd.mcd",
            PermissibleValue(text="application/vnd.mcd"))
        setattr(cls, "application/vnd.mdl",
            PermissibleValue(text="application/vnd.mdl"))
        setattr(cls, "application/vnd.mdl-mbsdf",
            PermissibleValue(text="application/vnd.mdl-mbsdf"))
        setattr(cls, "application/vnd.medcalcdata",
            PermissibleValue(text="application/vnd.medcalcdata"))
        setattr(cls, "application/vnd.mediastation.cdkey",
            PermissibleValue(text="application/vnd.mediastation.cdkey"))
        setattr(cls, "application/vnd.medicalholodeck.recordxr",
            PermissibleValue(text="application/vnd.medicalholodeck.recordxr"))
        setattr(cls, "application/vnd.meridian-slingshot",
            PermissibleValue(text="application/vnd.meridian-slingshot"))
        setattr(cls, "application/vnd.mermaid",
            PermissibleValue(text="application/vnd.mermaid"))
        setattr(cls, "application/vnd.MFER",
            PermissibleValue(text="application/vnd.MFER"))
        setattr(cls, "application/vnd.mfmp",
            PermissibleValue(text="application/vnd.mfmp"))
        setattr(cls, "application/vnd.micro+json",
            PermissibleValue(text="application/vnd.micro+json"))
        setattr(cls, "application/vnd.micrografx.flo",
            PermissibleValue(text="application/vnd.micrografx.flo"))
        setattr(cls, "application/vnd.micrografx.igx",
            PermissibleValue(text="application/vnd.micrografx.igx"))
        setattr(cls, "application/vnd.microsoft.portable-executable",
            PermissibleValue(text="application/vnd.microsoft.portable-executable"))
        setattr(cls, "application/vnd.microsoft.windows.thumbnail-cache",
            PermissibleValue(text="application/vnd.microsoft.windows.thumbnail-cache"))
        setattr(cls, "application/vnd.miele+json",
            PermissibleValue(text="application/vnd.miele+json"))
        setattr(cls, "application/vnd.mif",
            PermissibleValue(text="application/vnd.mif"))
        setattr(cls, "application/vnd.minisoft-hp3000-save",
            PermissibleValue(text="application/vnd.minisoft-hp3000-save"))
        setattr(cls, "application/vnd.mitsubishi.misty-guard.trustweb",
            PermissibleValue(text="application/vnd.mitsubishi.misty-guard.trustweb"))
        setattr(cls, "application/vnd.Mobius.DAF",
            PermissibleValue(text="application/vnd.Mobius.DAF"))
        setattr(cls, "application/vnd.Mobius.DIS",
            PermissibleValue(text="application/vnd.Mobius.DIS"))
        setattr(cls, "application/vnd.Mobius.MBK",
            PermissibleValue(text="application/vnd.Mobius.MBK"))
        setattr(cls, "application/vnd.Mobius.MQY",
            PermissibleValue(text="application/vnd.Mobius.MQY"))
        setattr(cls, "application/vnd.Mobius.MSL",
            PermissibleValue(text="application/vnd.Mobius.MSL"))
        setattr(cls, "application/vnd.Mobius.PLC",
            PermissibleValue(text="application/vnd.Mobius.PLC"))
        setattr(cls, "application/vnd.Mobius.TXF",
            PermissibleValue(text="application/vnd.Mobius.TXF"))
        setattr(cls, "application/vnd.modl",
            PermissibleValue(text="application/vnd.modl"))
        setattr(cls, "application/vnd.mophun.application",
            PermissibleValue(text="application/vnd.mophun.application"))
        setattr(cls, "application/vnd.mophun.certificate",
            PermissibleValue(text="application/vnd.mophun.certificate"))
        setattr(cls, "application/vnd.motorola.flexsuite",
            PermissibleValue(text="application/vnd.motorola.flexsuite"))
        setattr(cls, "application/vnd.motorola.flexsuite.adsi",
            PermissibleValue(text="application/vnd.motorola.flexsuite.adsi"))
        setattr(cls, "application/vnd.motorola.flexsuite.fis",
            PermissibleValue(text="application/vnd.motorola.flexsuite.fis"))
        setattr(cls, "application/vnd.motorola.flexsuite.gotap",
            PermissibleValue(text="application/vnd.motorola.flexsuite.gotap"))
        setattr(cls, "application/vnd.motorola.flexsuite.kmr",
            PermissibleValue(text="application/vnd.motorola.flexsuite.kmr"))
        setattr(cls, "application/vnd.motorola.flexsuite.ttc",
            PermissibleValue(text="application/vnd.motorola.flexsuite.ttc"))
        setattr(cls, "application/vnd.motorola.flexsuite.wem",
            PermissibleValue(text="application/vnd.motorola.flexsuite.wem"))
        setattr(cls, "application/vnd.motorola.iprm",
            PermissibleValue(text="application/vnd.motorola.iprm"))
        setattr(cls, "application/vnd.mozilla.xul+xml",
            PermissibleValue(text="application/vnd.mozilla.xul+xml"))
        setattr(cls, "application/vnd.ms-3mfdocument",
            PermissibleValue(text="application/vnd.ms-3mfdocument"))
        setattr(cls, "application/vnd.msa-disk-image",
            PermissibleValue(text="application/vnd.msa-disk-image"))
        setattr(cls, "application/vnd.ms-artgalry",
            PermissibleValue(text="application/vnd.ms-artgalry"))
        setattr(cls, "application/vnd.ms-asf",
            PermissibleValue(text="application/vnd.ms-asf"))
        setattr(cls, "application/vnd.ms-cab-compressed",
            PermissibleValue(text="application/vnd.ms-cab-compressed"))
        setattr(cls, "application/vnd.mseq",
            PermissibleValue(text="application/vnd.mseq"))
        setattr(cls, "application/vnd.ms-excel",
            PermissibleValue(text="application/vnd.ms-excel"))
        setattr(cls, "application/vnd.ms-excel.addin.macroEnabled.12",
            PermissibleValue(text="application/vnd.ms-excel.addin.macroEnabled.12"))
        setattr(cls, "application/vnd.ms-excel.sheet.binary.macroEnabled.12",
            PermissibleValue(text="application/vnd.ms-excel.sheet.binary.macroEnabled.12"))
        setattr(cls, "application/vnd.ms-excel.sheet.macroEnabled.12",
            PermissibleValue(text="application/vnd.ms-excel.sheet.macroEnabled.12"))
        setattr(cls, "application/vnd.ms-excel.template.macroEnabled.12",
            PermissibleValue(text="application/vnd.ms-excel.template.macroEnabled.12"))
        setattr(cls, "application/vnd.ms-fontobject",
            PermissibleValue(text="application/vnd.ms-fontobject"))
        setattr(cls, "application/vnd.msgpack",
            PermissibleValue(text="application/vnd.msgpack"))
        setattr(cls, "application/vnd.ms-htmlhelp",
            PermissibleValue(text="application/vnd.ms-htmlhelp"))
        setattr(cls, "application/vnd.msign",
            PermissibleValue(text="application/vnd.msign"))
        setattr(cls, "application/vnd.ms-ims",
            PermissibleValue(text="application/vnd.ms-ims"))
        setattr(cls, "application/vnd.ms-lrm",
            PermissibleValue(text="application/vnd.ms-lrm"))
        setattr(cls, "application/vnd.ms-office.activeX+xml",
            PermissibleValue(text="application/vnd.ms-office.activeX+xml"))
        setattr(cls, "application/vnd.ms-officetheme",
            PermissibleValue(text="application/vnd.ms-officetheme"))
        setattr(cls, "application/vnd.ms-playready.initiator+xml",
            PermissibleValue(text="application/vnd.ms-playready.initiator+xml"))
        setattr(cls, "application/vnd.ms-powerpoint",
            PermissibleValue(text="application/vnd.ms-powerpoint"))
        setattr(cls, "application/vnd.ms-powerpoint.addin.macroEnabled.12",
            PermissibleValue(text="application/vnd.ms-powerpoint.addin.macroEnabled.12"))
        setattr(cls, "application/vnd.ms-powerpoint.presentation.macroEnabled.12",
            PermissibleValue(text="application/vnd.ms-powerpoint.presentation.macroEnabled.12"))
        setattr(cls, "application/vnd.ms-powerpoint.slide.macroEnabled.12",
            PermissibleValue(text="application/vnd.ms-powerpoint.slide.macroEnabled.12"))
        setattr(cls, "application/vnd.ms-powerpoint.slideshow.macroEnabled.12",
            PermissibleValue(text="application/vnd.ms-powerpoint.slideshow.macroEnabled.12"))
        setattr(cls, "application/vnd.ms-powerpoint.template.macroEnabled.12",
            PermissibleValue(text="application/vnd.ms-powerpoint.template.macroEnabled.12"))
        setattr(cls, "application/vnd.ms-PrintDeviceCapabilities+xml",
            PermissibleValue(text="application/vnd.ms-PrintDeviceCapabilities+xml"))
        setattr(cls, "application/vnd.ms-PrintSchemaTicket+xml",
            PermissibleValue(text="application/vnd.ms-PrintSchemaTicket+xml"))
        setattr(cls, "application/vnd.ms-project",
            PermissibleValue(text="application/vnd.ms-project"))
        setattr(cls, "application/vnd.ms-tnef",
            PermissibleValue(text="application/vnd.ms-tnef"))
        setattr(cls, "application/vnd.ms-windows.devicepairing",
            PermissibleValue(text="application/vnd.ms-windows.devicepairing"))
        setattr(cls, "application/vnd.ms-windows.nwprinting.oob",
            PermissibleValue(text="application/vnd.ms-windows.nwprinting.oob"))
        setattr(cls, "application/vnd.ms-windows.printerpairing",
            PermissibleValue(text="application/vnd.ms-windows.printerpairing"))
        setattr(cls, "application/vnd.ms-windows.wsd.oob",
            PermissibleValue(text="application/vnd.ms-windows.wsd.oob"))
        setattr(cls, "application/vnd.ms-wmdrm.lic-chlg-req",
            PermissibleValue(text="application/vnd.ms-wmdrm.lic-chlg-req"))
        setattr(cls, "application/vnd.ms-wmdrm.lic-resp",
            PermissibleValue(text="application/vnd.ms-wmdrm.lic-resp"))
        setattr(cls, "application/vnd.ms-wmdrm.meter-chlg-req",
            PermissibleValue(text="application/vnd.ms-wmdrm.meter-chlg-req"))
        setattr(cls, "application/vnd.ms-wmdrm.meter-resp",
            PermissibleValue(text="application/vnd.ms-wmdrm.meter-resp"))
        setattr(cls, "application/vnd.ms-word.document.macroEnabled.12",
            PermissibleValue(text="application/vnd.ms-word.document.macroEnabled.12"))
        setattr(cls, "application/vnd.ms-word.template.macroEnabled.12",
            PermissibleValue(text="application/vnd.ms-word.template.macroEnabled.12"))
        setattr(cls, "application/vnd.ms-works",
            PermissibleValue(text="application/vnd.ms-works"))
        setattr(cls, "application/vnd.ms-wpl",
            PermissibleValue(text="application/vnd.ms-wpl"))
        setattr(cls, "application/vnd.ms-xpsdocument",
            PermissibleValue(text="application/vnd.ms-xpsdocument"))
        setattr(cls, "application/vnd.multiad.creator",
            PermissibleValue(text="application/vnd.multiad.creator"))
        setattr(cls, "application/vnd.multiad.creator.cif",
            PermissibleValue(text="application/vnd.multiad.creator.cif"))
        setattr(cls, "application/vnd.musician",
            PermissibleValue(text="application/vnd.musician"))
        setattr(cls, "application/vnd.music-niff",
            PermissibleValue(text="application/vnd.music-niff"))
        setattr(cls, "application/vnd.muvee.style",
            PermissibleValue(text="application/vnd.muvee.style"))
        setattr(cls, "application/vnd.mynfc",
            PermissibleValue(text="application/vnd.mynfc"))
        setattr(cls, "application/vnd.nacamar.ybrid+json",
            PermissibleValue(text="application/vnd.nacamar.ybrid+json"))
        setattr(cls, "application/vnd.nato.bindingdataobject+cbor",
            PermissibleValue(text="application/vnd.nato.bindingdataobject+cbor"))
        setattr(cls, "application/vnd.nato.bindingdataobject+json",
            PermissibleValue(text="application/vnd.nato.bindingdataobject+json"))
        setattr(cls, "application/vnd.nato.bindingdataobject+xml",
            PermissibleValue(text="application/vnd.nato.bindingdataobject+xml"))
        setattr(cls, "application/vnd.nato.openxmlformats-package.iepd+zip",
            PermissibleValue(text="application/vnd.nato.openxmlformats-package.iepd+zip"))
        setattr(cls, "application/vnd.ncd.control",
            PermissibleValue(text="application/vnd.ncd.control"))
        setattr(cls, "application/vnd.ncd.reference",
            PermissibleValue(text="application/vnd.ncd.reference"))
        setattr(cls, "application/vnd.nearst.inv+json",
            PermissibleValue(text="application/vnd.nearst.inv+json"))
        setattr(cls, "application/vnd.nebumind.line",
            PermissibleValue(text="application/vnd.nebumind.line"))
        setattr(cls, "application/vnd.nervana",
            PermissibleValue(text="application/vnd.nervana"))
        setattr(cls, "application/vnd.netfpx",
            PermissibleValue(text="application/vnd.netfpx"))
        setattr(cls, "application/vnd.neurolanguage.nlu",
            PermissibleValue(text="application/vnd.neurolanguage.nlu"))
        setattr(cls, "application/vnd.nimn",
            PermissibleValue(text="application/vnd.nimn"))
        setattr(cls, "application/vnd.nintendo.nitro.rom",
            PermissibleValue(text="application/vnd.nintendo.nitro.rom"))
        setattr(cls, "application/vnd.nintendo.snes.rom",
            PermissibleValue(text="application/vnd.nintendo.snes.rom"))
        setattr(cls, "application/vnd.nitf",
            PermissibleValue(text="application/vnd.nitf"))
        setattr(cls, "application/vnd.noblenet-directory",
            PermissibleValue(text="application/vnd.noblenet-directory"))
        setattr(cls, "application/vnd.noblenet-sealer",
            PermissibleValue(text="application/vnd.noblenet-sealer"))
        setattr(cls, "application/vnd.noblenet-web",
            PermissibleValue(text="application/vnd.noblenet-web"))
        setattr(cls, "application/vnd.nokia.catalogs",
            PermissibleValue(text="application/vnd.nokia.catalogs"))
        setattr(cls, "application/vnd.nokia.conml+wbxml",
            PermissibleValue(text="application/vnd.nokia.conml+wbxml"))
        setattr(cls, "application/vnd.nokia.conml+xml",
            PermissibleValue(text="application/vnd.nokia.conml+xml"))
        setattr(cls, "application/vnd.nokia.iptv.config+xml",
            PermissibleValue(text="application/vnd.nokia.iptv.config+xml"))
        setattr(cls, "application/vnd.nokia.iSDS-radio-presets",
            PermissibleValue(text="application/vnd.nokia.iSDS-radio-presets"))
        setattr(cls, "application/vnd.nokia.landmark+wbxml",
            PermissibleValue(text="application/vnd.nokia.landmark+wbxml"))
        setattr(cls, "application/vnd.nokia.landmark+xml",
            PermissibleValue(text="application/vnd.nokia.landmark+xml"))
        setattr(cls, "application/vnd.nokia.landmarkcollection+xml",
            PermissibleValue(text="application/vnd.nokia.landmarkcollection+xml"))
        setattr(cls, "application/vnd.nokia.ncd",
            PermissibleValue(text="application/vnd.nokia.ncd"))
        setattr(cls, "application/vnd.nokia.n-gage.ac+xml",
            PermissibleValue(text="application/vnd.nokia.n-gage.ac+xml"))
        setattr(cls, "application/vnd.nokia.n-gage.data",
            PermissibleValue(text="application/vnd.nokia.n-gage.data"))
        setattr(cls, "application/vnd.nokia.n-gage.symbian.install",
            PermissibleValue(text="application/vnd.nokia.n-gage.symbian.install"))
        setattr(cls, "application/vnd.nokia.pcd+wbxml",
            PermissibleValue(text="application/vnd.nokia.pcd+wbxml"))
        setattr(cls, "application/vnd.nokia.pcd+xml",
            PermissibleValue(text="application/vnd.nokia.pcd+xml"))
        setattr(cls, "application/vnd.nokia.radio-preset",
            PermissibleValue(text="application/vnd.nokia.radio-preset"))
        setattr(cls, "application/vnd.nokia.radio-presets",
            PermissibleValue(text="application/vnd.nokia.radio-presets"))
        setattr(cls, "application/vnd.novadigm.EDM",
            PermissibleValue(text="application/vnd.novadigm.EDM"))
        setattr(cls, "application/vnd.novadigm.EDX",
            PermissibleValue(text="application/vnd.novadigm.EDX"))
        setattr(cls, "application/vnd.novadigm.EXT",
            PermissibleValue(text="application/vnd.novadigm.EXT"))
        setattr(cls, "application/vnd.ntt-local.content-share",
            PermissibleValue(text="application/vnd.ntt-local.content-share"))
        setattr(cls, "application/vnd.ntt-local.file-transfer",
            PermissibleValue(text="application/vnd.ntt-local.file-transfer"))
        setattr(cls, "application/vnd.ntt-local.ogw_remote-access",
            PermissibleValue(text="application/vnd.ntt-local.ogw_remote-access"))
        setattr(cls, "application/vnd.ntt-local.sip-ta_remote",
            PermissibleValue(text="application/vnd.ntt-local.sip-ta_remote"))
        setattr(cls, "application/vnd.ntt-local.sip-ta_tcp_stream",
            PermissibleValue(text="application/vnd.ntt-local.sip-ta_tcp_stream"))
        setattr(cls, "application/vnd.oai.workflows",
            PermissibleValue(text="application/vnd.oai.workflows"))
        setattr(cls, "application/vnd.oai.workflows+json",
            PermissibleValue(text="application/vnd.oai.workflows+json"))
        setattr(cls, "application/vnd.oai.workflows+yaml",
            PermissibleValue(text="application/vnd.oai.workflows+yaml"))
        setattr(cls, "application/vnd.oasis.opendocument.base",
            PermissibleValue(text="application/vnd.oasis.opendocument.base"))
        setattr(cls, "application/vnd.oasis.opendocument.chart",
            PermissibleValue(text="application/vnd.oasis.opendocument.chart"))
        setattr(cls, "application/vnd.oasis.opendocument.chart-template",
            PermissibleValue(text="application/vnd.oasis.opendocument.chart-template"))
        setattr(cls, "application/vnd.oasis.opendocument.database",
            PermissibleValue(text="application/vnd.oasis.opendocument.database"))
        setattr(cls, "application/vnd.oasis.opendocument.formula",
            PermissibleValue(text="application/vnd.oasis.opendocument.formula"))
        setattr(cls, "application/vnd.oasis.opendocument.formula-template",
            PermissibleValue(text="application/vnd.oasis.opendocument.formula-template"))
        setattr(cls, "application/vnd.oasis.opendocument.graphics",
            PermissibleValue(text="application/vnd.oasis.opendocument.graphics"))
        setattr(cls, "application/vnd.oasis.opendocument.graphics-template",
            PermissibleValue(text="application/vnd.oasis.opendocument.graphics-template"))
        setattr(cls, "application/vnd.oasis.opendocument.image",
            PermissibleValue(text="application/vnd.oasis.opendocument.image"))
        setattr(cls, "application/vnd.oasis.opendocument.image-template",
            PermissibleValue(text="application/vnd.oasis.opendocument.image-template"))
        setattr(cls, "application/vnd.oasis.opendocument.presentation",
            PermissibleValue(text="application/vnd.oasis.opendocument.presentation"))
        setattr(cls, "application/vnd.oasis.opendocument.presentation-template",
            PermissibleValue(text="application/vnd.oasis.opendocument.presentation-template"))
        setattr(cls, "application/vnd.oasis.opendocument.spreadsheet",
            PermissibleValue(text="application/vnd.oasis.opendocument.spreadsheet"))
        setattr(cls, "application/vnd.oasis.opendocument.spreadsheet-template",
            PermissibleValue(text="application/vnd.oasis.opendocument.spreadsheet-template"))
        setattr(cls, "application/vnd.oasis.opendocument.text",
            PermissibleValue(text="application/vnd.oasis.opendocument.text"))
        setattr(cls, "application/vnd.oasis.opendocument.text-master",
            PermissibleValue(text="application/vnd.oasis.opendocument.text-master"))
        setattr(cls, "application/vnd.oasis.opendocument.text-master-template",
            PermissibleValue(text="application/vnd.oasis.opendocument.text-master-template"))
        setattr(cls, "application/vnd.oasis.opendocument.text-template",
            PermissibleValue(text="application/vnd.oasis.opendocument.text-template"))
        setattr(cls, "application/vnd.oasis.opendocument.text-web",
            PermissibleValue(text="application/vnd.oasis.opendocument.text-web"))
        setattr(cls, "application/vnd.obn",
            PermissibleValue(text="application/vnd.obn"))
        setattr(cls, "application/vnd.ocf+cbor",
            PermissibleValue(text="application/vnd.ocf+cbor"))
        setattr(cls, "application/vnd.oci.image.manifest.v1+json",
            PermissibleValue(text="application/vnd.oci.image.manifest.v1+json"))
        setattr(cls, "application/vnd.oftn.l10n+json",
            PermissibleValue(text="application/vnd.oftn.l10n+json"))
        setattr(cls, "application/vnd.oipf.contentaccessdownload+xml",
            PermissibleValue(text="application/vnd.oipf.contentaccessdownload+xml"))
        setattr(cls, "application/vnd.oipf.contentaccessstreaming+xml",
            PermissibleValue(text="application/vnd.oipf.contentaccessstreaming+xml"))
        setattr(cls, "application/vnd.oipf.cspg-hexbinary",
            PermissibleValue(text="application/vnd.oipf.cspg-hexbinary"))
        setattr(cls, "application/vnd.oipf.dae.svg+xml",
            PermissibleValue(text="application/vnd.oipf.dae.svg+xml"))
        setattr(cls, "application/vnd.oipf.dae.xhtml+xml",
            PermissibleValue(text="application/vnd.oipf.dae.xhtml+xml"))
        setattr(cls, "application/vnd.oipf.mippvcontrolmessage+xml",
            PermissibleValue(text="application/vnd.oipf.mippvcontrolmessage+xml"))
        setattr(cls, "application/vnd.oipf.pae.gem",
            PermissibleValue(text="application/vnd.oipf.pae.gem"))
        setattr(cls, "application/vnd.oipf.spdiscovery+xml",
            PermissibleValue(text="application/vnd.oipf.spdiscovery+xml"))
        setattr(cls, "application/vnd.oipf.spdlist+xml",
            PermissibleValue(text="application/vnd.oipf.spdlist+xml"))
        setattr(cls, "application/vnd.oipf.ueprofile+xml",
            PermissibleValue(text="application/vnd.oipf.ueprofile+xml"))
        setattr(cls, "application/vnd.oipf.userprofile+xml",
            PermissibleValue(text="application/vnd.oipf.userprofile+xml"))
        setattr(cls, "application/vnd.olpc-sugar",
            PermissibleValue(text="application/vnd.olpc-sugar"))
        setattr(cls, "application/vnd.oma.bcast.associated-procedure-parameter+xml",
            PermissibleValue(text="application/vnd.oma.bcast.associated-procedure-parameter+xml"))
        setattr(cls, "application/vnd.oma.bcast.drm-trigger+xml",
            PermissibleValue(text="application/vnd.oma.bcast.drm-trigger+xml"))
        setattr(cls, "application/vnd.oma.bcast.imd+xml",
            PermissibleValue(text="application/vnd.oma.bcast.imd+xml"))
        setattr(cls, "application/vnd.oma.bcast.ltkm",
            PermissibleValue(text="application/vnd.oma.bcast.ltkm"))
        setattr(cls, "application/vnd.oma.bcast.notification+xml",
            PermissibleValue(text="application/vnd.oma.bcast.notification+xml"))
        setattr(cls, "application/vnd.oma.bcast.provisioningtrigger",
            PermissibleValue(text="application/vnd.oma.bcast.provisioningtrigger"))
        setattr(cls, "application/vnd.oma.bcast.sgboot",
            PermissibleValue(text="application/vnd.oma.bcast.sgboot"))
        setattr(cls, "application/vnd.oma.bcast.sgdd+xml",
            PermissibleValue(text="application/vnd.oma.bcast.sgdd+xml"))
        setattr(cls, "application/vnd.oma.bcast.sgdu",
            PermissibleValue(text="application/vnd.oma.bcast.sgdu"))
        setattr(cls, "application/vnd.oma.bcast.simple-symbol-container",
            PermissibleValue(text="application/vnd.oma.bcast.simple-symbol-container"))
        setattr(cls, "application/vnd.oma.bcast.smartcard-trigger+xml",
            PermissibleValue(text="application/vnd.oma.bcast.smartcard-trigger+xml"))
        setattr(cls, "application/vnd.oma.bcast.sprov+xml",
            PermissibleValue(text="application/vnd.oma.bcast.sprov+xml"))
        setattr(cls, "application/vnd.oma.bcast.stkm",
            PermissibleValue(text="application/vnd.oma.bcast.stkm"))
        setattr(cls, "application/vnd.oma.cab-address-book+xml",
            PermissibleValue(text="application/vnd.oma.cab-address-book+xml"))
        setattr(cls, "application/vnd.oma.cab-feature-handler+xml",
            PermissibleValue(text="application/vnd.oma.cab-feature-handler+xml"))
        setattr(cls, "application/vnd.oma.cab-pcc+xml",
            PermissibleValue(text="application/vnd.oma.cab-pcc+xml"))
        setattr(cls, "application/vnd.oma.cab-subs-invite+xml",
            PermissibleValue(text="application/vnd.oma.cab-subs-invite+xml"))
        setattr(cls, "application/vnd.oma.cab-user-prefs+xml",
            PermissibleValue(text="application/vnd.oma.cab-user-prefs+xml"))
        setattr(cls, "application/vnd.oma.dcd",
            PermissibleValue(text="application/vnd.oma.dcd"))
        setattr(cls, "application/vnd.oma.dcdc",
            PermissibleValue(text="application/vnd.oma.dcdc"))
        setattr(cls, "application/vnd.oma.dd2+xml",
            PermissibleValue(text="application/vnd.oma.dd2+xml"))
        setattr(cls, "application/vnd.oma.drm.risd+xml",
            PermissibleValue(text="application/vnd.oma.drm.risd+xml"))
        setattr(cls, "application/vnd.oma.group-usage-list+xml",
            PermissibleValue(text="application/vnd.oma.group-usage-list+xml"))
        setattr(cls, "application/vnd.oma.lwm2m+cbor",
            PermissibleValue(text="application/vnd.oma.lwm2m+cbor"))
        setattr(cls, "application/vnd.oma.lwm2m+json",
            PermissibleValue(text="application/vnd.oma.lwm2m+json"))
        setattr(cls, "application/vnd.oma.lwm2m+tlv",
            PermissibleValue(text="application/vnd.oma.lwm2m+tlv"))
        setattr(cls, "application/vnd.oma.pal+xml",
            PermissibleValue(text="application/vnd.oma.pal+xml"))
        setattr(cls, "application/vnd.oma.poc.detailed-progress-report+xml",
            PermissibleValue(text="application/vnd.oma.poc.detailed-progress-report+xml"))
        setattr(cls, "application/vnd.oma.poc.final-report+xml",
            PermissibleValue(text="application/vnd.oma.poc.final-report+xml"))
        setattr(cls, "application/vnd.oma.poc.groups+xml",
            PermissibleValue(text="application/vnd.oma.poc.groups+xml"))
        setattr(cls, "application/vnd.oma.poc.invocation-descriptor+xml",
            PermissibleValue(text="application/vnd.oma.poc.invocation-descriptor+xml"))
        setattr(cls, "application/vnd.oma.poc.optimized-progress-report+xml",
            PermissibleValue(text="application/vnd.oma.poc.optimized-progress-report+xml"))
        setattr(cls, "application/vnd.oma.push",
            PermissibleValue(text="application/vnd.oma.push"))
        setattr(cls, "application/vnd.oma.scidm.messages+xml",
            PermissibleValue(text="application/vnd.oma.scidm.messages+xml"))
        setattr(cls, "application/vnd.oma.xcap-directory+xml",
            PermissibleValue(text="application/vnd.oma.xcap-directory+xml"))
        setattr(cls, "application/vnd.omads-email+xml",
            PermissibleValue(text="application/vnd.omads-email+xml"))
        setattr(cls, "application/vnd.omads-file+xml",
            PermissibleValue(text="application/vnd.omads-file+xml"))
        setattr(cls, "application/vnd.omads-folder+xml",
            PermissibleValue(text="application/vnd.omads-folder+xml"))
        setattr(cls, "application/vnd.omaloc-supl-init",
            PermissibleValue(text="application/vnd.omaloc-supl-init"))
        setattr(cls, "application/vnd.oma-scws-config",
            PermissibleValue(text="application/vnd.oma-scws-config"))
        setattr(cls, "application/vnd.oma-scws-http-request",
            PermissibleValue(text="application/vnd.oma-scws-http-request"))
        setattr(cls, "application/vnd.oma-scws-http-response",
            PermissibleValue(text="application/vnd.oma-scws-http-response"))
        setattr(cls, "application/vnd.onepager",
            PermissibleValue(text="application/vnd.onepager"))
        setattr(cls, "application/vnd.onepagertamp",
            PermissibleValue(text="application/vnd.onepagertamp"))
        setattr(cls, "application/vnd.onepagertamx",
            PermissibleValue(text="application/vnd.onepagertamx"))
        setattr(cls, "application/vnd.onepagertat",
            PermissibleValue(text="application/vnd.onepagertat"))
        setattr(cls, "application/vnd.onepagertatp",
            PermissibleValue(text="application/vnd.onepagertatp"))
        setattr(cls, "application/vnd.onepagertatx",
            PermissibleValue(text="application/vnd.onepagertatx"))
        setattr(cls, "application/vnd.onvif.metadata",
            PermissibleValue(text="application/vnd.onvif.metadata"))
        setattr(cls, "application/vnd.openblox.game+xml",
            PermissibleValue(text="application/vnd.openblox.game+xml"))
        setattr(cls, "application/vnd.openblox.game-binary",
            PermissibleValue(text="application/vnd.openblox.game-binary"))
        setattr(cls, "application/vnd.openeye.oeb",
            PermissibleValue(text="application/vnd.openeye.oeb"))
        setattr(cls, "application/vnd.openstreetmap.data+xml",
            PermissibleValue(text="application/vnd.openstreetmap.data+xml"))
        setattr(cls, "application/vnd.opentimestamps.ots",
            PermissibleValue(text="application/vnd.opentimestamps.ots"))
        setattr(cls, "application/vnd.openvpi.dspx+json",
            PermissibleValue(text="application/vnd.openvpi.dspx+json"))
        setattr(cls, "application/vnd.openxmlformats-officedocument.custom-properties+xml",
            PermissibleValue(text="application/vnd.openxmlformats-officedocument.custom-properties+xml"))
        setattr(cls, "application/vnd.openxmlformats-officedocument.customXmlProperties+xml",
            PermissibleValue(text="application/vnd.openxmlformats-officedocument.customXmlProperties+xml"))
        setattr(cls, "application/vnd.openxmlformats-officedocument.drawing+xml",
            PermissibleValue(text="application/vnd.openxmlformats-officedocument.drawing+xml"))
        setattr(cls, "application/vnd.openxmlformats-officedocument.drawingml.chart+xml",
            PermissibleValue(text="application/vnd.openxmlformats-officedocument.drawingml.chart+xml"))
        setattr(cls, "application/vnd.openxmlformats-officedocument.drawingml.chartshapes+xml",
            PermissibleValue(text="application/vnd.openxmlformats-officedocument.drawingml.chartshapes+xml"))
        setattr(cls, "application/vnd.openxmlformats-officedocument.drawingml.diagramColors+xml",
            PermissibleValue(text="application/vnd.openxmlformats-officedocument.drawingml.diagramColors+xml"))
        setattr(cls, "application/vnd.openxmlformats-officedocument.drawingml.diagramData+xml",
            PermissibleValue(text="application/vnd.openxmlformats-officedocument.drawingml.diagramData+xml"))
        setattr(cls, "application/vnd.openxmlformats-officedocument.drawingml.diagramLayout+xml",
            PermissibleValue(text="application/vnd.openxmlformats-officedocument.drawingml.diagramLayout+xml"))
        setattr(cls, "application/vnd.openxmlformats-officedocument.drawingml.diagramStyle+xml",
            PermissibleValue(text="application/vnd.openxmlformats-officedocument.drawingml.diagramStyle+xml"))
        setattr(cls, "application/vnd.openxmlformats-officedocument.extended-properties+xml",
            PermissibleValue(text="application/vnd.openxmlformats-officedocument.extended-properties+xml"))
        setattr(cls, "application/vnd.openxmlformats-officedocument.presentationml.commentAuthors+xml",
            PermissibleValue(text="application/vnd.openxmlformats-officedocument.presentationml.commentAuthors+xml"))
        setattr(cls, "application/vnd.openxmlformats-officedocument.presentationml.comments+xml",
            PermissibleValue(text="application/vnd.openxmlformats-officedocument.presentationml.comments+xml"))
        setattr(cls, "application/vnd.openxmlformats-officedocument.presentationml.handoutMaster+xml",
            PermissibleValue(text="application/vnd.openxmlformats-officedocument.presentationml.handoutMaster+xml"))
        setattr(cls, "application/vnd.openxmlformats-officedocument.presentationml.notesMaster+xml",
            PermissibleValue(text="application/vnd.openxmlformats-officedocument.presentationml.notesMaster+xml"))
        setattr(cls, "application/vnd.openxmlformats-officedocument.presentationml.notesSlide+xml",
            PermissibleValue(text="application/vnd.openxmlformats-officedocument.presentationml.notesSlide+xml"))
        setattr(cls, "application/vnd.openxmlformats-officedocument.presentationml.presentation",
            PermissibleValue(text="application/vnd.openxmlformats-officedocument.presentationml.presentation"))
        setattr(cls, "application/vnd.openxmlformats-officedocument.presentationml.presentation.main+xml",
            PermissibleValue(text="application/vnd.openxmlformats-officedocument.presentationml.presentation.main+xml"))
        setattr(cls, "application/vnd.openxmlformats-officedocument.presentationml.presProps+xml",
            PermissibleValue(text="application/vnd.openxmlformats-officedocument.presentationml.presProps+xml"))
        setattr(cls, "application/vnd.openxmlformats-officedocument.presentationml.slide",
            PermissibleValue(text="application/vnd.openxmlformats-officedocument.presentationml.slide"))
        setattr(cls, "application/vnd.openxmlformats-officedocument.presentationml.slide+xml",
            PermissibleValue(text="application/vnd.openxmlformats-officedocument.presentationml.slide+xml"))
        setattr(cls, "application/vnd.openxmlformats-officedocument.presentationml.slideLayout+xml",
            PermissibleValue(text="application/vnd.openxmlformats-officedocument.presentationml.slideLayout+xml"))
        setattr(cls, "application/vnd.openxmlformats-officedocument.presentationml.slideMaster+xml",
            PermissibleValue(text="application/vnd.openxmlformats-officedocument.presentationml.slideMaster+xml"))
        setattr(cls, "application/vnd.openxmlformats-officedocument.presentationml.slideshow",
            PermissibleValue(text="application/vnd.openxmlformats-officedocument.presentationml.slideshow"))
        setattr(cls, "application/vnd.openxmlformats-officedocument.presentationml.slideshow.main+xml",
            PermissibleValue(text="application/vnd.openxmlformats-officedocument.presentationml.slideshow.main+xml"))
        setattr(cls, "application/vnd.openxmlformats-officedocument.presentationml.slideUpdateInfo+xml",
            PermissibleValue(text="application/vnd.openxmlformats-officedocument.presentationml.slideUpdateInfo+xml"))
        setattr(cls, "application/vnd.openxmlformats-officedocument.presentationml.tableStyles+xml",
            PermissibleValue(text="application/vnd.openxmlformats-officedocument.presentationml.tableStyles+xml"))
        setattr(cls, "application/vnd.openxmlformats-officedocument.presentationml.tags+xml",
            PermissibleValue(text="application/vnd.openxmlformats-officedocument.presentationml.tags+xml"))
        setattr(cls, "application/vnd.openxmlformats-officedocument.presentationml.template",
            PermissibleValue(text="application/vnd.openxmlformats-officedocument.presentationml.template"))
        setattr(cls, "application/vnd.openxmlformats-officedocument.presentationml.template.main+xml",
            PermissibleValue(text="application/vnd.openxmlformats-officedocument.presentationml.template.main+xml"))
        setattr(cls, "application/vnd.openxmlformats-officedocument.presentationml.viewProps+xml",
            PermissibleValue(text="application/vnd.openxmlformats-officedocument.presentationml.viewProps+xml"))
        setattr(cls, "application/vnd.openxmlformats-officedocument.spreadsheetml.calcChain+xml",
            PermissibleValue(text="application/vnd.openxmlformats-officedocument.spreadsheetml.calcChain+xml"))
        setattr(cls, "application/vnd.openxmlformats-officedocument.spreadsheetml.chartsheet+xml",
            PermissibleValue(text="application/vnd.openxmlformats-officedocument.spreadsheetml.chartsheet+xml"))
        setattr(cls, "application/vnd.openxmlformats-officedocument.spreadsheetml.comments+xml",
            PermissibleValue(text="application/vnd.openxmlformats-officedocument.spreadsheetml.comments+xml"))
        setattr(cls, "application/vnd.openxmlformats-officedocument.spreadsheetml.connections+xml",
            PermissibleValue(text="application/vnd.openxmlformats-officedocument.spreadsheetml.connections+xml"))
        setattr(cls, "application/vnd.openxmlformats-officedocument.spreadsheetml.dialogsheet+xml",
            PermissibleValue(text="application/vnd.openxmlformats-officedocument.spreadsheetml.dialogsheet+xml"))
        setattr(cls, "application/vnd.openxmlformats-officedocument.spreadsheetml.externalLink+xml",
            PermissibleValue(text="application/vnd.openxmlformats-officedocument.spreadsheetml.externalLink+xml"))
        setattr(cls, "application/vnd.openxmlformats-officedocument.spreadsheetml.pivotCacheDefinition+xml",
            PermissibleValue(text="application/vnd.openxmlformats-officedocument.spreadsheetml.pivotCacheDefinition+xml"))
        setattr(cls, "application/vnd.openxmlformats-officedocument.spreadsheetml.pivotCacheRecords+xml",
            PermissibleValue(text="application/vnd.openxmlformats-officedocument.spreadsheetml.pivotCacheRecords+xml"))
        setattr(cls, "application/vnd.openxmlformats-officedocument.spreadsheetml.pivotTable+xml",
            PermissibleValue(text="application/vnd.openxmlformats-officedocument.spreadsheetml.pivotTable+xml"))
        setattr(cls, "application/vnd.openxmlformats-officedocument.spreadsheetml.queryTable+xml",
            PermissibleValue(text="application/vnd.openxmlformats-officedocument.spreadsheetml.queryTable+xml"))
        setattr(cls, "application/vnd.openxmlformats-officedocument.spreadsheetml.revisionHeaders+xml",
            PermissibleValue(text="application/vnd.openxmlformats-officedocument.spreadsheetml.revisionHeaders+xml"))
        setattr(cls, "application/vnd.openxmlformats-officedocument.spreadsheetml.revisionLog+xml",
            PermissibleValue(text="application/vnd.openxmlformats-officedocument.spreadsheetml.revisionLog+xml"))
        setattr(cls, "application/vnd.openxmlformats-officedocument.spreadsheetml.sharedStrings+xml",
            PermissibleValue(text="application/vnd.openxmlformats-officedocument.spreadsheetml.sharedStrings+xml"))
        setattr(cls, "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            PermissibleValue(text="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"))
        setattr(cls, "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml",
            PermissibleValue(text="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"))
        setattr(cls, "application/vnd.openxmlformats-officedocument.spreadsheetml.sheetMetadata+xml",
            PermissibleValue(text="application/vnd.openxmlformats-officedocument.spreadsheetml.sheetMetadata+xml"))
        setattr(cls, "application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml",
            PermissibleValue(text="application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml"))
        setattr(cls, "application/vnd.openxmlformats-officedocument.spreadsheetml.table+xml",
            PermissibleValue(text="application/vnd.openxmlformats-officedocument.spreadsheetml.table+xml"))
        setattr(cls, "application/vnd.openxmlformats-officedocument.spreadsheetml.tableSingleCells+xml",
            PermissibleValue(text="application/vnd.openxmlformats-officedocument.spreadsheetml.tableSingleCells+xml"))
        setattr(cls, "application/vnd.openxmlformats-officedocument.spreadsheetml.template",
            PermissibleValue(text="application/vnd.openxmlformats-officedocument.spreadsheetml.template"))
        setattr(cls, "application/vnd.openxmlformats-officedocument.spreadsheetml.template.main+xml",
            PermissibleValue(text="application/vnd.openxmlformats-officedocument.spreadsheetml.template.main+xml"))
        setattr(cls, "application/vnd.openxmlformats-officedocument.spreadsheetml.userNames+xml",
            PermissibleValue(text="application/vnd.openxmlformats-officedocument.spreadsheetml.userNames+xml"))
        setattr(cls, "application/vnd.openxmlformats-officedocument.spreadsheetml.volatileDependencies+xml",
            PermissibleValue(text="application/vnd.openxmlformats-officedocument.spreadsheetml.volatileDependencies+xml"))
        setattr(cls, "application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml",
            PermissibleValue(text="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"))
        setattr(cls, "application/vnd.openxmlformats-officedocument.theme+xml",
            PermissibleValue(text="application/vnd.openxmlformats-officedocument.theme+xml"))
        setattr(cls, "application/vnd.openxmlformats-officedocument.themeOverride+xml",
            PermissibleValue(text="application/vnd.openxmlformats-officedocument.themeOverride+xml"))
        setattr(cls, "application/vnd.openxmlformats-officedocument.vmlDrawing",
            PermissibleValue(text="application/vnd.openxmlformats-officedocument.vmlDrawing"))
        setattr(cls, "application/vnd.openxmlformats-officedocument.wordprocessingml.comments+xml",
            PermissibleValue(text="application/vnd.openxmlformats-officedocument.wordprocessingml.comments+xml"))
        setattr(cls, "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            PermissibleValue(text="application/vnd.openxmlformats-officedocument.wordprocessingml.document"))
        setattr(cls, "application/vnd.openxmlformats-officedocument.wordprocessingml.document.glossary+xml",
            PermissibleValue(text="application/vnd.openxmlformats-officedocument.wordprocessingml.document.glossary+xml"))
        setattr(cls, "application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml",
            PermissibleValue(text="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"))
        setattr(cls, "application/vnd.openxmlformats-officedocument.wordprocessingml.endnotes+xml",
            PermissibleValue(text="application/vnd.openxmlformats-officedocument.wordprocessingml.endnotes+xml"))
        setattr(cls, "application/vnd.openxmlformats-officedocument.wordprocessingml.fontTable+xml",
            PermissibleValue(text="application/vnd.openxmlformats-officedocument.wordprocessingml.fontTable+xml"))
        setattr(cls, "application/vnd.openxmlformats-officedocument.wordprocessingml.footer+xml",
            PermissibleValue(text="application/vnd.openxmlformats-officedocument.wordprocessingml.footer+xml"))
        setattr(cls, "application/vnd.openxmlformats-officedocument.wordprocessingml.footnotes+xml",
            PermissibleValue(text="application/vnd.openxmlformats-officedocument.wordprocessingml.footnotes+xml"))
        setattr(cls, "application/vnd.openxmlformats-officedocument.wordprocessingml.numbering+xml",
            PermissibleValue(text="application/vnd.openxmlformats-officedocument.wordprocessingml.numbering+xml"))
        setattr(cls, "application/vnd.openxmlformats-officedocument.wordprocessingml.settings+xml",
            PermissibleValue(text="application/vnd.openxmlformats-officedocument.wordprocessingml.settings+xml"))
        setattr(cls, "application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml",
            PermissibleValue(text="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"))
        setattr(cls, "application/vnd.openxmlformats-officedocument.wordprocessingml.template",
            PermissibleValue(text="application/vnd.openxmlformats-officedocument.wordprocessingml.template"))
        setattr(cls, "application/vnd.openxmlformats-officedocument.wordprocessingml.template.main+xml",
            PermissibleValue(text="application/vnd.openxmlformats-officedocument.wordprocessingml.template.main+xml"))
        setattr(cls, "application/vnd.openxmlformats-officedocument.wordprocessingml.webSettings+xml",
            PermissibleValue(text="application/vnd.openxmlformats-officedocument.wordprocessingml.webSettings+xml"))
        setattr(cls, "application/vnd.openxmlformats-package.core-properties+xml",
            PermissibleValue(text="application/vnd.openxmlformats-package.core-properties+xml"))
        setattr(cls, "application/vnd.openxmlformats-package.digital-signature-xmlsignature+xml",
            PermissibleValue(text="application/vnd.openxmlformats-package.digital-signature-xmlsignature+xml"))
        setattr(cls, "application/vnd.openxmlformats-package.relationships+xml",
            PermissibleValue(text="application/vnd.openxmlformats-package.relationships+xml"))
        setattr(cls, "application/vnd.oracle.resource+json",
            PermissibleValue(text="application/vnd.oracle.resource+json"))
        setattr(cls, "application/vnd.orange.indata",
            PermissibleValue(text="application/vnd.orange.indata"))
        setattr(cls, "application/vnd.osa.netdeploy",
            PermissibleValue(text="application/vnd.osa.netdeploy"))
        setattr(cls, "application/vnd.osgeo.mapguide.package",
            PermissibleValue(text="application/vnd.osgeo.mapguide.package"))
        setattr(cls, "application/vnd.osgi.bundle",
            PermissibleValue(text="application/vnd.osgi.bundle"))
        setattr(cls, "application/vnd.osgi.dp",
            PermissibleValue(text="application/vnd.osgi.dp"))
        setattr(cls, "application/vnd.osgi.subsystem",
            PermissibleValue(text="application/vnd.osgi.subsystem"))
        setattr(cls, "application/vnd.otps.ct-kip+xml",
            PermissibleValue(text="application/vnd.otps.ct-kip+xml"))
        setattr(cls, "application/vnd.oxli.countgraph",
            PermissibleValue(text="application/vnd.oxli.countgraph"))
        setattr(cls, "application/vnd.pagerduty+json",
            PermissibleValue(text="application/vnd.pagerduty+json"))
        setattr(cls, "application/vnd.palm",
            PermissibleValue(text="application/vnd.palm"))
        setattr(cls, "application/vnd.panoply",
            PermissibleValue(text="application/vnd.panoply"))
        setattr(cls, "application/vnd.paos.xml",
            PermissibleValue(text="application/vnd.paos.xml"))
        setattr(cls, "application/vnd.patentdive",
            PermissibleValue(text="application/vnd.patentdive"))
        setattr(cls, "application/vnd.patientecommsdoc",
            PermissibleValue(text="application/vnd.patientecommsdoc"))
        setattr(cls, "application/vnd.pawaafile",
            PermissibleValue(text="application/vnd.pawaafile"))
        setattr(cls, "application/vnd.pcos",
            PermissibleValue(text="application/vnd.pcos"))
        setattr(cls, "application/vnd.pg.format",
            PermissibleValue(text="application/vnd.pg.format"))
        setattr(cls, "application/vnd.pg.osasli",
            PermissibleValue(text="application/vnd.pg.osasli"))
        setattr(cls, "application/vnd.piaccess.application-licence",
            PermissibleValue(text="application/vnd.piaccess.application-licence"))
        setattr(cls, "application/vnd.picsel",
            PermissibleValue(text="application/vnd.picsel"))
        setattr(cls, "application/vnd.pmi.widget",
            PermissibleValue(text="application/vnd.pmi.widget"))
        setattr(cls, "application/vnd.poc.group-advertisement+xml",
            PermissibleValue(text="application/vnd.poc.group-advertisement+xml"))
        setattr(cls, "application/vnd.pocketlearn",
            PermissibleValue(text="application/vnd.pocketlearn"))
        setattr(cls, "application/vnd.powerbuilder6",
            PermissibleValue(text="application/vnd.powerbuilder6"))
        setattr(cls, "application/vnd.powerbuilder6-s",
            PermissibleValue(text="application/vnd.powerbuilder6-s"))
        setattr(cls, "application/vnd.powerbuilder7",
            PermissibleValue(text="application/vnd.powerbuilder7"))
        setattr(cls, "application/vnd.powerbuilder75",
            PermissibleValue(text="application/vnd.powerbuilder75"))
        setattr(cls, "application/vnd.powerbuilder75-s",
            PermissibleValue(text="application/vnd.powerbuilder75-s"))
        setattr(cls, "application/vnd.powerbuilder7-s",
            PermissibleValue(text="application/vnd.powerbuilder7-s"))
        setattr(cls, "application/vnd.preminet",
            PermissibleValue(text="application/vnd.preminet"))
        setattr(cls, "application/vnd.previewsystems.box",
            PermissibleValue(text="application/vnd.previewsystems.box"))
        setattr(cls, "application/vnd.proteus.magazine",
            PermissibleValue(text="application/vnd.proteus.magazine"))
        setattr(cls, "application/vnd.psfs",
            PermissibleValue(text="application/vnd.psfs"))
        setattr(cls, "application/vnd.pt.mundusmundi",
            PermissibleValue(text="application/vnd.pt.mundusmundi"))
        setattr(cls, "application/vnd.publishare-delta-tree",
            PermissibleValue(text="application/vnd.publishare-delta-tree"))
        setattr(cls, "application/vnd.pvi.ptid1",
            PermissibleValue(text="application/vnd.pvi.ptid1"))
        setattr(cls, "application/vnd.pwg-multiplexed",
            PermissibleValue(text="application/vnd.pwg-multiplexed"))
        setattr(cls, "application/vnd.pwg-xhtml-print+xml",
            PermissibleValue(text="application/vnd.pwg-xhtml-print+xml"))
        setattr(cls, "application/vnd.qualcomm.brew-app-res",
            PermissibleValue(text="application/vnd.qualcomm.brew-app-res"))
        setattr(cls, "application/vnd.quarantainenet",
            PermissibleValue(text="application/vnd.quarantainenet"))
        setattr(cls, "application/vnd.Quark.QuarkXPress",
            PermissibleValue(text="application/vnd.Quark.QuarkXPress"))
        setattr(cls, "application/vnd.quobject-quoxdocument",
            PermissibleValue(text="application/vnd.quobject-quoxdocument"))
        setattr(cls, "application/vnd.radisys.moml+xml",
            PermissibleValue(text="application/vnd.radisys.moml+xml"))
        setattr(cls, "application/vnd.radisys.msml+xml",
            PermissibleValue(text="application/vnd.radisys.msml+xml"))
        setattr(cls, "application/vnd.radisys.msml-audit+xml",
            PermissibleValue(text="application/vnd.radisys.msml-audit+xml"))
        setattr(cls, "application/vnd.radisys.msml-audit-conf+xml",
            PermissibleValue(text="application/vnd.radisys.msml-audit-conf+xml"))
        setattr(cls, "application/vnd.radisys.msml-audit-conn+xml",
            PermissibleValue(text="application/vnd.radisys.msml-audit-conn+xml"))
        setattr(cls, "application/vnd.radisys.msml-audit-dialog+xml",
            PermissibleValue(text="application/vnd.radisys.msml-audit-dialog+xml"))
        setattr(cls, "application/vnd.radisys.msml-audit-stream+xml",
            PermissibleValue(text="application/vnd.radisys.msml-audit-stream+xml"))
        setattr(cls, "application/vnd.radisys.msml-conf+xml",
            PermissibleValue(text="application/vnd.radisys.msml-conf+xml"))
        setattr(cls, "application/vnd.radisys.msml-dialog+xml",
            PermissibleValue(text="application/vnd.radisys.msml-dialog+xml"))
        setattr(cls, "application/vnd.radisys.msml-dialog-base+xml",
            PermissibleValue(text="application/vnd.radisys.msml-dialog-base+xml"))
        setattr(cls, "application/vnd.radisys.msml-dialog-fax-detect+xml",
            PermissibleValue(text="application/vnd.radisys.msml-dialog-fax-detect+xml"))
        setattr(cls, "application/vnd.radisys.msml-dialog-fax-sendrecv+xml",
            PermissibleValue(text="application/vnd.radisys.msml-dialog-fax-sendrecv+xml"))
        setattr(cls, "application/vnd.radisys.msml-dialog-group+xml",
            PermissibleValue(text="application/vnd.radisys.msml-dialog-group+xml"))
        setattr(cls, "application/vnd.radisys.msml-dialog-speech+xml",
            PermissibleValue(text="application/vnd.radisys.msml-dialog-speech+xml"))
        setattr(cls, "application/vnd.radisys.msml-dialog-transform+xml",
            PermissibleValue(text="application/vnd.radisys.msml-dialog-transform+xml"))
        setattr(cls, "application/vnd.rainstor.data",
            PermissibleValue(text="application/vnd.rainstor.data"))
        setattr(cls, "application/vnd.rapid",
            PermissibleValue(text="application/vnd.rapid"))
        setattr(cls, "application/vnd.rar",
            PermissibleValue(text="application/vnd.rar"))
        setattr(cls, "application/vnd.realvnc.bed",
            PermissibleValue(text="application/vnd.realvnc.bed"))
        setattr(cls, "application/vnd.recordare.musicxml",
            PermissibleValue(text="application/vnd.recordare.musicxml"))
        setattr(cls, "application/vnd.recordare.musicxml+xml",
            PermissibleValue(text="application/vnd.recordare.musicxml+xml"))
        setattr(cls, "application/vnd.relpipe",
            PermissibleValue(text="application/vnd.relpipe"))
        setattr(cls, "application/vnd.RenLearn.rlprint",
            PermissibleValue(text="application/vnd.RenLearn.rlprint"))
        setattr(cls, "application/vnd.resilient.logic",
            PermissibleValue(text="application/vnd.resilient.logic"))
        setattr(cls, "application/vnd.restful+json",
            PermissibleValue(text="application/vnd.restful+json"))
        setattr(cls, "application/vnd.rig.cryptonote",
            PermissibleValue(text="application/vnd.rig.cryptonote"))
        setattr(cls, "application/vnd.route66.link66+xml",
            PermissibleValue(text="application/vnd.route66.link66+xml"))
        setattr(cls, "application/vnd.rs-274x",
            PermissibleValue(text="application/vnd.rs-274x"))
        setattr(cls, "application/vnd.ruckus.download",
            PermissibleValue(text="application/vnd.ruckus.download"))
        setattr(cls, "application/vnd.s3sms",
            PermissibleValue(text="application/vnd.s3sms"))
        setattr(cls, "application/vnd.sailingtracker.track",
            PermissibleValue(text="application/vnd.sailingtracker.track"))
        setattr(cls, "application/vnd.sar",
            PermissibleValue(text="application/vnd.sar"))
        setattr(cls, "application/vnd.sbm.cid",
            PermissibleValue(text="application/vnd.sbm.cid"))
        setattr(cls, "application/vnd.sbm.mid2",
            PermissibleValue(text="application/vnd.sbm.mid2"))
        setattr(cls, "application/vnd.scribus",
            PermissibleValue(text="application/vnd.scribus"))
        setattr(cls, "application/vnd.sealed.3df",
            PermissibleValue(text="application/vnd.sealed.3df"))
        setattr(cls, "application/vnd.sealed.csf",
            PermissibleValue(text="application/vnd.sealed.csf"))
        setattr(cls, "application/vnd.sealed.doc",
            PermissibleValue(text="application/vnd.sealed.doc"))
        setattr(cls, "application/vnd.sealed.eml",
            PermissibleValue(text="application/vnd.sealed.eml"))
        setattr(cls, "application/vnd.sealed.mht",
            PermissibleValue(text="application/vnd.sealed.mht"))
        setattr(cls, "application/vnd.sealed.net",
            PermissibleValue(text="application/vnd.sealed.net"))
        setattr(cls, "application/vnd.sealed.ppt",
            PermissibleValue(text="application/vnd.sealed.ppt"))
        setattr(cls, "application/vnd.sealed.tiff",
            PermissibleValue(text="application/vnd.sealed.tiff"))
        setattr(cls, "application/vnd.sealed.xls",
            PermissibleValue(text="application/vnd.sealed.xls"))
        setattr(cls, "application/vnd.sealedmedia.softseal.html",
            PermissibleValue(text="application/vnd.sealedmedia.softseal.html"))
        setattr(cls, "application/vnd.sealedmedia.softseal.pdf",
            PermissibleValue(text="application/vnd.sealedmedia.softseal.pdf"))
        setattr(cls, "application/vnd.seemail",
            PermissibleValue(text="application/vnd.seemail"))
        setattr(cls, "application/vnd.seis+json",
            PermissibleValue(text="application/vnd.seis+json"))
        setattr(cls, "application/vnd.sema",
            PermissibleValue(text="application/vnd.sema"))
        setattr(cls, "application/vnd.semd",
            PermissibleValue(text="application/vnd.semd"))
        setattr(cls, "application/vnd.semf",
            PermissibleValue(text="application/vnd.semf"))
        setattr(cls, "application/vnd.shade-save-file",
            PermissibleValue(text="application/vnd.shade-save-file"))
        setattr(cls, "application/vnd.shana.informed.formdata",
            PermissibleValue(text="application/vnd.shana.informed.formdata"))
        setattr(cls, "application/vnd.shana.informed.formtemplate",
            PermissibleValue(text="application/vnd.shana.informed.formtemplate"))
        setattr(cls, "application/vnd.shana.informed.interchange",
            PermissibleValue(text="application/vnd.shana.informed.interchange"))
        setattr(cls, "application/vnd.shana.informed.package",
            PermissibleValue(text="application/vnd.shana.informed.package"))
        setattr(cls, "application/vnd.shootproof+json",
            PermissibleValue(text="application/vnd.shootproof+json"))
        setattr(cls, "application/vnd.shopkick+json",
            PermissibleValue(text="application/vnd.shopkick+json"))
        setattr(cls, "application/vnd.shp",
            PermissibleValue(text="application/vnd.shp"))
        setattr(cls, "application/vnd.shx",
            PermissibleValue(text="application/vnd.shx"))
        setattr(cls, "application/vnd.sigrok.session",
            PermissibleValue(text="application/vnd.sigrok.session"))
        setattr(cls, "application/vnd.SimTech-MindMapper",
            PermissibleValue(text="application/vnd.SimTech-MindMapper"))
        setattr(cls, "application/vnd.siren+json",
            PermissibleValue(text="application/vnd.siren+json"))
        setattr(cls, "application/vnd.sketchometry",
            PermissibleValue(text="application/vnd.sketchometry"))
        setattr(cls, "application/vnd.smaf",
            PermissibleValue(text="application/vnd.smaf"))
        setattr(cls, "application/vnd.smart.notebook",
            PermissibleValue(text="application/vnd.smart.notebook"))
        setattr(cls, "application/vnd.smart.teacher",
            PermissibleValue(text="application/vnd.smart.teacher"))
        setattr(cls, "application/vnd.smintio.portals.archive",
            PermissibleValue(text="application/vnd.smintio.portals.archive"))
        setattr(cls, "application/vnd.snesdev-page-table",
            PermissibleValue(text="application/vnd.snesdev-page-table"))
        setattr(cls, "application/vnd.software602.filler.form+xml",
            PermissibleValue(text="application/vnd.software602.filler.form+xml"))
        setattr(cls, "application/vnd.software602.filler.form-xml-zip",
            PermissibleValue(text="application/vnd.software602.filler.form-xml-zip"))
        setattr(cls, "application/vnd.solent.sdkm+xml",
            PermissibleValue(text="application/vnd.solent.sdkm+xml"))
        setattr(cls, "application/vnd.spotfire.dxp",
            PermissibleValue(text="application/vnd.spotfire.dxp"))
        setattr(cls, "application/vnd.spotfire.sfs",
            PermissibleValue(text="application/vnd.spotfire.sfs"))
        setattr(cls, "application/vnd.sqlite3",
            PermissibleValue(text="application/vnd.sqlite3"))
        setattr(cls, "application/vnd.sss-cod",
            PermissibleValue(text="application/vnd.sss-cod"))
        setattr(cls, "application/vnd.sss-dtf",
            PermissibleValue(text="application/vnd.sss-dtf"))
        setattr(cls, "application/vnd.sss-ntf",
            PermissibleValue(text="application/vnd.sss-ntf"))
        setattr(cls, "application/vnd.stepmania.package",
            PermissibleValue(text="application/vnd.stepmania.package"))
        setattr(cls, "application/vnd.stepmania.stepchart",
            PermissibleValue(text="application/vnd.stepmania.stepchart"))
        setattr(cls, "application/vnd.street-stream",
            PermissibleValue(text="application/vnd.street-stream"))
        setattr(cls, "application/vnd.sun.wadl+xml",
            PermissibleValue(text="application/vnd.sun.wadl+xml"))
        setattr(cls, "application/vnd.sus-calendar",
            PermissibleValue(text="application/vnd.sus-calendar"))
        setattr(cls, "application/vnd.svd",
            PermissibleValue(text="application/vnd.svd"))
        setattr(cls, "application/vnd.swiftview-ics",
            PermissibleValue(text="application/vnd.swiftview-ics"))
        setattr(cls, "application/vnd.sybyl.mol2",
            PermissibleValue(text="application/vnd.sybyl.mol2"))
        setattr(cls, "application/vnd.sycle+xml",
            PermissibleValue(text="application/vnd.sycle+xml"))
        setattr(cls, "application/vnd.syft+json",
            PermissibleValue(text="application/vnd.syft+json"))
        setattr(cls, "application/vnd.syncml.dm.notification",
            PermissibleValue(text="application/vnd.syncml.dm.notification"))
        setattr(cls, "application/vnd.syncml.dm+wbxml",
            PermissibleValue(text="application/vnd.syncml.dm+wbxml"))
        setattr(cls, "application/vnd.syncml.dm+xml",
            PermissibleValue(text="application/vnd.syncml.dm+xml"))
        setattr(cls, "application/vnd.syncml.dmddf+wbxml",
            PermissibleValue(text="application/vnd.syncml.dmddf+wbxml"))
        setattr(cls, "application/vnd.syncml.dmddf+xml",
            PermissibleValue(text="application/vnd.syncml.dmddf+xml"))
        setattr(cls, "application/vnd.syncml.dmtnds+wbxml",
            PermissibleValue(text="application/vnd.syncml.dmtnds+wbxml"))
        setattr(cls, "application/vnd.syncml.dmtnds+xml",
            PermissibleValue(text="application/vnd.syncml.dmtnds+xml"))
        setattr(cls, "application/vnd.syncml.ds.notification",
            PermissibleValue(text="application/vnd.syncml.ds.notification"))
        setattr(cls, "application/vnd.syncml+xml",
            PermissibleValue(text="application/vnd.syncml+xml"))
        setattr(cls, "application/vnd.tableschema+json",
            PermissibleValue(text="application/vnd.tableschema+json"))
        setattr(cls, "application/vnd.tao.intent-module-archive",
            PermissibleValue(text="application/vnd.tao.intent-module-archive"))
        setattr(cls, "application/vnd.tcpdump.pcap",
            PermissibleValue(text="application/vnd.tcpdump.pcap"))
        setattr(cls, "application/vnd.think-cell.ppttc+json",
            PermissibleValue(text="application/vnd.think-cell.ppttc+json"))
        setattr(cls, "application/vnd.tmd.mediaflex.api+xml",
            PermissibleValue(text="application/vnd.tmd.mediaflex.api+xml"))
        setattr(cls, "application/vnd.tml",
            PermissibleValue(text="application/vnd.tml"))
        setattr(cls, "application/vnd.tmobile-livetv",
            PermissibleValue(text="application/vnd.tmobile-livetv"))
        setattr(cls, "application/vnd.tri.onesource",
            PermissibleValue(text="application/vnd.tri.onesource"))
        setattr(cls, "application/vnd.trid.tpt",
            PermissibleValue(text="application/vnd.trid.tpt"))
        setattr(cls, "application/vnd.triscape.mxs",
            PermissibleValue(text="application/vnd.triscape.mxs"))
        setattr(cls, "application/vnd.trueapp",
            PermissibleValue(text="application/vnd.trueapp"))
        setattr(cls, "application/vnd.truedoc",
            PermissibleValue(text="application/vnd.truedoc"))
        setattr(cls, "application/vnd.ubisoft.webplayer",
            PermissibleValue(text="application/vnd.ubisoft.webplayer"))
        setattr(cls, "application/vnd.ufdl",
            PermissibleValue(text="application/vnd.ufdl"))
        setattr(cls, "application/vnd.uic.osdm+json",
            PermissibleValue(text="application/vnd.uic.osdm+json"))
        setattr(cls, "application/vnd.uiq.theme",
            PermissibleValue(text="application/vnd.uiq.theme"))
        setattr(cls, "application/vnd.umajin",
            PermissibleValue(text="application/vnd.umajin"))
        setattr(cls, "application/vnd.unity",
            PermissibleValue(text="application/vnd.unity"))
        setattr(cls, "application/vnd.uoml+xml",
            PermissibleValue(text="application/vnd.uoml+xml"))
        setattr(cls, "application/vnd.uplanet.alert",
            PermissibleValue(text="application/vnd.uplanet.alert"))
        setattr(cls, "application/vnd.uplanet.alert-wbxml",
            PermissibleValue(text="application/vnd.uplanet.alert-wbxml"))
        setattr(cls, "application/vnd.uplanet.bearer-choice",
            PermissibleValue(text="application/vnd.uplanet.bearer-choice"))
        setattr(cls, "application/vnd.uplanet.bearer-choice-wbxml",
            PermissibleValue(text="application/vnd.uplanet.bearer-choice-wbxml"))
        setattr(cls, "application/vnd.uplanet.cacheop",
            PermissibleValue(text="application/vnd.uplanet.cacheop"))
        setattr(cls, "application/vnd.uplanet.cacheop-wbxml",
            PermissibleValue(text="application/vnd.uplanet.cacheop-wbxml"))
        setattr(cls, "application/vnd.uplanet.channel",
            PermissibleValue(text="application/vnd.uplanet.channel"))
        setattr(cls, "application/vnd.uplanet.channel-wbxml",
            PermissibleValue(text="application/vnd.uplanet.channel-wbxml"))
        setattr(cls, "application/vnd.uplanet.list",
            PermissibleValue(text="application/vnd.uplanet.list"))
        setattr(cls, "application/vnd.uplanet.listcmd",
            PermissibleValue(text="application/vnd.uplanet.listcmd"))
        setattr(cls, "application/vnd.uplanet.listcmd-wbxml",
            PermissibleValue(text="application/vnd.uplanet.listcmd-wbxml"))
        setattr(cls, "application/vnd.uplanet.list-wbxml",
            PermissibleValue(text="application/vnd.uplanet.list-wbxml"))
        setattr(cls, "application/vnd.uplanet.signal",
            PermissibleValue(text="application/vnd.uplanet.signal"))
        setattr(cls, "application/vnd.uri-map",
            PermissibleValue(text="application/vnd.uri-map"))
        setattr(cls, "application/vnd.valve.source.material",
            PermissibleValue(text="application/vnd.valve.source.material"))
        setattr(cls, "application/vnd.vcx",
            PermissibleValue(text="application/vnd.vcx"))
        setattr(cls, "application/vnd.vd-study",
            PermissibleValue(text="application/vnd.vd-study"))
        setattr(cls, "application/vnd.vectorworks",
            PermissibleValue(text="application/vnd.vectorworks"))
        setattr(cls, "application/vnd.vel+json",
            PermissibleValue(text="application/vnd.vel+json"))
        setattr(cls, "application/vnd.veraison.tsm-report+cbor",
            PermissibleValue(text="application/vnd.veraison.tsm-report+cbor"))
        setattr(cls, "application/vnd.veraison.tsm-report+json",
            PermissibleValue(text="application/vnd.veraison.tsm-report+json"))
        setattr(cls, "application/vnd.verimatrix.vcas",
            PermissibleValue(text="application/vnd.verimatrix.vcas"))
        setattr(cls, "application/vnd.veritone.aion+json",
            PermissibleValue(text="application/vnd.veritone.aion+json"))
        setattr(cls, "application/vnd.veryant.thin",
            PermissibleValue(text="application/vnd.veryant.thin"))
        setattr(cls, "application/vnd.ves.encrypted",
            PermissibleValue(text="application/vnd.ves.encrypted"))
        setattr(cls, "application/vnd.vidsoft.vidconference",
            PermissibleValue(text="application/vnd.vidsoft.vidconference"))
        setattr(cls, "application/vnd.visio",
            PermissibleValue(text="application/vnd.visio"))
        setattr(cls, "application/vnd.visionary",
            PermissibleValue(text="application/vnd.visionary"))
        setattr(cls, "application/vnd.vividence.scriptfile",
            PermissibleValue(text="application/vnd.vividence.scriptfile"))
        setattr(cls, "application/vnd.vocalshaper.vsp4",
            PermissibleValue(text="application/vnd.vocalshaper.vsp4"))
        setattr(cls, "application/vnd.vsf",
            PermissibleValue(text="application/vnd.vsf"))
        setattr(cls, "application/vnd.wap.sic",
            PermissibleValue(text="application/vnd.wap.sic"))
        setattr(cls, "application/vnd.wap.slc",
            PermissibleValue(text="application/vnd.wap.slc"))
        setattr(cls, "application/vnd.wap.wbxml",
            PermissibleValue(text="application/vnd.wap.wbxml"))
        setattr(cls, "application/vnd.wap.wmlc",
            PermissibleValue(text="application/vnd.wap.wmlc"))
        setattr(cls, "application/vnd.wap.wmlscriptc",
            PermissibleValue(text="application/vnd.wap.wmlscriptc"))
        setattr(cls, "application/vnd.wasmflow.wafl",
            PermissibleValue(text="application/vnd.wasmflow.wafl"))
        setattr(cls, "application/vnd.webturbo",
            PermissibleValue(text="application/vnd.webturbo"))
        setattr(cls, "application/vnd.wfa.dpp",
            PermissibleValue(text="application/vnd.wfa.dpp"))
        setattr(cls, "application/vnd.wfa.p2p",
            PermissibleValue(text="application/vnd.wfa.p2p"))
        setattr(cls, "application/vnd.wfa.wsc",
            PermissibleValue(text="application/vnd.wfa.wsc"))
        setattr(cls, "application/vnd.windows.devicepairing",
            PermissibleValue(text="application/vnd.windows.devicepairing"))
        setattr(cls, "application/vnd.wmc",
            PermissibleValue(text="application/vnd.wmc"))
        setattr(cls, "application/vnd.wmf.bootstrap",
            PermissibleValue(text="application/vnd.wmf.bootstrap"))
        setattr(cls, "application/vnd.wolfram.mathematica",
            PermissibleValue(text="application/vnd.wolfram.mathematica"))
        setattr(cls, "application/vnd.wolfram.mathematica.package",
            PermissibleValue(text="application/vnd.wolfram.mathematica.package"))
        setattr(cls, "application/vnd.wolfram.player",
            PermissibleValue(text="application/vnd.wolfram.player"))
        setattr(cls, "application/vnd.wordlift",
            PermissibleValue(text="application/vnd.wordlift"))
        setattr(cls, "application/vnd.wordperfect",
            PermissibleValue(text="application/vnd.wordperfect"))
        setattr(cls, "application/vnd.wqd",
            PermissibleValue(text="application/vnd.wqd"))
        setattr(cls, "application/vnd.wrq-hp3000-labelled",
            PermissibleValue(text="application/vnd.wrq-hp3000-labelled"))
        setattr(cls, "application/vnd.wt.stf",
            PermissibleValue(text="application/vnd.wt.stf"))
        setattr(cls, "application/vnd.wv.csp+wbxml",
            PermissibleValue(text="application/vnd.wv.csp+wbxml"))
        setattr(cls, "application/vnd.wv.csp+xml",
            PermissibleValue(text="application/vnd.wv.csp+xml"))
        setattr(cls, "application/vnd.wv.ssp+xml",
            PermissibleValue(text="application/vnd.wv.ssp+xml"))
        setattr(cls, "application/vnd.xacml+json",
            PermissibleValue(text="application/vnd.xacml+json"))
        setattr(cls, "application/vnd.xara",
            PermissibleValue(text="application/vnd.xara"))
        setattr(cls, "application/vnd.xarin.cpj",
            PermissibleValue(text="application/vnd.xarin.cpj"))
        setattr(cls, "application/vnd.xecrets-encrypted",
            PermissibleValue(text="application/vnd.xecrets-encrypted"))
        setattr(cls, "application/vnd.xfdl",
            PermissibleValue(text="application/vnd.xfdl"))
        setattr(cls, "application/vnd.xfdl.webform",
            PermissibleValue(text="application/vnd.xfdl.webform"))
        setattr(cls, "application/vnd.xmi+xml",
            PermissibleValue(text="application/vnd.xmi+xml"))
        setattr(cls, "application/vnd.xmpie.cpkg",
            PermissibleValue(text="application/vnd.xmpie.cpkg"))
        setattr(cls, "application/vnd.xmpie.dpkg",
            PermissibleValue(text="application/vnd.xmpie.dpkg"))
        setattr(cls, "application/vnd.xmpie.plan",
            PermissibleValue(text="application/vnd.xmpie.plan"))
        setattr(cls, "application/vnd.xmpie.ppkg",
            PermissibleValue(text="application/vnd.xmpie.ppkg"))
        setattr(cls, "application/vnd.xmpie.xlim",
            PermissibleValue(text="application/vnd.xmpie.xlim"))
        setattr(cls, "application/vnd.yamaha.hv-dic",
            PermissibleValue(text="application/vnd.yamaha.hv-dic"))
        setattr(cls, "application/vnd.yamaha.hv-script",
            PermissibleValue(text="application/vnd.yamaha.hv-script"))
        setattr(cls, "application/vnd.yamaha.hv-voice",
            PermissibleValue(text="application/vnd.yamaha.hv-voice"))
        setattr(cls, "application/vnd.yamaha.openscoreformat",
            PermissibleValue(text="application/vnd.yamaha.openscoreformat"))
        setattr(cls, "application/vnd.yamaha.openscoreformat.osfpvg+xml",
            PermissibleValue(text="application/vnd.yamaha.openscoreformat.osfpvg+xml"))
        setattr(cls, "application/vnd.yamaha.remote-setup",
            PermissibleValue(text="application/vnd.yamaha.remote-setup"))
        setattr(cls, "application/vnd.yamaha.smaf-audio",
            PermissibleValue(text="application/vnd.yamaha.smaf-audio"))
        setattr(cls, "application/vnd.yamaha.smaf-phrase",
            PermissibleValue(text="application/vnd.yamaha.smaf-phrase"))
        setattr(cls, "application/vnd.yamaha.through-ngn",
            PermissibleValue(text="application/vnd.yamaha.through-ngn"))
        setattr(cls, "application/vnd.yamaha.tunnel-udpencap",
            PermissibleValue(text="application/vnd.yamaha.tunnel-udpencap"))
        setattr(cls, "application/vnd.yaoweme",
            PermissibleValue(text="application/vnd.yaoweme"))
        setattr(cls, "application/vnd.yellowriver-custom-menu",
            PermissibleValue(text="application/vnd.yellowriver-custom-menu"))
        setattr(cls, "application/vnd.youtube.yt",
            PermissibleValue(text="application/vnd.youtube.yt"))
        setattr(cls, "application/vnd.zul",
            PermissibleValue(text="application/vnd.zul"))
        setattr(cls, "application/vnd.zzazz.deck+xml",
            PermissibleValue(text="application/vnd.zzazz.deck+xml"))
        setattr(cls, "application/voicexml+xml",
            PermissibleValue(text="application/voicexml+xml"))
        setattr(cls, "application/voucher-cms+json",
            PermissibleValue(text="application/voucher-cms+json"))
        setattr(cls, "application/voucher-jws+json",
            PermissibleValue(text="application/voucher-jws+json"))
        setattr(cls, "application/vp",
            PermissibleValue(text="application/vp"))
        setattr(cls, "application/vp+cose",
            PermissibleValue(text="application/vp+cose"))
        setattr(cls, "application/vp+jwt",
            PermissibleValue(text="application/vp+jwt"))
        setattr(cls, "application/vq-rtcpxr",
            PermissibleValue(text="application/vq-rtcpxr"))
        setattr(cls, "application/wasm",
            PermissibleValue(text="application/wasm"))
        setattr(cls, "application/watcherinfo+xml",
            PermissibleValue(text="application/watcherinfo+xml"))
        setattr(cls, "application/webpush-options+json",
            PermissibleValue(text="application/webpush-options+json"))
        setattr(cls, "application/whoispp-query",
            PermissibleValue(text="application/whoispp-query"))
        setattr(cls, "application/whoispp-response",
            PermissibleValue(text="application/whoispp-response"))
        setattr(cls, "application/widget",
            PermissibleValue(text="application/widget"))
        setattr(cls, "application/wita",
            PermissibleValue(text="application/wita"))
        setattr(cls, "application/wordperfect5.1",
            PermissibleValue(text="application/wordperfect5.1"))
        setattr(cls, "application/wsdl+xml",
            PermissibleValue(text="application/wsdl+xml"))
        setattr(cls, "application/wspolicy+xml",
            PermissibleValue(text="application/wspolicy+xml"))
        setattr(cls, "application/x400-bp",
            PermissibleValue(text="application/x400-bp"))
        setattr(cls, "application/xacml+xml",
            PermissibleValue(text="application/xacml+xml"))
        setattr(cls, "application/xcap-att+xml",
            PermissibleValue(text="application/xcap-att+xml"))
        setattr(cls, "application/xcap-caps+xml",
            PermissibleValue(text="application/xcap-caps+xml"))
        setattr(cls, "application/xcap-diff+xml",
            PermissibleValue(text="application/xcap-diff+xml"))
        setattr(cls, "application/xcap-el+xml",
            PermissibleValue(text="application/xcap-el+xml"))
        setattr(cls, "application/xcap-error+xml",
            PermissibleValue(text="application/xcap-error+xml"))
        setattr(cls, "application/xcap-ns+xml",
            PermissibleValue(text="application/xcap-ns+xml"))
        setattr(cls, "application/xcon-conference-info+xml",
            PermissibleValue(text="application/xcon-conference-info+xml"))
        setattr(cls, "application/xcon-conference-info-diff+xml",
            PermissibleValue(text="application/xcon-conference-info-diff+xml"))
        setattr(cls, "application/xenc+xml",
            PermissibleValue(text="application/xenc+xml"))
        setattr(cls, "application/xfdf",
            PermissibleValue(text="application/xfdf"))
        setattr(cls, "application/xhtml+xml",
            PermissibleValue(text="application/xhtml+xml"))
        setattr(cls, "application/xliff+xml",
            PermissibleValue(text="application/xliff+xml"))
        setattr(cls, "application/xml",
            PermissibleValue(text="application/xml"))
        setattr(cls, "application/xml-dtd",
            PermissibleValue(text="application/xml-dtd"))
        setattr(cls, "application/xml-external-parsed-entity",
            PermissibleValue(text="application/xml-external-parsed-entity"))
        setattr(cls, "application/xml-patch+xml",
            PermissibleValue(text="application/xml-patch+xml"))
        setattr(cls, "application/xmpp+xml",
            PermissibleValue(text="application/xmpp+xml"))
        setattr(cls, "application/xop+xml",
            PermissibleValue(text="application/xop+xml"))
        setattr(cls, "application/x-pki-message",
            PermissibleValue(text="application/x-pki-message"))
        setattr(cls, "application/xslt+xml",
            PermissibleValue(text="application/xslt+xml"))
        setattr(cls, "application/xv+xml",
            PermissibleValue(text="application/xv+xml"))
        setattr(cls, "application/x-www-form-urlencoded",
            PermissibleValue(text="application/x-www-form-urlencoded"))
        setattr(cls, "application/x-x509-ca-cert",
            PermissibleValue(text="application/x-x509-ca-cert"))
        setattr(cls, "application/x-x509-ca-ra-cert",
            PermissibleValue(text="application/x-x509-ca-ra-cert"))
        setattr(cls, "application/x-x509-next-ca-cert",
            PermissibleValue(text="application/x-x509-next-ca-cert"))
        setattr(cls, "application/yaml",
            PermissibleValue(text="application/yaml"))
        setattr(cls, "application/yang",
            PermissibleValue(text="application/yang"))
        setattr(cls, "application/yang-data+cbor",
            PermissibleValue(text="application/yang-data+cbor"))
        setattr(cls, "application/yang-data+json",
            PermissibleValue(text="application/yang-data+json"))
        setattr(cls, "application/yang-data+xml",
            PermissibleValue(text="application/yang-data+xml"))
        setattr(cls, "application/yang-patch+json",
            PermissibleValue(text="application/yang-patch+json"))
        setattr(cls, "application/yang-patch+xml",
            PermissibleValue(text="application/yang-patch+xml"))
        setattr(cls, "application/yang-sid+json",
            PermissibleValue(text="application/yang-sid+json"))
        setattr(cls, "application/yin+xml",
            PermissibleValue(text="application/yin+xml"))
        setattr(cls, "application/zip",
            PermissibleValue(text="application/zip"))
        setattr(cls, "application/zlib",
            PermissibleValue(text="application/zlib"))
        setattr(cls, "application/zstd",
            PermissibleValue(text="application/zstd"))
        setattr(cls, "audio/1d-interleaved-parityfec",
            PermissibleValue(text="audio/1d-interleaved-parityfec"))
        setattr(cls, "audio/32kadpcm",
            PermissibleValue(text="audio/32kadpcm"))
        setattr(cls, "audio/3gpp",
            PermissibleValue(text="audio/3gpp"))
        setattr(cls, "audio/3gpp2",
            PermissibleValue(text="audio/3gpp2"))
        setattr(cls, "audio/aac",
            PermissibleValue(text="audio/aac"))
        setattr(cls, "audio/ac3",
            PermissibleValue(text="audio/ac3"))
        setattr(cls, "audio/AMR",
            PermissibleValue(text="audio/AMR"))
        setattr(cls, "audio/AMR-WB",
            PermissibleValue(text="audio/AMR-WB"))
        setattr(cls, "audio/amr-wb+",
            PermissibleValue(text="audio/amr-wb+"))
        setattr(cls, "audio/aptx",
            PermissibleValue(text="audio/aptx"))
        setattr(cls, "audio/asc",
            PermissibleValue(text="audio/asc"))
        setattr(cls, "audio/ATRAC3",
            PermissibleValue(text="audio/ATRAC3"))
        setattr(cls, "audio/ATRAC-ADVANCED-LOSSLESS",
            PermissibleValue(text="audio/ATRAC-ADVANCED-LOSSLESS"))
        setattr(cls, "audio/ATRAC-X",
            PermissibleValue(text="audio/ATRAC-X"))
        setattr(cls, "audio/basic",
            PermissibleValue(text="audio/basic"))
        setattr(cls, "audio/BV16",
            PermissibleValue(text="audio/BV16"))
        setattr(cls, "audio/BV32",
            PermissibleValue(text="audio/BV32"))
        setattr(cls, "audio/clearmode",
            PermissibleValue(text="audio/clearmode"))
        setattr(cls, "audio/CN",
            PermissibleValue(text="audio/CN"))
        setattr(cls, "audio/DAT12",
            PermissibleValue(text="audio/DAT12"))
        setattr(cls, "audio/dls",
            PermissibleValue(text="audio/dls"))
        setattr(cls, "audio/dsr-es201108",
            PermissibleValue(text="audio/dsr-es201108"))
        setattr(cls, "audio/dsr-es202050",
            PermissibleValue(text="audio/dsr-es202050"))
        setattr(cls, "audio/dsr-es202211",
            PermissibleValue(text="audio/dsr-es202211"))
        setattr(cls, "audio/dsr-es202212",
            PermissibleValue(text="audio/dsr-es202212"))
        setattr(cls, "audio/DV",
            PermissibleValue(text="audio/DV"))
        setattr(cls, "audio/DVI4",
            PermissibleValue(text="audio/DVI4"))
        setattr(cls, "audio/eac3",
            PermissibleValue(text="audio/eac3"))
        setattr(cls, "audio/encaprtp",
            PermissibleValue(text="audio/encaprtp"))
        setattr(cls, "audio/EVRC",
            PermissibleValue(text="audio/EVRC"))
        setattr(cls, "audio/EVRC0",
            PermissibleValue(text="audio/EVRC0"))
        setattr(cls, "audio/EVRC1",
            PermissibleValue(text="audio/EVRC1"))
        setattr(cls, "audio/EVRCB",
            PermissibleValue(text="audio/EVRCB"))
        setattr(cls, "audio/EVRCB0",
            PermissibleValue(text="audio/EVRCB0"))
        setattr(cls, "audio/EVRCB1",
            PermissibleValue(text="audio/EVRCB1"))
        setattr(cls, "audio/EVRCNW",
            PermissibleValue(text="audio/EVRCNW"))
        setattr(cls, "audio/EVRCNW0",
            PermissibleValue(text="audio/EVRCNW0"))
        setattr(cls, "audio/EVRCNW1",
            PermissibleValue(text="audio/EVRCNW1"))
        setattr(cls, "audio/EVRC-QCP",
            PermissibleValue(text="audio/EVRC-QCP"))
        setattr(cls, "audio/EVRCWB",
            PermissibleValue(text="audio/EVRCWB"))
        setattr(cls, "audio/EVRCWB0",
            PermissibleValue(text="audio/EVRCWB0"))
        setattr(cls, "audio/EVRCWB1",
            PermissibleValue(text="audio/EVRCWB1"))
        setattr(cls, "audio/EVS",
            PermissibleValue(text="audio/EVS"))
        setattr(cls, "audio/example",
            PermissibleValue(text="audio/example"))
        setattr(cls, "audio/flac",
            PermissibleValue(text="audio/flac"))
        setattr(cls, "audio/flexfec",
            PermissibleValue(text="audio/flexfec"))
        setattr(cls, "audio/fwdred",
            PermissibleValue(text="audio/fwdred"))
        setattr(cls, "audio/G711-0",
            PermissibleValue(text="audio/G711-0"))
        setattr(cls, "audio/G719",
            PermissibleValue(text="audio/G719"))
        setattr(cls, "audio/G722",
            PermissibleValue(text="audio/G722"))
        setattr(cls, "audio/G7221",
            PermissibleValue(text="audio/G7221"))
        setattr(cls, "audio/G723",
            PermissibleValue(text="audio/G723"))
        setattr(cls, "audio/G726-16",
            PermissibleValue(text="audio/G726-16"))
        setattr(cls, "audio/G726-24",
            PermissibleValue(text="audio/G726-24"))
        setattr(cls, "audio/G726-32",
            PermissibleValue(text="audio/G726-32"))
        setattr(cls, "audio/G726-40",
            PermissibleValue(text="audio/G726-40"))
        setattr(cls, "audio/G728",
            PermissibleValue(text="audio/G728"))
        setattr(cls, "audio/G729",
            PermissibleValue(text="audio/G729"))
        setattr(cls, "audio/G7291",
            PermissibleValue(text="audio/G7291"))
        setattr(cls, "audio/G729D",
            PermissibleValue(text="audio/G729D"))
        setattr(cls, "audio/G729E",
            PermissibleValue(text="audio/G729E"))
        setattr(cls, "audio/GSM",
            PermissibleValue(text="audio/GSM"))
        setattr(cls, "audio/GSM-EFR",
            PermissibleValue(text="audio/GSM-EFR"))
        setattr(cls, "audio/GSM-HR-08",
            PermissibleValue(text="audio/GSM-HR-08"))
        setattr(cls, "audio/iLBC",
            PermissibleValue(text="audio/iLBC"))
        setattr(cls, "audio/ip-mr_v2.5",
            PermissibleValue(text="audio/ip-mr_v2.5"))
        setattr(cls, "audio/L16",
            PermissibleValue(text="audio/L16"))
        setattr(cls, "audio/L20",
            PermissibleValue(text="audio/L20"))
        setattr(cls, "audio/L24",
            PermissibleValue(text="audio/L24"))
        setattr(cls, "audio/L8",
            PermissibleValue(text="audio/L8"))
        setattr(cls, "audio/LPC",
            PermissibleValue(text="audio/LPC"))
        setattr(cls, "audio/matroska",
            PermissibleValue(text="audio/matroska"))
        setattr(cls, "audio/MELP",
            PermissibleValue(text="audio/MELP"))
        setattr(cls, "audio/MELP1200",
            PermissibleValue(text="audio/MELP1200"))
        setattr(cls, "audio/MELP2400",
            PermissibleValue(text="audio/MELP2400"))
        setattr(cls, "audio/MELP600",
            PermissibleValue(text="audio/MELP600"))
        setattr(cls, "audio/mhas",
            PermissibleValue(text="audio/mhas"))
        setattr(cls, "audio/midi-clip",
            PermissibleValue(text="audio/midi-clip"))
        setattr(cls, "audio/mobile-xmf",
            PermissibleValue(text="audio/mobile-xmf"))
        setattr(cls, "audio/mp4",
            PermissibleValue(text="audio/mp4"))
        setattr(cls, "audio/MP4A-LATM",
            PermissibleValue(text="audio/MP4A-LATM"))
        setattr(cls, "audio/MPA",
            PermissibleValue(text="audio/MPA"))
        setattr(cls, "audio/mpa-robust",
            PermissibleValue(text="audio/mpa-robust"))
        setattr(cls, "audio/mpeg",
            PermissibleValue(text="audio/mpeg"))
        setattr(cls, "audio/mpeg4-generic",
            PermissibleValue(text="audio/mpeg4-generic"))
        setattr(cls, "audio/ogg",
            PermissibleValue(text="audio/ogg"))
        setattr(cls, "audio/opus",
            PermissibleValue(text="audio/opus"))
        setattr(cls, "audio/parityfec",
            PermissibleValue(text="audio/parityfec"))
        setattr(cls, "audio/PCMA",
            PermissibleValue(text="audio/PCMA"))
        setattr(cls, "audio/PCMA-WB",
            PermissibleValue(text="audio/PCMA-WB"))
        setattr(cls, "audio/PCMU",
            PermissibleValue(text="audio/PCMU"))
        setattr(cls, "audio/PCMU-WB",
            PermissibleValue(text="audio/PCMU-WB"))
        setattr(cls, "audio/prs.sid",
            PermissibleValue(text="audio/prs.sid"))
        setattr(cls, "audio/QCELP",
            PermissibleValue(text="audio/QCELP"))
        setattr(cls, "audio/raptorfec",
            PermissibleValue(text="audio/raptorfec"))
        setattr(cls, "audio/RED",
            PermissibleValue(text="audio/RED"))
        setattr(cls, "audio/rtp-enc-aescm128",
            PermissibleValue(text="audio/rtp-enc-aescm128"))
        setattr(cls, "audio/rtploopback",
            PermissibleValue(text="audio/rtploopback"))
        setattr(cls, "audio/rtp-midi",
            PermissibleValue(text="audio/rtp-midi"))
        setattr(cls, "audio/rtx",
            PermissibleValue(text="audio/rtx"))
        setattr(cls, "audio/scip",
            PermissibleValue(text="audio/scip"))
        setattr(cls, "audio/SMV",
            PermissibleValue(text="audio/SMV"))
        setattr(cls, "audio/SMV0",
            PermissibleValue(text="audio/SMV0"))
        setattr(cls, "audio/SMV-QCP",
            PermissibleValue(text="audio/SMV-QCP"))
        setattr(cls, "audio/sofa",
            PermissibleValue(text="audio/sofa"))
        setattr(cls, "audio/speex",
            PermissibleValue(text="audio/speex"))
        setattr(cls, "audio/sp-midi",
            PermissibleValue(text="audio/sp-midi"))
        setattr(cls, "audio/t140c",
            PermissibleValue(text="audio/t140c"))
        setattr(cls, "audio/t38",
            PermissibleValue(text="audio/t38"))
        setattr(cls, "audio/telephone-event",
            PermissibleValue(text="audio/telephone-event"))
        setattr(cls, "audio/TETRA_ACELP",
            PermissibleValue(text="audio/TETRA_ACELP"))
        setattr(cls, "audio/TETRA_ACELP_BB",
            PermissibleValue(text="audio/TETRA_ACELP_BB"))
        setattr(cls, "audio/tone",
            PermissibleValue(text="audio/tone"))
        setattr(cls, "audio/TSVCIS",
            PermissibleValue(text="audio/TSVCIS"))
        setattr(cls, "audio/UEMCLIP",
            PermissibleValue(text="audio/UEMCLIP"))
        setattr(cls, "audio/ulpfec",
            PermissibleValue(text="audio/ulpfec"))
        setattr(cls, "audio/usac",
            PermissibleValue(text="audio/usac"))
        setattr(cls, "audio/VDVI",
            PermissibleValue(text="audio/VDVI"))
        setattr(cls, "audio/VMR-WB",
            PermissibleValue(text="audio/VMR-WB"))
        setattr(cls, "audio/vnd.3gpp.iufp",
            PermissibleValue(text="audio/vnd.3gpp.iufp"))
        setattr(cls, "audio/vnd.4SB",
            PermissibleValue(text="audio/vnd.4SB"))
        setattr(cls, "audio/vnd.audiokoz",
            PermissibleValue(text="audio/vnd.audiokoz"))
        setattr(cls, "audio/vnd.CELP",
            PermissibleValue(text="audio/vnd.CELP"))
        setattr(cls, "audio/vnd.cisco.nse",
            PermissibleValue(text="audio/vnd.cisco.nse"))
        setattr(cls, "audio/vnd.cmles.radio-events",
            PermissibleValue(text="audio/vnd.cmles.radio-events"))
        setattr(cls, "audio/vnd.cns.anp1",
            PermissibleValue(text="audio/vnd.cns.anp1"))
        setattr(cls, "audio/vnd.cns.inf1",
            PermissibleValue(text="audio/vnd.cns.inf1"))
        setattr(cls, "audio/vnd.dece.audio",
            PermissibleValue(text="audio/vnd.dece.audio"))
        setattr(cls, "audio/vnd.digital-winds",
            PermissibleValue(text="audio/vnd.digital-winds"))
        setattr(cls, "audio/vnd.dlna.adts",
            PermissibleValue(text="audio/vnd.dlna.adts"))
        setattr(cls, "audio/vnd.dolby.heaac.1",
            PermissibleValue(text="audio/vnd.dolby.heaac.1"))
        setattr(cls, "audio/vnd.dolby.heaac.2",
            PermissibleValue(text="audio/vnd.dolby.heaac.2"))
        setattr(cls, "audio/vnd.dolby.mlp",
            PermissibleValue(text="audio/vnd.dolby.mlp"))
        setattr(cls, "audio/vnd.dolby.mps",
            PermissibleValue(text="audio/vnd.dolby.mps"))
        setattr(cls, "audio/vnd.dolby.pl2",
            PermissibleValue(text="audio/vnd.dolby.pl2"))
        setattr(cls, "audio/vnd.dolby.pl2x",
            PermissibleValue(text="audio/vnd.dolby.pl2x"))
        setattr(cls, "audio/vnd.dolby.pl2z",
            PermissibleValue(text="audio/vnd.dolby.pl2z"))
        setattr(cls, "audio/vnd.dolby.pulse.1",
            PermissibleValue(text="audio/vnd.dolby.pulse.1"))
        setattr(cls, "audio/vnd.dra",
            PermissibleValue(text="audio/vnd.dra"))
        setattr(cls, "audio/vnd.dts",
            PermissibleValue(text="audio/vnd.dts"))
        setattr(cls, "audio/vnd.dts.hd",
            PermissibleValue(text="audio/vnd.dts.hd"))
        setattr(cls, "audio/vnd.dts.uhd",
            PermissibleValue(text="audio/vnd.dts.uhd"))
        setattr(cls, "audio/vnd.dvb.file",
            PermissibleValue(text="audio/vnd.dvb.file"))
        setattr(cls, "audio/vnd.everad.plj",
            PermissibleValue(text="audio/vnd.everad.plj"))
        setattr(cls, "audio/vnd.hns.audio",
            PermissibleValue(text="audio/vnd.hns.audio"))
        setattr(cls, "audio/vnd.lucent.voice",
            PermissibleValue(text="audio/vnd.lucent.voice"))
        setattr(cls, "audio/vnd.ms-playready.media.pya",
            PermissibleValue(text="audio/vnd.ms-playready.media.pya"))
        setattr(cls, "audio/vnd.nokia.mobile-xmf",
            PermissibleValue(text="audio/vnd.nokia.mobile-xmf"))
        setattr(cls, "audio/vnd.nortel.vbk",
            PermissibleValue(text="audio/vnd.nortel.vbk"))
        setattr(cls, "audio/vnd.nuera.ecelp4800",
            PermissibleValue(text="audio/vnd.nuera.ecelp4800"))
        setattr(cls, "audio/vnd.nuera.ecelp7470",
            PermissibleValue(text="audio/vnd.nuera.ecelp7470"))
        setattr(cls, "audio/vnd.nuera.ecelp9600",
            PermissibleValue(text="audio/vnd.nuera.ecelp9600"))
        setattr(cls, "audio/vnd.octel.sbc",
            PermissibleValue(text="audio/vnd.octel.sbc"))
        setattr(cls, "audio/vnd.presonus.multitrack",
            PermissibleValue(text="audio/vnd.presonus.multitrack"))
        setattr(cls, "audio/vnd.qcelp",
            PermissibleValue(text="audio/vnd.qcelp"))
        setattr(cls, "audio/vnd.rhetorex.32kadpcm",
            PermissibleValue(text="audio/vnd.rhetorex.32kadpcm"))
        setattr(cls, "audio/vnd.rip",
            PermissibleValue(text="audio/vnd.rip"))
        setattr(cls, "audio/vnd.sealedmedia.softseal.mpeg",
            PermissibleValue(text="audio/vnd.sealedmedia.softseal.mpeg"))
        setattr(cls, "audio/vnd.vmx.cvsd",
            PermissibleValue(text="audio/vnd.vmx.cvsd"))
        setattr(cls, "audio/vorbis",
            PermissibleValue(text="audio/vorbis"))
        setattr(cls, "audio/vorbis-config",
            PermissibleValue(text="audio/vorbis-config"))
        setattr(cls, "font/collection",
            PermissibleValue(text="font/collection"))
        setattr(cls, "font/otf",
            PermissibleValue(text="font/otf"))
        setattr(cls, "font/sfnt",
            PermissibleValue(text="font/sfnt"))
        setattr(cls, "font/ttf",
            PermissibleValue(text="font/ttf"))
        setattr(cls, "font/woff",
            PermissibleValue(text="font/woff"))
        setattr(cls, "font/woff2",
            PermissibleValue(text="font/woff2"))
        setattr(cls, "haptics/hjif",
            PermissibleValue(text="haptics/hjif"))
        setattr(cls, "haptics/hmpg",
            PermissibleValue(text="haptics/hmpg"))
        setattr(cls, "haptics/ivs",
            PermissibleValue(text="haptics/ivs"))
        setattr(cls, "image/aces",
            PermissibleValue(text="image/aces"))
        setattr(cls, "image/apng",
            PermissibleValue(text="image/apng"))
        setattr(cls, "image/avci",
            PermissibleValue(text="image/avci"))
        setattr(cls, "image/avcs",
            PermissibleValue(text="image/avcs"))
        setattr(cls, "image/avif",
            PermissibleValue(text="image/avif"))
        setattr(cls, "image/bmp",
            PermissibleValue(text="image/bmp"))
        setattr(cls, "image/cgm",
            PermissibleValue(text="image/cgm"))
        setattr(cls, "image/dicom-rle",
            PermissibleValue(text="image/dicom-rle"))
        setattr(cls, "image/dpx",
            PermissibleValue(text="image/dpx"))
        setattr(cls, "image/emf",
            PermissibleValue(text="image/emf"))
        setattr(cls, "image/example",
            PermissibleValue(text="image/example"))
        setattr(cls, "image/fits",
            PermissibleValue(text="image/fits"))
        setattr(cls, "image/g3fax",
            PermissibleValue(text="image/g3fax"))
        setattr(cls, "image/gif",
            PermissibleValue(text="image/gif"))
        setattr(cls, "image/heic",
            PermissibleValue(text="image/heic"))
        setattr(cls, "image/heic-sequence",
            PermissibleValue(text="image/heic-sequence"))
        setattr(cls, "image/heif",
            PermissibleValue(text="image/heif"))
        setattr(cls, "image/heif-sequence",
            PermissibleValue(text="image/heif-sequence"))
        setattr(cls, "image/hej2k",
            PermissibleValue(text="image/hej2k"))
        setattr(cls, "image/hsj2",
            PermissibleValue(text="image/hsj2"))
        setattr(cls, "image/ief",
            PermissibleValue(text="image/ief"))
        setattr(cls, "image/j2c",
            PermissibleValue(text="image/j2c"))
        setattr(cls, "image/jaii",
            PermissibleValue(text="image/jaii"))
        setattr(cls, "image/jais",
            PermissibleValue(text="image/jais"))
        setattr(cls, "image/jls",
            PermissibleValue(text="image/jls"))
        setattr(cls, "image/jp2",
            PermissibleValue(text="image/jp2"))
        setattr(cls, "image/jpeg",
            PermissibleValue(text="image/jpeg"))
        setattr(cls, "image/jph",
            PermissibleValue(text="image/jph"))
        setattr(cls, "image/jphc",
            PermissibleValue(text="image/jphc"))
        setattr(cls, "image/jpm",
            PermissibleValue(text="image/jpm"))
        setattr(cls, "image/jpx",
            PermissibleValue(text="image/jpx"))
        setattr(cls, "image/jxl",
            PermissibleValue(text="image/jxl"))
        setattr(cls, "image/jxr",
            PermissibleValue(text="image/jxr"))
        setattr(cls, "image/jxrA",
            PermissibleValue(text="image/jxrA"))
        setattr(cls, "image/jxrS",
            PermissibleValue(text="image/jxrS"))
        setattr(cls, "image/jxs",
            PermissibleValue(text="image/jxs"))
        setattr(cls, "image/jxsc",
            PermissibleValue(text="image/jxsc"))
        setattr(cls, "image/jxsi",
            PermissibleValue(text="image/jxsi"))
        setattr(cls, "image/jxss",
            PermissibleValue(text="image/jxss"))
        setattr(cls, "image/ktx",
            PermissibleValue(text="image/ktx"))
        setattr(cls, "image/ktx2",
            PermissibleValue(text="image/ktx2"))
        setattr(cls, "image/naplps",
            PermissibleValue(text="image/naplps"))
        setattr(cls, "image/png",
            PermissibleValue(text="image/png"))
        setattr(cls, "image/prs.btif",
            PermissibleValue(text="image/prs.btif"))
        setattr(cls, "image/prs.pti",
            PermissibleValue(text="image/prs.pti"))
        setattr(cls, "image/pwg-raster",
            PermissibleValue(text="image/pwg-raster"))
        setattr(cls, "image/svg+xml",
            PermissibleValue(text="image/svg+xml"))
        setattr(cls, "image/t38",
            PermissibleValue(text="image/t38"))
        setattr(cls, "image/tiff",
            PermissibleValue(text="image/tiff"))
        setattr(cls, "image/tiff-fx",
            PermissibleValue(text="image/tiff-fx"))
        setattr(cls, "image/vnd.adobe.photoshop",
            PermissibleValue(text="image/vnd.adobe.photoshop"))
        setattr(cls, "image/vnd.airzip.accelerator.azv",
            PermissibleValue(text="image/vnd.airzip.accelerator.azv"))
        setattr(cls, "image/vnd.cns.inf2",
            PermissibleValue(text="image/vnd.cns.inf2"))
        setattr(cls, "image/vnd.dece.graphic",
            PermissibleValue(text="image/vnd.dece.graphic"))
        setattr(cls, "image/vnd.djvu",
            PermissibleValue(text="image/vnd.djvu"))
        setattr(cls, "image/vnd.dvb.subtitle",
            PermissibleValue(text="image/vnd.dvb.subtitle"))
        setattr(cls, "image/vnd.dwg",
            PermissibleValue(text="image/vnd.dwg"))
        setattr(cls, "image/vnd.dxf",
            PermissibleValue(text="image/vnd.dxf"))
        setattr(cls, "image/vnd.fastbidsheet",
            PermissibleValue(text="image/vnd.fastbidsheet"))
        setattr(cls, "image/vnd.fpx",
            PermissibleValue(text="image/vnd.fpx"))
        setattr(cls, "image/vnd.fst",
            PermissibleValue(text="image/vnd.fst"))
        setattr(cls, "image/vnd.fujixerox.edmics-mmr",
            PermissibleValue(text="image/vnd.fujixerox.edmics-mmr"))
        setattr(cls, "image/vnd.fujixerox.edmics-rlc",
            PermissibleValue(text="image/vnd.fujixerox.edmics-rlc"))
        setattr(cls, "image/vnd.globalgraphics.pgb",
            PermissibleValue(text="image/vnd.globalgraphics.pgb"))
        setattr(cls, "image/vnd.microsoft.icon",
            PermissibleValue(text="image/vnd.microsoft.icon"))
        setattr(cls, "image/vnd.mix",
            PermissibleValue(text="image/vnd.mix"))
        setattr(cls, "image/vnd.mozilla.apng",
            PermissibleValue(text="image/vnd.mozilla.apng"))
        setattr(cls, "image/vnd.ms-modi",
            PermissibleValue(text="image/vnd.ms-modi"))
        setattr(cls, "image/vnd.net-fpx",
            PermissibleValue(text="image/vnd.net-fpx"))
        setattr(cls, "image/vnd.pco.b16",
            PermissibleValue(text="image/vnd.pco.b16"))
        setattr(cls, "image/vnd.radiance",
            PermissibleValue(text="image/vnd.radiance"))
        setattr(cls, "image/vnd.sealed.png",
            PermissibleValue(text="image/vnd.sealed.png"))
        setattr(cls, "image/vnd.sealedmedia.softseal.gif",
            PermissibleValue(text="image/vnd.sealedmedia.softseal.gif"))
        setattr(cls, "image/vnd.sealedmedia.softseal.jpg",
            PermissibleValue(text="image/vnd.sealedmedia.softseal.jpg"))
        setattr(cls, "image/vnd.svf",
            PermissibleValue(text="image/vnd.svf"))
        setattr(cls, "image/vnd.tencent.tap",
            PermissibleValue(text="image/vnd.tencent.tap"))
        setattr(cls, "image/vnd.valve.source.texture",
            PermissibleValue(text="image/vnd.valve.source.texture"))
        setattr(cls, "image/vnd.wap.wbmp",
            PermissibleValue(text="image/vnd.wap.wbmp"))
        setattr(cls, "image/vnd.xiff",
            PermissibleValue(text="image/vnd.xiff"))
        setattr(cls, "image/vnd.zbrush.pcx",
            PermissibleValue(text="image/vnd.zbrush.pcx"))
        setattr(cls, "image/webp",
            PermissibleValue(text="image/webp"))
        setattr(cls, "image/wmf",
            PermissibleValue(text="image/wmf"))
        setattr(cls, "image/x-emf",
            PermissibleValue(text="image/x-emf"))
        setattr(cls, "image/x-wmf",
            PermissibleValue(text="image/x-wmf"))
        setattr(cls, "message/bhttp",
            PermissibleValue(text="message/bhttp"))
        setattr(cls, "message/CPIM",
            PermissibleValue(text="message/CPIM"))
        setattr(cls, "message/delivery-status",
            PermissibleValue(text="message/delivery-status"))
        setattr(cls, "message/disposition-notification",
            PermissibleValue(text="message/disposition-notification"))
        setattr(cls, "message/example",
            PermissibleValue(text="message/example"))
        setattr(cls, "message/external-body",
            PermissibleValue(text="message/external-body"))
        setattr(cls, "message/feedback-report",
            PermissibleValue(text="message/feedback-report"))
        setattr(cls, "message/global",
            PermissibleValue(text="message/global"))
        setattr(cls, "message/global-delivery-status",
            PermissibleValue(text="message/global-delivery-status"))
        setattr(cls, "message/global-disposition-notification",
            PermissibleValue(text="message/global-disposition-notification"))
        setattr(cls, "message/global-headers",
            PermissibleValue(text="message/global-headers"))
        setattr(cls, "message/http",
            PermissibleValue(text="message/http"))
        setattr(cls, "message/imdn+xml",
            PermissibleValue(text="message/imdn+xml"))
        setattr(cls, "message/mls",
            PermissibleValue(text="message/mls"))
        setattr(cls, "message/news",
            PermissibleValue(text="message/news"))
        setattr(cls, "message/ohttp-req",
            PermissibleValue(text="message/ohttp-req"))
        setattr(cls, "message/ohttp-res",
            PermissibleValue(text="message/ohttp-res"))
        setattr(cls, "message/partial",
            PermissibleValue(text="message/partial"))
        setattr(cls, "message/rfc822",
            PermissibleValue(text="message/rfc822"))
        setattr(cls, "message/s-http",
            PermissibleValue(text="message/s-http"))
        setattr(cls, "message/sip",
            PermissibleValue(text="message/sip"))
        setattr(cls, "message/sipfrag",
            PermissibleValue(text="message/sipfrag"))
        setattr(cls, "message/tracking-status",
            PermissibleValue(text="message/tracking-status"))
        setattr(cls, "message/vnd.si.simp",
            PermissibleValue(text="message/vnd.si.simp"))
        setattr(cls, "message/vnd.wfa.wsc",
            PermissibleValue(text="message/vnd.wfa.wsc"))
        setattr(cls, "model/3mf",
            PermissibleValue(text="model/3mf"))
        setattr(cls, "model/e57",
            PermissibleValue(text="model/e57"))
        setattr(cls, "model/example",
            PermissibleValue(text="model/example"))
        setattr(cls, "model/gltf+json",
            PermissibleValue(text="model/gltf+json"))
        setattr(cls, "model/gltf-binary",
            PermissibleValue(text="model/gltf-binary"))
        setattr(cls, "model/iges",
            PermissibleValue(text="model/iges"))
        setattr(cls, "model/JT",
            PermissibleValue(text="model/JT"))
        setattr(cls, "model/mesh",
            PermissibleValue(text="model/mesh"))
        setattr(cls, "model/mtl",
            PermissibleValue(text="model/mtl"))
        setattr(cls, "model/obj",
            PermissibleValue(text="model/obj"))
        setattr(cls, "model/prc",
            PermissibleValue(text="model/prc"))
        setattr(cls, "model/step",
            PermissibleValue(text="model/step"))
        setattr(cls, "model/step+xml",
            PermissibleValue(text="model/step+xml"))
        setattr(cls, "model/step+zip",
            PermissibleValue(text="model/step+zip"))
        setattr(cls, "model/step-xml+zip",
            PermissibleValue(text="model/step-xml+zip"))
        setattr(cls, "model/stl",
            PermissibleValue(text="model/stl"))
        setattr(cls, "model/u3d",
            PermissibleValue(text="model/u3d"))
        setattr(cls, "model/vnd.bary",
            PermissibleValue(text="model/vnd.bary"))
        setattr(cls, "model/vnd.cld",
            PermissibleValue(text="model/vnd.cld"))
        setattr(cls, "model/vnd.collada+xml",
            PermissibleValue(text="model/vnd.collada+xml"))
        setattr(cls, "model/vnd.dwf",
            PermissibleValue(text="model/vnd.dwf"))
        setattr(cls, "model/vnd.flatland.3dml",
            PermissibleValue(text="model/vnd.flatland.3dml"))
        setattr(cls, "model/vnd.gdl",
            PermissibleValue(text="model/vnd.gdl"))
        setattr(cls, "model/vnd.gs-gdl",
            PermissibleValue(text="model/vnd.gs-gdl"))
        setattr(cls, "model/vnd.gtw",
            PermissibleValue(text="model/vnd.gtw"))
        setattr(cls, "model/vnd.moml+xml",
            PermissibleValue(text="model/vnd.moml+xml"))
        setattr(cls, "model/vnd.mts",
            PermissibleValue(text="model/vnd.mts"))
        setattr(cls, "model/vnd.opengex",
            PermissibleValue(text="model/vnd.opengex"))
        setattr(cls, "model/vnd.parasolid.transmit.binary",
            PermissibleValue(text="model/vnd.parasolid.transmit.binary"))
        setattr(cls, "model/vnd.parasolid.transmit.text",
            PermissibleValue(text="model/vnd.parasolid.transmit.text"))
        setattr(cls, "model/vnd.pytha.pyox",
            PermissibleValue(text="model/vnd.pytha.pyox"))
        setattr(cls, "model/vnd.rosette.annotated-data-model",
            PermissibleValue(text="model/vnd.rosette.annotated-data-model"))
        setattr(cls, "model/vnd.sap.vds",
            PermissibleValue(text="model/vnd.sap.vds"))
        setattr(cls, "model/vnd.usda",
            PermissibleValue(text="model/vnd.usda"))
        setattr(cls, "model/vnd.usdz+zip",
            PermissibleValue(text="model/vnd.usdz+zip"))
        setattr(cls, "model/vnd.valve.source.compiled-map",
            PermissibleValue(text="model/vnd.valve.source.compiled-map"))
        setattr(cls, "model/vnd.vtu",
            PermissibleValue(text="model/vnd.vtu"))
        setattr(cls, "model/vrml",
            PermissibleValue(text="model/vrml"))
        setattr(cls, "model/x3d+fastinfoset",
            PermissibleValue(text="model/x3d+fastinfoset"))
        setattr(cls, "model/x3d+xml",
            PermissibleValue(text="model/x3d+xml"))
        setattr(cls, "model/x3d-vrml",
            PermissibleValue(text="model/x3d-vrml"))
        setattr(cls, "multipart/alternative",
            PermissibleValue(text="multipart/alternative"))
        setattr(cls, "multipart/appledouble",
            PermissibleValue(text="multipart/appledouble"))
        setattr(cls, "multipart/byteranges",
            PermissibleValue(text="multipart/byteranges"))
        setattr(cls, "multipart/digest",
            PermissibleValue(text="multipart/digest"))
        setattr(cls, "multipart/encrypted",
            PermissibleValue(text="multipart/encrypted"))
        setattr(cls, "multipart/example",
            PermissibleValue(text="multipart/example"))
        setattr(cls, "multipart/form-data",
            PermissibleValue(text="multipart/form-data"))
        setattr(cls, "multipart/header-set",
            PermissibleValue(text="multipart/header-set"))
        setattr(cls, "multipart/mixed",
            PermissibleValue(text="multipart/mixed"))
        setattr(cls, "multipart/multilingual",
            PermissibleValue(text="multipart/multilingual"))
        setattr(cls, "multipart/parallel",
            PermissibleValue(text="multipart/parallel"))
        setattr(cls, "multipart/related",
            PermissibleValue(text="multipart/related"))
        setattr(cls, "multipart/report",
            PermissibleValue(text="multipart/report"))
        setattr(cls, "multipart/signed",
            PermissibleValue(text="multipart/signed"))
        setattr(cls, "multipart/vnd.bint.med-plus",
            PermissibleValue(text="multipart/vnd.bint.med-plus"))
        setattr(cls, "multipart/voice-message",
            PermissibleValue(text="multipart/voice-message"))
        setattr(cls, "multipart/x-mixed-replace",
            PermissibleValue(text="multipart/x-mixed-replace"))
        setattr(cls, "text/1d-interleaved-parityfec",
            PermissibleValue(text="text/1d-interleaved-parityfec"))
        setattr(cls, "text/cache-manifest",
            PermissibleValue(text="text/cache-manifest"))
        setattr(cls, "text/calendar",
            PermissibleValue(text="text/calendar"))
        setattr(cls, "text/cql",
            PermissibleValue(text="text/cql"))
        setattr(cls, "text/cql-expression",
            PermissibleValue(text="text/cql-expression"))
        setattr(cls, "text/cql-identifier",
            PermissibleValue(text="text/cql-identifier"))
        setattr(cls, "text/css",
            PermissibleValue(text="text/css"))
        setattr(cls, "text/csv",
            PermissibleValue(text="text/csv"))
        setattr(cls, "text/csv-schema",
            PermissibleValue(text="text/csv-schema"))
        setattr(cls, "text/directory",
            PermissibleValue(text="text/directory"))
        setattr(cls, "text/dns",
            PermissibleValue(text="text/dns"))
        setattr(cls, "text/ecmascript",
            PermissibleValue(text="text/ecmascript"))
        setattr(cls, "text/encaprtp",
            PermissibleValue(text="text/encaprtp"))
        setattr(cls, "text/enriched",
            PermissibleValue(text="text/enriched"))
        setattr(cls, "text/example",
            PermissibleValue(text="text/example"))
        setattr(cls, "text/fhirpath",
            PermissibleValue(text="text/fhirpath"))
        setattr(cls, "text/flexfec",
            PermissibleValue(text="text/flexfec"))
        setattr(cls, "text/fwdred",
            PermissibleValue(text="text/fwdred"))
        setattr(cls, "text/gff3",
            PermissibleValue(text="text/gff3"))
        setattr(cls, "text/grammar-ref-list",
            PermissibleValue(text="text/grammar-ref-list"))
        setattr(cls, "text/hl7v2",
            PermissibleValue(text="text/hl7v2"))
        setattr(cls, "text/html",
            PermissibleValue(text="text/html"))
        setattr(cls, "text/javascript",
            PermissibleValue(text="text/javascript"))
        setattr(cls, "text/jcr-cnd",
            PermissibleValue(text="text/jcr-cnd"))
        setattr(cls, "text/markdown",
            PermissibleValue(text="text/markdown"))
        setattr(cls, "text/mizar",
            PermissibleValue(text="text/mizar"))
        setattr(cls, "text/n3",
            PermissibleValue(text="text/n3"))
        setattr(cls, "text/parameters",
            PermissibleValue(text="text/parameters"))
        setattr(cls, "text/parityfec",
            PermissibleValue(text="text/parityfec"))
        setattr(cls, "text/plain",
            PermissibleValue(text="text/plain"))
        setattr(cls, "text/provenance-notation",
            PermissibleValue(text="text/provenance-notation"))
        setattr(cls, "text/prs.fallenstein.rst",
            PermissibleValue(text="text/prs.fallenstein.rst"))
        setattr(cls, "text/prs.lines.tag",
            PermissibleValue(text="text/prs.lines.tag"))
        setattr(cls, "text/prs.prop.logic",
            PermissibleValue(text="text/prs.prop.logic"))
        setattr(cls, "text/prs.texi",
            PermissibleValue(text="text/prs.texi"))
        setattr(cls, "text/raptorfec",
            PermissibleValue(text="text/raptorfec"))
        setattr(cls, "text/RED",
            PermissibleValue(text="text/RED"))
        setattr(cls, "text/rfc822-headers",
            PermissibleValue(text="text/rfc822-headers"))
        setattr(cls, "text/richtext",
            PermissibleValue(text="text/richtext"))
        setattr(cls, "text/rtf",
            PermissibleValue(text="text/rtf"))
        setattr(cls, "text/rtp-enc-aescm128",
            PermissibleValue(text="text/rtp-enc-aescm128"))
        setattr(cls, "text/rtploopback",
            PermissibleValue(text="text/rtploopback"))
        setattr(cls, "text/rtx",
            PermissibleValue(text="text/rtx"))
        setattr(cls, "text/SGML",
            PermissibleValue(text="text/SGML"))
        setattr(cls, "text/shaclc",
            PermissibleValue(text="text/shaclc"))
        setattr(cls, "text/shex",
            PermissibleValue(text="text/shex"))
        setattr(cls, "text/spdx",
            PermissibleValue(text="text/spdx"))
        setattr(cls, "text/strings",
            PermissibleValue(text="text/strings"))
        setattr(cls, "text/t140",
            PermissibleValue(text="text/t140"))
        setattr(cls, "text/tab-separated-values",
            PermissibleValue(text="text/tab-separated-values"))
        setattr(cls, "text/troff",
            PermissibleValue(text="text/troff"))
        setattr(cls, "text/turtle",
            PermissibleValue(text="text/turtle"))
        setattr(cls, "text/ulpfec",
            PermissibleValue(text="text/ulpfec"))
        setattr(cls, "text/uri-list",
            PermissibleValue(text="text/uri-list"))
        setattr(cls, "text/vcard",
            PermissibleValue(text="text/vcard"))
        setattr(cls, "text/vnd.a",
            PermissibleValue(text="text/vnd.a"))
        setattr(cls, "text/vnd.abc",
            PermissibleValue(text="text/vnd.abc"))
        setattr(cls, "text/vnd.ascii-art",
            PermissibleValue(text="text/vnd.ascii-art"))
        setattr(cls, "text/vnd.curl",
            PermissibleValue(text="text/vnd.curl"))
        setattr(cls, "text/vnd.debian.copyright",
            PermissibleValue(text="text/vnd.debian.copyright"))
        setattr(cls, "text/vnd.DMClientScript",
            PermissibleValue(text="text/vnd.DMClientScript"))
        setattr(cls, "text/vnd.dvb.subtitle",
            PermissibleValue(text="text/vnd.dvb.subtitle"))
        setattr(cls, "text/vnd.esmertec.theme-descriptor",
            PermissibleValue(text="text/vnd.esmertec.theme-descriptor"))
        setattr(cls, "text/vnd.exchangeable",
            PermissibleValue(text="text/vnd.exchangeable"))
        setattr(cls, "text/vnd.familysearch.gedcom",
            PermissibleValue(text="text/vnd.familysearch.gedcom"))
        setattr(cls, "text/vnd.ficlab.flt",
            PermissibleValue(text="text/vnd.ficlab.flt"))
        setattr(cls, "text/vnd.fly",
            PermissibleValue(text="text/vnd.fly"))
        setattr(cls, "text/vnd.fmi.flexstor",
            PermissibleValue(text="text/vnd.fmi.flexstor"))
        setattr(cls, "text/vnd.gml",
            PermissibleValue(text="text/vnd.gml"))
        setattr(cls, "text/vnd.graphviz",
            PermissibleValue(text="text/vnd.graphviz"))
        setattr(cls, "text/vnd.hans",
            PermissibleValue(text="text/vnd.hans"))
        setattr(cls, "text/vnd.hgl",
            PermissibleValue(text="text/vnd.hgl"))
        setattr(cls, "text/vnd.in3d.3dml",
            PermissibleValue(text="text/vnd.in3d.3dml"))
        setattr(cls, "text/vnd.in3d.spot",
            PermissibleValue(text="text/vnd.in3d.spot"))
        setattr(cls, "text/vnd.IPTC.NewsML",
            PermissibleValue(text="text/vnd.IPTC.NewsML"))
        setattr(cls, "text/vnd.IPTC.NITF",
            PermissibleValue(text="text/vnd.IPTC.NITF"))
        setattr(cls, "text/vnd.latex-z",
            PermissibleValue(text="text/vnd.latex-z"))
        setattr(cls, "text/vnd.motorola.reflex",
            PermissibleValue(text="text/vnd.motorola.reflex"))
        setattr(cls, "text/vnd.ms-mediapackage",
            PermissibleValue(text="text/vnd.ms-mediapackage"))
        setattr(cls, "text/vnd.net2phone.commcenter.command",
            PermissibleValue(text="text/vnd.net2phone.commcenter.command"))
        setattr(cls, "text/vnd.radisys.msml-basic-layout",
            PermissibleValue(text="text/vnd.radisys.msml-basic-layout"))
        setattr(cls, "text/vnd.senx.warpscript",
            PermissibleValue(text="text/vnd.senx.warpscript"))
        setattr(cls, "text/vnd.si.uricatalogue",
            PermissibleValue(text="text/vnd.si.uricatalogue"))
        setattr(cls, "text/vnd.sosi",
            PermissibleValue(text="text/vnd.sosi"))
        setattr(cls, "text/vnd.sun.j2me.app-descriptor",
            PermissibleValue(text="text/vnd.sun.j2me.app-descriptor"))
        setattr(cls, "text/vnd.trolltech.linguist",
            PermissibleValue(text="text/vnd.trolltech.linguist"))
        setattr(cls, "text/vnd.vcf",
            PermissibleValue(text="text/vnd.vcf"))
        setattr(cls, "text/vnd.wap.si",
            PermissibleValue(text="text/vnd.wap.si"))
        setattr(cls, "text/vnd.wap.sl",
            PermissibleValue(text="text/vnd.wap.sl"))
        setattr(cls, "text/vnd.wap.wml",
            PermissibleValue(text="text/vnd.wap.wml"))
        setattr(cls, "text/vnd.wap.wmlscript",
            PermissibleValue(text="text/vnd.wap.wmlscript"))
        setattr(cls, "text/vnd.zoo.kcl",
            PermissibleValue(text="text/vnd.zoo.kcl"))
        setattr(cls, "text/vtt",
            PermissibleValue(text="text/vtt"))
        setattr(cls, "text/wgsl",
            PermissibleValue(text="text/wgsl"))
        setattr(cls, "text/xml",
            PermissibleValue(text="text/xml"))
        setattr(cls, "text/xml-external-parsed-entity",
            PermissibleValue(text="text/xml-external-parsed-entity"))
        setattr(cls, "video/1d-interleaved-parityfec",
            PermissibleValue(text="video/1d-interleaved-parityfec"))
        setattr(cls, "video/3gpp",
            PermissibleValue(text="video/3gpp"))
        setattr(cls, "video/3gpp2",
            PermissibleValue(text="video/3gpp2"))
        setattr(cls, "video/3gpp-tt",
            PermissibleValue(text="video/3gpp-tt"))
        setattr(cls, "video/AV1",
            PermissibleValue(text="video/AV1"))
        setattr(cls, "video/BMPEG",
            PermissibleValue(text="video/BMPEG"))
        setattr(cls, "video/BT656",
            PermissibleValue(text="video/BT656"))
        setattr(cls, "video/CelB",
            PermissibleValue(text="video/CelB"))
        setattr(cls, "video/DV",
            PermissibleValue(text="video/DV"))
        setattr(cls, "video/encaprtp",
            PermissibleValue(text="video/encaprtp"))
        setattr(cls, "video/evc",
            PermissibleValue(text="video/evc"))
        setattr(cls, "video/example",
            PermissibleValue(text="video/example"))
        setattr(cls, "video/FFV1",
            PermissibleValue(text="video/FFV1"))
        setattr(cls, "video/flexfec",
            PermissibleValue(text="video/flexfec"))
        setattr(cls, "video/H261",
            PermissibleValue(text="video/H261"))
        setattr(cls, "video/H263",
            PermissibleValue(text="video/H263"))
        setattr(cls, "video/H263-1998",
            PermissibleValue(text="video/H263-1998"))
        setattr(cls, "video/H263-2000",
            PermissibleValue(text="video/H263-2000"))
        setattr(cls, "video/H264",
            PermissibleValue(text="video/H264"))
        setattr(cls, "video/H264-RCDO",
            PermissibleValue(text="video/H264-RCDO"))
        setattr(cls, "video/H264-SVC",
            PermissibleValue(text="video/H264-SVC"))
        setattr(cls, "video/H265",
            PermissibleValue(text="video/H265"))
        setattr(cls, "video/H266",
            PermissibleValue(text="video/H266"))
        setattr(cls, "video/iso.segment",
            PermissibleValue(text="video/iso.segment"))
        setattr(cls, "video/JPEG",
            PermissibleValue(text="video/JPEG"))
        setattr(cls, "video/jpeg2000",
            PermissibleValue(text="video/jpeg2000"))
        setattr(cls, "video/jxsv",
            PermissibleValue(text="video/jxsv"))
        setattr(cls, "video/matroska",
            PermissibleValue(text="video/matroska"))
        setattr(cls, "video/matroska-3d",
            PermissibleValue(text="video/matroska-3d"))
        setattr(cls, "video/mj2",
            PermissibleValue(text="video/mj2"))
        setattr(cls, "video/MP1S",
            PermissibleValue(text="video/MP1S"))
        setattr(cls, "video/MP2P",
            PermissibleValue(text="video/MP2P"))
        setattr(cls, "video/MP2T",
            PermissibleValue(text="video/MP2T"))
        setattr(cls, "video/mp4",
            PermissibleValue(text="video/mp4"))
        setattr(cls, "video/MP4V-ES",
            PermissibleValue(text="video/MP4V-ES"))
        setattr(cls, "video/mpeg",
            PermissibleValue(text="video/mpeg"))
        setattr(cls, "video/mpeg4-generic",
            PermissibleValue(text="video/mpeg4-generic"))
        setattr(cls, "video/MPV",
            PermissibleValue(text="video/MPV"))
        setattr(cls, "video/nv",
            PermissibleValue(text="video/nv"))
        setattr(cls, "video/ogg",
            PermissibleValue(text="video/ogg"))
        setattr(cls, "video/parityfec",
            PermissibleValue(text="video/parityfec"))
        setattr(cls, "video/pointer",
            PermissibleValue(text="video/pointer"))
        setattr(cls, "video/quicktime",
            PermissibleValue(text="video/quicktime"))
        setattr(cls, "video/raptorfec",
            PermissibleValue(text="video/raptorfec"))
        setattr(cls, "video/raw",
            PermissibleValue(text="video/raw"))
        setattr(cls, "video/rtp-enc-aescm128",
            PermissibleValue(text="video/rtp-enc-aescm128"))
        setattr(cls, "video/rtploopback",
            PermissibleValue(text="video/rtploopback"))
        setattr(cls, "video/rtx",
            PermissibleValue(text="video/rtx"))
        setattr(cls, "video/scip",
            PermissibleValue(text="video/scip"))
        setattr(cls, "video/smpte291",
            PermissibleValue(text="video/smpte291"))
        setattr(cls, "video/SMPTE292M",
            PermissibleValue(text="video/SMPTE292M"))
        setattr(cls, "video/ulpfec",
            PermissibleValue(text="video/ulpfec"))
        setattr(cls, "video/vc1",
            PermissibleValue(text="video/vc1"))
        setattr(cls, "video/vc2",
            PermissibleValue(text="video/vc2"))
        setattr(cls, "video/vnd.CCTV",
            PermissibleValue(text="video/vnd.CCTV"))
        setattr(cls, "video/vnd.dece.hd",
            PermissibleValue(text="video/vnd.dece.hd"))
        setattr(cls, "video/vnd.dece.mobile",
            PermissibleValue(text="video/vnd.dece.mobile"))
        setattr(cls, "video/vnd.dece.mp4",
            PermissibleValue(text="video/vnd.dece.mp4"))
        setattr(cls, "video/vnd.dece.pd",
            PermissibleValue(text="video/vnd.dece.pd"))
        setattr(cls, "video/vnd.dece.sd",
            PermissibleValue(text="video/vnd.dece.sd"))
        setattr(cls, "video/vnd.dece.video",
            PermissibleValue(text="video/vnd.dece.video"))
        setattr(cls, "video/vnd.directv.mpeg",
            PermissibleValue(text="video/vnd.directv.mpeg"))
        setattr(cls, "video/vnd.directv.mpeg-tts",
            PermissibleValue(text="video/vnd.directv.mpeg-tts"))
        setattr(cls, "video/vnd.dlna.mpeg-tts",
            PermissibleValue(text="video/vnd.dlna.mpeg-tts"))
        setattr(cls, "video/vnd.dvb.file",
            PermissibleValue(text="video/vnd.dvb.file"))
        setattr(cls, "video/vnd.fvt",
            PermissibleValue(text="video/vnd.fvt"))
        setattr(cls, "video/vnd.hns.video",
            PermissibleValue(text="video/vnd.hns.video"))
        setattr(cls, "video/vnd.iptvforum.1dparityfec-1010",
            PermissibleValue(text="video/vnd.iptvforum.1dparityfec-1010"))
        setattr(cls, "video/vnd.iptvforum.1dparityfec-2005",
            PermissibleValue(text="video/vnd.iptvforum.1dparityfec-2005"))
        setattr(cls, "video/vnd.iptvforum.2dparityfec-1010",
            PermissibleValue(text="video/vnd.iptvforum.2dparityfec-1010"))
        setattr(cls, "video/vnd.iptvforum.2dparityfec-2005",
            PermissibleValue(text="video/vnd.iptvforum.2dparityfec-2005"))
        setattr(cls, "video/vnd.iptvforum.ttsavc",
            PermissibleValue(text="video/vnd.iptvforum.ttsavc"))
        setattr(cls, "video/vnd.iptvforum.ttsmpeg2",
            PermissibleValue(text="video/vnd.iptvforum.ttsmpeg2"))
        setattr(cls, "video/vnd.motorola.video",
            PermissibleValue(text="video/vnd.motorola.video"))
        setattr(cls, "video/vnd.motorola.videop",
            PermissibleValue(text="video/vnd.motorola.videop"))
        setattr(cls, "video/vnd.mpegurl",
            PermissibleValue(text="video/vnd.mpegurl"))
        setattr(cls, "video/vnd.ms-playready.media.pyv",
            PermissibleValue(text="video/vnd.ms-playready.media.pyv"))
        setattr(cls, "video/vnd.nokia.interleaved-multimedia",
            PermissibleValue(text="video/vnd.nokia.interleaved-multimedia"))
        setattr(cls, "video/vnd.nokia.mp4vr",
            PermissibleValue(text="video/vnd.nokia.mp4vr"))
        setattr(cls, "video/vnd.nokia.videovoip",
            PermissibleValue(text="video/vnd.nokia.videovoip"))
        setattr(cls, "video/vnd.objectvideo",
            PermissibleValue(text="video/vnd.objectvideo"))
        setattr(cls, "video/vnd.radgamettools.bink",
            PermissibleValue(text="video/vnd.radgamettools.bink"))
        setattr(cls, "video/vnd.radgamettools.smacker",
            PermissibleValue(text="video/vnd.radgamettools.smacker"))
        setattr(cls, "video/vnd.sealed.mpeg1",
            PermissibleValue(text="video/vnd.sealed.mpeg1"))
        setattr(cls, "video/vnd.sealed.mpeg4",
            PermissibleValue(text="video/vnd.sealed.mpeg4"))
        setattr(cls, "video/vnd.sealed.swf",
            PermissibleValue(text="video/vnd.sealed.swf"))
        setattr(cls, "video/vnd.sealedmedia.softseal.mov",
            PermissibleValue(text="video/vnd.sealedmedia.softseal.mov"))
        setattr(cls, "video/vnd.uvvu.mp4",
            PermissibleValue(text="video/vnd.uvvu.mp4"))
        setattr(cls, "video/vnd.vivo",
            PermissibleValue(text="video/vnd.vivo"))
        setattr(cls, "video/vnd.youtube.yt",
            PermissibleValue(text="video/vnd.youtube.yt"))
        setattr(cls, "video/VP8",
            PermissibleValue(text="video/VP8"))
        setattr(cls, "video/VP9",
            PermissibleValue(text="video/VP9"))

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
                   model_uri=PID4CAT_MODEL.media_type, domain=None, range=Optional[Union[str, "MEDIATypes"]])

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