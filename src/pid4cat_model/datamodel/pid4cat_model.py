# Auto generated from pid4cat_model.yaml by pythongen.py version: 0.0.1
# Generation date: 2024-12-05T00:27:05
# Schema: pid4cat-model
#
# id: https://w3id.org/nfdi4cat/pid4cat-model
# description: A LinkML model for PIDs for resources in catalysis (PID4Cat). PID4Cat is a handle system based persistent identifier (PID) for digital or physical resources used in the catalysis research process. The handle record is used to store additional metadata about the PID besides the obligatory landing page URL.
#   The model describes metadata for the PID itself and how to access the identified resource. It does not describe the resource itself with the exception of the resource category, which is a high-level description of what is identified by the PID4Cat handle, e.g. a sample or a device.
# license: MIT

import dataclasses
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from datetime import date, datetime
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import String, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
DCAT = CurieNamespace('DCAT', 'http://www.w3.org/ns/dcat#')
DATACITE = CurieNamespace('DataCite', 'http://purl.org/spar/datacite/')
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
PID4CAT_MODEL = CurieNamespace('pid4cat_model', 'https://w3id.org/nfdi4cat/pid4cat-model/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = PID4CAT_MODEL


# Types

# Class references
class PID4CatRecordId(URIorCURIE):
    pass


@dataclass
class PID4CatRecord(YAMLRoot):
    """
    Represents a PID4CatRecord
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PID4CAT_MODEL["PID4CatRecord"]
    class_class_curie: ClassVar[str] = "pid4cat_model:PID4CatRecord"
    class_name: ClassVar[str] = "PID4CatRecord"
    class_model_uri: ClassVar[URIRef] = PID4CAT_MODEL.PID4CatRecord

    id: Union[str, PID4CatRecordId] = None
    change_log: Union[Union[dict, "LogRecord"], List[Union[dict, "LogRecord"]]] = None
    landing_page_url: Optional[str] = None
    status: Optional[Union[str, "PID4CatStatus"]] = None
    pid_schema_version: Optional[str] = None
    license: Optional[str] = None
    curation_contact_email: Optional[str] = None
    resource_info: Optional[Union[dict, "ResourceInfo"]] = None
    related_identifiers: Optional[Union[Union[dict, "PID4CatRelation"], List[Union[dict, "PID4CatRelation"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PID4CatRecordId):
            self.id = PID4CatRecordId(self.id)

        if self._is_empty(self.change_log):
            self.MissingRequiredField("change_log")
        if not isinstance(self.change_log, list):
            self.change_log = [self.change_log] if self.change_log is not None else []
        self.change_log = [v if isinstance(v, LogRecord) else LogRecord(**as_dict(v)) for v in self.change_log]

        if self.landing_page_url is not None and not isinstance(self.landing_page_url, str):
            self.landing_page_url = str(self.landing_page_url)

        if self.status is not None and not isinstance(self.status, PID4CatStatus):
            self.status = PID4CatStatus(self.status)

        if self.pid_schema_version is not None and not isinstance(self.pid_schema_version, str):
            self.pid_schema_version = str(self.pid_schema_version)

        if self.license is not None and not isinstance(self.license, str):
            self.license = str(self.license)

        if self.curation_contact_email is not None and not isinstance(self.curation_contact_email, str):
            self.curation_contact_email = str(self.curation_contact_email)

        if self.resource_info is not None and not isinstance(self.resource_info, ResourceInfo):
            self.resource_info = ResourceInfo(**as_dict(self.resource_info))

        if not isinstance(self.related_identifiers, list):
            self.related_identifiers = [self.related_identifiers] if self.related_identifiers is not None else []
        self.related_identifiers = [v if isinstance(v, PID4CatRelation) else PID4CatRelation(**as_dict(v)) for v in self.related_identifiers]

        super().__post_init__(**kwargs)


@dataclass
class PID4CatRelation(YAMLRoot):
    """
    A relation between PID4CatRecords or between a PID4CatRecord and other resources with a PID.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PID4CAT_MODEL["PID4CatRelation"]
    class_class_curie: ClassVar[str] = "pid4cat_model:PID4CatRelation"
    class_name: ClassVar[str] = "PID4CatRelation"
    class_model_uri: ClassVar[URIRef] = PID4CAT_MODEL.PID4CatRelation

    relation_type: Optional[Union[Union[str, "RelationType"], List[Union[str, "RelationType"]]]] = empty_list()
    related_identifier: Optional[str] = None
    datetime_log: Optional[str] = None
    has_agent: Optional[Union[dict, "Agent"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.relation_type, list):
            self.relation_type = [self.relation_type] if self.relation_type is not None else []
        self.relation_type = [v if isinstance(v, RelationType) else RelationType(v) for v in self.relation_type]

        if self.related_identifier is not None and not isinstance(self.related_identifier, str):
            self.related_identifier = str(self.related_identifier)

        if self.datetime_log is not None and not isinstance(self.datetime_log, str):
            self.datetime_log = str(self.datetime_log)

        if self.has_agent is not None and not isinstance(self.has_agent, Agent):
            self.has_agent = Agent(**as_dict(self.has_agent))

        super().__post_init__(**kwargs)


@dataclass
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
    rdf_url: Optional[str] = None
    rdf_type: Optional[str] = None
    schema_url: Optional[str] = None
    schema_type: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.resource_category is not None and not isinstance(self.resource_category, ResourceCategory):
            self.resource_category = ResourceCategory(self.resource_category)

        if self.rdf_url is not None and not isinstance(self.rdf_url, str):
            self.rdf_url = str(self.rdf_url)

        if self.rdf_type is not None and not isinstance(self.rdf_type, str):
            self.rdf_type = str(self.rdf_type)

        if self.schema_url is not None and not isinstance(self.schema_url, str):
            self.schema_url = str(self.schema_url)

        if self.schema_type is not None and not isinstance(self.schema_type, str):
            self.schema_type = str(self.schema_type)

        super().__post_init__(**kwargs)


@dataclass
class LogRecord(YAMLRoot):
    """
    A log record for changes made on a PID4CatRecord starting from registration.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PID4CAT_MODEL["LogRecord"]
    class_class_curie: ClassVar[str] = "pid4cat_model:LogRecord"
    class_name: ClassVar[str] = "LogRecord"
    class_model_uri: ClassVar[URIRef] = PID4CAT_MODEL.LogRecord

    datetime_log: Optional[str] = None
    has_agent: Optional[Union[dict, "Agent"]] = None
    changed_field: Optional[Union[str, "ChangeLogField"]] = None
    description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.datetime_log is not None and not isinstance(self.datetime_log, str):
            self.datetime_log = str(self.datetime_log)

        if self.has_agent is not None and not isinstance(self.has_agent, Agent):
            self.has_agent = Agent(**as_dict(self.has_agent))

        if self.changed_field is not None and not isinstance(self.changed_field, ChangeLogField):
            self.changed_field = ChangeLogField(self.changed_field)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass
class Agent(YAMLRoot):
    """
    Person who plays a role relative to PID creation or curation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PID4CAT_MODEL["Agent"]
    class_class_curie: ClassVar[str] = "pid4cat_model:Agent"
    class_name: ClassVar[str] = "Agent"
    class_model_uri: ClassVar[URIRef] = PID4CAT_MODEL.Agent

    name: Optional[str] = None
    email: Optional[str] = None
    orcid: Optional[str] = None
    affiliation_ror: Optional[str] = None
    role: Optional[Union[str, "PID4CatAgentRole"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.email is not None and not isinstance(self.email, str):
            self.email = str(self.email)

        if self.orcid is not None and not isinstance(self.orcid, str):
            self.orcid = str(self.orcid)

        if self.affiliation_ror is not None and not isinstance(self.affiliation_ror, str):
            self.affiliation_ror = str(self.affiliation_ror)

        if self.role is not None and not isinstance(self.role, PID4CatAgentRole):
            self.role = PID4CatAgentRole(self.role)

        super().__post_init__(**kwargs)


@dataclass
class Container(YAMLRoot):
    """
    A container for all PID4Cat instances.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PID4CAT_MODEL["Container"]
    class_class_curie: ClassVar[str] = "pid4cat_model:Container"
    class_name: ClassVar[str] = "Container"
    class_model_uri: ClassVar[URIRef] = PID4CAT_MODEL.Container

    contains_pids: Optional[Union[Dict[Union[str, PID4CatRecordId], Union[dict, PID4CatRecord]], List[Union[dict, PID4CatRecord]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(slot_name="contains_pids", slot_type=PID4CatRecord, key_name="id", keyed=True)

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

# Slots
class slots:
    pass

slots.id = Slot(uri=SCHEMA.identifier, name="id", curie=SCHEMA.curie('identifier'),
                   model_uri=PID4CAT_MODEL.id, domain=None, range=URIRef)

slots.landing_page_url = Slot(uri=SCHEMA.url, name="landing_page_url", curie=SCHEMA.curie('url'),
                   model_uri=PID4CAT_MODEL.landing_page_url, domain=None, range=Optional[str])

slots.status = Slot(uri=PID4CAT_MODEL.status, name="status", curie=PID4CAT_MODEL.curie('status'),
                   model_uri=PID4CAT_MODEL.status, domain=None, range=Optional[Union[str, "PID4CatStatus"]])

slots.pid_schema_version = Slot(uri=SCHEMA.identifier, name="pid_schema_version", curie=SCHEMA.curie('identifier'),
                   model_uri=PID4CAT_MODEL.pid_schema_version, domain=None, range=Optional[str])

slots.resource_info = Slot(uri=PID4CAT_MODEL.resource_info, name="resource_info", curie=PID4CAT_MODEL.curie('resource_info'),
                   model_uri=PID4CAT_MODEL.resource_info, domain=None, range=Optional[Union[dict, ResourceInfo]])

slots.related_identifiers = Slot(uri=SCHEMA.identifier, name="related_identifiers", curie=SCHEMA.curie('identifier'),
                   model_uri=PID4CAT_MODEL.related_identifiers, domain=None, range=Optional[Union[Union[dict, PID4CatRelation], List[Union[dict, PID4CatRelation]]]])

slots.license = Slot(uri=SCHEMA.license, name="license", curie=SCHEMA.curie('license'),
                   model_uri=PID4CAT_MODEL.license, domain=None, range=Optional[str])

slots.curation_contact_email = Slot(uri=SCHEMA.email, name="curation_contact_email", curie=SCHEMA.curie('email'),
                   model_uri=PID4CAT_MODEL.curation_contact_email, domain=None, range=Optional[str])

slots.change_log = Slot(uri=SCHEMA.identifier, name="change_log", curie=SCHEMA.curie('identifier'),
                   model_uri=PID4CAT_MODEL.change_log, domain=None, range=Union[Union[dict, LogRecord], List[Union[dict, LogRecord]]])

slots.relation_type = Slot(uri=SCHEMA.identifier, name="relation_type", curie=SCHEMA.curie('identifier'),
                   model_uri=PID4CAT_MODEL.relation_type, domain=None, range=Optional[Union[Union[str, "RelationType"], List[Union[str, "RelationType"]]]])

slots.related_identifier = Slot(uri=SCHEMA.identifier, name="related_identifier", curie=SCHEMA.curie('identifier'),
                   model_uri=PID4CAT_MODEL.related_identifier, domain=None, range=Optional[str])

slots.datetime_log = Slot(uri=SCHEMA.DateTime, name="datetime_log", curie=SCHEMA.curie('DateTime'),
                   model_uri=PID4CAT_MODEL.datetime_log, domain=None, range=Optional[str])

slots.has_agent = Slot(uri=SCHEMA.Agent, name="has_agent", curie=SCHEMA.curie('Agent'),
                   model_uri=PID4CAT_MODEL.has_agent, domain=None, range=Optional[Union[dict, Agent]])

slots.label = Slot(uri=SCHEMA.name, name="label", curie=SCHEMA.curie('name'),
                   model_uri=PID4CAT_MODEL.label, domain=None, range=Optional[str])

slots.description = Slot(uri=SCHEMA.description, name="description", curie=SCHEMA.curie('description'),
                   model_uri=PID4CAT_MODEL.description, domain=None, range=Optional[str])

slots.resource_category = Slot(uri=SCHEMA.additionalType, name="resource_category", curie=SCHEMA.curie('additionalType'),
                   model_uri=PID4CAT_MODEL.resource_category, domain=None, range=Optional[Union[str, "ResourceCategory"]])

slots.rdf_url = Slot(uri=SCHEMA.additionalType, name="rdf_url", curie=SCHEMA.curie('additionalType'),
                   model_uri=PID4CAT_MODEL.rdf_url, domain=None, range=Optional[str])

slots.rdf_type = Slot(uri=SCHEMA.additionalType, name="rdf_type", curie=SCHEMA.curie('additionalType'),
                   model_uri=PID4CAT_MODEL.rdf_type, domain=None, range=Optional[str])

slots.schema_url = Slot(uri=SCHEMA.additionalType, name="schema_url", curie=SCHEMA.curie('additionalType'),
                   model_uri=PID4CAT_MODEL.schema_url, domain=None, range=Optional[str])

slots.schema_type = Slot(uri=SCHEMA.additionalType, name="schema_type", curie=SCHEMA.curie('additionalType'),
                   model_uri=PID4CAT_MODEL.schema_type, domain=None, range=Optional[str])

slots.changed_field = Slot(uri=SCHEMA.identifier, name="changed_field", curie=SCHEMA.curie('identifier'),
                   model_uri=PID4CAT_MODEL.changed_field, domain=None, range=Optional[Union[str, "ChangeLogField"]])

slots.name = Slot(uri=SCHEMA.name, name="name", curie=SCHEMA.curie('name'),
                   model_uri=PID4CAT_MODEL.name, domain=None, range=Optional[str])

slots.email = Slot(uri=SCHEMA.email, name="email", curie=SCHEMA.curie('email'),
                   model_uri=PID4CAT_MODEL.email, domain=None, range=Optional[str])

slots.orcid = Slot(uri=SCHEMA.identifier, name="orcid", curie=SCHEMA.curie('identifier'),
                   model_uri=PID4CAT_MODEL.orcid, domain=None, range=Optional[str])

slots.affiliation_ror = Slot(uri=SCHEMA.identifier, name="affiliation_ror", curie=SCHEMA.curie('identifier'),
                   model_uri=PID4CAT_MODEL.affiliation_ror, domain=None, range=Optional[str])

slots.role = Slot(uri=SCHEMA.identifier, name="role", curie=SCHEMA.curie('identifier'),
                   model_uri=PID4CAT_MODEL.role, domain=None, range=Optional[Union[str, "PID4CatAgentRole"]])

slots.container__contains_pids = Slot(uri=PID4CAT_MODEL.contains_pids, name="container__contains_pids", curie=PID4CAT_MODEL.curie('contains_pids'),
                   model_uri=PID4CAT_MODEL.container__contains_pids, domain=None, range=Optional[Union[Dict[Union[str, PID4CatRecordId], Union[dict, PID4CatRecord]], List[Union[dict, PID4CatRecord]]]])

slots.PID4CatRecord_curation_contact_email = Slot(uri=SCHEMA.email, name="PID4CatRecord_curation_contact_email", curie=SCHEMA.curie('email'),
                   model_uri=PID4CAT_MODEL.PID4CatRecord_curation_contact_email, domain=PID4CatRecord, range=Optional[str],
                   pattern=re.compile(r'^\S+@[\S+\.]+\S+'))

slots.Agent_email = Slot(uri=SCHEMA.email, name="Agent_email", curie=SCHEMA.curie('email'),
                   model_uri=PID4CAT_MODEL.Agent_email, domain=Agent, range=Optional[str],
                   pattern=re.compile(r'^\S+@[\S+\.]+\S+'))