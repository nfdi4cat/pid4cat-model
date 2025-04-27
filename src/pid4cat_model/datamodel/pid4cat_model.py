# Auto generated from pid4cat_model.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-04-29T23:35:15
# Schema: pid4cat-model
#
# id: https://w3id.org/nfdi4cat/pid4cat-model
# description: A LinkML model for persistent identifiers for resources in catalysis (pid4cat). pid4cat are handle based persistent identifiers (PIDs) for digital or physical resources used in the catalysis research process. PID-related metadata besides the obligatory landing page URL are stored directly in the handle records.
#   The model describes metadata for the PID itself and how to access the identified resource. It does not describe the resource itself with the exception of the resource category, which is a high-level description of what is identified by the pid4cat handle, e.g. a sample or a device.
# license: MIT

import re
from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from jsonasobj2 import as_dict
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.metamodelcore import empty_dict, empty_list
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str
from rdflib import URIRef

from linkml_runtime.utils.metamodelcore import URI, XSDDateTime

metamodel_version = "1.7.0"
version = "0.3.0.post17.dev0+93e88c2"

# Namespaces
DATACITE = CurieNamespace("DataCite", "https://purl.org/spar/datacite/")
DCAT = CurieNamespace("dcat", "https://www.w3.org/ns/dcat#")
DCTERMS = CurieNamespace("dcterms", "https://purl.org/dc/terms/")
LINKML = CurieNamespace("linkml", "https://w3id.org/linkml/")
MEDIATYPE = CurieNamespace("mediatype", "https://www.iana.org/assignments/media-types/")
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

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PID4CAT_MODEL["HandleAPIRecord"]
    class_class_curie: ClassVar[str] = "pid4cat_model:HandleAPIRecord"
    class_name: ClassVar[str] = "HandleAPIRecord"
    class_model_uri: ClassVar[URIRef] = PID4CAT_MODEL.HandleAPIRecord

    handle: Union[str, HandleAPIRecordHandle] = None
    values: Union[Union[dict, "HandleRecord"], list[Union[dict, "HandleRecord"]]] = None
    responseCode: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.handle):
            self.MissingRequiredField("handle")
        if not isinstance(self.handle, HandleAPIRecordHandle):
            self.handle = HandleAPIRecordHandle(self.handle)

        if self._is_empty(self.values):
            self.MissingRequiredField("values")
        self._normalize_inlined_as_dict(
            slot_name="values",
            slot_type=HandleRecord,
            key_name="timestamp",
            keyed=False,
        )

        if self.responseCode is not None and not isinstance(self.responseCode, int):
            self.responseCode = int(self.responseCode)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HandleRecord(YAMLRoot):
    """
    A base class for handle-data classes that represent a handle record in the same way as in the REST (json) API of a
    handle server.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PID4CAT_MODEL["HandleRecord"]
    class_class_curie: ClassVar[str] = "pid4cat_model:HandleRecord"
    class_name: ClassVar[str] = "HandleRecord"
    class_model_uri: ClassVar[URIRef] = PID4CAT_MODEL.HandleRecord

    timestamp: Union[str, XSDDateTime] = None
    type: str = None
    ttl: Optional[int] = 86400

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.timestamp):
            self.MissingRequiredField("timestamp")
        if not isinstance(self.timestamp, XSDDateTime):
            self.timestamp = XSDDateTime(self.timestamp)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_name)

        if self.ttl is not None and not isinstance(self.ttl, int):
            self.ttl = int(self.ttl)

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
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

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PID4CAT_MODEL["URL"]
    class_class_curie: ClassVar[str] = "pid4cat_model:URL"
    class_name: ClassVar[str] = "URL"
    class_model_uri: ClassVar[URIRef] = PID4CAT_MODEL.URL

    timestamp: Union[str, XSDDateTime] = None
    type: str = None
    index: int = None
    data: Union[dict, "HdlDataUrl"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.index):
            self.MissingRequiredField("index")
        if not isinstance(self.index, int):
            self.index = int(self.index)

        if self._is_empty(self.data):
            self.MissingRequiredField("data")
        if not isinstance(self.data, HdlDataUrl):
            self.data = HdlDataUrl(**as_dict(self.data))

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_name)


@dataclass(repr=False)
class HdlDataUrl(YAMLRoot):
    """
    The data class for the redirect url.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PID4CAT_MODEL["HdlDataUrl"]
    class_class_curie: ClassVar[str] = "pid4cat_model:HdlDataUrl"
    class_name: ClassVar[str] = "HdlDataUrl"
    class_model_uri: ClassVar[URIRef] = PID4CAT_MODEL.HdlDataUrl

    value: str = None
    format: Optional[str] = "string"

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, str):
            self.value = str(self.value)

        if self.format is not None and not isinstance(self.format, str):
            self.format = str(self.format)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EMAIL(HandleRecord):
    """
    The data element in the handle API for the contact email.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PID4CAT_MODEL["EMAIL"]
    class_class_curie: ClassVar[str] = "pid4cat_model:EMAIL"
    class_name: ClassVar[str] = "EMAIL"
    class_model_uri: ClassVar[URIRef] = PID4CAT_MODEL.EMAIL

    timestamp: Union[str, XSDDateTime] = None
    type: str = None
    index: int = None
    data: Union[dict, "HdlDataContact"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.index):
            self.MissingRequiredField("index")
        if not isinstance(self.index, int):
            self.index = int(self.index)

        if self._is_empty(self.data):
            self.MissingRequiredField("data")
        if not isinstance(self.data, HdlDataContact):
            self.data = HdlDataContact(**as_dict(self.data))

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_name)


@dataclass(repr=False)
class HdlDataContact(YAMLRoot):
    """
    The data class for the handle-record contact email.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PID4CAT_MODEL["HdlDataContact"]
    class_class_curie: ClassVar[str] = "pid4cat_model:HdlDataContact"
    class_name: ClassVar[str] = "HdlDataContact"
    class_model_uri: ClassVar[URIRef] = PID4CAT_MODEL.HdlDataContact

    value: str = None
    format: Optional[str] = "string"

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, str):
            self.value = str(self.value)

        if self.format is not None and not isinstance(self.format, str):
            self.format = str(self.format)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class STATUS(HandleRecord):
    """
    The data element in the handle API for the PID status information.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PID4CAT_MODEL["STATUS"]
    class_class_curie: ClassVar[str] = "pid4cat_model:STATUS"
    class_name: ClassVar[str] = "STATUS"
    class_model_uri: ClassVar[URIRef] = PID4CAT_MODEL.STATUS

    timestamp: Union[str, XSDDateTime] = None
    type: str = None
    index: int = None
    data: Union[dict, "HdlDataStatus"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.index):
            self.MissingRequiredField("index")
        if not isinstance(self.index, int):
            self.index = int(self.index)

        if self._is_empty(self.data):
            self.MissingRequiredField("data")
        if not isinstance(self.data, HdlDataStatus):
            self.data = HdlDataStatus(**as_dict(self.data))

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_name)


@dataclass(repr=False)
class HdlDataStatus(YAMLRoot):
    """
    The data class for the PID status information.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PID4CAT_MODEL["HdlDataStatus"]
    class_class_curie: ClassVar[str] = "pid4cat_model:HdlDataStatus"
    class_name: ClassVar[str] = "HdlDataStatus"
    class_model_uri: ClassVar[URIRef] = PID4CAT_MODEL.HdlDataStatus

    value: Union[str, "Pid4CatStatus"] = None
    format: Optional[str] = "string"

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, Pid4CatStatus):
            self.value = Pid4CatStatus(self.value)

        if self.format is not None and not isinstance(self.format, str):
            self.format = str(self.format)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SCHEMAVER(HandleRecord):
    """
    The data element in the handle API for the schema version.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PID4CAT_MODEL["SCHEMAVER"]
    class_class_curie: ClassVar[str] = "pid4cat_model:SCHEMAVER"
    class_name: ClassVar[str] = "SCHEMA_VER"
    class_model_uri: ClassVar[URIRef] = PID4CAT_MODEL.SCHEMAVER

    timestamp: Union[str, XSDDateTime] = None
    type: str = None
    index: int = None
    data: Union[dict, "HdlDataSchemaVer"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.index):
            self.MissingRequiredField("index")
        if not isinstance(self.index, int):
            self.index = int(self.index)

        if self._is_empty(self.data):
            self.MissingRequiredField("data")
        if not isinstance(self.data, HdlDataSchemaVer):
            self.data = HdlDataSchemaVer(**as_dict(self.data))

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_name)


@dataclass(repr=False)
class HdlDataSchemaVer(YAMLRoot):
    """
    The data class for the schema version.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PID4CAT_MODEL["HdlDataSchemaVer"]
    class_class_curie: ClassVar[str] = "pid4cat_model:HdlDataSchemaVer"
    class_name: ClassVar[str] = "HdlDataSchemaVer"
    class_model_uri: ClassVar[URIRef] = PID4CAT_MODEL.HdlDataSchemaVer

    value: str = None
    format: Optional[str] = "string"

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, str):
            self.value = str(self.value)

        if self.format is not None and not isinstance(self.format, str):
            self.format = str(self.format)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class METADATALICENSE(HandleRecord):
    """
    The data element in the handle API for the PID metadata license.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PID4CAT_MODEL["METADATALICENSE"]
    class_class_curie: ClassVar[str] = "pid4cat_model:METADATALICENSE"
    class_name: ClassVar[str] = "METADATA_LICENSE"
    class_model_uri: ClassVar[URIRef] = PID4CAT_MODEL.METADATALICENSE

    timestamp: Union[str, XSDDateTime] = None
    type: str = None
    index: int = None
    data: Union[dict, "HdlDataLicense"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.index):
            self.MissingRequiredField("index")
        if not isinstance(self.index, int):
            self.index = int(self.index)

        if self._is_empty(self.data):
            self.MissingRequiredField("data")
        if not isinstance(self.data, HdlDataLicense):
            self.data = HdlDataLicense(**as_dict(self.data))

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_name)


@dataclass(repr=False)
class HdlDataLicense(YAMLRoot):
    """
    The data class for the PID metadata license.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PID4CAT_MODEL["HdlDataLicense"]
    class_class_curie: ClassVar[str] = "pid4cat_model:HdlDataLicense"
    class_name: ClassVar[str] = "HdlDataLicense"
    class_model_uri: ClassVar[URIRef] = PID4CAT_MODEL.HdlDataLicense

    value: str = None
    format: Optional[str] = "string"

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, str):
            self.value = str(self.value)

        if self.format is not None and not isinstance(self.format, str):
            self.format = str(self.format)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RESOURCE(HandleRecord):
    """
    The data element in the handle API for the resource info.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PID4CAT_MODEL["RESOURCE"]
    class_class_curie: ClassVar[str] = "pid4cat_model:RESOURCE"
    class_name: ClassVar[str] = "RESOURCE"
    class_model_uri: ClassVar[URIRef] = PID4CAT_MODEL.RESOURCE

    timestamp: Union[str, XSDDateTime] = None
    type: str = None
    index: int = None
    data: Union[dict, "HdlDataResourceInfo"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.index):
            self.MissingRequiredField("index")
        if not isinstance(self.index, int):
            self.index = int(self.index)

        if self._is_empty(self.data):
            self.MissingRequiredField("data")
        if not isinstance(self.data, HdlDataResourceInfo):
            self.data = HdlDataResourceInfo(**as_dict(self.data))

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_name)


@dataclass(repr=False)
class HdlDataResourceInfo(YAMLRoot):
    """
    The data class for the resource info.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PID4CAT_MODEL["HdlDataResourceInfo"]
    class_class_curie: ClassVar[str] = "pid4cat_model:HdlDataResourceInfo"
    class_name: ClassVar[str] = "HdlDataResourceInfo"
    class_model_uri: ClassVar[URIRef] = PID4CAT_MODEL.HdlDataResourceInfo

    value: Union[dict, "ResourceInfo"] = None
    format: Optional[str] = "string"

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, ResourceInfo):
            self.value = ResourceInfo(**as_dict(self.value))

        if self.format is not None and not isinstance(self.format, str):
            self.format = str(self.format)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RELATED(HandleRecord):
    """
    The data element in the handle API for related identifiers.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PID4CAT_MODEL["RELATED"]
    class_class_curie: ClassVar[str] = "pid4cat_model:RELATED"
    class_name: ClassVar[str] = "RELATED"
    class_model_uri: ClassVar[URIRef] = PID4CAT_MODEL.RELATED

    timestamp: Union[str, XSDDateTime] = None
    type: str = None
    index: int = None
    data: Union[dict, "HdlDataRelated"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.index):
            self.MissingRequiredField("index")
        if not isinstance(self.index, int):
            self.index = int(self.index)

        if self._is_empty(self.data):
            self.MissingRequiredField("data")
        if not isinstance(self.data, HdlDataRelated):
            self.data = HdlDataRelated(**as_dict(self.data))

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_name)


@dataclass(repr=False)
class HdlDataRelated(YAMLRoot):
    """
    The data class for related identifiers.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PID4CAT_MODEL["HdlDataRelated"]
    class_class_curie: ClassVar[str] = "pid4cat_model:HdlDataRelated"
    class_name: ClassVar[str] = "HdlDataRelated"
    class_model_uri: ClassVar[URIRef] = PID4CAT_MODEL.HdlDataRelated

    format: Optional[str] = "string"
    value: Optional[
        Union[Union[dict, "Pid4CatRelation"], list[Union[dict, "Pid4CatRelation"]]]
    ] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
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
class CHANGES(HandleRecord):
    """
    The data element in the handle API for the change log.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PID4CAT_MODEL["CHANGES"]
    class_class_curie: ClassVar[str] = "pid4cat_model:CHANGES"
    class_name: ClassVar[str] = "CHANGES"
    class_model_uri: ClassVar[URIRef] = PID4CAT_MODEL.CHANGES

    timestamp: Union[str, XSDDateTime] = None
    type: str = None
    index: int = None
    data: Union[dict, "HdlDataLog"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.index):
            self.MissingRequiredField("index")
        if not isinstance(self.index, int):
            self.index = int(self.index)

        if self._is_empty(self.data):
            self.MissingRequiredField("data")
        if not isinstance(self.data, HdlDataLog):
            self.data = HdlDataLog(**as_dict(self.data))

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_name)


@dataclass(repr=False)
class HdlDataLog(YAMLRoot):
    """
    The data class for the change log.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PID4CAT_MODEL["HdlDataLog"]
    class_class_curie: ClassVar[str] = "pid4cat_model:HdlDataLog"
    class_name: ClassVar[str] = "HdlDataLog"
    class_model_uri: ClassVar[URIRef] = PID4CAT_MODEL.HdlDataLog

    value: Union[Union[dict, "LogRecord"], list[Union[dict, "LogRecord"]]] = None
    format: Optional[str] = "string"

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        self._normalize_inlined_as_dict(
            slot_name="value", slot_type=LogRecord, key_name="datetime_log", keyed=False
        )

        if self.format is not None and not isinstance(self.format, str):
            self.format = str(self.format)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HandleRecordContainer(YAMLRoot):
    """
    A container for all HandleRecords.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PID4CAT_MODEL["HandleRecordContainer"]
    class_class_curie: ClassVar[str] = "pid4cat_model:HandleRecordContainer"
    class_name: ClassVar[str] = "HandleRecordContainer"
    class_model_uri: ClassVar[URIRef] = PID4CAT_MODEL.HandleRecordContainer

    contains_pids: Optional[
        Union[
            dict[Union[str, HandleAPIRecordHandle], Union[dict, HandleAPIRecord]],
            list[Union[dict, HandleAPIRecord]],
        ]
    ] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
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
    Data class for a relation to another resource identified by a pid4cat handle or another PID type.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PID4CAT_MODEL["Pid4CatRelation"]
    class_class_curie: ClassVar[str] = "pid4cat_model:Pid4CatRelation"
    class_name: ClassVar[str] = "Pid4CatRelation"
    class_model_uri: ClassVar[URIRef] = PID4CAT_MODEL.Pid4CatRelation

    relation_type: Optional[Union[str, "RelationType"]] = None
    related_identifier: Optional[Union[dict, "RelatedIdentifier"]] = None
    datetime_log: Optional[Union[str, XSDDateTime]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
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
    Data class to hold information about the resource and its representation.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PID4CAT_MODEL["ResourceInfo"]
    class_class_curie: ClassVar[str] = "pid4cat_model:ResourceInfo"
    class_name: ClassVar[str] = "ResourceInfo"
    class_model_uri: ClassVar[URIRef] = PID4CAT_MODEL.ResourceInfo

    resource_category: Union[str, "ResourceCategory"] = None
    representation_variants: Union[
        Union[dict, "RepresentationVariant"], list[Union[dict, "RepresentationVariant"]]
    ] = None
    label: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.resource_category):
            self.MissingRequiredField("resource_category")
        if not isinstance(self.resource_category, ResourceCategory):
            self.resource_category = ResourceCategory(self.resource_category)

        if self._is_empty(self.representation_variants):
            self.MissingRequiredField("representation_variants")
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

        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LogRecord(YAMLRoot):
    """
    Data class for a change log of modification made on a pid4cat handle record starting from its registration.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PID4CAT_MODEL["LogRecord"]
    class_class_curie: ClassVar[str] = "pid4cat_model:LogRecord"
    class_name: ClassVar[str] = "LogRecord"
    class_model_uri: ClassVar[URIRef] = PID4CAT_MODEL.LogRecord

    datetime_log: Union[str, XSDDateTime] = None
    has_agent: Union[dict, "Agent"] = None
    changed_field: Union[str, "ChangeLogField"] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.datetime_log):
            self.MissingRequiredField("datetime_log")
        if not isinstance(self.datetime_log, XSDDateTime):
            self.datetime_log = XSDDateTime(self.datetime_log)

        if self._is_empty(self.has_agent):
            self.MissingRequiredField("has_agent")
        if not isinstance(self.has_agent, Agent):
            self.has_agent = Agent(**as_dict(self.has_agent))

        if self._is_empty(self.changed_field):
            self.MissingRequiredField("changed_field")
        if not isinstance(self.changed_field, ChangeLogField):
            self.changed_field = ChangeLogField(self.changed_field)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Agent(YAMLRoot):
    """
    Data class for a person who plays a role relative to PID creation or curation.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV["Agent"]
    class_class_curie: ClassVar[str] = "prov:Agent"
    class_name: ClassVar[str] = "Agent"
    class_model_uri: ClassVar[URIRef] = PID4CAT_MODEL.Agent

    name: str = None
    email_address: str = None
    role: Union[str, "Pid4CatAgentRole"] = None
    orcid: Optional[str] = None
    affiliation_ror: Optional[Union[str, URI]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.email_address):
            self.MissingRequiredField("email_address")
        if not isinstance(self.email_address, str):
            self.email_address = str(self.email_address)

        if self._is_empty(self.role):
            self.MissingRequiredField("role")
        if not isinstance(self.role, Pid4CatAgentRole):
            self.role = Pid4CatAgentRole(self.role)

        if self.orcid is not None and not isinstance(self.orcid, str):
            self.orcid = str(self.orcid)

        if self.affiliation_ror is not None and not isinstance(
            self.affiliation_ror, URI
        ):
            self.affiliation_ror = URI(self.affiliation_ror)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RepresentationVariant(YAMLRoot):
    """
    Data class for representations of the resource in other media types than text/html which is the default for
    landing_page_url.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PID4CAT_MODEL["RepresentationVariant"]
    class_class_curie: ClassVar[str] = "pid4cat_model:RepresentationVariant"
    class_name: ClassVar[str] = "RepresentationVariant"
    class_model_uri: ClassVar[URIRef] = PID4CAT_MODEL.RepresentationVariant

    variant_url: Optional[Union[str, URI]] = None
    media_type: Optional[Union[str, "MediaTypesEnum"]] = None
    encoding_format: Optional[str] = None
    size: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.variant_url is not None and not isinstance(self.variant_url, URI):
            self.variant_url = URI(self.variant_url)

        if self.media_type is not None and not isinstance(
            self.media_type, MediaTypesEnum
        ):
            self.media_type = MediaTypesEnum(self.media_type)

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
    A base class for all types of related identifiers.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PID4CAT_MODEL["RelatedIdentifier"]
    class_class_curie: ClassVar[str] = "pid4cat_model:RelatedIdentifier"
    class_name: ClassVar[str] = "RelatedIdentifier"
    class_model_uri: ClassVar[URIRef] = PID4CAT_MODEL.RelatedIdentifier

    type: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_name)

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
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

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PID4CAT_MODEL["PurlIdentifier"]
    class_class_curie: ClassVar[str] = "pid4cat_model:PurlIdentifier"
    class_name: ClassVar[str] = "PurlIdentifier"
    class_model_uri: ClassVar[URIRef] = PID4CAT_MODEL.PurlIdentifier

    type: str = None
    resolving_url: Union[str, URI] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.resolving_url):
            self.MissingRequiredField("resolving_url")
        if not isinstance(self.resolving_url, URI):
            self.resolving_url = URI(self.resolving_url)

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_name)


@dataclass(repr=False)
class DoiIdentifier(RelatedIdentifier):
    """
    A digital object identifier (DOI).
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PID4CAT_MODEL["DoiIdentifier"]
    class_class_curie: ClassVar[str] = "pid4cat_model:DoiIdentifier"
    class_name: ClassVar[str] = "DoiIdentifier"
    class_model_uri: ClassVar[URIRef] = PID4CAT_MODEL.DoiIdentifier

    type: str = None
    resolving_url: Union[str, URI] = None
    identifier: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.resolving_url):
            self.MissingRequiredField("resolving_url")
        if not isinstance(self.resolving_url, URI):
            self.resolving_url = URI(self.resolving_url)

        if self.identifier is not None and not isinstance(self.identifier, str):
            self.identifier = str(self.identifier)

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_name)


@dataclass(repr=False)
class HandleIdentifier(RelatedIdentifier):
    """
    A handle identifier.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PID4CAT_MODEL["HandleIdentifier"]
    class_class_curie: ClassVar[str] = "pid4cat_model:HandleIdentifier"
    class_name: ClassVar[str] = "HandleIdentifier"
    class_model_uri: ClassVar[URIRef] = PID4CAT_MODEL.HandleIdentifier

    type: str = None
    resolving_url: Union[str, URI] = None
    identifier: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.resolving_url):
            self.MissingRequiredField("resolving_url")
        if not isinstance(self.resolving_url, URI):
            self.resolving_url = URI(self.resolving_url)

        if self.identifier is not None and not isinstance(self.identifier, str):
            self.identifier = str(self.identifier)

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_name)


@dataclass(repr=False)
class ArkIdentifier(RelatedIdentifier):
    """
    An ARK (Archival Resource Key).
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PID4CAT_MODEL["ArkIdentifier"]
    class_class_curie: ClassVar[str] = "pid4cat_model:ArkIdentifier"
    class_name: ClassVar[str] = "ArkIdentifier"
    class_model_uri: ClassVar[URIRef] = PID4CAT_MODEL.ArkIdentifier

    type: str = None
    resolving_url: Union[str, URI] = None
    identifier: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.resolving_url):
            self.MissingRequiredField("resolving_url")
        if not isinstance(self.resolving_url, URI):
            self.resolving_url = URI(self.resolving_url)

        if self.identifier is not None and not isinstance(self.identifier, str):
            self.identifier = str(self.identifier)

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_name)


@dataclass(repr=False)
class UrnIdentifier(RelatedIdentifier):
    """
    A URN (Uniform Resource Name).
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PID4CAT_MODEL["UrnIdentifier"]
    class_class_curie: ClassVar[str] = "pid4cat_model:UrnIdentifier"
    class_name: ClassVar[str] = "UrnIdentifier"
    class_model_uri: ClassVar[URIRef] = PID4CAT_MODEL.UrnIdentifier

    type: str = None
    identifier: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.identifier):
            self.MissingRequiredField("identifier")
        if not isinstance(self.identifier, str):
            self.identifier = str(self.identifier)

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_name)


@dataclass(repr=False)
class GtinIdentifier(RelatedIdentifier):
    """
    A Global Trade Item Number (GTIN) previously called European Article Number (EAN) often encoded as EAN13 barcode.
    The identifier is used to identify products. GTINs don't have a resolvable URL.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PID4CAT_MODEL["GtinIdentifier"]
    class_class_curie: ClassVar[str] = "pid4cat_model:GtinIdentifier"
    class_name: ClassVar[str] = "GtinIdentifier"
    class_model_uri: ClassVar[URIRef] = PID4CAT_MODEL.GtinIdentifier

    type: str = None
    identifier: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.identifier):
            self.MissingRequiredField("identifier")
        if not isinstance(self.identifier, str):
            self.identifier = str(self.identifier)

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_name)


@dataclass(repr=False)
class ExampleIdentifier(RelatedIdentifier):
    """
    An example.org test identifier.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PID4CAT_MODEL["ExampleIdentifier"]
    class_class_curie: ClassVar[str] = "pid4cat_model:ExampleIdentifier"
    class_name: ClassVar[str] = "ExampleIdentifier"
    class_model_uri: ClassVar[URIRef] = PID4CAT_MODEL.ExampleIdentifier

    type: str = None
    identifier: Optional[str] = None
    resolving_url: Optional[Union[str, URI]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.identifier is not None and not isinstance(self.identifier, str):
            self.identifier = str(self.identifier)

        if self.resolving_url is not None and not isinstance(self.resolving_url, URI):
            self.resolving_url = URI(self.resolving_url)

        super().__post_init__(**kwargs)
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_name)


@dataclass(repr=False)
class Pid4CatRecord(YAMLRoot):
    """
    A class representing pid4cat identifiers with its metadata as objects. This is a neutral object-oriented
    representation that does not mirror the record structure of the handle system but is provided as representation
    that is more convenient to use in programming languages.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PID4CAT_MODEL["Pid4CatRecord"]
    class_class_curie: ClassVar[str] = "pid4cat_model:Pid4CatRecord"
    class_name: ClassVar[str] = "Pid4CatRecord"
    class_model_uri: ClassVar[URIRef] = PID4CAT_MODEL.Pid4CatRecord

    landing_page_url: str = None
    status: Union[str, "Pid4CatStatus"] = None
    schema_version: str = None
    metadata_license: str = None
    curation_contact: str = None
    resource_info: Union[dict, ResourceInfo] = None
    change_log: Union[Union[dict, LogRecord], list[Union[dict, LogRecord]]] = None
    related_identifiers: Optional[
        Union[Union[dict, Pid4CatRelation], list[Union[dict, Pid4CatRelation]]]
    ] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.landing_page_url):
            self.MissingRequiredField("landing_page_url")
        if not isinstance(self.landing_page_url, str):
            self.landing_page_url = str(self.landing_page_url)

        if self._is_empty(self.status):
            self.MissingRequiredField("status")
        if not isinstance(self.status, Pid4CatStatus):
            self.status = Pid4CatStatus(self.status)

        if self._is_empty(self.schema_version):
            self.MissingRequiredField("schema_version")
        if not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        if self._is_empty(self.metadata_license):
            self.MissingRequiredField("metadata_license")
        if not isinstance(self.metadata_license, str):
            self.metadata_license = str(self.metadata_license)

        if self._is_empty(self.curation_contact):
            self.MissingRequiredField("curation_contact")
        if not isinstance(self.curation_contact, str):
            self.curation_contact = str(self.curation_contact)

        if self._is_empty(self.resource_info):
            self.MissingRequiredField("resource_info")
        if not isinstance(self.resource_info, ResourceInfo):
            self.resource_info = ResourceInfo(**as_dict(self.resource_info))

        if self._is_empty(self.change_log):
            self.MissingRequiredField("change_log")
        self._normalize_inlined_as_dict(
            slot_name="change_log",
            slot_type=LogRecord,
            key_name="datetime_log",
            keyed=False,
        )

        if not isinstance(self.related_identifiers, list):
            self.related_identifiers = (
                [self.related_identifiers]
                if self.related_identifiers is not None
                else []
            )
        self.related_identifiers = [
            v if isinstance(v, Pid4CatRelation) else Pid4CatRelation(**as_dict(v))
            for v in self.related_identifiers
        ]

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
        description="""The resource has a version. This is useful to express the relation between a abstract resource to its versioned instances, for example, \"Python has_version Python 3.12\".""",
        meaning=VOC4CAT["0005027"],
    )
    IS_VERSION_OF = PermissibleValue(
        text="IS_VERSION_OF",
        description="""The resource is a version of another resource. This is useful to refer to an abstract resource that has different versions, for example, \"Python 3.12 is a version of Python\".""",
        meaning=VOC4CAT["0005028"],
    )
    IS_NEW_VERSION_OF = PermissibleValue(
        text="IS_NEW_VERSION_OF",
        description="""The resource is a new version of another versioned resource. This is useful to refer between versioned resources, for example, \"Python 3.12.1 is_new_version_of Python 3.12.0\".""",
        meaning=VOC4CAT["0005029"],
    )
    IS_PREVIOUS_VERSION_OF = PermissibleValue(
        text="IS_PREVIOUS_VERSION_OF",
        description="""The resource is a previous version of another versioned resource. This is useful to refer between versioned resources, for example, \"Python 3.12.0 is_previous_version_of Python 3.12.1\".""",
        meaning=VOC4CAT["0005030"],
    )
    IS_PART_OF = PermissibleValue(
        text="IS_PART_OF",
        description="""The resource is part of another resource. This relation applies to container-contained type relationships. If the relation refers to publishing one resource as part of another resource, use \"IS_PUBLISHED_IN\" instead. If the relation refers to a versioned resource and non-versioned resource, use \"IS_VERSION_OF\" instead.""",
        meaning=VOC4CAT["0005031"],
    )
    HAS_PART = PermissibleValue(
        text="HAS_PART",
        description="""The resource has part another resource. This relation applies to container-contained type relationships. If the relation refers to publishing one resource as part of another resource, \"IS_PUBLISHED_IN\" instead. If the relation refers to a versioned resource and non-versioned resource, use \"HAS_VERSION\" instead.""",
        meaning=VOC4CAT["0005032"],
    )
    IS_PUBLISHED_IN = PermissibleValue(
        text="IS_PUBLISHED_IN",
        description="""The resource is published in another resource. A resource A that is_published_in a resource B is independent from other resources published in the same resource B.""",
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
        description="""The resource is compiled by another resource. Resources may be text or software. The compiler may be a computer program or a person.""",
        meaning=VOC4CAT["0005038"],
    )
    COMPILES = PermissibleValue(
        text="COMPILES",
        description="""The resource compiles another resource. Resources may be text or software. The compiler may be a computer program or a person.""",
        meaning=VOC4CAT["0005039"],
    )
    IS_VARIANT_FORM_OF = PermissibleValue(
        text="IS_VARIANT_FORM_OF",
        description="""The resource is variant form of another resource. This may be used e.g. for relating architecture-specific builds of a a software program to a source-code release. It may also be used to express the relation between data in different formats (e.g. PNG, JPEG) of the same image.""",
        meaning=VOC4CAT["0005040"],
    )
    IS_ORIGINAL_FORM_OF = PermissibleValue(
        text="IS_ORIGINAL_FORM_OF",
        description="""The resource is original form of another resource. This may be used e.g. for relating architecture-specific builds of a a software program to a source-code release. It may also be used to express the relation between data in different formats (e.g. PNG, JPEG) of the same image.""",
        meaning=VOC4CAT["0005041"],
    )
    IS_IDENTICAL_TO = PermissibleValue(
        text="IS_IDENTICAL_TO",
        description="""The resource is identical to another resource. May be used to indicate the relationship between an exact copy of a resource that is published at another location.""",
        meaning=VOC4CAT["0005042"],
    )
    IS_DERIVED_FROM = PermissibleValue(
        text="IS_DERIVED_FROM",
        description="""The resource is derived from another resource. This may be used for relating a new dataset created by data processing to its original source dataset. For samples it may express the relation between the original sample and another sample derived from it by physical or chemical treatment.""",
        meaning=VOC4CAT["0005043"],
    )
    IS_SOURCE_OF = PermissibleValue(
        text="IS_SOURCE_OF",
        description="""The resource is source of another resource. This may be used for example to express the relation between a source dataset and a new dataset derived from it by data processing. For samples it may express the relation between a sample processed by physical or chemical treatment and the original sample.""",
        meaning=VOC4CAT["0005044"],
    )
    IS_COLLECTED_BY = PermissibleValue(
        text="IS_COLLECTED_BY",
        description="""The resource is collected by another resource. May be used to indicate the relationship between a dataset and an instrument that is used to collect, measure, obtain, or observe data.""",
        meaning=VOC4CAT["0005045"],
    )
    COLLECTS = PermissibleValue(
        text="COLLECTS",
        description="""The resource collects another resource. May be used to indicate the relationship between an instrument and where it has been used to collect, measure, obtain, or observe data.""",
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
    CONFORMS_TO = PermissibleValue(
        text="CONFORMS_TO",
        description="""An established standard to which the described resource conforms. This relation should be used to indicate the model, schema, ontology, or profile that the resource content conforms to.""",
        meaning=VOC4CAT["0005059"],
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


class MediaTypesEnum(EnumDefinitionImpl):
    """
    IANA media types are used to specify the type of data.
    """

    _defn = EnumDefinition(
        name="MediaTypesEnum",
        description="IANA media types are used to specify the type of data.",
    )

    @classmethod
    def _addvals(cls):
        setattr(
            cls,
            "application/epub+zip",
            PermissibleValue(
                text="application/epub+zip",
                description="For data in Electronic Publication Format (EPUB).",
                meaning=MEDIATYPE["application/epub+zip"],
            ),
        )
        setattr(
            cls,
            "application/json",
            PermissibleValue(
                text="application/json",
                description="For data in JavaScript Object Notation (JSON).",
                meaning=MEDIATYPE["application/json"],
            ),
        )
        setattr(
            cls,
            "application/ld+json",
            PermissibleValue(
                text="application/ld+json",
                description="For data in Linked Data json (JSON-LD).",
                meaning=MEDIATYPE["application/ld+json"],
            ),
        )
        setattr(
            cls,
            "application/octet-stream",
            PermissibleValue(
                text="application/octet-stream",
                description="For binary data.",
                meaning=MEDIATYPE["application/octet-stream"],
            ),
        )
        setattr(
            cls,
            "application/pdf",
            PermissibleValue(
                text="application/pdf",
                description="For data in Portable Document Format (PDF).",
                meaning=MEDIATYPE["application/pdf"],
            ),
        )
        setattr(
            cls,
            "application/vnd.eln+zip",
            PermissibleValue(
                text="application/vnd.eln+zip",
                description="For data in ELN ZIP format.",
                meaning=MEDIATYPE["application/vnd.eln+zip"],
            ),
        )
        setattr(
            cls,
            "application/vnd.openxmlformats-officedocument.presentationml.presentation",
            PermissibleValue(
                text="application/vnd.openxmlformats-officedocument.presentationml.presentation",
                description="For data in PowerPoint pptx format.",
                meaning=MEDIATYPE[
                    "application/vnd.openxmlformats-officedocument.presentationml.presentation"
                ],
            ),
        )
        setattr(
            cls,
            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            PermissibleValue(
                text="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                description="For data in Excel xlsx format.",
                meaning=MEDIATYPE[
                    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                ],
            ),
        )
        setattr(
            cls,
            "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            PermissibleValue(
                text="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                description="For data in Word docx format.",
                meaning=MEDIATYPE[
                    "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                ],
            ),
        )
        setattr(
            cls,
            "application/xml",
            PermissibleValue(
                text="application/xml",
                description="For generic XML data.",
                meaning=MEDIATYPE["application/xml"],
            ),
        )
        setattr(
            cls,
            "application/yaml",
            PermissibleValue(
                text="application/yaml",
                description="For YAML data.",
                meaning=MEDIATYPE["application/yaml"],
            ),
        )
        setattr(
            cls,
            "application/zip",
            PermissibleValue(
                text="application/zip",
                description="For zip archives.",
                meaning=MEDIATYPE["application/zip"],
            ),
        )
        setattr(
            cls,
            "image/gif",
            PermissibleValue(
                text="image/gif",
                description="For GIF images.",
                meaning=MEDIATYPE["image/gif"],
            ),
        )
        setattr(
            cls,
            "image/jpeg",
            PermissibleValue(
                text="image/jpeg",
                description="For JPEG images.",
                meaning=MEDIATYPE["image/jpeg"],
            ),
        )
        setattr(
            cls,
            "image/png",
            PermissibleValue(
                text="image/png",
                description="For PNG images.",
                meaning=MEDIATYPE["image/png"],
            ),
        )
        setattr(
            cls,
            "image/svg+xml",
            PermissibleValue(
                text="image/svg+xml",
                description="For SVG images.",
                meaning=MEDIATYPE["image/svg+xml"],
            ),
        )
        setattr(
            cls,
            "image/tiff",
            PermissibleValue(
                text="image/tiff",
                description="For TIFF images.",
                meaning=MEDIATYPE["image/tiff"],
            ),
        )
        setattr(
            cls,
            "image/webp",
            PermissibleValue(
                text="image/webp",
                description="For WebP images.",
                meaning=MEDIATYPE["image/webp"],
            ),
        )
        setattr(
            cls,
            "text/csv",
            PermissibleValue(
                text="text/csv",
                description="For data in comma-separated values (CSV) format.",
                meaning=MEDIATYPE["text/csv"],
            ),
        )
        setattr(
            cls,
            "text/html",
            PermissibleValue(
                text="text/html",
                description="For html web pages.",
                meaning=MEDIATYPE["text/html"],
            ),
        )
        setattr(
            cls,
            "text/javascript",
            PermissibleValue(
                text="text/javascript",
                description="For JavaScript code.",
                meaning=MEDIATYPE["text/javascript"],
            ),
        )
        setattr(
            cls,
            "text/markdown",
            PermissibleValue(
                text="text/markdown",
                description="For data in markdown text format.",
                meaning=MEDIATYPE["text/markdown"],
            ),
        )
        setattr(
            cls,
            "text/plain",
            PermissibleValue(
                text="text/plain",
                description="For plain text data (default text media type).",
                meaning=MEDIATYPE["text/plain"],
            ),
        )
        setattr(
            cls,
            "text/tab-separated-values",
            PermissibleValue(
                text="text/tab-separated-values",
                description="For data in tab-separated values (TSV) format.",
                meaning=MEDIATYPE["text/tab-separated-values"],
            ),
        )
        setattr(
            cls,
            "text/turtle",
            PermissibleValue(
                text="text/turtle",
                description="For data in turtle format.",
                meaning=MEDIATYPE["text/turtle"],
            ),
        )
        setattr(
            cls,
            "text/xml",
            PermissibleValue(
                text="text/xml",
                description="For XML data.",
                meaning=MEDIATYPE["text/xml"],
            ),
        )
        setattr(
            cls,
            "video/mp4",
            PermissibleValue(
                text="video/mp4",
                description="For mp4 video files.",
                meaning=MEDIATYPE["video/mp4"],
            ),
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
    range=Optional[Union[Union[dict, HandleRecord], list[Union[dict, HandleRecord]]]],
)

slots.timestamp = Slot(
    uri=PID4CAT_MODEL.timestamp,
    name="timestamp",
    curie=PID4CAT_MODEL.curie("timestamp"),
    model_uri=PID4CAT_MODEL.timestamp,
    domain=None,
    range=Optional[Union[str, XSDDateTime]],
)

slots.ttl = Slot(
    uri=PID4CAT_MODEL.ttl,
    name="ttl",
    curie=PID4CAT_MODEL.curie("ttl"),
    model_uri=PID4CAT_MODEL.ttl,
    domain=None,
    range=Optional[int],
)

slots.type = Slot(
    uri=PID4CAT_MODEL.type,
    name="type",
    curie=PID4CAT_MODEL.curie("type"),
    model_uri=PID4CAT_MODEL.type,
    domain=None,
    range=Optional[str],
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
            Union[dict, RepresentationVariant], list[Union[dict, RepresentationVariant]]
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

slots.email_address = Slot(
    uri=PID4CAT_MODEL.email_address,
    name="email_address",
    curie=PID4CAT_MODEL.curie("email_address"),
    model_uri=PID4CAT_MODEL.email_address,
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
    range=Optional[Union[str, "MediaTypesEnum"]],
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

slots.variant_url = Slot(
    uri=PID4CAT_MODEL.variant_url,
    name="variant_url",
    curie=PID4CAT_MODEL.curie("variant_url"),
    model_uri=PID4CAT_MODEL.variant_url,
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

slots.landing_page_url = Slot(
    uri=PID4CAT_MODEL.landing_page_url,
    name="landing_page_url",
    curie=PID4CAT_MODEL.curie("landing_page_url"),
    model_uri=PID4CAT_MODEL.landing_page_url,
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

slots.schema_version = Slot(
    uri=PID4CAT_MODEL.schema_version,
    name="schema_version",
    curie=PID4CAT_MODEL.curie("schema_version"),
    model_uri=PID4CAT_MODEL.schema_version,
    domain=None,
    range=Optional[str],
)

slots.metadata_license = Slot(
    uri=PID4CAT_MODEL.metadata_license,
    name="metadata_license",
    curie=PID4CAT_MODEL.curie("metadata_license"),
    model_uri=PID4CAT_MODEL.metadata_license,
    domain=None,
    range=Optional[str],
)

slots.curation_contact = Slot(
    uri=PID4CAT_MODEL.curation_contact,
    name="curation_contact",
    curie=PID4CAT_MODEL.curie("curation_contact"),
    model_uri=PID4CAT_MODEL.curation_contact,
    domain=None,
    range=Optional[str],
)

slots.resource_info = Slot(
    uri=PID4CAT_MODEL.resource_info,
    name="resource_info",
    curie=PID4CAT_MODEL.curie("resource_info"),
    model_uri=PID4CAT_MODEL.resource_info,
    domain=None,
    range=Optional[Union[dict, ResourceInfo]],
)

slots.related_identifiers = Slot(
    uri=PID4CAT_MODEL.related_identifiers,
    name="related_identifiers",
    curie=PID4CAT_MODEL.curie("related_identifiers"),
    model_uri=PID4CAT_MODEL.related_identifiers,
    domain=None,
    range=Optional[
        Union[Union[dict, Pid4CatRelation], list[Union[dict, Pid4CatRelation]]]
    ],
)

slots.change_log = Slot(
    uri=PID4CAT_MODEL.change_log,
    name="change_log",
    curie=PID4CAT_MODEL.curie("change_log"),
    model_uri=PID4CAT_MODEL.change_log,
    domain=None,
    range=Optional[Union[dict, LogRecord]],
)

slots.handleRecordContainer__contains_pids = Slot(
    uri=PID4CAT_MODEL.contains_pids,
    name="handleRecordContainer__contains_pids",
    curie=PID4CAT_MODEL.curie("contains_pids"),
    model_uri=PID4CAT_MODEL.handleRecordContainer__contains_pids,
    domain=None,
    range=Optional[
        Union[
            dict[Union[str, HandleAPIRecordHandle], Union[dict, HandleAPIRecord]],
            list[Union[dict, HandleAPIRecord]],
        ]
    ],
)

slots.relatedIdentifier__type = Slot(
    uri=PID4CAT_MODEL.type,
    name="relatedIdentifier__type",
    curie=PID4CAT_MODEL.curie("type"),
    model_uri=PID4CAT_MODEL.relatedIdentifier__type,
    domain=None,
    range=str,
)

slots.HandleAPIRecord_handle = Slot(
    uri=PID4CAT_MODEL.handle,
    name="HandleAPIRecord_handle",
    curie=PID4CAT_MODEL.curie("handle"),
    model_uri=PID4CAT_MODEL.HandleAPIRecord_handle,
    domain=HandleAPIRecord,
    range=Union[str, HandleAPIRecordHandle],
    pattern=re.compile(r"^\d{2}\.T?\d{4,}\/.*$"),
)

slots.HandleAPIRecord_values = Slot(
    uri=PID4CAT_MODEL.values,
    name="HandleAPIRecord_values",
    curie=PID4CAT_MODEL.curie("values"),
    model_uri=PID4CAT_MODEL.HandleAPIRecord_values,
    domain=HandleAPIRecord,
    range=Union[Union[dict, "HandleRecord"], list[Union[dict, "HandleRecord"]]],
)

slots.HandleRecord_timestamp = Slot(
    uri=PID4CAT_MODEL.timestamp,
    name="HandleRecord_timestamp",
    curie=PID4CAT_MODEL.curie("timestamp"),
    model_uri=PID4CAT_MODEL.HandleRecord_timestamp,
    domain=HandleRecord,
    range=Union[str, XSDDateTime],
)

slots.HandleRecord_ttl = Slot(
    uri=PID4CAT_MODEL.ttl,
    name="HandleRecord_ttl",
    curie=PID4CAT_MODEL.curie("ttl"),
    model_uri=PID4CAT_MODEL.HandleRecord_ttl,
    domain=HandleRecord,
    range=Optional[int],
)

slots.HandleRecord_type = Slot(
    uri=PID4CAT_MODEL.type,
    name="HandleRecord_type",
    curie=PID4CAT_MODEL.curie("type"),
    model_uri=PID4CAT_MODEL.HandleRecord_type,
    domain=HandleRecord,
    range=str,
)

slots.URL_index = Slot(
    uri=PID4CAT_MODEL.index,
    name="URL_index",
    curie=PID4CAT_MODEL.curie("index"),
    model_uri=PID4CAT_MODEL.URL_index,
    domain=URL,
    range=int,
)

slots.URL_data = Slot(
    uri=PID4CAT_MODEL.data,
    name="URL_data",
    curie=PID4CAT_MODEL.curie("data"),
    model_uri=PID4CAT_MODEL.URL_data,
    domain=URL,
    range=Union[dict, "HdlDataUrl"],
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
    range=str,
    pattern=re.compile(r"^https?:\/\/.*$"),
)

slots.EMAIL_index = Slot(
    uri=PID4CAT_MODEL.index,
    name="EMAIL_index",
    curie=PID4CAT_MODEL.curie("index"),
    model_uri=PID4CAT_MODEL.EMAIL_index,
    domain=EMAIL,
    range=int,
)

slots.EMAIL_data = Slot(
    uri=PID4CAT_MODEL.data,
    name="EMAIL_data",
    curie=PID4CAT_MODEL.curie("data"),
    model_uri=PID4CAT_MODEL.EMAIL_data,
    domain=EMAIL,
    range=Union[dict, "HdlDataContact"],
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
    range=str,
    pattern=re.compile(r"^\S+@[\S+\.]+\S+"),
)

slots.STATUS_index = Slot(
    uri=PID4CAT_MODEL.index,
    name="STATUS_index",
    curie=PID4CAT_MODEL.curie("index"),
    model_uri=PID4CAT_MODEL.STATUS_index,
    domain=STATUS,
    range=int,
)

slots.STATUS_data = Slot(
    uri=PID4CAT_MODEL.data,
    name="STATUS_data",
    curie=PID4CAT_MODEL.curie("data"),
    model_uri=PID4CAT_MODEL.STATUS_data,
    domain=STATUS,
    range=Union[dict, "HdlDataStatus"],
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
    range=Union[str, "Pid4CatStatus"],
)

slots.SCHEMA_VER_index = Slot(
    uri=PID4CAT_MODEL.index,
    name="SCHEMA_VER_index",
    curie=PID4CAT_MODEL.curie("index"),
    model_uri=PID4CAT_MODEL.SCHEMA_VER_index,
    domain=SCHEMAVER,
    range=int,
)

slots.SCHEMA_VER_data = Slot(
    uri=PID4CAT_MODEL.data,
    name="SCHEMA_VER_data",
    curie=PID4CAT_MODEL.curie("data"),
    model_uri=PID4CAT_MODEL.SCHEMA_VER_data,
    domain=SCHEMAVER,
    range=Union[dict, "HdlDataSchemaVer"],
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
    range=str,
    pattern=re.compile(r"^v\d+\.\d+\.\d+$"),
)

slots.METADATA_LICENSE_index = Slot(
    uri=PID4CAT_MODEL.index,
    name="METADATA_LICENSE_index",
    curie=PID4CAT_MODEL.curie("index"),
    model_uri=PID4CAT_MODEL.METADATA_LICENSE_index,
    domain=METADATALICENSE,
    range=int,
)

slots.METADATA_LICENSE_data = Slot(
    uri=PID4CAT_MODEL.data,
    name="METADATA_LICENSE_data",
    curie=PID4CAT_MODEL.curie("data"),
    model_uri=PID4CAT_MODEL.METADATA_LICENSE_data,
    domain=METADATALICENSE,
    range=Union[dict, "HdlDataLicense"],
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
    range=str,
)

slots.RESOURCE_index = Slot(
    uri=PID4CAT_MODEL.index,
    name="RESOURCE_index",
    curie=PID4CAT_MODEL.curie("index"),
    model_uri=PID4CAT_MODEL.RESOURCE_index,
    domain=RESOURCE,
    range=int,
)

slots.RESOURCE_data = Slot(
    uri=PID4CAT_MODEL.data,
    name="RESOURCE_data",
    curie=PID4CAT_MODEL.curie("data"),
    model_uri=PID4CAT_MODEL.RESOURCE_data,
    domain=RESOURCE,
    range=Union[dict, "HdlDataResourceInfo"],
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
    range=Union[dict, "ResourceInfo"],
)

slots.RELATED_index = Slot(
    uri=PID4CAT_MODEL.index,
    name="RELATED_index",
    curie=PID4CAT_MODEL.curie("index"),
    model_uri=PID4CAT_MODEL.RELATED_index,
    domain=RELATED,
    range=int,
)

slots.RELATED_data = Slot(
    uri=PID4CAT_MODEL.data,
    name="RELATED_data",
    curie=PID4CAT_MODEL.curie("data"),
    model_uri=PID4CAT_MODEL.RELATED_data,
    domain=RELATED,
    range=Union[dict, "HdlDataRelated"],
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
        Union[Union[dict, "Pid4CatRelation"], list[Union[dict, "Pid4CatRelation"]]]
    ],
)

slots.CHANGES_index = Slot(
    uri=PID4CAT_MODEL.index,
    name="CHANGES_index",
    curie=PID4CAT_MODEL.curie("index"),
    model_uri=PID4CAT_MODEL.CHANGES_index,
    domain=CHANGES,
    range=int,
)

slots.CHANGES_data = Slot(
    uri=PID4CAT_MODEL.data,
    name="CHANGES_data",
    curie=PID4CAT_MODEL.curie("data"),
    model_uri=PID4CAT_MODEL.CHANGES_data,
    domain=CHANGES,
    range=Union[dict, "HdlDataLog"],
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
    range=Union[Union[dict, "LogRecord"], list[Union[dict, "LogRecord"]]],
)

slots.ResourceInfo_resource_category = Slot(
    uri=PID4CAT_MODEL.resource_category,
    name="ResourceInfo_resource_category",
    curie=PID4CAT_MODEL.curie("resource_category"),
    model_uri=PID4CAT_MODEL.ResourceInfo_resource_category,
    domain=ResourceInfo,
    range=Union[str, "ResourceCategory"],
)

slots.ResourceInfo_representation_variants = Slot(
    uri=PID4CAT_MODEL.representation_variants,
    name="ResourceInfo_representation_variants",
    curie=PID4CAT_MODEL.curie("representation_variants"),
    model_uri=PID4CAT_MODEL.ResourceInfo_representation_variants,
    domain=ResourceInfo,
    range=Union[
        Union[dict, "RepresentationVariant"], list[Union[dict, "RepresentationVariant"]]
    ],
)

slots.LogRecord_datetime_log = Slot(
    uri=PID4CAT_MODEL.datetime_log,
    name="LogRecord_datetime_log",
    curie=PID4CAT_MODEL.curie("datetime_log"),
    model_uri=PID4CAT_MODEL.LogRecord_datetime_log,
    domain=LogRecord,
    range=Union[str, XSDDateTime],
)

slots.LogRecord_has_agent = Slot(
    uri=PID4CAT_MODEL.has_agent,
    name="LogRecord_has_agent",
    curie=PID4CAT_MODEL.curie("has_agent"),
    model_uri=PID4CAT_MODEL.LogRecord_has_agent,
    domain=LogRecord,
    range=Union[dict, "Agent"],
)

slots.LogRecord_changed_field = Slot(
    uri=PID4CAT_MODEL.changed_field,
    name="LogRecord_changed_field",
    curie=PID4CAT_MODEL.curie("changed_field"),
    model_uri=PID4CAT_MODEL.LogRecord_changed_field,
    domain=LogRecord,
    range=Union[str, "ChangeLogField"],
)

slots.LogRecord_description = Slot(
    uri=PID4CAT_MODEL.description,
    name="LogRecord_description",
    curie=PID4CAT_MODEL.curie("description"),
    model_uri=PID4CAT_MODEL.LogRecord_description,
    domain=LogRecord,
    range=Optional[str],
)

slots.Agent_name = Slot(
    uri=PID4CAT_MODEL.name,
    name="Agent_name",
    curie=PID4CAT_MODEL.curie("name"),
    model_uri=PID4CAT_MODEL.Agent_name,
    domain=Agent,
    range=str,
)

slots.Agent_email_address = Slot(
    uri=PID4CAT_MODEL.email_address,
    name="Agent_email_address",
    curie=PID4CAT_MODEL.curie("email_address"),
    model_uri=PID4CAT_MODEL.Agent_email_address,
    domain=Agent,
    range=str,
    pattern=re.compile(r"^\S+@[\S+\.]+\S+"),
)

slots.Agent_orcid = Slot(
    uri=PID4CAT_MODEL.orcid,
    name="Agent_orcid",
    curie=PID4CAT_MODEL.curie("orcid"),
    model_uri=PID4CAT_MODEL.Agent_orcid,
    domain=Agent,
    range=Optional[str],
    pattern=re.compile(r"^\d{4}-\d{4}-\d{4}-\d{3}[0-9X]$"),
)

slots.Agent_affiliation_ror = Slot(
    uri=PID4CAT_MODEL.affiliation_ror,
    name="Agent_affiliation_ror",
    curie=PID4CAT_MODEL.curie("affiliation_ror"),
    model_uri=PID4CAT_MODEL.Agent_affiliation_ror,
    domain=Agent,
    range=Optional[Union[str, URI]],
    pattern=re.compile(r"^https:\/\/ror\.org\/0[a-hj-km-np-tv-z|0-9]{6}[0-9]{2}$"),
)

slots.Agent_role = Slot(
    uri=PID4CAT_MODEL.role,
    name="Agent_role",
    curie=PID4CAT_MODEL.curie("role"),
    model_uri=PID4CAT_MODEL.Agent_role,
    domain=Agent,
    range=Union[str, "Pid4CatAgentRole"],
)

slots.RepresentationVariant_media_type = Slot(
    uri=PID4CAT_MODEL.media_type,
    name="RepresentationVariant_media_type",
    curie=PID4CAT_MODEL.curie("media_type"),
    model_uri=PID4CAT_MODEL.RepresentationVariant_media_type,
    domain=RepresentationVariant,
    range=Optional[Union[str, "MediaTypesEnum"]],
)

slots.PurlIdentifier_resolving_url = Slot(
    uri=PID4CAT_MODEL.resolving_url,
    name="PurlIdentifier_resolving_url",
    curie=PID4CAT_MODEL.curie("resolving_url"),
    model_uri=PID4CAT_MODEL.PurlIdentifier_resolving_url,
    domain=PurlIdentifier,
    range=Union[str, URI],
    pattern=re.compile(r"^https:\/\/(purl|pida|w3id)\.org\/.*$"),
)

slots.DoiIdentifier_identifier = Slot(
    uri=PID4CAT_MODEL.identifier,
    name="DoiIdentifier_identifier",
    curie=PID4CAT_MODEL.curie("identifier"),
    model_uri=PID4CAT_MODEL.DoiIdentifier_identifier,
    domain=DoiIdentifier,
    range=Optional[str],
    pattern=re.compile(r"^10\.\d{4,}\/.*$"),
)

slots.DoiIdentifier_resolving_url = Slot(
    uri=PID4CAT_MODEL.resolving_url,
    name="DoiIdentifier_resolving_url",
    curie=PID4CAT_MODEL.curie("resolving_url"),
    model_uri=PID4CAT_MODEL.DoiIdentifier_resolving_url,
    domain=DoiIdentifier,
    range=Union[str, URI],
    pattern=re.compile(r"^https:\/\/doi\.org\/10.*$"),
)

slots.HandleIdentifier_identifier = Slot(
    uri=PID4CAT_MODEL.identifier,
    name="HandleIdentifier_identifier",
    curie=PID4CAT_MODEL.curie("identifier"),
    model_uri=PID4CAT_MODEL.HandleIdentifier_identifier,
    domain=HandleIdentifier,
    range=Optional[str],
    pattern=re.compile(r"^\d{2}\.T?\d{4,}\/.*$"),
)

slots.HandleIdentifier_resolving_url = Slot(
    uri=PID4CAT_MODEL.resolving_url,
    name="HandleIdentifier_resolving_url",
    curie=PID4CAT_MODEL.curie("resolving_url"),
    model_uri=PID4CAT_MODEL.HandleIdentifier_resolving_url,
    domain=HandleIdentifier,
    range=Union[str, URI],
    pattern=re.compile(r"^https:\/\/hdl\.handle\.net\/\d{2}\.T?\d{4,}\/.*$"),
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
    range=Union[str, URI],
    pattern=re.compile(r"^https?:\/\/.*\/ark:\/\d{5}/.*$"),
)

slots.UrnIdentifier_identifier = Slot(
    uri=PID4CAT_MODEL.identifier,
    name="UrnIdentifier_identifier",
    curie=PID4CAT_MODEL.curie("identifier"),
    model_uri=PID4CAT_MODEL.UrnIdentifier_identifier,
    domain=UrnIdentifier,
    range=str,
    pattern=re.compile(r"^urn:[a-zA-Z0-9][a-zA-Z0-9-]{0,31}:[^\s]*$"),
)

slots.GtinIdentifier_identifier = Slot(
    uri=PID4CAT_MODEL.identifier,
    name="GtinIdentifier_identifier",
    curie=PID4CAT_MODEL.curie("identifier"),
    model_uri=PID4CAT_MODEL.GtinIdentifier_identifier,
    domain=GtinIdentifier,
    range=str,
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

slots.Pid4CatRecord_landing_page_url = Slot(
    uri=PID4CAT_MODEL.landing_page_url,
    name="Pid4CatRecord_landing_page_url",
    curie=PID4CAT_MODEL.curie("landing_page_url"),
    model_uri=PID4CAT_MODEL.Pid4CatRecord_landing_page_url,
    domain=Pid4CatRecord,
    range=str,
    pattern=re.compile(r"^https?:\/\/.*$"),
)

slots.Pid4CatRecord_status = Slot(
    uri=PID4CAT_MODEL.status,
    name="Pid4CatRecord_status",
    curie=PID4CAT_MODEL.curie("status"),
    model_uri=PID4CAT_MODEL.Pid4CatRecord_status,
    domain=Pid4CatRecord,
    range=Union[str, "Pid4CatStatus"],
)

slots.Pid4CatRecord_schema_version = Slot(
    uri=PID4CAT_MODEL.schema_version,
    name="Pid4CatRecord_schema_version",
    curie=PID4CAT_MODEL.curie("schema_version"),
    model_uri=PID4CAT_MODEL.Pid4CatRecord_schema_version,
    domain=Pid4CatRecord,
    range=str,
)

slots.Pid4CatRecord_metadata_license = Slot(
    uri=PID4CAT_MODEL.metadata_license,
    name="Pid4CatRecord_metadata_license",
    curie=PID4CAT_MODEL.curie("metadata_license"),
    model_uri=PID4CAT_MODEL.Pid4CatRecord_metadata_license,
    domain=Pid4CatRecord,
    range=str,
)

slots.Pid4CatRecord_curation_contact = Slot(
    uri=PID4CAT_MODEL.curation_contact,
    name="Pid4CatRecord_curation_contact",
    curie=PID4CAT_MODEL.curie("curation_contact"),
    model_uri=PID4CAT_MODEL.Pid4CatRecord_curation_contact,
    domain=Pid4CatRecord,
    range=str,
    pattern=re.compile(r"^\S+@[\S+\.]+\S+"),
)

slots.Pid4CatRecord_resource_info = Slot(
    uri=PID4CAT_MODEL.resource_info,
    name="Pid4CatRecord_resource_info",
    curie=PID4CAT_MODEL.curie("resource_info"),
    model_uri=PID4CAT_MODEL.Pid4CatRecord_resource_info,
    domain=Pid4CatRecord,
    range=Union[dict, ResourceInfo],
)

slots.Pid4CatRecord_related_identifiers = Slot(
    uri=PID4CAT_MODEL.related_identifiers,
    name="Pid4CatRecord_related_identifiers",
    curie=PID4CAT_MODEL.curie("related_identifiers"),
    model_uri=PID4CAT_MODEL.Pid4CatRecord_related_identifiers,
    domain=Pid4CatRecord,
    range=Optional[
        Union[Union[dict, Pid4CatRelation], list[Union[dict, Pid4CatRelation]]]
    ],
)

slots.Pid4CatRecord_change_log = Slot(
    uri=PID4CAT_MODEL.change_log,
    name="Pid4CatRecord_change_log",
    curie=PID4CAT_MODEL.curie("change_log"),
    model_uri=PID4CAT_MODEL.Pid4CatRecord_change_log,
    domain=Pid4CatRecord,
    range=Union[Union[dict, LogRecord], list[Union[dict, LogRecord]]],
)
