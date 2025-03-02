# Auto generated from pid4cat_model.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-03-02T19:38:51
# Schema: pid4cat-model
#
# id: https://w3id.org/nfdi4cat/pid4cat-model
# description: A LinkML model for PIDs for resources in catalysis (pid4cat). pid4cat is a handle system based persistent identifier (PID) for digital or physical resources used in the catalysis research process. The handle record is used to store additional metadata about the PID besides the obligatory landing page URL.
#   The model describes metadata for the PID itself and how to access the identified resource. It does not describe the resource itself with the exception of the resource category, which is a high-level description of what is identified by the pid4cat handle, e.g. a sample or a device.
# license: MIT

import dataclasses
import re
from dataclasses import dataclass
from typing import Any, ClassVar, Dict, List, Optional, Union

from jsonasobj2 import as_dict
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.dataclass_extensions_376 import (
    dataclasses_init_fn_with_kwargs,
)
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.metamodelcore import empty_dict, empty_list
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str
from rdflib import URIRef

from linkml_runtime.utils.metamodelcore import URI, XSDDateTime

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
DATACITE = CurieNamespace("DataCite", "https://purl.org/spar/datacite/")
DCAT = CurieNamespace("dcat", "https://www.w3.org/ns/dcat#")
DCTERMS = CurieNamespace("dcterms", "https://purl.org/dc/terms/")
LINKML = CurieNamespace("linkml", "https://w3id.org/linkml/")
PID4CAT_MODEL = CurieNamespace(
    "pid4cat_model", "https://w3id.org/nfdi4cat/pid4cat-model/"
)
PROV = CurieNamespace("prov", "https://www.w3.org/ns/prov#")
VOC4CAT = CurieNamespace("voc4cat", "https://w3id.org/nfdi4cat/voc4cat_")
DEFAULT_ = PID4CAT_MODEL


# Types


# Class references
class HandleAPIRecordHandle(extended_str):
    pass


@dataclass(repr=False)
class HandleAPIRecord(YAMLRoot):
    """
    A class representing a handle record query response of the REST (json) API of a handle server.
    """

    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PID4CAT_MODEL["HandleAPIRecord"]
    class_class_curie: ClassVar[str] = "pid4cat_model:HandleAPIRecord"
    class_name: ClassVar[str] = "HandleAPIRecord"
    class_model_uri: ClassVar[URIRef] = PID4CAT_MODEL.HandleAPIRecord

    handle: Union[str, HandleAPIRecordHandle] = None
    responseCode: Optional[int] = None
    values: Optional[
        Union[Union[dict, "HandleRecord"], List[Union[dict, "HandleRecord"]]]
    ] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.handle):
            self.MissingRequiredField("handle")
        if not isinstance(self.handle, HandleAPIRecordHandle):
            self.handle = HandleAPIRecordHandle(self.handle)

        if self.responseCode is not None and not isinstance(self.responseCode, int):
            self.responseCode = int(self.responseCode)

        if not isinstance(self.values, list):
            self.values = [self.values] if self.values is not None else []
        self.values = [
            v if isinstance(v, HandleRecord) else HandleRecord(**as_dict(v))
            for v in self.values
        ]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HandleRecord(YAMLRoot):
    """
    A class representing a handle record in the same way as in the REST (json) API of a handle server.
    """

    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PID4CAT_MODEL["HandleRecord"]
    class_class_curie: ClassVar[str] = "pid4cat_model:HandleRecord"
    class_name: ClassVar[str] = "HandleRecord"
    class_model_uri: ClassVar[URIRef] = PID4CAT_MODEL.HandleRecord

    ttl: Optional[int] = None
    timestamp: Optional[Union[str, XSDDateTime]] = None
    type: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.ttl is not None and not isinstance(self.ttl, int):
            self.ttl = int(self.ttl)

        if self.timestamp is not None and not isinstance(self.timestamp, XSDDateTime):
            self.timestamp = XSDDateTime(self.timestamp)

        self.type = str(self.class_name)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)

    def __new__(cls, *args, **kwargs):
        type_designator = "type"
        if type_designator not in kwargs:
            return super().__new__(cls, *args, **kwargs)
        else:
            type_designator_value = kwargs[type_designator]
            target_cls = cls._class_for("class_name", type_designator_value)

            if target_cls is None:
                raise ValueError(
                    f"Wrong type designator value: class {cls.__name__} "
                    f"has no subclass with ['class_name']='{kwargs[type_designator]}'"
                )
            return super().__new__(target_cls, *args, **kwargs)


@dataclass(repr=False)
class URL(HandleRecord):
    """
    The data element in the handle API for the landing page URL.
    """

    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PID4CAT_MODEL["URL"]
    class_class_curie: ClassVar[str] = "pid4cat_model:URL"
    class_name: ClassVar[str] = "URL"
    class_model_uri: ClassVar[URIRef] = PID4CAT_MODEL.URL

    index: Optional[int] = None
    data: Optional[Union[dict, "HdlDataUrl"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.index is not None and not isinstance(self.index, int):
            self.index = int(self.index)

        if self.data is not None and not isinstance(self.data, HdlDataUrl):
            self.data = HdlDataUrl(**as_dict(self.data))

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class HdlDataUrl(YAMLRoot):
    """
    The data element in the handle API for the redirect url.
    """

    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PID4CAT_MODEL["HdlDataUrl"]
    class_class_curie: ClassVar[str] = "pid4cat_model:HdlDataUrl"
    class_name: ClassVar[str] = "HdlDataUrl"
    class_model_uri: ClassVar[URIRef] = PID4CAT_MODEL.HdlDataUrl

    format: Optional[str] = None
    value: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.format is not None and not isinstance(self.format, str):
            self.format = str(self.format)

        if self.value is not None and not isinstance(self.value, str):
            self.value = str(self.value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class STATUS(HandleRecord):
    """
    A data element in the handle API.
    """

    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PID4CAT_MODEL["STATUS"]
    class_class_curie: ClassVar[str] = "pid4cat_model:STATUS"
    class_name: ClassVar[str] = "STATUS"
    class_model_uri: ClassVar[URIRef] = PID4CAT_MODEL.STATUS

    index: Optional[int] = None
    data: Optional[Union[dict, "HdlDataStatus"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.index is not None and not isinstance(self.index, int):
            self.index = int(self.index)

        if self.data is not None and not isinstance(self.data, HdlDataStatus):
            self.data = HdlDataStatus(**as_dict(self.data))

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class HdlDataStatus(YAMLRoot):
    """
    The data element in the handle API for the status.
    """

    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PID4CAT_MODEL["HdlDataStatus"]
    class_class_curie: ClassVar[str] = "pid4cat_model:HdlDataStatus"
    class_name: ClassVar[str] = "HdlDataStatus"
    class_model_uri: ClassVar[URIRef] = PID4CAT_MODEL.HdlDataStatus

    format: Optional[str] = None
    value: Optional[Union[str, "Pid4CatStatus"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.format is not None and not isinstance(self.format, str):
            self.format = str(self.format)

        if self.value is not None and not isinstance(self.value, Pid4CatStatus):
            self.value = Pid4CatStatus(self.value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SCHEMAVER(HandleRecord):
    """
    The data element in the handle API for the schema version.
    """

    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PID4CAT_MODEL["SCHEMAVER"]
    class_class_curie: ClassVar[str] = "pid4cat_model:SCHEMAVER"
    class_name: ClassVar[str] = "SCHEMA_VER"
    class_model_uri: ClassVar[URIRef] = PID4CAT_MODEL.SCHEMAVER

    index: Optional[int] = None
    data: Optional[Union[dict, "HdlDataSchemaVer"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.index is not None and not isinstance(self.index, int):
            self.index = int(self.index)

        if self.data is not None and not isinstance(self.data, HdlDataSchemaVer):
            self.data = HdlDataSchemaVer(**as_dict(self.data))

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class HdlDataSchemaVer(YAMLRoot):
    """
    The data element in the handle API for the schema version.
    """

    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PID4CAT_MODEL["HdlDataSchemaVer"]
    class_class_curie: ClassVar[str] = "pid4cat_model:HdlDataSchemaVer"
    class_name: ClassVar[str] = "HdlDataSchemaVer"
    class_model_uri: ClassVar[URIRef] = PID4CAT_MODEL.HdlDataSchemaVer

    format: Optional[str] = None
    value: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.format is not None and not isinstance(self.format, str):
            self.format = str(self.format)

        if self.value is not None and not isinstance(self.value, str):
            self.value = str(self.value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LICENSE(HandleRecord):
    """
    The data element in the handle API for the schema version.
    """

    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PID4CAT_MODEL["LICENSE"]
    class_class_curie: ClassVar[str] = "pid4cat_model:LICENSE"
    class_name: ClassVar[str] = "LICENSE"
    class_model_uri: ClassVar[URIRef] = PID4CAT_MODEL.LICENSE

    index: Optional[int] = None
    data: Optional[Union[dict, "HdlDataLicense"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.index is not None and not isinstance(self.index, int):
            self.index = int(self.index)

        if self.data is not None and not isinstance(self.data, HdlDataLicense):
            self.data = HdlDataLicense(**as_dict(self.data))

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class HdlDataLicense(YAMLRoot):
    """
    The data element in the handle API for the license.
    """

    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PID4CAT_MODEL["HdlDataLicense"]
    class_class_curie: ClassVar[str] = "pid4cat_model:HdlDataLicense"
    class_name: ClassVar[str] = "HdlDataLicense"
    class_model_uri: ClassVar[URIRef] = PID4CAT_MODEL.HdlDataLicense

    format: Optional[str] = None
    value: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.format is not None and not isinstance(self.format, str):
            self.format = str(self.format)

        if self.value is not None and not isinstance(self.value, str):
            self.value = str(self.value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EMAIL(HandleRecord):
    """
    The data element in the handle API for the contact email.
    """

    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PID4CAT_MODEL["EMAIL"]
    class_class_curie: ClassVar[str] = "pid4cat_model:EMAIL"
    class_name: ClassVar[str] = "EMAIL"
    class_model_uri: ClassVar[URIRef] = PID4CAT_MODEL.EMAIL

    index: Optional[int] = None
    data: Optional[Union[dict, "HdlDataContact"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.index is not None and not isinstance(self.index, int):
            self.index = int(self.index)

        if self.data is not None and not isinstance(self.data, HdlDataContact):
            self.data = HdlDataContact(**as_dict(self.data))

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class HdlDataContact(YAMLRoot):
    """
    The data element in the handle API for the contact email.
    """

    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PID4CAT_MODEL["HdlDataContact"]
    class_class_curie: ClassVar[str] = "pid4cat_model:HdlDataContact"
    class_name: ClassVar[str] = "HdlDataContact"
    class_model_uri: ClassVar[URIRef] = PID4CAT_MODEL.HdlDataContact

    format: Optional[str] = None
    value: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.format is not None and not isinstance(self.format, str):
            self.format = str(self.format)

        if self.value is not None and not isinstance(self.value, str):
            self.value = str(self.value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RESOURCEINFO(HandleRecord):
    """
    The data element in the handle API for the resource info.
    """

    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PID4CAT_MODEL["RESOURCEINFO"]
    class_class_curie: ClassVar[str] = "pid4cat_model:RESOURCEINFO"
    class_name: ClassVar[str] = "RESOURCE_INFO"
    class_model_uri: ClassVar[URIRef] = PID4CAT_MODEL.RESOURCEINFO

    index: Optional[int] = None
    data: Optional[Union[dict, "HdlDataResourceInfo"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.index is not None and not isinstance(self.index, int):
            self.index = int(self.index)

        if self.data is not None and not isinstance(self.data, HdlDataResourceInfo):
            self.data = HdlDataResourceInfo(**as_dict(self.data))

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class HdlDataResourceInfo(YAMLRoot):
    """
    The data element in the handle API for the resource info.
    """

    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PID4CAT_MODEL["HdlDataResourceInfo"]
    class_class_curie: ClassVar[str] = "pid4cat_model:HdlDataResourceInfo"
    class_name: ClassVar[str] = "HdlDataResourceInfo"
    class_model_uri: ClassVar[URIRef] = PID4CAT_MODEL.HdlDataResourceInfo

    format: Optional[str] = None
    value: Optional[Union[dict, "ResourceInfo"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.format is not None and not isinstance(self.format, str):
            self.format = str(self.format)

        if self.value is not None and not isinstance(self.value, ResourceInfo):
            self.value = ResourceInfo(**as_dict(self.value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RELATED(HandleRecord):
    """
    The data element in the handle API for related identifiers.
    """

    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PID4CAT_MODEL["RELATED"]
    class_class_curie: ClassVar[str] = "pid4cat_model:RELATED"
    class_name: ClassVar[str] = "RELATED"
    class_model_uri: ClassVar[URIRef] = PID4CAT_MODEL.RELATED

    index: Optional[int] = None
    data: Optional[Union[dict, "HdlDataRelated"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.index is not None and not isinstance(self.index, int):
            self.index = int(self.index)

        if self.data is not None and not isinstance(self.data, HdlDataRelated):
            self.data = HdlDataRelated(**as_dict(self.data))

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class HdlDataRelated(YAMLRoot):
    """
    The data element in the handle API for related identifiers.
    """

    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PID4CAT_MODEL["HdlDataRelated"]
    class_class_curie: ClassVar[str] = "pid4cat_model:HdlDataRelated"
    class_name: ClassVar[str] = "HdlDataRelated"
    class_model_uri: ClassVar[URIRef] = PID4CAT_MODEL.HdlDataRelated

    format: Optional[str] = None
    value: Optional[
        Union[Union[dict, "Pid4CatRelation"], List[Union[dict, "Pid4CatRelation"]]]
    ] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.format is not None and not isinstance(self.format, str):
            self.format = str(self.format)

        if not isinstance(self.value, list):
            self.value = [self.value] if self.value is not None else []
        self.value = [
            v if isinstance(v, Pid4CatRelation) else Pid4CatRelation(**as_dict(v))
            for v in self.value
        ]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LOG(HandleRecord):
    """
    The data element in the handle API for the change log.
    """

    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PID4CAT_MODEL["LOG"]
    class_class_curie: ClassVar[str] = "pid4cat_model:LOG"
    class_name: ClassVar[str] = "LOG"
    class_model_uri: ClassVar[URIRef] = PID4CAT_MODEL.LOG

    index: Optional[int] = None
    data: Optional[Union[dict, "HdlDataLog"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.index is not None and not isinstance(self.index, int):
            self.index = int(self.index)

        if self.data is not None and not isinstance(self.data, HdlDataLog):
            self.data = HdlDataLog(**as_dict(self.data))

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class HdlDataLog(YAMLRoot):
    """
    The data element in the handle API for the change log.
    """

    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PID4CAT_MODEL["HdlDataLog"]
    class_class_curie: ClassVar[str] = "pid4cat_model:HdlDataLog"
    class_name: ClassVar[str] = "HdlDataLog"
    class_model_uri: ClassVar[URIRef] = PID4CAT_MODEL.HdlDataLog

    format: Optional[str] = None
    value: Optional[Union[Union[dict, "LogRecord"], List[Union[dict, "LogRecord"]]]] = (
        empty_list()
    )

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.format is not None and not isinstance(self.format, str):
            self.format = str(self.format)

        if not isinstance(self.value, list):
            self.value = [self.value] if self.value is not None else []
        self.value = [
            v if isinstance(v, LogRecord) else LogRecord(**as_dict(v))
            for v in self.value
        ]

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

    contains_pids: Optional[
        Union[
            Dict[Union[str, HandleAPIRecordHandle], Union[dict, HandleAPIRecord]],
            List[Union[dict, HandleAPIRecord]],
        ]
    ] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(
            slot_name="contains_pids",
            slot_type=HandleAPIRecord,
            key_name="handle",
            keyed=True,
        )

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Pid4CatRelation(YAMLRoot):
    """
    A relation between pid4cat handles or between a pid4cat handle and other resources identified by a PID.
    """

    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PID4CAT_MODEL["Pid4CatRelation"]
    class_class_curie: ClassVar[str] = "pid4cat_model:Pid4CatRelation"
    class_name: ClassVar[str] = "Pid4CatRelation"
    class_model_uri: ClassVar[URIRef] = PID4CAT_MODEL.Pid4CatRelation

    relation_type: Optional[Union[str, "RelationType"]] = None
    related_identifier: Optional[Union[dict, "RelatedIdentifier"]] = None
    datetime_log: Optional[Union[str, XSDDateTime]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.relation_type is not None and not isinstance(
            self.relation_type, RelationType
        ):
            self.relation_type = RelationType(self.relation_type)

        if self.related_identifier is not None and not isinstance(
            self.related_identifier, RelatedIdentifier
        ):
            self.related_identifier = RelatedIdentifier(
                **as_dict(self.related_identifier)
            )

        if self.datetime_log is not None and not isinstance(
            self.datetime_log, XSDDateTime
        ):
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
    representation_variants: Optional[
        Union[
            Union[dict, "RepresentationVariant"],
            List[Union[dict, "RepresentationVariant"]],
        ]
    ] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.resource_category is not None and not isinstance(
            self.resource_category, ResourceCategory
        ):
            self.resource_category = ResourceCategory(self.resource_category)

        if not isinstance(self.representation_variants, list):
            self.representation_variants = (
                [self.representation_variants]
                if self.representation_variants is not None
                else []
            )
        self.representation_variants = [
            v
            if isinstance(v, RepresentationVariant)
            else RepresentationVariant(**as_dict(v))
            for v in self.representation_variants
        ]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LogRecord(YAMLRoot):
    """
    A log record for changes made in a pid4cat handle record starting from registration.
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
        if self.datetime_log is not None and not isinstance(
            self.datetime_log, XSDDateTime
        ):
            self.datetime_log = XSDDateTime(self.datetime_log)

        if self.has_agent is not None and not isinstance(self.has_agent, Agent):
            self.has_agent = Agent(**as_dict(self.has_agent))

        if self.changed_field is not None and not isinstance(
            self.changed_field, ChangeLogField
        ):
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
    role: Optional[Union[str, "Pid4CatAgentRole"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.email is not None and not isinstance(self.email, str):
            self.email = str(self.email)

        if self.orcid is not None and not isinstance(self.orcid, str):
            self.orcid = str(self.orcid)

        if self.affiliation_ror is not None and not isinstance(
            self.affiliation_ror, URI
        ):
            self.affiliation_ror = URI(self.affiliation_ror)

        if self.role is not None and not isinstance(self.role, Pid4CatAgentRole):
            self.role = Pid4CatAgentRole(self.role)

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

        if self.encoding_format is not None and not isinstance(
            self.encoding_format, str
        ):
            self.encoding_format = str(self.encoding_format)

        if self.size is not None and not isinstance(self.size, int):
            self.size = int(self.size)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RelatedIdentifier(YAMLRoot):
    """
    A class for all types pf related identifiers.
    """

    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PID4CAT_MODEL["RelatedIdentifier"]
    class_class_curie: ClassVar[str] = "pid4cat_model:RelatedIdentifier"
    class_name: ClassVar[str] = "RelatedIdentifier"
    class_model_uri: ClassVar[URIRef] = PID4CAT_MODEL.RelatedIdentifier

    type: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self.type = str(self.class_name)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)

    def __new__(cls, *args, **kwargs):
        type_designator = "type"
        if type_designator not in kwargs:
            return super().__new__(cls, *args, **kwargs)
        else:
            type_designator_value = kwargs[type_designator]
            target_cls = cls._class_for("class_name", type_designator_value)

            if target_cls is None:
                raise ValueError(
                    f"Wrong type designator value: class {cls.__name__} "
                    f"has no subclass with ['class_name']='{kwargs[type_designator]}'"
                )
            return super().__new__(target_cls, *args, **kwargs)


@dataclass(repr=False)
class PurlIdentifier(RelatedIdentifier):
    """
    A PURL (permanent uniform resource locator).
    """

    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PID4CAT_MODEL["PurlIdentifier"]
    class_class_curie: ClassVar[str] = "pid4cat_model:PurlIdentifier"
    class_name: ClassVar[str] = "PurlIdentifier"
    class_model_uri: ClassVar[URIRef] = PID4CAT_MODEL.PurlIdentifier

    resolving_url: Optional[Union[str, URI]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.resolving_url is not None and not isinstance(self.resolving_url, URI):
            self.resolving_url = URI(self.resolving_url)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class DoiIdentifier(RelatedIdentifier):
    """
    A digital object identifier (DOI).
    """

    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PID4CAT_MODEL["DoiIdentifier"]
    class_class_curie: ClassVar[str] = "pid4cat_model:DoiIdentifier"
    class_name: ClassVar[str] = "DoiIdentifier"
    class_model_uri: ClassVar[URIRef] = PID4CAT_MODEL.DoiIdentifier

    resolving_url: Optional[Union[str, URI]] = None
    identifier: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.resolving_url is not None and not isinstance(self.resolving_url, URI):
            self.resolving_url = URI(self.resolving_url)

        if self.identifier is not None and not isinstance(self.identifier, str):
            self.identifier = str(self.identifier)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class HandleIdentifier(RelatedIdentifier):
    """
    A handle identifier.
    """

    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PID4CAT_MODEL["HandleIdentifier"]
    class_class_curie: ClassVar[str] = "pid4cat_model:HandleIdentifier"
    class_name: ClassVar[str] = "HandleIdentifier"
    class_model_uri: ClassVar[URIRef] = PID4CAT_MODEL.HandleIdentifier

    resolving_url: Optional[Union[str, URI]] = None
    identifier: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.resolving_url is not None and not isinstance(self.resolving_url, URI):
            self.resolving_url = URI(self.resolving_url)

        if self.identifier is not None and not isinstance(self.identifier, str):
            self.identifier = str(self.identifier)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class ArkIdentifier(RelatedIdentifier):
    """
    An ARK (Archival Resource Key).
    """

    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PID4CAT_MODEL["ArkIdentifier"]
    class_class_curie: ClassVar[str] = "pid4cat_model:ArkIdentifier"
    class_name: ClassVar[str] = "ArkIdentifier"
    class_model_uri: ClassVar[URIRef] = PID4CAT_MODEL.ArkIdentifier

    identifier: Optional[str] = None
    resolving_url: Optional[Union[str, URI]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.identifier is not None and not isinstance(self.identifier, str):
            self.identifier = str(self.identifier)

        if self.resolving_url is not None and not isinstance(self.resolving_url, URI):
            self.resolving_url = URI(self.resolving_url)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class UrnIdentifier(RelatedIdentifier):
    """
    A URN (Uniform Resource Name).
    """

    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PID4CAT_MODEL["UrnIdentifier"]
    class_class_curie: ClassVar[str] = "pid4cat_model:UrnIdentifier"
    class_name: ClassVar[str] = "UrnIdentifier"
    class_model_uri: ClassVar[URIRef] = PID4CAT_MODEL.UrnIdentifier

    identifier: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.identifier is not None and not isinstance(self.identifier, str):
            self.identifier = str(self.identifier)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class GtinIdentifier(RelatedIdentifier):
    """
    A Global Trade Item Number (GTIN) previously called European Article Number (EAN) often encoded as EAN13 barcode.
    The identifier is used to identify products. GTINs don't have a resolvable URL.
    """

    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PID4CAT_MODEL["GtinIdentifier"]
    class_class_curie: ClassVar[str] = "pid4cat_model:GtinIdentifier"
    class_name: ClassVar[str] = "GtinIdentifier"
    class_model_uri: ClassVar[URIRef] = PID4CAT_MODEL.GtinIdentifier

    identifier: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.identifier is not None and not isinstance(self.identifier, str):
            self.identifier = str(self.identifier)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class ExampleIdentifier(RelatedIdentifier):
    """
    An example.org test identifier.
    """

    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PID4CAT_MODEL["ExampleIdentifier"]
    class_class_curie: ClassVar[str] = "pid4cat_model:ExampleIdentifier"
    class_name: ClassVar[str] = "ExampleIdentifier"
    class_model_uri: ClassVar[URIRef] = PID4CAT_MODEL.ExampleIdentifier

    identifier: Optional[str] = None
    resolving_url: Optional[Union[str, URI]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.identifier is not None and not isinstance(self.identifier, str):
            self.identifier = str(self.identifier)

        if self.resolving_url is not None and not isinstance(self.resolving_url, URI):
            self.resolving_url = URI(self.resolving_url)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


# Enumerations
class ResourceCategory(EnumDefinitionImpl):
    """
    The ResourceCategory expresses for which type of resource the PID is used, e.g. if the PID is for a sample or a
    device.
    """

    COLLECTION = PermissibleValue(
        text="COLLECTION",
        description="A collection is a group of resources and/or other collections.",
        meaning=VOC4CAT["0005012"],
    )
    SAMPLE = PermissibleValue(
        text="SAMPLE",
        description="A representative part of a material of interest on which observations are made.",
        meaning=VOC4CAT["0005013"],
    )
    MATERIAL = PermissibleValue(
        text="MATERIAL",
        description="A material used in the research process (except samples).",
        meaning=VOC4CAT["0005014"],
    )
    DEVICE = PermissibleValue(
        text="DEVICE",
        description="A physical device used in a research or manufacturing process.",
        meaning=VOC4CAT["0005015"],
    )
    DATA_OBJECT = PermissibleValue(
        text="DATA_OBJECT",
        description="""A collection of data available for access or download. A data object might be a data file, a data set, a data collection.""",
        meaning=VOC4CAT["0005016"],
    )
    DATA_SERVICE = PermissibleValue(
        text="DATA_SERVICE",
        description="""An organized system of operations that provide data processing functions or access to datasets.""",
        meaning=VOC4CAT["0005017"],
    )

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
        meaning=VOC4CAT["0005019"],
    )
    CITES = PermissibleValue(
        text="CITES",
        description="The resource cites another resource.",
        meaning=VOC4CAT["0005020"],
    )
    IS_SUPPLEMENT_TO = PermissibleValue(
        text="IS_SUPPLEMENT_TO",
        description="The resource is supplemented by another resource.",
        meaning=VOC4CAT["0005021"],
    )
    IS_SUPPLEMENTED_BY = PermissibleValue(
        text="IS_SUPPLEMENTED_BY",
        description="The resource supplements another resource.",
        meaning=VOC4CAT["0005022"],
    )
    IS_CONTINUED_BY = PermissibleValue(
        text="IS_CONTINUED_BY",
        description="The resource is continued by another resource.",
        meaning=VOC4CAT["0005023"],
    )
    CONTINUES = PermissibleValue(
        text="CONTINUES",
        description="The resource continues another resource.",
        meaning=VOC4CAT["0005024"],
    )
    HAS_METADATA = PermissibleValue(
        text="HAS_METADATA",
        description="The resource has metadata in another resource.",
        meaning=VOC4CAT["0005025"],
    )
    IS_METADATA_FOR = PermissibleValue(
        text="IS_METADATA_FOR",
        description="The resource is metadata for another resource.",
        meaning=VOC4CAT["0005026"],
    )
    HAS_VERSION = PermissibleValue(
        text="HAS_VERSION",
        description="The resource has a version.",
        meaning=VOC4CAT["0005027"],
    )
    IS_VERSION_OF = PermissibleValue(
        text="IS_VERSION_OF",
        description="""The resource is a version of another resource. This is useful to refer to an abstract resource that has different versions, for example, \"Python 3.12 is a version of Python\".""",
        meaning=VOC4CAT["0005028"],
    )
    IS_NEW_VERSION_OF = PermissibleValue(
        text="IS_NEW_VERSION_OF",
        description="The resource is a new version of another resource.",
        meaning=VOC4CAT["0005029"],
    )
    IS_PREVIOUS_VERSION_OF = PermissibleValue(
        text="IS_PREVIOUS_VERSION_OF",
        description="The resource is a previous version of another resource.",
        meaning=VOC4CAT["0005030"],
    )
    IS_PART_OF = PermissibleValue(
        text="IS_PART_OF",
        description="The resource is part of another resource.",
        meaning=VOC4CAT["0005031"],
    )
    HAS_PART = PermissibleValue(
        text="HAS_PART",
        description="The resource has part another resource.",
        meaning=VOC4CAT["0005032"],
    )
    IS_PUBLISHED_IN = PermissibleValue(
        text="IS_PUBLISHED_IN",
        description="The resource is published in another resource.",
        meaning=VOC4CAT["0005033"],
    )
    IS_REFERENCED_BY = PermissibleValue(
        text="IS_REFERENCED_BY",
        description="The resource is referenced by another resource.",
        meaning=VOC4CAT["0005034"],
    )
    REFERENCES = PermissibleValue(
        text="REFERENCES",
        description="The resource references another resource.",
        meaning=VOC4CAT["0005035"],
    )
    IS_DOCUMENTED_BY = PermissibleValue(
        text="IS_DOCUMENTED_BY",
        description="The resource is documented by another resource.",
        meaning=VOC4CAT["0005036"],
    )
    DOCUMENTS = PermissibleValue(
        text="DOCUMENTS",
        description="The resource documents another resource.",
        meaning=VOC4CAT["0005037"],
    )
    IS_COMPILED_BY = PermissibleValue(
        text="IS_COMPILED_BY",
        description="The resource is compiled by another resource.",
        meaning=VOC4CAT["0005038"],
    )
    COMPILES = PermissibleValue(
        text="COMPILES",
        description="The resource compiles another resource.",
        meaning=VOC4CAT["0005039"],
    )
    IS_VARIANT_FORM_OF = PermissibleValue(
        text="IS_VARIANT_FORM_OF",
        description="The resource is variant form of another resource.",
        meaning=VOC4CAT["0005040"],
    )
    IS_ORIGINAL_FORM_OF = PermissibleValue(
        text="IS_ORIGINAL_FORM_OF",
        description="The resource is original form of another resource.",
        meaning=VOC4CAT["0005041"],
    )
    IS_IDENTICAL_TO = PermissibleValue(
        text="IS_IDENTICAL_TO",
        description="The resource is identical to another resource.",
        meaning=VOC4CAT["0005042"],
    )
    IS_DERIVED_FROM = PermissibleValue(
        text="IS_DERIVED_FROM",
        description="The resource is derived from another resource.",
        meaning=VOC4CAT["0005043"],
    )
    IS_SOURCE_OF = PermissibleValue(
        text="IS_SOURCE_OF",
        description="The resource is source of another resource.",
        meaning=VOC4CAT["0005044"],
    )
    IS_COLLECTED_BY = PermissibleValue(
        text="IS_COLLECTED_BY",
        description="The resource is collected by another resource.",
        meaning=VOC4CAT["0005045"],
    )
    COLLECTS = PermissibleValue(
        text="COLLECTS",
        description="The resource collects another resource.",
        meaning=VOC4CAT["0005046"],
    )
    IS_REQUIRED_BY = PermissibleValue(
        text="IS_REQUIRED_BY",
        description="The resource is required by another resource.",
        meaning=VOC4CAT["0005047"],
    )
    REQUIRES = PermissibleValue(
        text="REQUIRES",
        description="The resource requires another resource.",
        meaning=VOC4CAT["0005048"],
    )
    IS_OBSOLETED_BY = PermissibleValue(
        text="IS_OBSOLETED_BY",
        description="The resource is obsoleted by another resource.",
        meaning=VOC4CAT["0005049"],
    )
    OBSOLETES = PermissibleValue(
        text="OBSOLETES",
        description="The resource obsoletes another resource.",
        meaning=VOC4CAT["0005050"],
    )

    _defn = EnumDefinition(
        name="RelationType",
        description="The type of relation between two resources referenced by their PIDs.",
    )


class Pid4CatStatus(EnumDefinitionImpl):
    """
    The usage status of the pid4cat record.
    """

    SUBMITTED = PermissibleValue(
        text="SUBMITTED",
        description="The pid4cat handle is reserved but the resource is not yet linked.",
        meaning=VOC4CAT["0005052"],
    )
    REGISTERED = PermissibleValue(
        text="REGISTERED",
        description="The pid4cat handle is linked to a concrete resource.",
        meaning=VOC4CAT["0005053"],
    )
    OBSOLETED = PermissibleValue(
        text="OBSOLETED",
        description="The pid4cat handle is obsolete, e.g. because the resource is referenced by another pid4cat.",
        meaning=VOC4CAT["0005054"],
    )
    DEPRECATED = PermissibleValue(
        text="DEPRECATED",
        description="The pid4cat record is deprecated, e.g. because the resource can no longer be found.",
        meaning=VOC4CAT["0005055"],
    )

    _defn = EnumDefinition(
        name="Pid4CatStatus",
        description="The usage status of the pid4cat record.",
    )


class Pid4CatAgentRole(EnumDefinitionImpl):
    """
    The role of an agent relative to the resource.
    """

    TRUSTEE = PermissibleValue(
        text="TRUSTEE", description="The agent is the trustee of the resource."
    )
    OWNER = PermissibleValue(
        text="OWNER", description="The agent is the owner of the resource."
    )

    _defn = EnumDefinition(
        name="Pid4CatAgentRole",
        description="The role of an agent relative to the resource.",
    )


class ChangeLogField(EnumDefinitionImpl):
    """
    The field of the pid4cat record that was changed.
    """

    STATUS = PermissibleValue(
        text="STATUS", description="The status of the pid4cat record was changed."
    )
    LANDING_PAGE = PermissibleValue(
        text="LANDING_PAGE",
        description="The URL of the landing page in the pid4cat record was changed.",
    )
    RESOURCE_INFO = PermissibleValue(
        text="RESOURCE_INFO",
        description="The resource info of the pid4cat record was changed.",
    )
    RELATED_IDS = PermissibleValue(
        text="RELATED_IDS",
        description="The related identifiers of the pid4cat record were changed.",
    )
    CONTACT = PermissibleValue(
        text="CONTACT",
        description="The contact information of the pid4cat record was changed.",
    )
    LICENSE = PermissibleValue(
        text="LICENSE", description="The license of the pid4cat record was changed."
    )
    SCHEMA_VER = PermissibleValue(
        text="SCHEMA_VER",
        description="The pid4cat-model version of the pid4cat record was changed.",
    )

    _defn = EnumDefinition(
        name="ChangeLogField",
        description="The field of the pid4cat record that was changed.",
    )


class MEDIATypes(EnumDefinitionImpl):
    """
    The IANA media types are used to specify the type of data.
    """

    _defn = EnumDefinition(
        name="MEDIATypes",
        description="The IANA media types are used to specify the type of data.",
    )

    @classmethod
    def _addvals(cls):
        setattr(
            cls,
            "application/epub+zip",
            PermissibleValue(
                text="application/epub+zip",
                description="For data in Electronic Publication Format (EPUB).",
            ),
        )
        setattr(
            cls,
            "application/json",
            PermissibleValue(
                text="application/json",
                description="For data in JavaScript Object Notation (JSON).",
            ),
        )
        setattr(
            cls,
            "application/ld+json",
            PermissibleValue(
                text="application/ld+json",
                description="For data in Linked Data json (JSON-LD).",
            ),
        )
        setattr(
            cls,
            "application/octet-stream",
            PermissibleValue(
                text="application/octet-stream", description="For binary data."
            ),
        )
        setattr(
            cls,
            "application/pdf",
            PermissibleValue(
                text="application/pdf",
                description="For data in Portable Document Format (PDF).",
            ),
        )
        setattr(
            cls,
            "application/vnd.eln+zip",
            PermissibleValue(
                text="application/vnd.eln+zip",
                description="For data in ELN ZIP format.",
            ),
        )
        setattr(
            cls,
            "application/vnd.openxmlformats-officedocument.presentationml.presentation",
            PermissibleValue(
                text="application/vnd.openxmlformats-officedocument.presentationml.presentation",
                description="For data in PowerPoint pptx format.",
            ),
        )
        setattr(
            cls,
            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            PermissibleValue(
                text="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                description="For data in Excel xlsx format.",
            ),
        )
        setattr(
            cls,
            "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            PermissibleValue(
                text="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                description="For data in Word docx format.",
            ),
        )
        setattr(
            cls,
            "application/xml",
            PermissibleValue(
                text="application/xml", description="For generic XML data."
            ),
        )
        setattr(
            cls,
            "application/yaml",
            PermissibleValue(text="application/yaml", description="For YAML data."),
        )
        setattr(
            cls,
            "application/zip",
            PermissibleValue(text="application/zip", description="For zip archives."),
        )
        setattr(
            cls,
            "image/gif",
            PermissibleValue(text="image/gif", description="For GIF images."),
        )
        setattr(
            cls,
            "image/jpeg",
            PermissibleValue(text="image/jpeg", description="For JPEG images."),
        )
        setattr(
            cls,
            "image/png",
            PermissibleValue(text="image/png", description="For PNG images."),
        )
        setattr(
            cls,
            "image/svg+xml",
            PermissibleValue(text="image/svg+xml", description="For SVG images."),
        )
        setattr(
            cls,
            "image/tiff",
            PermissibleValue(text="image/tiff", description="For TIFF images."),
        )
        setattr(
            cls,
            "image/webp",
            PermissibleValue(text="image/webp", description="For WebP images."),
        )
        setattr(
            cls,
            "text/csv",
            PermissibleValue(
                text="text/csv",
                description="For data in comma-separated values (CSV) format.",
            ),
        )
        setattr(
            cls,
            "text/html",
            PermissibleValue(text="text/html", description="For html web pages."),
        )
        setattr(
            cls,
            "text/javascript",
            PermissibleValue(
                text="text/javascript", description="For JavaScript code."
            ),
        )
        setattr(
            cls,
            "text/markdown",
            PermissibleValue(
                text="text/markdown", description="For data in markdown text format."
            ),
        )
        setattr(
            cls,
            "text/plain",
            PermissibleValue(
                text="text/plain",
                description="For plain text data (default text media type).",
            ),
        )
        setattr(
            cls,
            "text/tab-separated-values",
            PermissibleValue(
                text="text/tab-separated-values",
                description="For data in tab-separated values (TSV) format.",
            ),
        )
        setattr(
            cls,
            "text/turtle",
            PermissibleValue(
                text="text/turtle", description="For data in turtle format."
            ),
        )
        setattr(
            cls,
            "text/xml",
            PermissibleValue(text="text/xml", description="For XML data."),
        )
        setattr(
            cls,
            "video/mp4",
            PermissibleValue(text="video/mp4", description="For mp4 video files."),
        )
        setattr(
            cls,
            "video/webm",
            PermissibleValue(text="video/webm", description="For webm video files."),
        )


# Slots
class slots:
    pass


slots.responseCode = Slot(
    uri=PID4CAT_MODEL.responseCode,
    name="responseCode",
    curie=PID4CAT_MODEL.curie("responseCode"),
    model_uri=PID4CAT_MODEL.responseCode,
    domain=None,
    range=Optional[int],
)

slots.handle = Slot(
    uri=PID4CAT_MODEL.handle,
    name="handle",
    curie=PID4CAT_MODEL.curie("handle"),
    model_uri=PID4CAT_MODEL.handle,
    domain=None,
    range=URIRef,
)

slots.values = Slot(
    uri=PID4CAT_MODEL.values,
    name="values",
    curie=PID4CAT_MODEL.curie("values"),
    model_uri=PID4CAT_MODEL.values,
    domain=None,
    range=Optional[Union[Union[dict, HandleRecord], List[Union[dict, HandleRecord]]]],
)

slots.index = Slot(
    uri=PID4CAT_MODEL.index,
    name="index",
    curie=PID4CAT_MODEL.curie("index"),
    model_uri=PID4CAT_MODEL.index,
    domain=None,
    range=Optional[int],
)

slots.data = Slot(
    uri=PID4CAT_MODEL.data,
    name="data",
    curie=PID4CAT_MODEL.curie("data"),
    model_uri=PID4CAT_MODEL.data,
    domain=None,
    range=Optional[str],
)

slots.type = Slot(
    uri=PID4CAT_MODEL.type,
    name="type",
    curie=PID4CAT_MODEL.curie("type"),
    model_uri=PID4CAT_MODEL.type,
    domain=None,
    range=Optional[str],
)

slots.ttl = Slot(
    uri=PID4CAT_MODEL.ttl,
    name="ttl",
    curie=PID4CAT_MODEL.curie("ttl"),
    model_uri=PID4CAT_MODEL.ttl,
    domain=None,
    range=Optional[int],
)

slots.timestamp = Slot(
    uri=PID4CAT_MODEL.timestamp,
    name="timestamp",
    curie=PID4CAT_MODEL.curie("timestamp"),
    model_uri=PID4CAT_MODEL.timestamp,
    domain=None,
    range=Optional[Union[str, XSDDateTime]],
)

slots.format = Slot(
    uri=PID4CAT_MODEL.format,
    name="format",
    curie=PID4CAT_MODEL.curie("format"),
    model_uri=PID4CAT_MODEL.format,
    domain=None,
    range=Optional[str],
)

slots.value = Slot(
    uri=PID4CAT_MODEL.value,
    name="value",
    curie=PID4CAT_MODEL.curie("value"),
    model_uri=PID4CAT_MODEL.value,
    domain=None,
    range=Optional[str],
)

slots.status = Slot(
    uri=PID4CAT_MODEL.status,
    name="status",
    curie=PID4CAT_MODEL.curie("status"),
    model_uri=PID4CAT_MODEL.status,
    domain=None,
    range=Optional[Union[str, "Pid4CatStatus"]],
)

slots.license = Slot(
    uri=PID4CAT_MODEL.license,
    name="license",
    curie=PID4CAT_MODEL.curie("license"),
    model_uri=PID4CAT_MODEL.license,
    domain=None,
    range=Optional[str],
)

slots.curation_contact_email = Slot(
    uri=PID4CAT_MODEL.curation_contact_email,
    name="curation_contact_email",
    curie=PID4CAT_MODEL.curie("curation_contact_email"),
    model_uri=PID4CAT_MODEL.curation_contact_email,
    domain=None,
    range=Optional[str],
)

slots.relation_type = Slot(
    uri=PID4CAT_MODEL.relation_type,
    name="relation_type",
    curie=PID4CAT_MODEL.curie("relation_type"),
    model_uri=PID4CAT_MODEL.relation_type,
    domain=None,
    range=Optional[Union[str, "RelationType"]],
)

slots.related_identifier = Slot(
    uri=PID4CAT_MODEL.related_identifier,
    name="related_identifier",
    curie=PID4CAT_MODEL.curie("related_identifier"),
    model_uri=PID4CAT_MODEL.related_identifier,
    domain=None,
    range=Optional[Union[dict, RelatedIdentifier]],
)

slots.datetime_log = Slot(
    uri=PID4CAT_MODEL.datetime_log,
    name="datetime_log",
    curie=PID4CAT_MODEL.curie("datetime_log"),
    model_uri=PID4CAT_MODEL.datetime_log,
    domain=None,
    range=Optional[Union[str, XSDDateTime]],
)

slots.label = Slot(
    uri=PID4CAT_MODEL.label,
    name="label",
    curie=PID4CAT_MODEL.curie("label"),
    model_uri=PID4CAT_MODEL.label,
    domain=None,
    range=Optional[str],
)

slots.description = Slot(
    uri=PID4CAT_MODEL.description,
    name="description",
    curie=PID4CAT_MODEL.curie("description"),
    model_uri=PID4CAT_MODEL.description,
    domain=None,
    range=Optional[str],
)

slots.resource_category = Slot(
    uri=PID4CAT_MODEL.resource_category,
    name="resource_category",
    curie=PID4CAT_MODEL.curie("resource_category"),
    model_uri=PID4CAT_MODEL.resource_category,
    domain=None,
    range=Optional[Union[str, "ResourceCategory"]],
)

slots.representation_variants = Slot(
    uri=PID4CAT_MODEL.representation_variants,
    name="representation_variants",
    curie=PID4CAT_MODEL.curie("representation_variants"),
    model_uri=PID4CAT_MODEL.representation_variants,
    domain=None,
    range=Optional[
        Union[
            Union[dict, RepresentationVariant], List[Union[dict, RepresentationVariant]]
        ]
    ],
)

slots.changed_field = Slot(
    uri=PID4CAT_MODEL.changed_field,
    name="changed_field",
    curie=PID4CAT_MODEL.curie("changed_field"),
    model_uri=PID4CAT_MODEL.changed_field,
    domain=None,
    range=Optional[Union[str, "ChangeLogField"]],
)

slots.has_agent = Slot(
    uri=PID4CAT_MODEL.has_agent,
    name="has_agent",
    curie=PID4CAT_MODEL.curie("has_agent"),
    model_uri=PID4CAT_MODEL.has_agent,
    domain=None,
    range=Optional[Union[dict, Agent]],
)

slots.name = Slot(
    uri=PID4CAT_MODEL.name,
    name="name",
    curie=PID4CAT_MODEL.curie("name"),
    model_uri=PID4CAT_MODEL.name,
    domain=None,
    range=Optional[str],
)

slots.email = Slot(
    uri=PID4CAT_MODEL.email,
    name="email",
    curie=PID4CAT_MODEL.curie("email"),
    model_uri=PID4CAT_MODEL.email,
    domain=None,
    range=Optional[str],
)

slots.orcid = Slot(
    uri=PID4CAT_MODEL.orcid,
    name="orcid",
    curie=PID4CAT_MODEL.curie("orcid"),
    model_uri=PID4CAT_MODEL.orcid,
    domain=None,
    range=Optional[str],
)

slots.affiliation_ror = Slot(
    uri=PID4CAT_MODEL.affiliation_ror,
    name="affiliation_ror",
    curie=PID4CAT_MODEL.curie("affiliation_ror"),
    model_uri=PID4CAT_MODEL.affiliation_ror,
    domain=None,
    range=Optional[Union[str, URI]],
)

slots.role = Slot(
    uri=PID4CAT_MODEL.role,
    name="role",
    curie=PID4CAT_MODEL.curie("role"),
    model_uri=PID4CAT_MODEL.role,
    domain=None,
    range=Optional[Union[str, "Pid4CatAgentRole"]],
)

slots.media_type = Slot(
    uri=PID4CAT_MODEL.media_type,
    name="media_type",
    curie=PID4CAT_MODEL.curie("media_type"),
    model_uri=PID4CAT_MODEL.media_type,
    domain=None,
    range=Optional[Union[str, "MEDIATypes"]],
)

slots.encoding_format = Slot(
    uri=PID4CAT_MODEL.encoding_format,
    name="encoding_format",
    curie=PID4CAT_MODEL.curie("encoding_format"),
    model_uri=PID4CAT_MODEL.encoding_format,
    domain=None,
    range=Optional[str],
)

slots.size = Slot(
    uri=PID4CAT_MODEL.size,
    name="size",
    curie=PID4CAT_MODEL.curie("size"),
    model_uri=PID4CAT_MODEL.size,
    domain=None,
    range=Optional[int],
)

slots.url = Slot(
    uri=PID4CAT_MODEL.url,
    name="url",
    curie=PID4CAT_MODEL.curie("url"),
    model_uri=PID4CAT_MODEL.url,
    domain=None,
    range=Optional[Union[str, URI]],
)

slots.resolving_url = Slot(
    uri=PID4CAT_MODEL.resolving_url,
    name="resolving_url",
    curie=PID4CAT_MODEL.curie("resolving_url"),
    model_uri=PID4CAT_MODEL.resolving_url,
    domain=None,
    range=Optional[Union[str, URI]],
)

slots.identifier = Slot(
    uri=PID4CAT_MODEL.identifier,
    name="identifier",
    curie=PID4CAT_MODEL.curie("identifier"),
    model_uri=PID4CAT_MODEL.identifier,
    domain=None,
    range=Optional[str],
)

slots.handleRecordContainer__contains_pids = Slot(
    uri=PID4CAT_MODEL.contains_pids,
    name="handleRecordContainer__contains_pids",
    curie=PID4CAT_MODEL.curie("contains_pids"),
    model_uri=PID4CAT_MODEL.handleRecordContainer__contains_pids,
    domain=None,
    range=Optional[
        Union[
            Dict[Union[str, HandleAPIRecordHandle], Union[dict, HandleAPIRecord]],
            List[Union[dict, HandleAPIRecord]],
        ]
    ],
)

slots.relatedIdentifier__type = Slot(
    uri=PID4CAT_MODEL.type,
    name="relatedIdentifier__type",
    curie=PID4CAT_MODEL.curie("type"),
    model_uri=PID4CAT_MODEL.relatedIdentifier__type,
    domain=None,
    range=Optional[str],
)

slots.HandleRecord_type = Slot(
    uri=PID4CAT_MODEL.type,
    name="HandleRecord_type",
    curie=PID4CAT_MODEL.curie("type"),
    model_uri=PID4CAT_MODEL.HandleRecord_type,
    domain=HandleRecord,
    range=Optional[str],
)

slots.URL_index = Slot(
    uri=PID4CAT_MODEL.index,
    name="URL_index",
    curie=PID4CAT_MODEL.curie("index"),
    model_uri=PID4CAT_MODEL.URL_index,
    domain=URL,
    range=Optional[int],
)

slots.URL_data = Slot(
    uri=PID4CAT_MODEL.data,
    name="URL_data",
    curie=PID4CAT_MODEL.curie("data"),
    model_uri=PID4CAT_MODEL.URL_data,
    domain=URL,
    range=Optional[Union[dict, "HdlDataUrl"]],
)

slots.HdlDataUrl_format = Slot(
    uri=PID4CAT_MODEL.format,
    name="HdlDataUrl_format",
    curie=PID4CAT_MODEL.curie("format"),
    model_uri=PID4CAT_MODEL.HdlDataUrl_format,
    domain=HdlDataUrl,
    range=Optional[str],
)

slots.HdlDataUrl_value = Slot(
    uri=PID4CAT_MODEL.value,
    name="HdlDataUrl_value",
    curie=PID4CAT_MODEL.curie("value"),
    model_uri=PID4CAT_MODEL.HdlDataUrl_value,
    domain=HdlDataUrl,
    range=Optional[str],
    pattern=re.compile(r"^https?:\/\/.*$"),
)

slots.STATUS_index = Slot(
    uri=PID4CAT_MODEL.index,
    name="STATUS_index",
    curie=PID4CAT_MODEL.curie("index"),
    model_uri=PID4CAT_MODEL.STATUS_index,
    domain=STATUS,
    range=Optional[int],
)

slots.STATUS_data = Slot(
    uri=PID4CAT_MODEL.data,
    name="STATUS_data",
    curie=PID4CAT_MODEL.curie("data"),
    model_uri=PID4CAT_MODEL.STATUS_data,
    domain=STATUS,
    range=Optional[Union[dict, "HdlDataStatus"]],
)

slots.HdlDataStatus_format = Slot(
    uri=PID4CAT_MODEL.format,
    name="HdlDataStatus_format",
    curie=PID4CAT_MODEL.curie("format"),
    model_uri=PID4CAT_MODEL.HdlDataStatus_format,
    domain=HdlDataStatus,
    range=Optional[str],
)

slots.HdlDataStatus_value = Slot(
    uri=PID4CAT_MODEL.value,
    name="HdlDataStatus_value",
    curie=PID4CAT_MODEL.curie("value"),
    model_uri=PID4CAT_MODEL.HdlDataStatus_value,
    domain=HdlDataStatus,
    range=Optional[Union[str, "Pid4CatStatus"]],
)

slots.SCHEMA_VER_index = Slot(
    uri=PID4CAT_MODEL.index,
    name="SCHEMA_VER_index",
    curie=PID4CAT_MODEL.curie("index"),
    model_uri=PID4CAT_MODEL.SCHEMA_VER_index,
    domain=SCHEMAVER,
    range=Optional[int],
)

slots.SCHEMA_VER_data = Slot(
    uri=PID4CAT_MODEL.data,
    name="SCHEMA_VER_data",
    curie=PID4CAT_MODEL.curie("data"),
    model_uri=PID4CAT_MODEL.SCHEMA_VER_data,
    domain=SCHEMAVER,
    range=Optional[Union[dict, "HdlDataSchemaVer"]],
)

slots.HdlDataSchemaVer_format = Slot(
    uri=PID4CAT_MODEL.format,
    name="HdlDataSchemaVer_format",
    curie=PID4CAT_MODEL.curie("format"),
    model_uri=PID4CAT_MODEL.HdlDataSchemaVer_format,
    domain=HdlDataSchemaVer,
    range=Optional[str],
)

slots.HdlDataSchemaVer_value = Slot(
    uri=PID4CAT_MODEL.value,
    name="HdlDataSchemaVer_value",
    curie=PID4CAT_MODEL.curie("value"),
    model_uri=PID4CAT_MODEL.HdlDataSchemaVer_value,
    domain=HdlDataSchemaVer,
    range=Optional[str],
    pattern=re.compile(r"^v\d+\.\d+\.\d+$"),
)

slots.LICENSE_index = Slot(
    uri=PID4CAT_MODEL.index,
    name="LICENSE_index",
    curie=PID4CAT_MODEL.curie("index"),
    model_uri=PID4CAT_MODEL.LICENSE_index,
    domain=LICENSE,
    range=Optional[int],
)

slots.LICENSE_data = Slot(
    uri=PID4CAT_MODEL.data,
    name="LICENSE_data",
    curie=PID4CAT_MODEL.curie("data"),
    model_uri=PID4CAT_MODEL.LICENSE_data,
    domain=LICENSE,
    range=Optional[Union[dict, "HdlDataLicense"]],
)

slots.HdlDataLicense_format = Slot(
    uri=PID4CAT_MODEL.format,
    name="HdlDataLicense_format",
    curie=PID4CAT_MODEL.curie("format"),
    model_uri=PID4CAT_MODEL.HdlDataLicense_format,
    domain=HdlDataLicense,
    range=Optional[str],
)

slots.HdlDataLicense_value = Slot(
    uri=PID4CAT_MODEL.value,
    name="HdlDataLicense_value",
    curie=PID4CAT_MODEL.curie("value"),
    model_uri=PID4CAT_MODEL.HdlDataLicense_value,
    domain=HdlDataLicense,
    range=Optional[str],
)

slots.EMAIL_index = Slot(
    uri=PID4CAT_MODEL.index,
    name="EMAIL_index",
    curie=PID4CAT_MODEL.curie("index"),
    model_uri=PID4CAT_MODEL.EMAIL_index,
    domain=EMAIL,
    range=Optional[int],
)

slots.EMAIL_data = Slot(
    uri=PID4CAT_MODEL.data,
    name="EMAIL_data",
    curie=PID4CAT_MODEL.curie("data"),
    model_uri=PID4CAT_MODEL.EMAIL_data,
    domain=EMAIL,
    range=Optional[Union[dict, "HdlDataContact"]],
)

slots.HdlDataContact_format = Slot(
    uri=PID4CAT_MODEL.format,
    name="HdlDataContact_format",
    curie=PID4CAT_MODEL.curie("format"),
    model_uri=PID4CAT_MODEL.HdlDataContact_format,
    domain=HdlDataContact,
    range=Optional[str],
)

slots.HdlDataContact_value = Slot(
    uri=PID4CAT_MODEL.value,
    name="HdlDataContact_value",
    curie=PID4CAT_MODEL.curie("value"),
    model_uri=PID4CAT_MODEL.HdlDataContact_value,
    domain=HdlDataContact,
    range=Optional[str],
    pattern=re.compile(r"^\S+@[\S+\.]+\S+"),
)

slots.RESOURCE_INFO_index = Slot(
    uri=PID4CAT_MODEL.index,
    name="RESOURCE_INFO_index",
    curie=PID4CAT_MODEL.curie("index"),
    model_uri=PID4CAT_MODEL.RESOURCE_INFO_index,
    domain=RESOURCEINFO,
    range=Optional[int],
)

slots.RESOURCE_INFO_data = Slot(
    uri=PID4CAT_MODEL.data,
    name="RESOURCE_INFO_data",
    curie=PID4CAT_MODEL.curie("data"),
    model_uri=PID4CAT_MODEL.RESOURCE_INFO_data,
    domain=RESOURCEINFO,
    range=Optional[Union[dict, "HdlDataResourceInfo"]],
)

slots.HdlDataResourceInfo_format = Slot(
    uri=PID4CAT_MODEL.format,
    name="HdlDataResourceInfo_format",
    curie=PID4CAT_MODEL.curie("format"),
    model_uri=PID4CAT_MODEL.HdlDataResourceInfo_format,
    domain=HdlDataResourceInfo,
    range=Optional[str],
)

slots.HdlDataResourceInfo_value = Slot(
    uri=PID4CAT_MODEL.value,
    name="HdlDataResourceInfo_value",
    curie=PID4CAT_MODEL.curie("value"),
    model_uri=PID4CAT_MODEL.HdlDataResourceInfo_value,
    domain=HdlDataResourceInfo,
    range=Optional[Union[dict, "ResourceInfo"]],
)

slots.RELATED_index = Slot(
    uri=PID4CAT_MODEL.index,
    name="RELATED_index",
    curie=PID4CAT_MODEL.curie("index"),
    model_uri=PID4CAT_MODEL.RELATED_index,
    domain=RELATED,
    range=Optional[int],
)

slots.RELATED_data = Slot(
    uri=PID4CAT_MODEL.data,
    name="RELATED_data",
    curie=PID4CAT_MODEL.curie("data"),
    model_uri=PID4CAT_MODEL.RELATED_data,
    domain=RELATED,
    range=Optional[Union[dict, "HdlDataRelated"]],
)

slots.HdlDataRelated_format = Slot(
    uri=PID4CAT_MODEL.format,
    name="HdlDataRelated_format",
    curie=PID4CAT_MODEL.curie("format"),
    model_uri=PID4CAT_MODEL.HdlDataRelated_format,
    domain=HdlDataRelated,
    range=Optional[str],
)

slots.HdlDataRelated_value = Slot(
    uri=PID4CAT_MODEL.value,
    name="HdlDataRelated_value",
    curie=PID4CAT_MODEL.curie("value"),
    model_uri=PID4CAT_MODEL.HdlDataRelated_value,
    domain=HdlDataRelated,
    range=Optional[
        Union[Union[dict, "Pid4CatRelation"], List[Union[dict, "Pid4CatRelation"]]]
    ],
)

slots.LOG_index = Slot(
    uri=PID4CAT_MODEL.index,
    name="LOG_index",
    curie=PID4CAT_MODEL.curie("index"),
    model_uri=PID4CAT_MODEL.LOG_index,
    domain=LOG,
    range=Optional[int],
)

slots.LOG_data = Slot(
    uri=PID4CAT_MODEL.data,
    name="LOG_data",
    curie=PID4CAT_MODEL.curie("data"),
    model_uri=PID4CAT_MODEL.LOG_data,
    domain=LOG,
    range=Optional[Union[dict, "HdlDataLog"]],
)

slots.HdlDataLog_format = Slot(
    uri=PID4CAT_MODEL.format,
    name="HdlDataLog_format",
    curie=PID4CAT_MODEL.curie("format"),
    model_uri=PID4CAT_MODEL.HdlDataLog_format,
    domain=HdlDataLog,
    range=Optional[str],
)

slots.HdlDataLog_value = Slot(
    uri=PID4CAT_MODEL.value,
    name="HdlDataLog_value",
    curie=PID4CAT_MODEL.curie("value"),
    model_uri=PID4CAT_MODEL.HdlDataLog_value,
    domain=HdlDataLog,
    range=Optional[Union[Union[dict, "LogRecord"], List[Union[dict, "LogRecord"]]]],
)

slots.Agent_email = Slot(
    uri=PID4CAT_MODEL.email,
    name="Agent_email",
    curie=PID4CAT_MODEL.curie("email"),
    model_uri=PID4CAT_MODEL.Agent_email,
    domain=Agent,
    range=Optional[str],
    pattern=re.compile(r"^\S+@[\S+\.]+\S+"),
)

slots.PurlIdentifier_resolving_url = Slot(
    uri=PID4CAT_MODEL.resolving_url,
    name="PurlIdentifier_resolving_url",
    curie=PID4CAT_MODEL.curie("resolving_url"),
    model_uri=PID4CAT_MODEL.PurlIdentifier_resolving_url,
    domain=PurlIdentifier,
    range=Optional[Union[str, URI]],
    pattern=re.compile(r"^https:\/\/(purl|pida|w3id)\.org\/.*$"),
)

slots.DoiIdentifier_identifier = Slot(
    uri=PID4CAT_MODEL.identifier,
    name="DoiIdentifier_identifier",
    curie=PID4CAT_MODEL.curie("identifier"),
    model_uri=PID4CAT_MODEL.DoiIdentifier_identifier,
    domain=DoiIdentifier,
    range=Optional[str],
    pattern=re.compile(r"^doi:10\.\d{4,}\/.*$"),
)

slots.DoiIdentifier_resolving_url = Slot(
    uri=PID4CAT_MODEL.resolving_url,
    name="DoiIdentifier_resolving_url",
    curie=PID4CAT_MODEL.curie("resolving_url"),
    model_uri=PID4CAT_MODEL.DoiIdentifier_resolving_url,
    domain=DoiIdentifier,
    range=Optional[Union[str, URI]],
    pattern=re.compile(r"^https:\/\/doi\.org\/10.*$"),
)

slots.HandleIdentifier_identifier = Slot(
    uri=PID4CAT_MODEL.identifier,
    name="HandleIdentifier_identifier",
    curie=PID4CAT_MODEL.curie("identifier"),
    model_uri=PID4CAT_MODEL.HandleIdentifier_identifier,
    domain=HandleIdentifier,
    range=Optional[str],
    pattern=re.compile(r"^(hdl|handle):\d{2}\.\d{4,}\/.*$"),
)

slots.HandleIdentifier_resolving_url = Slot(
    uri=PID4CAT_MODEL.resolving_url,
    name="HandleIdentifier_resolving_url",
    curie=PID4CAT_MODEL.curie("resolving_url"),
    model_uri=PID4CAT_MODEL.HandleIdentifier_resolving_url,
    domain=HandleIdentifier,
    range=Optional[Union[str, URI]],
    pattern=re.compile(r"^https:\/\/hdl\.handle\.net\/\d{2}\.\d{4,}\/.*$"),
)

slots.ArkIdentifier_identifier = Slot(
    uri=PID4CAT_MODEL.identifier,
    name="ArkIdentifier_identifier",
    curie=PID4CAT_MODEL.curie("identifier"),
    model_uri=PID4CAT_MODEL.ArkIdentifier_identifier,
    domain=ArkIdentifier,
    range=Optional[str],
    pattern=re.compile(r"^ark:\/\d{5}/.*$"),
)

slots.ArkIdentifier_resolving_url = Slot(
    uri=PID4CAT_MODEL.resolving_url,
    name="ArkIdentifier_resolving_url",
    curie=PID4CAT_MODEL.curie("resolving_url"),
    model_uri=PID4CAT_MODEL.ArkIdentifier_resolving_url,
    domain=ArkIdentifier,
    range=Optional[Union[str, URI]],
    pattern=re.compile(r"^https?:\/\/.*\/ark:\/\d{5}/.*$"),
)

slots.UrnIdentifier_identifier = Slot(
    uri=PID4CAT_MODEL.identifier,
    name="UrnIdentifier_identifier",
    curie=PID4CAT_MODEL.curie("identifier"),
    model_uri=PID4CAT_MODEL.UrnIdentifier_identifier,
    domain=UrnIdentifier,
    range=Optional[str],
    pattern=re.compile(r"^urn:[a-zA-Z0-9][a-zA-Z0-9-]{0,31}:[^\s]*$"),
)

slots.GtinIdentifier_identifier = Slot(
    uri=PID4CAT_MODEL.identifier,
    name="GtinIdentifier_identifier",
    curie=PID4CAT_MODEL.curie("identifier"),
    model_uri=PID4CAT_MODEL.GtinIdentifier_identifier,
    domain=GtinIdentifier,
    range=Optional[str],
    pattern=re.compile(r"^\d{13}$"),
)

slots.ExampleIdentifier_identifier = Slot(
    uri=PID4CAT_MODEL.identifier,
    name="ExampleIdentifier_identifier",
    curie=PID4CAT_MODEL.curie("identifier"),
    model_uri=PID4CAT_MODEL.ExampleIdentifier_identifier,
    domain=ExampleIdentifier,
    range=Optional[str],
    pattern=re.compile(r"^ex:.*$"),
)

slots.ExampleIdentifier_resolving_url = Slot(
    uri=PID4CAT_MODEL.resolving_url,
    name="ExampleIdentifier_resolving_url",
    curie=PID4CAT_MODEL.curie("resolving_url"),
    model_uri=PID4CAT_MODEL.ExampleIdentifier_resolving_url,
    domain=ExampleIdentifier,
    range=Optional[Union[str, URI]],
    pattern=re.compile(r"^https?:\/\/(.+\.)?example.(org|com)\/.*$"),
)
