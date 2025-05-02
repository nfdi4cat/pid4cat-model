from __future__ import annotations

import re
from datetime import datetime
from enum import Enum
from typing import Any, ClassVar, Dict, List, Literal, Optional, Union

from pydantic import BaseModel, ConfigDict, Field, RootModel, field_validator


metamodel_version = "None"
version = "0.3.0.post25.dev0+d2bd0d4"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        validate_assignment=True,
        validate_default=True,
        extra="forbid",
        arbitrary_types_allowed=True,
        use_enum_values=True,
        strict=False,
    )
    pass


class LinkMLMeta(RootModel):
    root: Dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key: str):
        return getattr(self.root, key)

    def __getitem__(self, key: str):
        return self.root[key]

    def __setitem__(self, key: str, value):
        self.root[key] = value

    def __contains__(self, key: str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta(
    {
        "default_prefix": "pid4cat_model",
        "default_range": "string",
        "description": "A LinkML model for persistent identifiers for resources in "
        "catalysis (pid4cat). pid4cat are handle based persistent "
        "identifiers (PIDs) for digital or physical resources used in "
        "the catalysis research process. PID-related metadata besides "
        "the obligatory landing page URL are stored directly in the "
        "handle records.\n"
        "The model describes metadata for the PID itself and how to "
        "access the identified resource. It does not describe the "
        "resource itself with the exception of the resource category, "
        "which is a high-level description of what is identified by "
        "the pid4cat handle, e.g. a sample or a device.",
        "id": "https://w3id.org/nfdi4cat/pid4cat-model",
        "imports": ["linkml:types", "media_types"],
        "license": "MIT",
        "name": "pid4cat-model",
        "prefixes": {
            "DataCite": {
                "prefix_prefix": "DataCite",
                "prefix_reference": "https://purl.org/spar/datacite/",
            },
            "dcat": {
                "prefix_prefix": "dcat",
                "prefix_reference": "https://www.w3.org/ns/dcat#",
            },
            "dcterms": {
                "prefix_prefix": "dcterms",
                "prefix_reference": "https://purl.org/dc/terms/",
            },
            "linkml": {
                "prefix_prefix": "linkml",
                "prefix_reference": "https://w3id.org/linkml/",
            },
            "mediatype": {
                "prefix_prefix": "mediatype",
                "prefix_reference": "https://www.iana.org/assignments/media-types/",
            },
            "pid4cat_model": {
                "prefix_prefix": "pid4cat_model",
                "prefix_reference": "https://w3id.org/nfdi4cat/pid4cat-model/",
            },
            "prov": {
                "prefix_prefix": "prov",
                "prefix_reference": "https://www.w3.org/ns/prov#",
            },
            "voc4cat": {
                "prefix_prefix": "voc4cat",
                "prefix_reference": "https://w3id.org/nfdi4cat/voc4cat_",
            },
        },
        "see_also": ["https://nfdi4cat.github.io/pid4cat-model"],
        "source_file": "src/pid4cat_model/schema/pid4cat_model.yaml",
        "title": "pid4cat-model",
        "todos": ["none"],
    }
)


class MediaTypesEnum(str, Enum):
    """
    IANA media types are used to specify the type of data.
    """

    # For data in Electronic Publication Format (EPUB).
    applicationSOLIDUSepubPLUS_SIGNzip = "application/epub+zip"
    # For data in JavaScript Object Notation (JSON).
    applicationSOLIDUSjson = "application/json"
    # For data in Linked Data json (JSON-LD).
    applicationSOLIDUSldPLUS_SIGNjson = "application/ld+json"
    # For binary data.
    applicationSOLIDUSoctet_stream = "application/octet-stream"
    # For data in Portable Document Format (PDF).
    applicationSOLIDUSpdf = "application/pdf"
    # For data in ELN ZIP format.
    applicationSOLIDUSvndFULL_STOPelnPLUS_SIGNzip = "application/vnd.eln+zip"
    # For data in PowerPoint pptx format.
    applicationSOLIDUSvndFULL_STOPopenxmlformats_officedocumentFULL_STOPpresentationmlFULL_STOPpresentation = "application/vnd.openxmlformats-officedocument.presentationml.presentation"
    # For data in Excel xlsx format.
    applicationSOLIDUSvndFULL_STOPopenxmlformats_officedocumentFULL_STOPspreadsheetmlFULL_STOPsheet = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    # For data in Word docx format.
    applicationSOLIDUSvndFULL_STOPopenxmlformats_officedocumentFULL_STOPwordprocessingmlFULL_STOPdocument = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    # For generic XML data.
    applicationSOLIDUSxml = "application/xml"
    # For YAML data.
    applicationSOLIDUSyaml = "application/yaml"
    # For zip archives.
    applicationSOLIDUSzip = "application/zip"
    # For GIF images.
    imageSOLIDUSgif = "image/gif"
    # For JPEG images.
    imageSOLIDUSjpeg = "image/jpeg"
    # For PNG images.
    imageSOLIDUSpng = "image/png"
    # For SVG images.
    imageSOLIDUSsvgPLUS_SIGNxml = "image/svg+xml"
    # For TIFF images.
    imageSOLIDUStiff = "image/tiff"
    # For WebP images.
    imageSOLIDUSwebp = "image/webp"
    # For data in comma-separated values (CSV) format.
    textSOLIDUScsv = "text/csv"
    # For html web pages.
    textSOLIDUShtml = "text/html"
    # For JavaScript code.
    textSOLIDUSjavascript = "text/javascript"
    # For data in markdown text format.
    textSOLIDUSmarkdown = "text/markdown"
    # For plain text data (default text media type).
    textSOLIDUSplain = "text/plain"
    # For data in tab-separated values (TSV) format.
    textSOLIDUStab_separated_values = "text/tab-separated-values"
    # For data in turtle format.
    textSOLIDUSturtle = "text/turtle"
    # For XML data.
    textSOLIDUSxml = "text/xml"
    # For mp4 video files.
    videoSOLIDUSmp4 = "video/mp4"
    # For webm video files.
    videoSOLIDUSwebm = "video/webm"


class ResourceCategory(str, Enum):
    """
    The ResourceCategory expresses for which type of resource the PID is used, e.g. if the PID is for a sample or a device.
    """

    # A collection is a group of resources and/or other collections.
    COLLECTION = "COLLECTION"
    # A representative part of a material of interest on which observations are made.
    SAMPLE = "SAMPLE"
    # A material used in the research process (except samples).
    MATERIAL = "MATERIAL"
    # A physical device used in a research or manufacturing process.
    DEVICE = "DEVICE"
    # A collection of data available for access or download. A data object might be a data file, a data set, a data collection.
    DATA_OBJECT = "DATA_OBJECT"
    # An organized system of operations that provide data processing functions or access to datasets.
    DATA_SERVICE = "DATA_SERVICE"


class RelationType(str, Enum):
    """
    The type of relation between two resources referenced by their PIDs.
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
    # The resource has a version. This is useful to express the relation between a abstract resource to its versioned instances, for example, "Python has_version Python 3.12".
    HAS_VERSION = "HAS_VERSION"
    # The resource is a version of another resource. This is useful to refer to an abstract resource that has different versions, for example, "Python 3.12 is a version of Python".
    IS_VERSION_OF = "IS_VERSION_OF"
    # The resource is a new version of another versioned resource. This is useful to refer between versioned resources, for example, "Python 3.12.1 is_new_version_of Python 3.12.0".
    IS_NEW_VERSION_OF = "IS_NEW_VERSION_OF"
    # The resource is a previous version of another versioned resource. This is useful to refer between versioned resources, for example, "Python 3.12.0 is_previous_version_of Python 3.12.1".
    IS_PREVIOUS_VERSION_OF = "IS_PREVIOUS_VERSION_OF"
    # The resource is part of another resource. This relation applies to container-contained type relationships. If the relation refers to publishing one resource as part of another resource, use "IS_PUBLISHED_IN" instead. If the relation refers to a versioned resource and non-versioned resource, use "IS_VERSION_OF" instead.
    IS_PART_OF = "IS_PART_OF"
    # The resource has part another resource. This relation applies to container-contained type relationships. If the relation refers to publishing one resource as part of another resource, "IS_PUBLISHED_IN" instead. If the relation refers to a versioned resource and non-versioned resource, use "HAS_VERSION" instead.
    HAS_PART = "HAS_PART"
    # The resource is published in another resource. A resource A that is_published_in a resource B is independent from other resources published in the same resource B.
    IS_PUBLISHED_IN = "IS_PUBLISHED_IN"
    # The resource is referenced by another resource.
    IS_REFERENCED_BY = "IS_REFERENCED_BY"
    # The resource references another resource.
    REFERENCES = "REFERENCES"
    # The resource is documented by another resource.
    IS_DOCUMENTED_BY = "IS_DOCUMENTED_BY"
    # The resource documents another resource.
    DOCUMENTS = "DOCUMENTS"
    # The resource is compiled by another resource. Resources may be text or software. The compiler may be a computer program or a person.
    IS_COMPILED_BY = "IS_COMPILED_BY"
    # The resource compiles another resource. Resources may be text or software. The compiler may be a computer program or a person.
    COMPILES = "COMPILES"
    # The resource is variant form of another resource. This may be used e.g. for relating architecture-specific builds of a software program to a source-code release. It may also be used to express the relation between data in different formats (e.g. PNG, JPEG) of the same image.
    IS_VARIANT_FORM_OF = "IS_VARIANT_FORM_OF"
    # The resource is original form of another resource. This may be used e.g. for relating architecture-specific builds of a software program to a source-code release. It may also be used to express the relation between data in different formats (e.g. PNG, JPEG) of the same image.
    IS_ORIGINAL_FORM_OF = "IS_ORIGINAL_FORM_OF"
    # The resource is identical to another resource. May be used to indicate the relationship between an exact copy of a resource that is published at another location.
    IS_IDENTICAL_TO = "IS_IDENTICAL_TO"
    # The resource is derived from another resource. This may be used for relating a new dataset created by data processing to its original source dataset. For samples it may express the relation between the original sample and another sample derived from it by physical or chemical treatment.
    IS_DERIVED_FROM = "IS_DERIVED_FROM"
    # The resource is source of another resource. This may be used for example to express the relation between a source dataset and a new dataset derived from it by data processing. For samples it may express the relation between a sample processed by physical or chemical treatment and the original sample.
    IS_SOURCE_OF = "IS_SOURCE_OF"
    # The resource is collected by another resource. May be used to indicate the relationship between a dataset and an instrument that is used to collect, measure, obtain, or observe data.
    IS_COLLECTED_BY = "IS_COLLECTED_BY"
    # The resource collects another resource. May be used to indicate the relationship between an instrument and where it has been used to collect, measure, obtain, or observe data.
    COLLECTS = "COLLECTS"
    # The resource is required by another resource.
    IS_REQUIRED_BY = "IS_REQUIRED_BY"
    # The resource requires another resource.
    REQUIRES = "REQUIRES"
    # The resource is obsoleted by another resource.
    IS_OBSOLETED_BY = "IS_OBSOLETED_BY"
    # The resource obsoletes another resource.
    OBSOLETES = "OBSOLETES"
    # An established standard to which the described resource conforms. This relation should be used to indicate the model, schema, ontology, or profile that the resource content conforms to.
    CONFORMS_TO = "CONFORMS_TO"


class Pid4CatStatus(str, Enum):
    """
    The usage status of the pid4cat record.
    """

    # The pid4cat handle is reserved but the resource is not yet linked.
    SUBMITTED = "SUBMITTED"
    # The pid4cat handle is linked to a concrete resource.
    REGISTERED = "REGISTERED"
    # The pid4cat handle is obsolete, e.g. because the resource is referenced by another pid4cat.
    OBSOLETED = "OBSOLETED"
    # The pid4cat record is deprecated, e.g. because the resource can no longer be found.
    DEPRECATED = "DEPRECATED"


class Pid4CatAgentRole(str, Enum):
    """
    The role of an agent relative to the resource.
    """

    # The agent is the trustee of the resource.
    TRUSTEE = "TRUSTEE"
    # The agent is the owner of the resource.
    OWNER = "OWNER"


class ChangeLogField(str, Enum):
    """
    The field of the pid4cat record that was changed.
    """

    # The status of the pid4cat record was changed.
    STATUS = "STATUS"
    # The URL of the landing page in the pid4cat record was changed.
    LANDING_PAGE = "LANDING_PAGE"
    # The resource info of the pid4cat record was changed.
    RESOURCE_INFO = "RESOURCE_INFO"
    # The related identifiers of the pid4cat record were changed.
    RELATED_IDS = "RELATED_IDS"
    # The contact information of the pid4cat record was changed.
    CONTACT = "CONTACT"
    # The license of the pid4cat record was changed.
    LICENSE = "LICENSE"
    # The pid4cat-model version of the pid4cat record was changed.
    SCHEMA_VER = "SCHEMA_VER"


class HandleAPIRecord(ConfiguredBaseModel):
    """
    A class representing a handle record query response of the REST (json) API of a handle server.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://w3id.org/nfdi4cat/pid4cat-model",
            "slot_usage": {
                "handle": {
                    "name": "handle",
                    "pattern": "^\\d{2}\\.T?\\d{4,}\\/.*$",
                    "required": True,
                },
                "values": {"name": "values", "required": True},
            },
        }
    )

    responseCode: Optional[int] = Field(
        default=None,
        description="""The response code of the handle API.""",
        json_schema_extra={
            "linkml_meta": {"alias": "responseCode", "domain_of": ["HandleAPIRecord"]}
        },
    )
    handle: str = Field(
        default=...,
        description="""The handle of the pid4cat record.""",
        json_schema_extra={
            "linkml_meta": {"alias": "handle", "domain_of": ["HandleAPIRecord"]}
        },
    )
    values: List[
        Union[
            HandleRecord,
            URL,
            EMAIL,
            STATUS,
            SCHEMAVER,
            METADATALICENSE,
            RESOURCE,
            RELATED,
            CHANGES,
        ]
    ] = Field(
        default=...,
        description="""The values of the pid4cat record.""",
        json_schema_extra={
            "linkml_meta": {"alias": "values", "domain_of": ["HandleAPIRecord"]}
        },
    )

    @field_validator("handle")
    def pattern_handle(cls, v):
        pattern = re.compile(r"^\d{2}\.T?\d{4,}\/.*$")
        if isinstance(v, list):
            for element in v:
                if isinstance(v, str) and not pattern.match(element):
                    raise ValueError(f"Invalid handle format: {element}")
        elif isinstance(v, str):
            if not pattern.match(v):
                raise ValueError(f"Invalid handle format: {v}")
        return v


class HandleRecord(ConfiguredBaseModel):
    """
    A base class for handle-data classes that represent a handle record in the same way as in the REST (json) API of a handle server.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://w3id.org/nfdi4cat/pid4cat-model",
            "slot_usage": {
                "timestamp": {"name": "timestamp", "required": True},
                "ttl": {"ifabsent": "86400", "name": "ttl"},
                "type": {
                    "description": "The type of handledata stored in the "
                    "handle record.",
                    "designates_type": True,
                    "name": "type",
                    "required": True,
                },
            },
        }
    )

    timestamp: datetime = Field(
        default=...,
        description="""The iso datetime for the last update of the handle data.""",
        json_schema_extra={
            "linkml_meta": {"alias": "timestamp", "domain_of": ["HandleRecord"]}
        },
    )
    ttl: Optional[int] = Field(
        default=86400,
        description="""A time to live in seconds for the handle record. Typically: 86400 => 1 day""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "ttl",
                "domain_of": ["HandleRecord"],
                "ifabsent": "86400",
            }
        },
    )
    type: Literal["HandleRecord"] = Field(
        default="HandleRecord",
        description="""The type of handledata stored in the handle record.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["HandleRecord", "RelatedIdentifier"],
            }
        },
    )


class URL(HandleRecord):
    """
    The data element in the handle API for the landing page URL.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://w3id.org/nfdi4cat/pid4cat-model",
            "slot_usage": {
                "data": {"name": "data", "range": "HdlDataUrl", "required": True},
                "index": {
                    "maximum_value": 1,
                    "minimum_value": 1,
                    "name": "index",
                    "required": True,
                },
            },
        }
    )

    index: int = Field(
        default=...,
        description="""The index of the handle record.""",
        ge=1,
        le=1,
        json_schema_extra={
            "linkml_meta": {
                "alias": "index",
                "domain_of": [
                    "URL",
                    "EMAIL",
                    "STATUS",
                    "SCHEMA_VER",
                    "METADATA_LICENSE",
                    "RESOURCE",
                    "RELATED",
                    "CHANGES",
                ],
            }
        },
    )
    data: HdlDataUrl = Field(
        default=...,
        description="""The data in the handle record.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "data",
                "domain_of": [
                    "URL",
                    "EMAIL",
                    "STATUS",
                    "SCHEMA_VER",
                    "METADATA_LICENSE",
                    "RESOURCE",
                    "RELATED",
                    "CHANGES",
                ],
            }
        },
    )
    timestamp: datetime = Field(
        default=...,
        description="""The iso datetime for the last update of the handle data.""",
        json_schema_extra={
            "linkml_meta": {"alias": "timestamp", "domain_of": ["HandleRecord"]}
        },
    )
    ttl: Optional[int] = Field(
        default=86400,
        description="""A time to live in seconds for the handle record. Typically: 86400 => 1 day""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "ttl",
                "domain_of": ["HandleRecord"],
                "ifabsent": "86400",
            }
        },
    )
    type: Literal["URL"] = Field(
        default="URL",
        description="""The type of handledata stored in the handle record.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["HandleRecord", "RelatedIdentifier"],
            }
        },
    )


class HdlDataUrl(ConfiguredBaseModel):
    """
    The data class for the redirect url.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://w3id.org/nfdi4cat/pid4cat-model",
            "slot_usage": {
                "format": {
                    "equals_string": "string",
                    "ifabsent": "string",
                    "name": "format",
                },
                "value": {
                    "name": "value",
                    "pattern": "^https?:\\/\\/.*$",
                    "required": True,
                },
            },
        }
    )

    format: Optional[Literal["string"]] = Field(
        default="string",
        description="""The format of the handle data.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "format",
                "domain_of": [
                    "HdlDataUrl",
                    "HdlDataContact",
                    "HdlDataStatus",
                    "HdlDataSchemaVer",
                    "HdlDataLicense",
                    "HdlDataResourceInfo",
                    "HdlDataRelated",
                    "HdlDataLog",
                ],
                "equals_string": "string",
                "ifabsent": "string",
            }
        },
    )
    value: str = Field(
        default=...,
        description="""The value of the handle data.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "value",
                "domain_of": [
                    "HdlDataUrl",
                    "HdlDataContact",
                    "HdlDataStatus",
                    "HdlDataSchemaVer",
                    "HdlDataLicense",
                    "HdlDataResourceInfo",
                    "HdlDataRelated",
                    "HdlDataLog",
                ],
            }
        },
    )

    @field_validator("value")
    def pattern_value(cls, v):
        pattern = re.compile(r"^https?:\/\/.*$")
        if isinstance(v, list):
            for element in v:
                if isinstance(v, str) and not pattern.match(element):
                    raise ValueError(f"Invalid value format: {element}")
        elif isinstance(v, str):
            if not pattern.match(v):
                raise ValueError(f"Invalid value format: {v}")
        return v


class EMAIL(HandleRecord):
    """
    The data element in the handle API for the contact email.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://w3id.org/nfdi4cat/pid4cat-model",
            "slot_usage": {
                "data": {"name": "data", "range": "HdlDataContact", "required": True},
                "index": {
                    "maximum_value": 10,
                    "minimum_value": 10,
                    "name": "index",
                    "required": True,
                },
            },
        }
    )

    index: int = Field(
        default=...,
        description="""The index of the handle record.""",
        ge=10,
        le=10,
        json_schema_extra={
            "linkml_meta": {
                "alias": "index",
                "domain_of": [
                    "URL",
                    "EMAIL",
                    "STATUS",
                    "SCHEMA_VER",
                    "METADATA_LICENSE",
                    "RESOURCE",
                    "RELATED",
                    "CHANGES",
                ],
            }
        },
    )
    data: HdlDataContact = Field(
        default=...,
        description="""The data in the handle record.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "data",
                "domain_of": [
                    "URL",
                    "EMAIL",
                    "STATUS",
                    "SCHEMA_VER",
                    "METADATA_LICENSE",
                    "RESOURCE",
                    "RELATED",
                    "CHANGES",
                ],
            }
        },
    )
    timestamp: datetime = Field(
        default=...,
        description="""The iso datetime for the last update of the handle data.""",
        json_schema_extra={
            "linkml_meta": {"alias": "timestamp", "domain_of": ["HandleRecord"]}
        },
    )
    ttl: Optional[int] = Field(
        default=86400,
        description="""A time to live in seconds for the handle record. Typically: 86400 => 1 day""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "ttl",
                "domain_of": ["HandleRecord"],
                "ifabsent": "86400",
            }
        },
    )
    type: Literal["EMAIL"] = Field(
        default="EMAIL",
        description="""The type of handledata stored in the handle record.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["HandleRecord", "RelatedIdentifier"],
            }
        },
    )


class HdlDataContact(ConfiguredBaseModel):
    """
    The data class for the handle-record contact email.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://w3id.org/nfdi4cat/pid4cat-model",
            "slot_usage": {
                "format": {
                    "equals_string": "string",
                    "ifabsent": "string",
                    "name": "format",
                },
                "value": {
                    "name": "value",
                    "pattern": "^\\S+@[\\S+\\.]+\\S+",
                    "required": True,
                },
            },
        }
    )

    format: Optional[Literal["string"]] = Field(
        default="string",
        description="""The format of the handle data.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "format",
                "domain_of": [
                    "HdlDataUrl",
                    "HdlDataContact",
                    "HdlDataStatus",
                    "HdlDataSchemaVer",
                    "HdlDataLicense",
                    "HdlDataResourceInfo",
                    "HdlDataRelated",
                    "HdlDataLog",
                ],
                "equals_string": "string",
                "ifabsent": "string",
            }
        },
    )
    value: str = Field(
        default=...,
        description="""The value of the handle data.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "value",
                "domain_of": [
                    "HdlDataUrl",
                    "HdlDataContact",
                    "HdlDataStatus",
                    "HdlDataSchemaVer",
                    "HdlDataLicense",
                    "HdlDataResourceInfo",
                    "HdlDataRelated",
                    "HdlDataLog",
                ],
            }
        },
    )

    @field_validator("value")
    def pattern_value(cls, v):
        pattern = re.compile(r"^\S+@[\S+\.]+\S+")
        if isinstance(v, list):
            for element in v:
                if isinstance(v, str) and not pattern.match(element):
                    raise ValueError(f"Invalid value format: {element}")
        elif isinstance(v, str):
            if not pattern.match(v):
                raise ValueError(f"Invalid value format: {v}")
        return v


class STATUS(HandleRecord):
    """
    The data element in the handle API for the PID status information.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://w3id.org/nfdi4cat/pid4cat-model",
            "slot_usage": {
                "data": {"name": "data", "range": "HdlDataStatus", "required": True},
                "index": {
                    "maximum_value": 11,
                    "minimum_value": 11,
                    "name": "index",
                    "required": True,
                },
            },
        }
    )

    index: int = Field(
        default=...,
        description="""The index of the handle record.""",
        ge=11,
        le=11,
        json_schema_extra={
            "linkml_meta": {
                "alias": "index",
                "domain_of": [
                    "URL",
                    "EMAIL",
                    "STATUS",
                    "SCHEMA_VER",
                    "METADATA_LICENSE",
                    "RESOURCE",
                    "RELATED",
                    "CHANGES",
                ],
            }
        },
    )
    data: HdlDataStatus = Field(
        default=...,
        description="""The data in the handle record.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "data",
                "domain_of": [
                    "URL",
                    "EMAIL",
                    "STATUS",
                    "SCHEMA_VER",
                    "METADATA_LICENSE",
                    "RESOURCE",
                    "RELATED",
                    "CHANGES",
                ],
            }
        },
    )
    timestamp: datetime = Field(
        default=...,
        description="""The iso datetime for the last update of the handle data.""",
        json_schema_extra={
            "linkml_meta": {"alias": "timestamp", "domain_of": ["HandleRecord"]}
        },
    )
    ttl: Optional[int] = Field(
        default=86400,
        description="""A time to live in seconds for the handle record. Typically: 86400 => 1 day""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "ttl",
                "domain_of": ["HandleRecord"],
                "ifabsent": "86400",
            }
        },
    )
    type: Literal["STATUS"] = Field(
        default="STATUS",
        description="""The type of handledata stored in the handle record.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["HandleRecord", "RelatedIdentifier"],
            }
        },
    )


class HdlDataStatus(ConfiguredBaseModel):
    """
    The data class for the PID status information.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://w3id.org/nfdi4cat/pid4cat-model",
            "slot_usage": {
                "format": {
                    "equals_string": "string",
                    "ifabsent": "string",
                    "name": "format",
                },
                "value": {"name": "value", "range": "Pid4CatStatus", "required": True},
            },
        }
    )

    format: Optional[Literal["string"]] = Field(
        default="string",
        description="""The format of the handle data.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "format",
                "domain_of": [
                    "HdlDataUrl",
                    "HdlDataContact",
                    "HdlDataStatus",
                    "HdlDataSchemaVer",
                    "HdlDataLicense",
                    "HdlDataResourceInfo",
                    "HdlDataRelated",
                    "HdlDataLog",
                ],
                "equals_string": "string",
                "ifabsent": "string",
            }
        },
    )
    value: Pid4CatStatus = Field(
        default=...,
        description="""The value of the handle data.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "value",
                "domain_of": [
                    "HdlDataUrl",
                    "HdlDataContact",
                    "HdlDataStatus",
                    "HdlDataSchemaVer",
                    "HdlDataLicense",
                    "HdlDataResourceInfo",
                    "HdlDataRelated",
                    "HdlDataLog",
                ],
            }
        },
    )


class SCHEMAVER(HandleRecord):
    """
    The data element in the handle API for the schema version.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://w3id.org/nfdi4cat/pid4cat-model",
            "slot_usage": {
                "data": {"name": "data", "range": "HdlDataSchemaVer", "required": True},
                "index": {
                    "maximum_value": 12,
                    "minimum_value": 12,
                    "name": "index",
                    "required": True,
                },
            },
        }
    )

    index: int = Field(
        default=...,
        description="""The index of the handle record.""",
        ge=12,
        le=12,
        json_schema_extra={
            "linkml_meta": {
                "alias": "index",
                "domain_of": [
                    "URL",
                    "EMAIL",
                    "STATUS",
                    "SCHEMA_VER",
                    "METADATA_LICENSE",
                    "RESOURCE",
                    "RELATED",
                    "CHANGES",
                ],
            }
        },
    )
    data: HdlDataSchemaVer = Field(
        default=...,
        description="""The data in the handle record.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "data",
                "domain_of": [
                    "URL",
                    "EMAIL",
                    "STATUS",
                    "SCHEMA_VER",
                    "METADATA_LICENSE",
                    "RESOURCE",
                    "RELATED",
                    "CHANGES",
                ],
            }
        },
    )
    timestamp: datetime = Field(
        default=...,
        description="""The iso datetime for the last update of the handle data.""",
        json_schema_extra={
            "linkml_meta": {"alias": "timestamp", "domain_of": ["HandleRecord"]}
        },
    )
    ttl: Optional[int] = Field(
        default=86400,
        description="""A time to live in seconds for the handle record. Typically: 86400 => 1 day""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "ttl",
                "domain_of": ["HandleRecord"],
                "ifabsent": "86400",
            }
        },
    )
    type: Literal["SCHEMA_VER"] = Field(
        default="SCHEMA_VER",
        description="""The type of handledata stored in the handle record.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["HandleRecord", "RelatedIdentifier"],
            }
        },
    )


class HdlDataSchemaVer(ConfiguredBaseModel):
    """
    The data class for the schema version.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://w3id.org/nfdi4cat/pid4cat-model",
            "slot_usage": {
                "format": {
                    "equals_string": "string",
                    "ifabsent": "string",
                    "name": "format",
                },
                "value": {
                    "name": "value",
                    "pattern": "^v\\d+\\.\\d+\\.\\d+$",
                    "required": True,
                },
            },
        }
    )

    format: Optional[Literal["string"]] = Field(
        default="string",
        description="""The format of the handle data.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "format",
                "domain_of": [
                    "HdlDataUrl",
                    "HdlDataContact",
                    "HdlDataStatus",
                    "HdlDataSchemaVer",
                    "HdlDataLicense",
                    "HdlDataResourceInfo",
                    "HdlDataRelated",
                    "HdlDataLog",
                ],
                "equals_string": "string",
                "ifabsent": "string",
            }
        },
    )
    value: str = Field(
        default=...,
        description="""The value of the handle data.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "value",
                "domain_of": [
                    "HdlDataUrl",
                    "HdlDataContact",
                    "HdlDataStatus",
                    "HdlDataSchemaVer",
                    "HdlDataLicense",
                    "HdlDataResourceInfo",
                    "HdlDataRelated",
                    "HdlDataLog",
                ],
            }
        },
    )

    @field_validator("value")
    def pattern_value(cls, v):
        pattern = re.compile(r"^v\d+\.\d+\.\d+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(v, str) and not pattern.match(element):
                    raise ValueError(f"Invalid value format: {element}")
        elif isinstance(v, str):
            if not pattern.match(v):
                raise ValueError(f"Invalid value format: {v}")
        return v


class METADATALICENSE(HandleRecord):
    """
    The data element in the handle API for the PID metadata license.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://w3id.org/nfdi4cat/pid4cat-model",
            "slot_usage": {
                "data": {"name": "data", "range": "HdlDataLicense", "required": True},
                "index": {
                    "maximum_value": 13,
                    "minimum_value": 13,
                    "name": "index",
                    "required": True,
                },
            },
        }
    )

    index: int = Field(
        default=...,
        description="""The index of the handle record.""",
        ge=13,
        le=13,
        json_schema_extra={
            "linkml_meta": {
                "alias": "index",
                "domain_of": [
                    "URL",
                    "EMAIL",
                    "STATUS",
                    "SCHEMA_VER",
                    "METADATA_LICENSE",
                    "RESOURCE",
                    "RELATED",
                    "CHANGES",
                ],
            }
        },
    )
    data: HdlDataLicense = Field(
        default=...,
        description="""The data in the handle record.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "data",
                "domain_of": [
                    "URL",
                    "EMAIL",
                    "STATUS",
                    "SCHEMA_VER",
                    "METADATA_LICENSE",
                    "RESOURCE",
                    "RELATED",
                    "CHANGES",
                ],
            }
        },
    )
    timestamp: datetime = Field(
        default=...,
        description="""The iso datetime for the last update of the handle data.""",
        json_schema_extra={
            "linkml_meta": {"alias": "timestamp", "domain_of": ["HandleRecord"]}
        },
    )
    ttl: Optional[int] = Field(
        default=86400,
        description="""A time to live in seconds for the handle record. Typically: 86400 => 1 day""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "ttl",
                "domain_of": ["HandleRecord"],
                "ifabsent": "86400",
            }
        },
    )
    type: Literal["METADATA_LICENSE"] = Field(
        default="METADATA_LICENSE",
        description="""The type of handledata stored in the handle record.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["HandleRecord", "RelatedIdentifier"],
            }
        },
    )


class HdlDataLicense(ConfiguredBaseModel):
    """
    The data class for the PID metadata license.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://w3id.org/nfdi4cat/pid4cat-model",
            "slot_usage": {
                "format": {
                    "equals_string": "string",
                    "ifabsent": "string",
                    "name": "format",
                },
                "value": {
                    "equals_string": "CC0-1.0",
                    "name": "value",
                    "required": True,
                },
            },
        }
    )

    format: Optional[Literal["string"]] = Field(
        default="string",
        description="""The format of the handle data.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "format",
                "domain_of": [
                    "HdlDataUrl",
                    "HdlDataContact",
                    "HdlDataStatus",
                    "HdlDataSchemaVer",
                    "HdlDataLicense",
                    "HdlDataResourceInfo",
                    "HdlDataRelated",
                    "HdlDataLog",
                ],
                "equals_string": "string",
                "ifabsent": "string",
            }
        },
    )
    value: Literal["CC0-1.0"] = Field(
        default=...,
        description="""The value of the handle data.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "value",
                "domain_of": [
                    "HdlDataUrl",
                    "HdlDataContact",
                    "HdlDataStatus",
                    "HdlDataSchemaVer",
                    "HdlDataLicense",
                    "HdlDataResourceInfo",
                    "HdlDataRelated",
                    "HdlDataLog",
                ],
                "equals_string": "CC0-1.0",
            }
        },
    )


class RESOURCE(HandleRecord):
    """
    The data element in the handle API for the resource info.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://w3id.org/nfdi4cat/pid4cat-model",
            "slot_usage": {
                "data": {
                    "name": "data",
                    "range": "HdlDataResourceInfo",
                    "required": True,
                },
                "index": {
                    "maximum_value": 14,
                    "minimum_value": 14,
                    "name": "index",
                    "required": True,
                },
            },
        }
    )

    index: int = Field(
        default=...,
        description="""The index of the handle record.""",
        ge=14,
        le=14,
        json_schema_extra={
            "linkml_meta": {
                "alias": "index",
                "domain_of": [
                    "URL",
                    "EMAIL",
                    "STATUS",
                    "SCHEMA_VER",
                    "METADATA_LICENSE",
                    "RESOURCE",
                    "RELATED",
                    "CHANGES",
                ],
            }
        },
    )
    data: HdlDataResourceInfo = Field(
        default=...,
        description="""The data in the handle record.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "data",
                "domain_of": [
                    "URL",
                    "EMAIL",
                    "STATUS",
                    "SCHEMA_VER",
                    "METADATA_LICENSE",
                    "RESOURCE",
                    "RELATED",
                    "CHANGES",
                ],
            }
        },
    )
    timestamp: datetime = Field(
        default=...,
        description="""The iso datetime for the last update of the handle data.""",
        json_schema_extra={
            "linkml_meta": {"alias": "timestamp", "domain_of": ["HandleRecord"]}
        },
    )
    ttl: Optional[int] = Field(
        default=86400,
        description="""A time to live in seconds for the handle record. Typically: 86400 => 1 day""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "ttl",
                "domain_of": ["HandleRecord"],
                "ifabsent": "86400",
            }
        },
    )
    type: Literal["RESOURCE"] = Field(
        default="RESOURCE",
        description="""The type of handledata stored in the handle record.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["HandleRecord", "RelatedIdentifier"],
            }
        },
    )


class HdlDataResourceInfo(ConfiguredBaseModel):
    """
    The data class for the resource info.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://w3id.org/nfdi4cat/pid4cat-model",
            "slot_usage": {
                "format": {
                    "equals_string": "string",
                    "ifabsent": "string",
                    "name": "format",
                },
                "value": {"name": "value", "range": "ResourceInfo", "required": True},
            },
        }
    )

    format: Optional[Literal["string"]] = Field(
        default="string",
        description="""The format of the handle data.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "format",
                "domain_of": [
                    "HdlDataUrl",
                    "HdlDataContact",
                    "HdlDataStatus",
                    "HdlDataSchemaVer",
                    "HdlDataLicense",
                    "HdlDataResourceInfo",
                    "HdlDataRelated",
                    "HdlDataLog",
                ],
                "equals_string": "string",
                "ifabsent": "string",
            }
        },
    )
    value: ResourceInfo = Field(
        default=...,
        description="""The value of the handle data.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "value",
                "domain_of": [
                    "HdlDataUrl",
                    "HdlDataContact",
                    "HdlDataStatus",
                    "HdlDataSchemaVer",
                    "HdlDataLicense",
                    "HdlDataResourceInfo",
                    "HdlDataRelated",
                    "HdlDataLog",
                ],
            }
        },
    )


class RELATED(HandleRecord):
    """
    The data element in the handle API for related identifiers.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://w3id.org/nfdi4cat/pid4cat-model",
            "slot_usage": {
                "data": {"name": "data", "range": "HdlDataRelated", "required": True},
                "index": {
                    "maximum_value": 15,
                    "minimum_value": 15,
                    "name": "index",
                    "required": True,
                },
            },
        }
    )

    index: int = Field(
        default=...,
        description="""The index of the handle record.""",
        ge=15,
        le=15,
        json_schema_extra={
            "linkml_meta": {
                "alias": "index",
                "domain_of": [
                    "URL",
                    "EMAIL",
                    "STATUS",
                    "SCHEMA_VER",
                    "METADATA_LICENSE",
                    "RESOURCE",
                    "RELATED",
                    "CHANGES",
                ],
            }
        },
    )
    data: HdlDataRelated = Field(
        default=...,
        description="""The data in the handle record.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "data",
                "domain_of": [
                    "URL",
                    "EMAIL",
                    "STATUS",
                    "SCHEMA_VER",
                    "METADATA_LICENSE",
                    "RESOURCE",
                    "RELATED",
                    "CHANGES",
                ],
            }
        },
    )
    timestamp: datetime = Field(
        default=...,
        description="""The iso datetime for the last update of the handle data.""",
        json_schema_extra={
            "linkml_meta": {"alias": "timestamp", "domain_of": ["HandleRecord"]}
        },
    )
    ttl: Optional[int] = Field(
        default=86400,
        description="""A time to live in seconds for the handle record. Typically: 86400 => 1 day""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "ttl",
                "domain_of": ["HandleRecord"],
                "ifabsent": "86400",
            }
        },
    )
    type: Literal["RELATED"] = Field(
        default="RELATED",
        description="""The type of handledata stored in the handle record.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["HandleRecord", "RelatedIdentifier"],
            }
        },
    )


class HdlDataRelated(ConfiguredBaseModel):
    """
    The data class for related identifiers.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://w3id.org/nfdi4cat/pid4cat-model",
            "slot_usage": {
                "format": {
                    "equals_string": "string",
                    "ifabsent": "string",
                    "name": "format",
                },
                "value": {
                    "multivalued": True,
                    "name": "value",
                    "range": "Pid4CatRelation",
                },
            },
        }
    )

    format: Optional[Literal["string"]] = Field(
        default="string",
        description="""The format of the handle data.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "format",
                "domain_of": [
                    "HdlDataUrl",
                    "HdlDataContact",
                    "HdlDataStatus",
                    "HdlDataSchemaVer",
                    "HdlDataLicense",
                    "HdlDataResourceInfo",
                    "HdlDataRelated",
                    "HdlDataLog",
                ],
                "equals_string": "string",
                "ifabsent": "string",
            }
        },
    )
    value: Optional[List[Pid4CatRelation]] = Field(
        default=None,
        description="""The value of the handle data.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "value",
                "domain_of": [
                    "HdlDataUrl",
                    "HdlDataContact",
                    "HdlDataStatus",
                    "HdlDataSchemaVer",
                    "HdlDataLicense",
                    "HdlDataResourceInfo",
                    "HdlDataRelated",
                    "HdlDataLog",
                ],
            }
        },
    )


class CHANGES(HandleRecord):
    """
    The data element in the handle API for the change log.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://w3id.org/nfdi4cat/pid4cat-model",
            "slot_usage": {
                "data": {"name": "data", "range": "HdlDataLog", "required": True},
                "index": {
                    "maximum_value": 16,
                    "minimum_value": 16,
                    "name": "index",
                    "required": True,
                },
            },
        }
    )

    index: int = Field(
        default=...,
        description="""The index of the handle record.""",
        ge=16,
        le=16,
        json_schema_extra={
            "linkml_meta": {
                "alias": "index",
                "domain_of": [
                    "URL",
                    "EMAIL",
                    "STATUS",
                    "SCHEMA_VER",
                    "METADATA_LICENSE",
                    "RESOURCE",
                    "RELATED",
                    "CHANGES",
                ],
            }
        },
    )
    data: HdlDataLog = Field(
        default=...,
        description="""The data in the handle record.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "data",
                "domain_of": [
                    "URL",
                    "EMAIL",
                    "STATUS",
                    "SCHEMA_VER",
                    "METADATA_LICENSE",
                    "RESOURCE",
                    "RELATED",
                    "CHANGES",
                ],
            }
        },
    )
    timestamp: datetime = Field(
        default=...,
        description="""The iso datetime for the last update of the handle data.""",
        json_schema_extra={
            "linkml_meta": {"alias": "timestamp", "domain_of": ["HandleRecord"]}
        },
    )
    ttl: Optional[int] = Field(
        default=86400,
        description="""A time to live in seconds for the handle record. Typically: 86400 => 1 day""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "ttl",
                "domain_of": ["HandleRecord"],
                "ifabsent": "86400",
            }
        },
    )
    type: Literal["CHANGES"] = Field(
        default="CHANGES",
        description="""The type of handledata stored in the handle record.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["HandleRecord", "RelatedIdentifier"],
            }
        },
    )


class HdlDataLog(ConfiguredBaseModel):
    """
    The data class for the change log.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://w3id.org/nfdi4cat/pid4cat-model",
            "slot_usage": {
                "format": {
                    "equals_string": "string",
                    "ifabsent": "string",
                    "name": "format",
                },
                "value": {
                    "multivalued": True,
                    "name": "value",
                    "range": "LogRecord",
                    "required": True,
                },
            },
        }
    )

    format: Optional[Literal["string"]] = Field(
        default="string",
        description="""The format of the handle data.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "format",
                "domain_of": [
                    "HdlDataUrl",
                    "HdlDataContact",
                    "HdlDataStatus",
                    "HdlDataSchemaVer",
                    "HdlDataLicense",
                    "HdlDataResourceInfo",
                    "HdlDataRelated",
                    "HdlDataLog",
                ],
                "equals_string": "string",
                "ifabsent": "string",
            }
        },
    )
    value: List[LogRecord] = Field(
        default=...,
        description="""The value of the handle data.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "value",
                "domain_of": [
                    "HdlDataUrl",
                    "HdlDataContact",
                    "HdlDataStatus",
                    "HdlDataSchemaVer",
                    "HdlDataLicense",
                    "HdlDataResourceInfo",
                    "HdlDataRelated",
                    "HdlDataLog",
                ],
            }
        },
    )


class HandleRecordContainer(ConfiguredBaseModel):
    """
    A container for all HandleRecords.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://w3id.org/nfdi4cat/pid4cat-model", "tree_root": True}
    )

    contains_pids: Optional[List[HandleAPIRecord]] = Field(
        default=None,
        description="""The HandleRecords contained in the container.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "contains_pids",
                "domain_of": ["HandleRecordContainer"],
            }
        },
    )


class Pid4CatRelation(ConfiguredBaseModel):
    """
    Data class for a relation to another resource identified by a pid4cat handle or another PID type.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://w3id.org/nfdi4cat/pid4cat-model"}
    )

    relation_type: Optional[RelationType] = Field(
        default=None,
        description="""Relation type between the resources.""",
        json_schema_extra={
            "linkml_meta": {"alias": "relation_type", "domain_of": ["Pid4CatRelation"]}
        },
    )
    related_identifier: Optional[
        Union[
            RelatedIdentifier,
            PurlIdentifier,
            DoiIdentifier,
            HandleIdentifier,
            ArkIdentifier,
            UrnIdentifier,
            GtinIdentifier,
            ExampleIdentifier,
        ]
    ] = Field(
        default=None,
        description="""The related identifier.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "related_identifier",
                "domain_of": ["Pid4CatRelation"],
            }
        },
    )
    datetime_log: Optional[datetime] = Field(
        default=None,
        description="""The date and time of a log record.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "datetime_log",
                "domain_of": ["Pid4CatRelation", "LogRecord"],
            }
        },
    )


class ResourceInfo(ConfiguredBaseModel):
    """
    Data class to hold information about the resource and its representation.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://w3id.org/nfdi4cat/pid4cat-model",
            "slot_usage": {
                "representation_variants": {
                    "name": "representation_variants",
                    "required": True,
                },
                "resource_category": {"name": "resource_category", "required": True},
            },
        }
    )

    label: Optional[str] = Field(
        default=None,
        description="""A human-readable name for a resource.""",
        json_schema_extra={
            "linkml_meta": {"alias": "label", "domain_of": ["ResourceInfo"]}
        },
    )
    description: Optional[str] = Field(
        default=None,
        description="""A human-readable description for a resource.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "description",
                "domain_of": ["ResourceInfo", "LogRecord"],
            }
        },
    )
    resource_category: ResourceCategory = Field(
        default=...,
        description="""The category of the resource.""",
        json_schema_extra={
            "linkml_meta": {"alias": "resource_category", "domain_of": ["ResourceInfo"]}
        },
    )
    representation_variants: List[RepresentationVariant] = Field(
        default=...,
        description="""The representations of the resource in other media types than text/html.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "representation_variants",
                "domain_of": ["ResourceInfo"],
            }
        },
    )


class LogRecord(ConfiguredBaseModel):
    """
    Data class for a change log of modification made on a pid4cat handle record starting from its registration.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://w3id.org/nfdi4cat/pid4cat-model",
            "slot_usage": {
                "changed_field": {"name": "changed_field", "required": True},
                "datetime_log": {"name": "datetime_log", "required": True},
                "description": {"name": "description"},
                "has_agent": {"name": "has_agent", "required": True},
            },
        }
    )

    datetime_log: datetime = Field(
        default=...,
        description="""The date and time of a log record.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "datetime_log",
                "domain_of": ["Pid4CatRelation", "LogRecord"],
            }
        },
    )
    has_agent: Agent = Field(
        default=...,
        description="""The person who registered or modified the PID record.""",
        json_schema_extra={
            "linkml_meta": {"alias": "has_agent", "domain_of": ["LogRecord"]}
        },
    )
    changed_field: ChangeLogField = Field(
        default=...,
        description="""The field that was changed.""",
        json_schema_extra={
            "linkml_meta": {"alias": "changed_field", "domain_of": ["LogRecord"]}
        },
    )
    description: Optional[str] = Field(
        default=None,
        description="""A human-readable description for a resource.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "description",
                "domain_of": ["ResourceInfo", "LogRecord"],
            }
        },
    )


class Agent(ConfiguredBaseModel):
    """
    Data class for a person who plays a role relative to PID creation or curation.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "class_uri": "prov:Agent",
            "from_schema": "https://w3id.org/nfdi4cat/pid4cat-model",
            "slot_usage": {
                "affiliation_ror": {
                    "name": "affiliation_ror",
                    "pattern": "^https:\\/\\/ror\\.org\\/0[a-hj-km-np-tv-z|0-9]{6}[0-9]{2}$",
                },
                "email_address": {
                    "name": "email_address",
                    "pattern": "^\\S+@[\\S+\\.]+\\S+",
                    "required": True,
                },
                "name": {"name": "name", "required": True},
                "orcid": {
                    "name": "orcid",
                    "pattern": "^\\d{4}-\\d{4}-\\d{4}-\\d{3}[0-9X]$",
                },
                "role": {"name": "role", "required": True},
            },
        }
    )

    name: str = Field(
        default=...,
        description="""The name of the agent that created or modified the PID record.""",
        json_schema_extra={"linkml_meta": {"alias": "name", "domain_of": ["Agent"]}},
    )
    email_address: str = Field(
        default=...,
        description="""Email address of the agent that created or modified the PID record.""",
        json_schema_extra={
            "linkml_meta": {"alias": "email_address", "domain_of": ["Agent"]}
        },
    )
    orcid: Optional[str] = Field(
        default=None,
        description="""The ORCID of the person""",
        json_schema_extra={"linkml_meta": {"alias": "orcid", "domain_of": ["Agent"]}},
    )
    affiliation_ror: Optional[str] = Field(
        default=None,
        description="""The ROR of the agent's affiliation.""",
        json_schema_extra={
            "linkml_meta": {"alias": "affiliation_ror", "domain_of": ["Agent"]}
        },
    )
    role: Pid4CatAgentRole = Field(
        default=...,
        description="""The role of the agent relative to the resource""",
        json_schema_extra={"linkml_meta": {"alias": "role", "domain_of": ["Agent"]}},
    )

    @field_validator("email_address")
    def pattern_email_address(cls, v):
        pattern = re.compile(r"^\S+@[\S+\.]+\S+")
        if isinstance(v, list):
            for element in v:
                if isinstance(v, str) and not pattern.match(element):
                    raise ValueError(f"Invalid email_address format: {element}")
        elif isinstance(v, str):
            if not pattern.match(v):
                raise ValueError(f"Invalid email_address format: {v}")
        return v

    @field_validator("orcid")
    def pattern_orcid(cls, v):
        pattern = re.compile(r"^\d{4}-\d{4}-\d{4}-\d{3}[0-9X]$")
        if isinstance(v, list):
            for element in v:
                if isinstance(v, str) and not pattern.match(element):
                    raise ValueError(f"Invalid orcid format: {element}")
        elif isinstance(v, str):
            if not pattern.match(v):
                raise ValueError(f"Invalid orcid format: {v}")
        return v

    @field_validator("affiliation_ror")
    def pattern_affiliation_ror(cls, v):
        pattern = re.compile(r"^https:\/\/ror\.org\/0[a-hj-km-np-tv-z|0-9]{6}[0-9]{2}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(v, str) and not pattern.match(element):
                    raise ValueError(f"Invalid affiliation_ror format: {element}")
        elif isinstance(v, str):
            if not pattern.match(v):
                raise ValueError(f"Invalid affiliation_ror format: {v}")
        return v


class RepresentationVariant(ConfiguredBaseModel):
    """
    Data class for representations of the resource in other media types than text/html which is the default for landing_page_url.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://w3id.org/nfdi4cat/pid4cat-model",
            "slot_usage": {"media_type": {"name": "media_type"}},
        }
    )

    variant_url: Optional[str] = Field(
        default=None,
        description="""The URL of the representation variant.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "variant_url",
                "domain_of": ["RepresentationVariant"],
            }
        },
    )
    media_type: Optional[MediaTypesEnum] = Field(
        default=None,
        description="""The media type of the representation as defined by [IANA](https://www.iana.org/assignments/media-types/media-types.xhtml)""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "media_type",
                "domain_of": ["RepresentationVariant"],
            }
        },
    )
    encoding_format: Optional[str] = Field(
        default=None,
        description="""The encoding of the representation. https://encoding.spec.whatwg.org/#names-and-labels""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "encoding_format",
                "domain_of": ["RepresentationVariant"],
            }
        },
    )
    size: Optional[int] = Field(
        default=None,
        description="""The size of the representation in bytes.""",
        ge=0,
        json_schema_extra={
            "linkml_meta": {"alias": "size", "domain_of": ["RepresentationVariant"]}
        },
    )


class RelatedIdentifier(ConfiguredBaseModel):
    """
    A base class for all types of related identifiers.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://w3id.org/nfdi4cat/pid4cat-model"}
    )

    type: Literal["RelatedIdentifier"] = Field(
        default="RelatedIdentifier",
        description="""The type of the identifier.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["HandleRecord", "RelatedIdentifier"],
            }
        },
    )


class PurlIdentifier(RelatedIdentifier):
    """
    A PURL (permanent uniform resource locator).
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://w3id.org/nfdi4cat/pid4cat-model",
            "slot_usage": {
                "resolving_url": {
                    "name": "resolving_url",
                    "pattern": "^https:\\/\\/(purl|pida|w3id)\\.org\\/.*$",
                    "required": True,
                }
            },
        }
    )

    resolving_url: str = Field(
        default=...,
        description="""The URL that resolves the identifier.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "resolving_url",
                "domain_of": [
                    "PurlIdentifier",
                    "DoiIdentifier",
                    "HandleIdentifier",
                    "ArkIdentifier",
                    "ExampleIdentifier",
                ],
            }
        },
    )
    type: Literal["PurlIdentifier"] = Field(
        default="PurlIdentifier",
        description="""The type of the identifier.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["HandleRecord", "RelatedIdentifier"],
            }
        },
    )

    @field_validator("resolving_url")
    def pattern_resolving_url(cls, v):
        pattern = re.compile(r"^https:\/\/(purl|pida|w3id)\.org\/.*$")
        if isinstance(v, list):
            for element in v:
                if isinstance(v, str) and not pattern.match(element):
                    raise ValueError(f"Invalid resolving_url format: {element}")
        elif isinstance(v, str):
            if not pattern.match(v):
                raise ValueError(f"Invalid resolving_url format: {v}")
        return v


class DoiIdentifier(RelatedIdentifier):
    """
    A digital object identifier (DOI).
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://w3id.org/nfdi4cat/pid4cat-model",
            "slot_usage": {
                "identifier": {"name": "identifier", "pattern": "^10\\.\\d{4,}\\/.*$"},
                "resolving_url": {
                    "name": "resolving_url",
                    "pattern": "^https:\\/\\/doi\\.org\\/10.*$",
                    "required": True,
                },
            },
        }
    )

    resolving_url: str = Field(
        default=...,
        description="""The URL that resolves the identifier.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "resolving_url",
                "domain_of": [
                    "PurlIdentifier",
                    "DoiIdentifier",
                    "HandleIdentifier",
                    "ArkIdentifier",
                    "ExampleIdentifier",
                ],
            }
        },
    )
    identifier: Optional[str] = Field(
        default=None,
        description="""The identifier in recommended notation.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "identifier",
                "domain_of": [
                    "DoiIdentifier",
                    "HandleIdentifier",
                    "ArkIdentifier",
                    "UrnIdentifier",
                    "GtinIdentifier",
                    "ExampleIdentifier",
                ],
            }
        },
    )
    type: Literal["DoiIdentifier"] = Field(
        default="DoiIdentifier",
        description="""The type of the identifier.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["HandleRecord", "RelatedIdentifier"],
            }
        },
    )

    @field_validator("resolving_url")
    def pattern_resolving_url(cls, v):
        pattern = re.compile(r"^https:\/\/doi\.org\/10.*$")
        if isinstance(v, list):
            for element in v:
                if isinstance(v, str) and not pattern.match(element):
                    raise ValueError(f"Invalid resolving_url format: {element}")
        elif isinstance(v, str):
            if not pattern.match(v):
                raise ValueError(f"Invalid resolving_url format: {v}")
        return v

    @field_validator("identifier")
    def pattern_identifier(cls, v):
        pattern = re.compile(r"^10\.\d{4,}\/.*$")
        if isinstance(v, list):
            for element in v:
                if isinstance(v, str) and not pattern.match(element):
                    raise ValueError(f"Invalid identifier format: {element}")
        elif isinstance(v, str):
            if not pattern.match(v):
                raise ValueError(f"Invalid identifier format: {v}")
        return v


class HandleIdentifier(RelatedIdentifier):
    """
    A handle identifier.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://w3id.org/nfdi4cat/pid4cat-model",
            "slot_usage": {
                "identifier": {
                    "name": "identifier",
                    "pattern": "^\\d{2}\\.T?\\d{4,}\\/.*$",
                },
                "resolving_url": {
                    "name": "resolving_url",
                    "pattern": "^https:\\/\\/hdl\\.handle\\.net\\/\\d{2}\\.T?\\d{4,}\\/.*$",
                    "required": True,
                },
            },
        }
    )

    resolving_url: str = Field(
        default=...,
        description="""The URL that resolves the identifier.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "resolving_url",
                "domain_of": [
                    "PurlIdentifier",
                    "DoiIdentifier",
                    "HandleIdentifier",
                    "ArkIdentifier",
                    "ExampleIdentifier",
                ],
            }
        },
    )
    identifier: Optional[str] = Field(
        default=None,
        description="""The identifier in recommended notation.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "identifier",
                "domain_of": [
                    "DoiIdentifier",
                    "HandleIdentifier",
                    "ArkIdentifier",
                    "UrnIdentifier",
                    "GtinIdentifier",
                    "ExampleIdentifier",
                ],
            }
        },
    )
    type: Literal["HandleIdentifier"] = Field(
        default="HandleIdentifier",
        description="""The type of the identifier.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["HandleRecord", "RelatedIdentifier"],
            }
        },
    )

    @field_validator("resolving_url")
    def pattern_resolving_url(cls, v):
        pattern = re.compile(r"^https:\/\/hdl\.handle\.net\/\d{2}\.T?\d{4,}\/.*$")
        if isinstance(v, list):
            for element in v:
                if isinstance(v, str) and not pattern.match(element):
                    raise ValueError(f"Invalid resolving_url format: {element}")
        elif isinstance(v, str):
            if not pattern.match(v):
                raise ValueError(f"Invalid resolving_url format: {v}")
        return v

    @field_validator("identifier")
    def pattern_identifier(cls, v):
        pattern = re.compile(r"^\d{2}\.T?\d{4,}\/.*$")
        if isinstance(v, list):
            for element in v:
                if isinstance(v, str) and not pattern.match(element):
                    raise ValueError(f"Invalid identifier format: {element}")
        elif isinstance(v, str):
            if not pattern.match(v):
                raise ValueError(f"Invalid identifier format: {v}")
        return v


class ArkIdentifier(RelatedIdentifier):
    """
    An ARK (Archival Resource Key).
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://w3id.org/nfdi4cat/pid4cat-model",
            "slot_usage": {
                "identifier": {"name": "identifier", "pattern": "^ark:\\/\\d{5}/.*$"},
                "resolving_url": {
                    "name": "resolving_url",
                    "pattern": "^https?:\\/\\/.*\\/ark:\\/\\d{5}/.*$",
                    "required": True,
                },
            },
        }
    )

    identifier: Optional[str] = Field(
        default=None,
        description="""The identifier in recommended notation.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "identifier",
                "domain_of": [
                    "DoiIdentifier",
                    "HandleIdentifier",
                    "ArkIdentifier",
                    "UrnIdentifier",
                    "GtinIdentifier",
                    "ExampleIdentifier",
                ],
            }
        },
    )
    resolving_url: str = Field(
        default=...,
        description="""The URL that resolves the identifier.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "resolving_url",
                "domain_of": [
                    "PurlIdentifier",
                    "DoiIdentifier",
                    "HandleIdentifier",
                    "ArkIdentifier",
                    "ExampleIdentifier",
                ],
            }
        },
    )
    type: Literal["ArkIdentifier"] = Field(
        default="ArkIdentifier",
        description="""The type of the identifier.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["HandleRecord", "RelatedIdentifier"],
            }
        },
    )

    @field_validator("identifier")
    def pattern_identifier(cls, v):
        pattern = re.compile(r"^ark:\/\d{5}/.*$")
        if isinstance(v, list):
            for element in v:
                if isinstance(v, str) and not pattern.match(element):
                    raise ValueError(f"Invalid identifier format: {element}")
        elif isinstance(v, str):
            if not pattern.match(v):
                raise ValueError(f"Invalid identifier format: {v}")
        return v

    @field_validator("resolving_url")
    def pattern_resolving_url(cls, v):
        pattern = re.compile(r"^https?:\/\/.*\/ark:\/\d{5}/.*$")
        if isinstance(v, list):
            for element in v:
                if isinstance(v, str) and not pattern.match(element):
                    raise ValueError(f"Invalid resolving_url format: {element}")
        elif isinstance(v, str):
            if not pattern.match(v):
                raise ValueError(f"Invalid resolving_url format: {v}")
        return v


class UrnIdentifier(RelatedIdentifier):
    """
    A URN (Uniform Resource Name).
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://w3id.org/nfdi4cat/pid4cat-model",
            "slot_usage": {
                "identifier": {
                    "name": "identifier",
                    "pattern": "^urn:[a-zA-Z0-9][a-zA-Z0-9-]{0,31}:[^\\s]*$",
                    "required": True,
                }
            },
        }
    )

    identifier: str = Field(
        default=...,
        description="""The identifier in recommended notation.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "identifier",
                "domain_of": [
                    "DoiIdentifier",
                    "HandleIdentifier",
                    "ArkIdentifier",
                    "UrnIdentifier",
                    "GtinIdentifier",
                    "ExampleIdentifier",
                ],
            }
        },
    )
    type: Literal["UrnIdentifier"] = Field(
        default="UrnIdentifier",
        description="""The type of the identifier.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["HandleRecord", "RelatedIdentifier"],
            }
        },
    )

    @field_validator("identifier")
    def pattern_identifier(cls, v):
        pattern = re.compile(r"^urn:[a-zA-Z0-9][a-zA-Z0-9-]{0,31}:[^\s]*$")
        if isinstance(v, list):
            for element in v:
                if isinstance(v, str) and not pattern.match(element):
                    raise ValueError(f"Invalid identifier format: {element}")
        elif isinstance(v, str):
            if not pattern.match(v):
                raise ValueError(f"Invalid identifier format: {v}")
        return v


class GtinIdentifier(RelatedIdentifier):
    """
    A Global Trade Item Number (GTIN) previously called European Article Number (EAN) often encoded as EAN13 barcode. The identifier is used to identify products. GTINs don't have a resolvable URL.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://w3id.org/nfdi4cat/pid4cat-model",
            "slot_usage": {
                "identifier": {
                    "name": "identifier",
                    "pattern": "^\\d{13}$",
                    "required": True,
                }
            },
        }
    )

    identifier: str = Field(
        default=...,
        description="""The identifier in recommended notation.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "identifier",
                "domain_of": [
                    "DoiIdentifier",
                    "HandleIdentifier",
                    "ArkIdentifier",
                    "UrnIdentifier",
                    "GtinIdentifier",
                    "ExampleIdentifier",
                ],
            }
        },
    )
    type: Literal["GtinIdentifier"] = Field(
        default="GtinIdentifier",
        description="""The type of the identifier.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["HandleRecord", "RelatedIdentifier"],
            }
        },
    )

    @field_validator("identifier")
    def pattern_identifier(cls, v):
        pattern = re.compile(r"^\d{13}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(v, str) and not pattern.match(element):
                    raise ValueError(f"Invalid identifier format: {element}")
        elif isinstance(v, str):
            if not pattern.match(v):
                raise ValueError(f"Invalid identifier format: {v}")
        return v


class ExampleIdentifier(RelatedIdentifier):
    """
    An example.org test identifier.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://w3id.org/nfdi4cat/pid4cat-model",
            "slot_usage": {
                "identifier": {"name": "identifier", "pattern": "^ex:.*$"},
                "resolving_url": {
                    "name": "resolving_url",
                    "pattern": "^https?:\\/\\/(.+\\.)?example.(org|com)\\/.*$",
                },
            },
        }
    )

    identifier: Optional[str] = Field(
        default=None,
        description="""The identifier in recommended notation.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "identifier",
                "domain_of": [
                    "DoiIdentifier",
                    "HandleIdentifier",
                    "ArkIdentifier",
                    "UrnIdentifier",
                    "GtinIdentifier",
                    "ExampleIdentifier",
                ],
            }
        },
    )
    resolving_url: Optional[str] = Field(
        default=None,
        description="""The URL that resolves the identifier.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "resolving_url",
                "domain_of": [
                    "PurlIdentifier",
                    "DoiIdentifier",
                    "HandleIdentifier",
                    "ArkIdentifier",
                    "ExampleIdentifier",
                ],
            }
        },
    )
    type: Literal["ExampleIdentifier"] = Field(
        default="ExampleIdentifier",
        description="""The type of the identifier.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "type",
                "designates_type": True,
                "domain_of": ["HandleRecord", "RelatedIdentifier"],
            }
        },
    )

    @field_validator("identifier")
    def pattern_identifier(cls, v):
        pattern = re.compile(r"^ex:.*$")
        if isinstance(v, list):
            for element in v:
                if isinstance(v, str) and not pattern.match(element):
                    raise ValueError(f"Invalid identifier format: {element}")
        elif isinstance(v, str):
            if not pattern.match(v):
                raise ValueError(f"Invalid identifier format: {v}")
        return v

    @field_validator("resolving_url")
    def pattern_resolving_url(cls, v):
        pattern = re.compile(r"^https?:\/\/(.+\.)?example.(org|com)\/.*$")
        if isinstance(v, list):
            for element in v:
                if isinstance(v, str) and not pattern.match(element):
                    raise ValueError(f"Invalid resolving_url format: {element}")
        elif isinstance(v, str):
            if not pattern.match(v):
                raise ValueError(f"Invalid resolving_url format: {v}")
        return v


class Pid4CatRecord(ConfiguredBaseModel):
    """
    A class representing pid4cat identifiers with its metadata as objects. This is a neutral object-oriented representation that does not mirror the record structure of the handle system but is provided as representation that is more convenient to use in programming languages.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://w3id.org/nfdi4cat/pid4cat-model",
            "slot_usage": {
                "change_log": {
                    "multivalued": True,
                    "name": "change_log",
                    "required": True,
                },
                "curation_contact": {
                    "name": "curation_contact",
                    "pattern": "^\\S+@[\\S+\\.]+\\S+",
                    "required": True,
                },
                "landing_page_url": {
                    "name": "landing_page_url",
                    "pattern": "^https?:\\/\\/.*$",
                    "required": True,
                },
                "metadata_license": {
                    "equals_string": "CC0-1.0",
                    "name": "metadata_license",
                    "required": True,
                },
                "related_identifiers": {
                    "multivalued": True,
                    "name": "related_identifiers",
                },
                "resource_info": {"name": "resource_info", "required": True},
                "schema_version": {"name": "schema_version", "required": True},
                "status": {"name": "status", "required": True},
            },
        }
    )

    landing_page_url: str = Field(
        default=...,
        description="""The URL of the landing page of the resource identified by the PID.""",
        json_schema_extra={
            "linkml_meta": {"alias": "landing_page_url", "domain_of": ["Pid4CatRecord"]}
        },
    )
    status: Pid4CatStatus = Field(
        default=...,
        description="""The status of the pid4cat record. The status is set to \"SUBMITTED\" when the handle is reserved but the resource is not yet linked. The status is set to \"REGISTERED\" when the handle is linked to a concrete resource.""",
        json_schema_extra={
            "linkml_meta": {"alias": "status", "domain_of": ["Pid4CatRecord"]}
        },
    )
    schema_version: str = Field(
        default=...,
        description="""The version of the pid4cat-model used to create the pid4cat record.""",
        json_schema_extra={
            "linkml_meta": {"alias": "schema_version", "domain_of": ["Pid4CatRecord"]}
        },
    )
    metadata_license: Literal["CC0-1.0"] = Field(
        default=...,
        description="""The license of the metadata of the pid4cat record. The license is set to \"CC0-1.0\" by default.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "metadata_license",
                "domain_of": ["Pid4CatRecord"],
                "equals_string": "CC0-1.0",
            }
        },
    )
    curation_contact: str = Field(
        default=...,
        description="""The email address of the person responsible for the curation of the pid4cat record.""",
        json_schema_extra={
            "linkml_meta": {"alias": "curation_contact", "domain_of": ["Pid4CatRecord"]}
        },
    )
    resource_info: ResourceInfo = Field(
        default=...,
        description="""The resource info of the pid4cat record. The resource info contains information about the resource identified by the PID.""",
        json_schema_extra={
            "linkml_meta": {"alias": "resource_info", "domain_of": ["Pid4CatRecord"]}
        },
    )
    related_identifiers: Optional[List[Pid4CatRelation]] = Field(
        default=None,
        description="""The related identifiers for the pid4cat record. The related identifiers are used to link the pid4cat record to other resources.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "related_identifiers",
                "domain_of": ["Pid4CatRecord"],
            }
        },
    )
    change_log: List[LogRecord] = Field(
        default=...,
        description="""The change log of the pid4cat record. The change log contains information about the changes made to the pid4cat record.""",
        json_schema_extra={
            "linkml_meta": {"alias": "change_log", "domain_of": ["Pid4CatRecord"]}
        },
    )

    @field_validator("landing_page_url")
    def pattern_landing_page_url(cls, v):
        pattern = re.compile(r"^https?:\/\/.*$")
        if isinstance(v, list):
            for element in v:
                if isinstance(v, str) and not pattern.match(element):
                    raise ValueError(f"Invalid landing_page_url format: {element}")
        elif isinstance(v, str):
            if not pattern.match(v):
                raise ValueError(f"Invalid landing_page_url format: {v}")
        return v

    @field_validator("curation_contact")
    def pattern_curation_contact(cls, v):
        pattern = re.compile(r"^\S+@[\S+\.]+\S+")
        if isinstance(v, list):
            for element in v:
                if isinstance(v, str) and not pattern.match(element):
                    raise ValueError(f"Invalid curation_contact format: {element}")
        elif isinstance(v, str):
            if not pattern.match(v):
                raise ValueError(f"Invalid curation_contact format: {v}")
        return v


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
HandleAPIRecord.model_rebuild()
HandleRecord.model_rebuild()
URL.model_rebuild()
HdlDataUrl.model_rebuild()
EMAIL.model_rebuild()
HdlDataContact.model_rebuild()
STATUS.model_rebuild()
HdlDataStatus.model_rebuild()
SCHEMAVER.model_rebuild()
HdlDataSchemaVer.model_rebuild()
METADATALICENSE.model_rebuild()
HdlDataLicense.model_rebuild()
RESOURCE.model_rebuild()
HdlDataResourceInfo.model_rebuild()
RELATED.model_rebuild()
HdlDataRelated.model_rebuild()
CHANGES.model_rebuild()
HdlDataLog.model_rebuild()
HandleRecordContainer.model_rebuild()
Pid4CatRelation.model_rebuild()
ResourceInfo.model_rebuild()
LogRecord.model_rebuild()
Agent.model_rebuild()
RepresentationVariant.model_rebuild()
RelatedIdentifier.model_rebuild()
PurlIdentifier.model_rebuild()
DoiIdentifier.model_rebuild()
HandleIdentifier.model_rebuild()
ArkIdentifier.model_rebuild()
UrnIdentifier.model_rebuild()
GtinIdentifier.model_rebuild()
ExampleIdentifier.model_rebuild()
Pid4CatRecord.model_rebuild()
