# Auto generated from pid4cat_model.yaml by pythongen.py version: 0.0.1
# Generation date: 2023-12-07T18:08:57
# Schema: pid4cat-model
#
# id: https://w3id.org/nfdi4cat/pid4cat-model
# description: LinkML model for PIDs for resources in catalysis(PID4Cat). PID4Cat is handle system based persistent identifier (PID) for digital or physical resources used in the catalysis research process. The handle record is used to store metadata about the PID besides the obligatory redirect URL.
#   The model define here describes metadata for the PID itself and how to access the identified resource. It does not describe the resource itself with the exception of the resource category, which is a high-level description of  what is identified by the PID4Cat, e.g. sample or device.
# license: MIT

import dataclasses
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
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
DCT = CurieNamespace('dct', 'http://purl.org/dc/terms/')
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
    resource_info: Optional[Union[Union[dict, "ResourceInfo"], List[Union[dict, "ResourceInfo"]]]] = empty_list()
    related_identifiers: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()
    dc_rights: Optional[str] = None
    curation_contact: Optional[str] = None

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

        if not isinstance(self.resource_info, list):
            self.resource_info = [self.resource_info] if self.resource_info is not None else []
        self.resource_info = [v if isinstance(v, ResourceInfo) else ResourceInfo(**as_dict(v)) for v in self.resource_info]

        if not isinstance(self.related_identifiers, list):
            self.related_identifiers = [self.related_identifiers] if self.related_identifiers is not None else []
        self.related_identifiers = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.related_identifiers]

        if self.dc_rights is not None and not isinstance(self.dc_rights, str):
            self.dc_rights = str(self.dc_rights)

        if self.curation_contact is not None and not isinstance(self.curation_contact, str):
            self.curation_contact = str(self.curation_contact)

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

    relation_type: Optional[Union[Union[str, "RelationTypes"], List[Union[str, "RelationTypes"]]]] = empty_list()
    related_identifier: Optional[str] = None
    datetime_log: Optional[str] = None
    agent: Optional[Union[dict, "Agent"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.relation_type, list):
            self.relation_type = [self.relation_type] if self.relation_type is not None else []
        self.relation_type = [v if isinstance(v, RelationTypes) else RelationTypes(v) for v in self.relation_type]

        if self.related_identifier is not None and not isinstance(self.related_identifier, str):
            self.related_identifier = str(self.related_identifier)

        if self.datetime_log is not None and not isinstance(self.datetime_log, str):
            self.datetime_log = str(self.datetime_log)

        if self.agent is not None and not isinstance(self.agent, Agent):
            self.agent = Agent(**as_dict(self.agent))

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
    resource_category: Optional[Union[str, "ResourceCategories"]] = None
    rdf_url: Optional[str] = None
    rdf_type: Optional[str] = None
    schema_url: Optional[str] = None
    schema_type: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.resource_category is not None and not isinstance(self.resource_category, ResourceCategories):
            self.resource_category = ResourceCategories(self.resource_category)

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
    agent: Optional[Union[dict, "Agent"]] = None
    changed_field: Optional[Union[str, "ChangeLogFields"]] = None
    description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.datetime_log is not None and not isinstance(self.datetime_log, str):
            self.datetime_log = str(self.datetime_log)

        if self.agent is not None and not isinstance(self.agent, Agent):
            self.agent = Agent(**as_dict(self.agent))

        if self.changed_field is not None and not isinstance(self.changed_field, ChangeLogFields):
            self.changed_field = ChangeLogFields(self.changed_field)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass
class Agent(YAMLRoot):
    """
    Person who plays a role relative to sample collection or curation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PID4CAT_MODEL["Agent"]
    class_class_curie: ClassVar[str] = "pid4cat_model:Agent"
    class_name: ClassVar[str] = "Agent"
    class_model_uri: ClassVar[URIRef] = PID4CAT_MODEL.Agent

    name: Optional[str] = None
    contact_information: Optional[str] = None
    person_orcid: Optional[str] = None
    affiliation_ror: Optional[str] = None
    role: Optional[Union[str, "PID4CatAgentRoles"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.contact_information is not None and not isinstance(self.contact_information, str):
            self.contact_information = str(self.contact_information)

        if self.person_orcid is not None and not isinstance(self.person_orcid, str):
            self.person_orcid = str(self.person_orcid)

        if self.affiliation_ror is not None and not isinstance(self.affiliation_ror, str):
            self.affiliation_ror = str(self.affiliation_ror)

        if self.role is not None and not isinstance(self.role, PID4CatAgentRoles):
            self.role = PID4CatAgentRoles(self.role)

        super().__post_init__(**kwargs)


# Enumerations
class ResourceCategories(EnumDefinitionImpl):
    """
    The category of the resource
    """
    COLLECTION = PermissibleValue(
        text="COLLECTION",
        description="A collection is described as a group; its parts may also be separately described.",
        meaning=None)
    CATALYST = PermissibleValue(
        text="CATALYST",
        description="A physical entity meant to be applied as catalyst.")
    MATERIAL = PermissibleValue(
        text="MATERIAL",
        description="A material used in the catalysis research process (except the catalyst itself).")
    DEVICE = PermissibleValue(
        text="DEVICE",
        description="A device used in the catalysis research process.")
    DATAOBJECT = PermissibleValue(
        text="DATAOBJECT",
        description="A data object might be a data file, a data set, a data collection, or a data service.")

    _defn = EnumDefinition(
        name="ResourceCategories",
        description="The category of the resource",
    )

class RelationTypes(EnumDefinitionImpl):
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
        description="The resource has metadata.")
    IS_METADATA_FOR = PermissibleValue(
        text="IS_METADATA_FOR",
        description="The resource is metadata for.")
    HAS_VERSION = PermissibleValue(
        text="HAS_VERSION",
        description="The resource has a version.",
        meaning=DCT["hasVersion"])
    IS_VERSION_OF = PermissibleValue(
        text="IS_VERSION_OF",
        description="The resource is a version of.",
        meaning=DCT["isVersionOf"])
    IS_NEW_VERSION_OF = PermissibleValue(
        text="IS_NEW_VERSION_OF",
        description="The resource is a new version of.")
    IS_PREVIOUS_VERSION_OF = PermissibleValue(
        text="IS_PREVIOUS_VERSION_OF",
        description="The resource is a previous version of.")
    IS_PART_OF = PermissibleValue(
        text="IS_PART_OF",
        description="The resource is part of another resource.",
        meaning=DCT["isPartOf"])
    HAS_PART = PermissibleValue(
        text="HAS_PART",
        description="The resource has part another resource.",
        meaning=DCT["hasPart"])
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
        meaning=DCT["isReferencedBy"])
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
    IS_REQUIRED_BY = PermissibleValue(
        text="IS_REQUIRED_BY",
        description="The resource is required by another resource.",
        meaning=DCT["isRequiredBy"])
    REQUIRES = PermissibleValue(
        text="REQUIRES",
        description="The resource requires another resource.",
        meaning=DCT["requires"])
    IS_OBSOLETED_BY = PermissibleValue(
        text="IS_OBSOLETED_BY",
        description="The resource or PID4Cat is obsoleted by another resource or PID4Cat.")
    OBSOLETES = PermissibleValue(
        text="OBSOLETES",
        description="The resource or PID4Cat obsoletes another resource or PID4Cat.")

    _defn = EnumDefinition(
        name="RelationTypes",
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
        description="The PID4CatRecord links to a concrete ressource.")
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

class PID4CatAgentRoles(EnumDefinitionImpl):
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
        name="PID4CatAgentRoles",
        description="The role of an agent relative to the resource.",
    )

class ChangeLogFields(EnumDefinitionImpl):
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
    RIGHTS = PermissibleValue(
        text="RIGHTS",
        description="The rights of the PID4CatRecord were changed.")

    _defn = EnumDefinition(
        name="ChangeLogFields",
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

slots.resource_info = Slot(uri=PID4CAT_MODEL.resource_info, name="resource_info", curie=PID4CAT_MODEL.curie('resource_info'),
                   model_uri=PID4CAT_MODEL.resource_info, domain=None, range=Optional[Union[Union[dict, ResourceInfo], List[Union[dict, ResourceInfo]]]])

slots.related_identifiers = Slot(uri=SCHEMA.identifier, name="related_identifiers", curie=SCHEMA.curie('identifier'),
                   model_uri=PID4CAT_MODEL.related_identifiers, domain=None, range=Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]])

slots.dc_rights = Slot(uri=SCHEMA.license, name="dc_rights", curie=SCHEMA.curie('license'),
                   model_uri=PID4CAT_MODEL.dc_rights, domain=None, range=Optional[str])

slots.curation_contact = Slot(uri=SCHEMA.email, name="curation_contact", curie=SCHEMA.curie('email'),
                   model_uri=PID4CAT_MODEL.curation_contact, domain=None, range=Optional[str])

slots.change_log = Slot(uri=SCHEMA.identifier, name="change_log", curie=SCHEMA.curie('identifier'),
                   model_uri=PID4CAT_MODEL.change_log, domain=None, range=Union[Union[dict, LogRecord], List[Union[dict, LogRecord]]])

slots.relation_type = Slot(uri=SCHEMA.identifier, name="relation_type", curie=SCHEMA.curie('identifier'),
                   model_uri=PID4CAT_MODEL.relation_type, domain=None, range=Optional[Union[Union[str, "RelationTypes"], List[Union[str, "RelationTypes"]]]])

slots.related_identifier = Slot(uri=SCHEMA.identifier, name="related_identifier", curie=SCHEMA.curie('identifier'),
                   model_uri=PID4CAT_MODEL.related_identifier, domain=None, range=Optional[str])

slots.datetime_log = Slot(uri=SCHEMA.DateTime, name="datetime_log", curie=SCHEMA.curie('DateTime'),
                   model_uri=PID4CAT_MODEL.datetime_log, domain=None, range=Optional[str])

slots.agent = Slot(uri=SCHEMA.Agent, name="agent", curie=SCHEMA.curie('Agent'),
                   model_uri=PID4CAT_MODEL.agent, domain=None, range=Optional[Union[dict, Agent]])

slots.label = Slot(uri=SCHEMA.name, name="label", curie=SCHEMA.curie('name'),
                   model_uri=PID4CAT_MODEL.label, domain=None, range=Optional[str])

slots.description = Slot(uri=SCHEMA.description, name="description", curie=SCHEMA.curie('description'),
                   model_uri=PID4CAT_MODEL.description, domain=None, range=Optional[str])

slots.resource_category = Slot(uri=SCHEMA.additionalType, name="resource_category", curie=SCHEMA.curie('additionalType'),
                   model_uri=PID4CAT_MODEL.resource_category, domain=None, range=Optional[Union[str, "ResourceCategories"]])

slots.rdf_url = Slot(uri=SCHEMA.additionalType, name="rdf_url", curie=SCHEMA.curie('additionalType'),
                   model_uri=PID4CAT_MODEL.rdf_url, domain=None, range=Optional[str])

slots.rdf_type = Slot(uri=SCHEMA.additionalType, name="rdf_type", curie=SCHEMA.curie('additionalType'),
                   model_uri=PID4CAT_MODEL.rdf_type, domain=None, range=Optional[str])

slots.schema_url = Slot(uri=SCHEMA.additionalType, name="schema_url", curie=SCHEMA.curie('additionalType'),
                   model_uri=PID4CAT_MODEL.schema_url, domain=None, range=Optional[str])

slots.schema_type = Slot(uri=SCHEMA.additionalType, name="schema_type", curie=SCHEMA.curie('additionalType'),
                   model_uri=PID4CAT_MODEL.schema_type, domain=None, range=Optional[str])

slots.changed_field = Slot(uri=SCHEMA.identifier, name="changed_field", curie=SCHEMA.curie('identifier'),
                   model_uri=PID4CAT_MODEL.changed_field, domain=None, range=Optional[Union[str, "ChangeLogFields"]])

slots.name = Slot(uri=SCHEMA.name, name="name", curie=SCHEMA.curie('name'),
                   model_uri=PID4CAT_MODEL.name, domain=None, range=Optional[str])

slots.contact_information = Slot(uri=SCHEMA.email, name="contact_information", curie=SCHEMA.curie('email'),
                   model_uri=PID4CAT_MODEL.contact_information, domain=None, range=Optional[str])

slots.person_orcid = Slot(uri=SCHEMA.identifier, name="person_orcid", curie=SCHEMA.curie('identifier'),
                   model_uri=PID4CAT_MODEL.person_orcid, domain=None, range=Optional[str])

slots.affiliation_ror = Slot(uri=SCHEMA.identifier, name="affiliation_ror", curie=SCHEMA.curie('identifier'),
                   model_uri=PID4CAT_MODEL.affiliation_ror, domain=None, range=Optional[str])

slots.role = Slot(uri=SCHEMA.identifier, name="role", curie=SCHEMA.curie('identifier'),
                   model_uri=PID4CAT_MODEL.role, domain=None, range=Optional[Union[str, "PID4CatAgentRoles"]])

slots.PID4CatRecord_curation_contact = Slot(uri=SCHEMA.email, name="PID4CatRecord_curation_contact", curie=SCHEMA.curie('email'),
                   model_uri=PID4CAT_MODEL.PID4CatRecord_curation_contact, domain=PID4CatRecord, range=Optional[str],
                   pattern=re.compile(r'^\S+@[\S+\.]+\S+'))