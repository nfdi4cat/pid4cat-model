from __future__ import annotations

import re
from datetime import datetime
from enum import Enum
from typing import Any, ClassVar, Dict, List, Literal, Optional, Union

from pydantic import BaseModel, ConfigDict, Field, RootModel, field_validator


metamodel_version = "None"
version = "None"


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
        "description": "A LinkML model for PIDs for resources in catalysis (pid4cat). "
        "pid4cat is a handle system based persistent identifier (PID) "
        "for digital or physical resources used in the catalysis "
        "research process. The handle record is used to store "
        "additional metadata about the PID besides the obligatory "
        "landing page URL.\n"
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
        "todos": ["Set required attribute where needed."],
    }
)


class MEDIATypes(str, Enum):
    applicationSOLIDUS1d_interleaved_parityfec = "application/1d-interleaved-parityfec"
    applicationSOLIDUS3gpdash_qoe_reportPLUS_SIGNxml = (
        "application/3gpdash-qoe-report+xml"
    )
    applicationSOLIDUS3gppHalPLUS_SIGNjson = "application/3gppHal+json"
    applicationSOLIDUS3gppHalFormsPLUS_SIGNjson = "application/3gppHalForms+json"
    applicationSOLIDUS3gpp_imsPLUS_SIGNxml = "application/3gpp-ims+xml"
    applicationSOLIDUSA2L = "application/A2L"
    applicationSOLIDUSacePLUS_SIGNcbor = "application/ace+cbor"
    applicationSOLIDUSacePLUS_SIGNjson = "application/ace+json"
    applicationSOLIDUSace_groupcommPLUS_SIGNcbor = "application/ace-groupcomm+cbor"
    applicationSOLIDUSace_trlPLUS_SIGNcbor = "application/ace-trl+cbor"
    applicationSOLIDUSactivemessage = "application/activemessage"
    applicationSOLIDUSactivityPLUS_SIGNjson = "application/activity+json"
    applicationSOLIDUSaifPLUS_SIGNcbor = "application/aif+cbor"
    applicationSOLIDUSaifPLUS_SIGNjson = "application/aif+json"
    applicationSOLIDUSalto_cdniPLUS_SIGNjson = "application/alto-cdni+json"
    applicationSOLIDUSalto_cdnifilterPLUS_SIGNjson = "application/alto-cdnifilter+json"
    applicationSOLIDUSalto_costmapPLUS_SIGNjson = "application/alto-costmap+json"
    applicationSOLIDUSalto_costmapfilterPLUS_SIGNjson = (
        "application/alto-costmapfilter+json"
    )
    applicationSOLIDUSalto_directoryPLUS_SIGNjson = "application/alto-directory+json"
    applicationSOLIDUSalto_endpointcostPLUS_SIGNjson = (
        "application/alto-endpointcost+json"
    )
    applicationSOLIDUSalto_endpointcostparamsPLUS_SIGNjson = (
        "application/alto-endpointcostparams+json"
    )
    applicationSOLIDUSalto_endpointpropPLUS_SIGNjson = (
        "application/alto-endpointprop+json"
    )
    applicationSOLIDUSalto_endpointpropparamsPLUS_SIGNjson = (
        "application/alto-endpointpropparams+json"
    )
    applicationSOLIDUSalto_errorPLUS_SIGNjson = "application/alto-error+json"
    applicationSOLIDUSalto_networkmapPLUS_SIGNjson = "application/alto-networkmap+json"
    applicationSOLIDUSalto_networkmapfilterPLUS_SIGNjson = (
        "application/alto-networkmapfilter+json"
    )
    applicationSOLIDUSalto_propmapPLUS_SIGNjson = "application/alto-propmap+json"
    applicationSOLIDUSalto_propmapparamsPLUS_SIGNjson = (
        "application/alto-propmapparams+json"
    )
    applicationSOLIDUSalto_tipsPLUS_SIGNjson = "application/alto-tips+json"
    applicationSOLIDUSalto_tipsparamsPLUS_SIGNjson = "application/alto-tipsparams+json"
    applicationSOLIDUSalto_updatestreamcontrolPLUS_SIGNjson = (
        "application/alto-updatestreamcontrol+json"
    )
    applicationSOLIDUSalto_updatestreamparamsPLUS_SIGNjson = (
        "application/alto-updatestreamparams+json"
    )
    applicationSOLIDUSAML = "application/AML"
    applicationSOLIDUSandrew_inset = "application/andrew-inset"
    applicationSOLIDUSapplefile = "application/applefile"
    applicationSOLIDUSatPLUS_SIGNjwt = "application/at+jwt"
    applicationSOLIDUSATF = "application/ATF"
    applicationSOLIDUSATFX = "application/ATFX"
    applicationSOLIDUSatomPLUS_SIGNxml = "application/atom+xml"
    applicationSOLIDUSatomcatPLUS_SIGNxml = "application/atomcat+xml"
    applicationSOLIDUSatomdeletedPLUS_SIGNxml = "application/atomdeleted+xml"
    applicationSOLIDUSatomicmail = "application/atomicmail"
    applicationSOLIDUSatomsvcPLUS_SIGNxml = "application/atomsvc+xml"
    applicationSOLIDUSatsc_dwdPLUS_SIGNxml = "application/atsc-dwd+xml"
    applicationSOLIDUSatsc_dynamic_event_message = (
        "application/atsc-dynamic-event-message"
    )
    applicationSOLIDUSatsc_heldPLUS_SIGNxml = "application/atsc-held+xml"
    applicationSOLIDUSatsc_rdtPLUS_SIGNjson = "application/atsc-rdt+json"
    applicationSOLIDUSatsc_rsatPLUS_SIGNxml = "application/atsc-rsat+xml"
    applicationSOLIDUSATXML = "application/ATXML"
    applicationSOLIDUSauth_policyPLUS_SIGNxml = "application/auth-policy+xml"
    applicationSOLIDUSautomationml_amlPLUS_SIGNxml = "application/automationml-aml+xml"
    applicationSOLIDUSautomationml_amlxPLUS_SIGNzip = (
        "application/automationml-amlx+zip"
    )
    applicationSOLIDUSbacnet_xddPLUS_SIGNzip = "application/bacnet-xdd+zip"
    applicationSOLIDUSbatch_SMTP = "application/batch-SMTP"
    applicationSOLIDUSbeepPLUS_SIGNxml = "application/beep+xml"
    applicationSOLIDUSbufr = "application/bufr"
    applicationSOLIDUSc2pa = "application/c2pa"
    applicationSOLIDUScalendarPLUS_SIGNjson = "application/calendar+json"
    applicationSOLIDUScalendarPLUS_SIGNxml = "application/calendar+xml"
    applicationSOLIDUScall_completion = "application/call-completion"
    applicationSOLIDUSCALS_1840 = "application/CALS-1840"
    applicationSOLIDUScaptivePLUS_SIGNjson = "application/captive+json"
    applicationSOLIDUScbor = "application/cbor"
    applicationSOLIDUScbor_seq = "application/cbor-seq"
    applicationSOLIDUScccex = "application/cccex"
    applicationSOLIDUSccmpPLUS_SIGNxml = "application/ccmp+xml"
    applicationSOLIDUSccxmlPLUS_SIGNxml = "application/ccxml+xml"
    applicationSOLIDUScdaPLUS_SIGNxml = "application/cda+xml"
    applicationSOLIDUSCDFXPLUS_SIGNXML = "application/CDFX+XML"
    applicationSOLIDUScdmi_capability = "application/cdmi-capability"
    applicationSOLIDUScdmi_container = "application/cdmi-container"
    applicationSOLIDUScdmi_domain = "application/cdmi-domain"
    applicationSOLIDUScdmi_object = "application/cdmi-object"
    applicationSOLIDUScdmi_queue = "application/cdmi-queue"
    applicationSOLIDUScdni = "application/cdni"
    applicationSOLIDUScePLUS_SIGNcbor = "application/ce+cbor"
    applicationSOLIDUSCEA = "application/CEA"
    applicationSOLIDUScea_2018PLUS_SIGNxml = "application/cea-2018+xml"
    applicationSOLIDUScellmlPLUS_SIGNxml = "application/cellml+xml"
    applicationSOLIDUScfw = "application/cfw"
    applicationSOLIDUScid_edhocPLUS_SIGNcbor_seq = "application/cid-edhoc+cbor-seq"
    applicationSOLIDUScityPLUS_SIGNjson = "application/city+json"
    applicationSOLIDUScityPLUS_SIGNjson_seq = "application/city+json-seq"
    applicationSOLIDUSclr = "application/clr"
    applicationSOLIDUSclue_infoPLUS_SIGNxml = "application/clue_info+xml"
    applicationSOLIDUScluePLUS_SIGNxml = "application/clue+xml"
    applicationSOLIDUScms = "application/cms"
    applicationSOLIDUScnrpPLUS_SIGNxml = "application/cnrp+xml"
    applicationSOLIDUScoap_groupPLUS_SIGNjson = "application/coap-group+json"
    applicationSOLIDUScoap_payload = "application/coap-payload"
    applicationSOLIDUScommonground = "application/commonground"
    applicationSOLIDUSconcise_problem_detailsPLUS_SIGNcbor = (
        "application/concise-problem-details+cbor"
    )
    applicationSOLIDUSconference_infoPLUS_SIGNxml = "application/conference-info+xml"
    applicationSOLIDUScose = "application/cose"
    applicationSOLIDUScose_key = "application/cose-key"
    applicationSOLIDUScose_key_set = "application/cose-key-set"
    applicationSOLIDUScose_x509 = "application/cose-x509"
    applicationSOLIDUScplPLUS_SIGNxml = "application/cpl+xml"
    applicationSOLIDUScsrattrs = "application/csrattrs"
    applicationSOLIDUScstaPLUS_SIGNxml = "application/csta+xml"
    applicationSOLIDUSCSTAdataPLUS_SIGNxml = "application/CSTAdata+xml"
    applicationSOLIDUScsvmPLUS_SIGNjson = "application/csvm+json"
    applicationSOLIDUScwl = "application/cwl"
    applicationSOLIDUScwlPLUS_SIGNjson = "application/cwl+json"
    applicationSOLIDUScwlPLUS_SIGNyaml = "application/cwl+yaml"
    applicationSOLIDUScwt = "application/cwt"
    applicationSOLIDUScybercash = "application/cybercash"
    applicationSOLIDUSdashPLUS_SIGNxml = "application/dash+xml"
    applicationSOLIDUSdashdelta = "application/dashdelta"
    applicationSOLIDUSdash_patchPLUS_SIGNxml = "application/dash-patch+xml"
    applicationSOLIDUSdavmountPLUS_SIGNxml = "application/davmount+xml"
    applicationSOLIDUSdca_rft = "application/dca-rft"
    applicationSOLIDUSDCD = "application/DCD"
    applicationSOLIDUSdec_dx = "application/dec-dx"
    applicationSOLIDUSdialog_infoPLUS_SIGNxml = "application/dialog-info+xml"
    applicationSOLIDUSdicom = "application/dicom"
    applicationSOLIDUSdicomPLUS_SIGNjson = "application/dicom+json"
    applicationSOLIDUSdicomPLUS_SIGNxml = "application/dicom+xml"
    applicationSOLIDUSDII = "application/DII"
    applicationSOLIDUSDIT = "application/DIT"
    applicationSOLIDUSdns = "application/dns"
    applicationSOLIDUSdnsPLUS_SIGNjson = "application/dns+json"
    applicationSOLIDUSdns_message = "application/dns-message"
    applicationSOLIDUSdotsPLUS_SIGNcbor = "application/dots+cbor"
    applicationSOLIDUSdpopPLUS_SIGNjwt = "application/dpop+jwt"
    applicationSOLIDUSdskppPLUS_SIGNxml = "application/dskpp+xml"
    applicationSOLIDUSdsscPLUS_SIGNder = "application/dssc+der"
    applicationSOLIDUSdsscPLUS_SIGNxml = "application/dssc+xml"
    applicationSOLIDUSdvcs = "application/dvcs"
    applicationSOLIDUSeatPLUS_SIGNcwt = "application/eat+cwt"
    applicationSOLIDUSeatPLUS_SIGNjwt = "application/eat+jwt"
    applicationSOLIDUSeat_bunPLUS_SIGNcbor = "application/eat-bun+cbor"
    applicationSOLIDUSeat_bunPLUS_SIGNjson = "application/eat-bun+json"
    applicationSOLIDUSeat_ucsPLUS_SIGNcbor = "application/eat-ucs+cbor"
    applicationSOLIDUSeat_ucsPLUS_SIGNjson = "application/eat-ucs+json"
    applicationSOLIDUSecmascript = "application/ecmascript"
    applicationSOLIDUSedhocPLUS_SIGNcbor_seq = "application/edhoc+cbor-seq"
    applicationSOLIDUSEDI_consent = "application/EDI-consent"
    applicationSOLIDUSEDIFACT = "application/EDIFACT"
    applicationSOLIDUSEDI_X12 = "application/EDI-X12"
    applicationSOLIDUSefi = "application/efi"
    applicationSOLIDUSelmPLUS_SIGNjson = "application/elm+json"
    applicationSOLIDUSelmPLUS_SIGNxml = "application/elm+xml"
    applicationSOLIDUSEmergencyCallDataFULL_STOPcapPLUS_SIGNxml = (
        "application/EmergencyCallData.cap+xml"
    )
    applicationSOLIDUSEmergencyCallDataFULL_STOPCommentPLUS_SIGNxml = (
        "application/EmergencyCallData.Comment+xml"
    )
    applicationSOLIDUSEmergencyCallDataFULL_STOPControlPLUS_SIGNxml = (
        "application/EmergencyCallData.Control+xml"
    )
    applicationSOLIDUSEmergencyCallDataFULL_STOPDeviceInfoPLUS_SIGNxml = (
        "application/EmergencyCallData.DeviceInfo+xml"
    )
    applicationSOLIDUSEmergencyCallDataFULL_STOPeCallFULL_STOPMSD = (
        "application/EmergencyCallData.eCall.MSD"
    )
    applicationSOLIDUSEmergencyCallDataFULL_STOPLegacyESNPLUS_SIGNjson = (
        "application/EmergencyCallData.LegacyESN+json"
    )
    applicationSOLIDUSEmergencyCallDataFULL_STOPProviderInfoPLUS_SIGNxml = (
        "application/EmergencyCallData.ProviderInfo+xml"
    )
    applicationSOLIDUSEmergencyCallDataFULL_STOPServiceInfoPLUS_SIGNxml = (
        "application/EmergencyCallData.ServiceInfo+xml"
    )
    applicationSOLIDUSEmergencyCallDataFULL_STOPSubscriberInfoPLUS_SIGNxml = (
        "application/EmergencyCallData.SubscriberInfo+xml"
    )
    applicationSOLIDUSEmergencyCallDataFULL_STOPVEDSPLUS_SIGNxml = (
        "application/EmergencyCallData.VEDS+xml"
    )
    applicationSOLIDUSemmaPLUS_SIGNxml = "application/emma+xml"
    applicationSOLIDUSemotionmlPLUS_SIGNxml = "application/emotionml+xml"
    applicationSOLIDUSencaprtp = "application/encaprtp"
    applicationSOLIDUSentity_statementPLUS_SIGNjwt = "application/entity-statement+jwt"
    applicationSOLIDUSeppPLUS_SIGNxml = "application/epp+xml"
    applicationSOLIDUSepubPLUS_SIGNzip = "application/epub+zip"
    applicationSOLIDUSeshop = "application/eshop"
    applicationSOLIDUSexample = "application/example"
    applicationSOLIDUSexi = "application/exi"
    applicationSOLIDUSexpect_ct_reportPLUS_SIGNjson = (
        "application/expect-ct-report+json"
    )
    applicationSOLIDUSexpress = "application/express"
    applicationSOLIDUSfastinfoset = "application/fastinfoset"
    applicationSOLIDUSfastsoap = "application/fastsoap"
    applicationSOLIDUSfdf = "application/fdf"
    applicationSOLIDUSfdtPLUS_SIGNxml = "application/fdt+xml"
    applicationSOLIDUSfhirPLUS_SIGNjson = "application/fhir+json"
    applicationSOLIDUSfhirPLUS_SIGNxml = "application/fhir+xml"
    applicationSOLIDUSfits = "application/fits"
    applicationSOLIDUSflexfec = "application/flexfec"
    applicationSOLIDUSfont_sfnt = "application/font-sfnt"
    applicationSOLIDUSfont_tdpfr = "application/font-tdpfr"
    applicationSOLIDUSfont_woff = "application/font-woff"
    applicationSOLIDUSframework_attributesPLUS_SIGNxml = (
        "application/framework-attributes+xml"
    )
    applicationSOLIDUSgeoPLUS_SIGNjson = "application/geo+json"
    applicationSOLIDUSgeoPLUS_SIGNjson_seq = "application/geo+json-seq"
    applicationSOLIDUSgeopackagePLUS_SIGNsqlite3 = "application/geopackage+sqlite3"
    applicationSOLIDUSgeoposePLUS_SIGNjson = "application/geopose+json"
    applicationSOLIDUSgeoxacmlPLUS_SIGNjson = "application/geoxacml+json"
    applicationSOLIDUSgeoxacmlPLUS_SIGNxml = "application/geoxacml+xml"
    applicationSOLIDUSgltf_buffer = "application/gltf-buffer"
    applicationSOLIDUSgmlPLUS_SIGNxml = "application/gml+xml"
    applicationSOLIDUSgnap_binding_jws = "application/gnap-binding-jws"
    applicationSOLIDUSgnap_binding_jwsd = "application/gnap-binding-jwsd"
    applicationSOLIDUSgnap_binding_rotation_jws = (
        "application/gnap-binding-rotation-jws"
    )
    applicationSOLIDUSgnap_binding_rotation_jwsd = (
        "application/gnap-binding-rotation-jwsd"
    )
    applicationSOLIDUSgrib = "application/grib"
    applicationSOLIDUSgzip = "application/gzip"
    applicationSOLIDUSH224 = "application/H224"
    applicationSOLIDUSheldPLUS_SIGNxml = "application/held+xml"
    applicationSOLIDUShl7v2PLUS_SIGNxml = "application/hl7v2+xml"
    applicationSOLIDUShttp = "application/http"
    applicationSOLIDUShyperstudio = "application/hyperstudio"
    applicationSOLIDUSibe_key_requestPLUS_SIGNxml = "application/ibe-key-request+xml"
    applicationSOLIDUSibe_pkg_replyPLUS_SIGNxml = "application/ibe-pkg-reply+xml"
    applicationSOLIDUSibe_pp_data = "application/ibe-pp-data"
    applicationSOLIDUSiges = "application/iges"
    applicationSOLIDUSim_iscomposingPLUS_SIGNxml = "application/im-iscomposing+xml"
    applicationSOLIDUSindex = "application/index"
    applicationSOLIDUSindexFULL_STOPcmd = "application/index.cmd"
    applicationSOLIDUSindexFULL_STOPobj = "application/index.obj"
    applicationSOLIDUSindexFULL_STOPresponse = "application/index.response"
    applicationSOLIDUSindexFULL_STOPvnd = "application/index.vnd"
    applicationSOLIDUSinkmlPLUS_SIGNxml = "application/inkml+xml"
    applicationSOLIDUSIOTP = "application/IOTP"
    applicationSOLIDUSipfix = "application/ipfix"
    applicationSOLIDUSipp = "application/ipp"
    applicationSOLIDUSISUP = "application/ISUP"
    applicationSOLIDUSitsPLUS_SIGNxml = "application/its+xml"
    applicationSOLIDUSjava_archive = "application/java-archive"
    applicationSOLIDUSjavascript = "application/javascript"
    applicationSOLIDUSjf2feedPLUS_SIGNjson = "application/jf2feed+json"
    applicationSOLIDUSjose = "application/jose"
    applicationSOLIDUSjosePLUS_SIGNjson = "application/jose+json"
    applicationSOLIDUSjrdPLUS_SIGNjson = "application/jrd+json"
    applicationSOLIDUSjscalendarPLUS_SIGNjson = "application/jscalendar+json"
    applicationSOLIDUSjscontactPLUS_SIGNjson = "application/jscontact+json"
    applicationSOLIDUSjson = "application/json"
    applicationSOLIDUSjson_patchPLUS_SIGNjson = "application/json-patch+json"
    applicationSOLIDUSjsonpath = "application/jsonpath"
    applicationSOLIDUSjson_seq = "application/json-seq"
    applicationSOLIDUSjwkPLUS_SIGNjson = "application/jwk+json"
    applicationSOLIDUSjwk_setPLUS_SIGNjson = "application/jwk-set+json"
    applicationSOLIDUSjwk_setPLUS_SIGNjwt = "application/jwk-set+jwt"
    applicationSOLIDUSjwt = "application/jwt"
    applicationSOLIDUSkpml_requestPLUS_SIGNxml = "application/kpml-request+xml"
    applicationSOLIDUSkpml_responsePLUS_SIGNxml = "application/kpml-response+xml"
    applicationSOLIDUSldPLUS_SIGNjson = "application/ld+json"
    applicationSOLIDUSlgrPLUS_SIGNxml = "application/lgr+xml"
    applicationSOLIDUSlink_format = "application/link-format"
    applicationSOLIDUSlinkset = "application/linkset"
    applicationSOLIDUSlinksetPLUS_SIGNjson = "application/linkset+json"
    applicationSOLIDUSload_controlPLUS_SIGNxml = "application/load-control+xml"
    applicationSOLIDUSlogoutPLUS_SIGNjwt = "application/logout+jwt"
    applicationSOLIDUSlostPLUS_SIGNxml = "application/lost+xml"
    applicationSOLIDUSlostsyncPLUS_SIGNxml = "application/lostsync+xml"
    applicationSOLIDUSlpfPLUS_SIGNzip = "application/lpf+zip"
    applicationSOLIDUSLXF = "application/LXF"
    applicationSOLIDUSmac_binhex40 = "application/mac-binhex40"
    applicationSOLIDUSmacwriteii = "application/macwriteii"
    applicationSOLIDUSmadsPLUS_SIGNxml = "application/mads+xml"
    applicationSOLIDUSmanifestPLUS_SIGNjson = "application/manifest+json"
    applicationSOLIDUSmarc = "application/marc"
    applicationSOLIDUSmarcxmlPLUS_SIGNxml = "application/marcxml+xml"
    applicationSOLIDUSmathematica = "application/mathematica"
    applicationSOLIDUSmathmlPLUS_SIGNxml = "application/mathml+xml"
    applicationSOLIDUSmathml_contentPLUS_SIGNxml = "application/mathml-content+xml"
    applicationSOLIDUSmathml_presentationPLUS_SIGNxml = (
        "application/mathml-presentation+xml"
    )
    applicationSOLIDUSmbms_associated_procedure_descriptionPLUS_SIGNxml = (
        "application/mbms-associated-procedure-description+xml"
    )
    applicationSOLIDUSmbms_deregisterPLUS_SIGNxml = "application/mbms-deregister+xml"
    applicationSOLIDUSmbms_envelopePLUS_SIGNxml = "application/mbms-envelope+xml"
    applicationSOLIDUSmbms_mskPLUS_SIGNxml = "application/mbms-msk+xml"
    applicationSOLIDUSmbms_msk_responsePLUS_SIGNxml = (
        "application/mbms-msk-response+xml"
    )
    applicationSOLIDUSmbms_protection_descriptionPLUS_SIGNxml = (
        "application/mbms-protection-description+xml"
    )
    applicationSOLIDUSmbms_reception_reportPLUS_SIGNxml = (
        "application/mbms-reception-report+xml"
    )
    applicationSOLIDUSmbms_registerPLUS_SIGNxml = "application/mbms-register+xml"
    applicationSOLIDUSmbms_register_responsePLUS_SIGNxml = (
        "application/mbms-register-response+xml"
    )
    applicationSOLIDUSmbms_schedulePLUS_SIGNxml = "application/mbms-schedule+xml"
    applicationSOLIDUSmbms_user_service_descriptionPLUS_SIGNxml = (
        "application/mbms-user-service-description+xml"
    )
    applicationSOLIDUSmbox = "application/mbox"
    applicationSOLIDUSmedia_controlPLUS_SIGNxml = "application/media_control+xml"
    applicationSOLIDUSmedia_policy_datasetPLUS_SIGNxml = (
        "application/media-policy-dataset+xml"
    )
    applicationSOLIDUSmediaservercontrolPLUS_SIGNxml = (
        "application/mediaservercontrol+xml"
    )
    applicationSOLIDUSmerge_patchPLUS_SIGNjson = "application/merge-patch+json"
    applicationSOLIDUSmetalink4PLUS_SIGNxml = "application/metalink4+xml"
    applicationSOLIDUSmetsPLUS_SIGNxml = "application/mets+xml"
    applicationSOLIDUSMF4 = "application/MF4"
    applicationSOLIDUSmikey = "application/mikey"
    applicationSOLIDUSmipc = "application/mipc"
    applicationSOLIDUSmissing_blocksPLUS_SIGNcbor_seq = (
        "application/missing-blocks+cbor-seq"
    )
    applicationSOLIDUSmmt_aeiPLUS_SIGNxml = "application/mmt-aei+xml"
    applicationSOLIDUSmmt_usdPLUS_SIGNxml = "application/mmt-usd+xml"
    applicationSOLIDUSmodsPLUS_SIGNxml = "application/mods+xml"
    applicationSOLIDUSmosskey_data = "application/mosskey-data"
    applicationSOLIDUSmosskey_request = "application/mosskey-request"
    applicationSOLIDUSmoss_keys = "application/moss-keys"
    applicationSOLIDUSmoss_signature = "application/moss-signature"
    applicationSOLIDUSmp21 = "application/mp21"
    applicationSOLIDUSmp4 = "application/mp4"
    applicationSOLIDUSmpeg4_generic = "application/mpeg4-generic"
    applicationSOLIDUSmpeg4_iod = "application/mpeg4-iod"
    applicationSOLIDUSmpeg4_iod_xmt = "application/mpeg4-iod-xmt"
    applicationSOLIDUSmrb_consumerPLUS_SIGNxml = "application/mrb-consumer+xml"
    applicationSOLIDUSmrb_publishPLUS_SIGNxml = "application/mrb-publish+xml"
    applicationSOLIDUSmsc_ivrPLUS_SIGNxml = "application/msc-ivr+xml"
    applicationSOLIDUSmsc_mixerPLUS_SIGNxml = "application/msc-mixer+xml"
    applicationSOLIDUSmsword = "application/msword"
    applicationSOLIDUSmudPLUS_SIGNjson = "application/mud+json"
    applicationSOLIDUSmultipart_core = "application/multipart-core"
    applicationSOLIDUSmxf = "application/mxf"
    applicationSOLIDUSnasdata = "application/nasdata"
    applicationSOLIDUSnews_checkgroups = "application/news-checkgroups"
    applicationSOLIDUSnews_groupinfo = "application/news-groupinfo"
    applicationSOLIDUSnews_transmission = "application/news-transmission"
    applicationSOLIDUSnlsmlPLUS_SIGNxml = "application/nlsml+xml"
    applicationSOLIDUSnode = "application/node"
    applicationSOLIDUSn_quads = "application/n-quads"
    applicationSOLIDUSnss = "application/nss"
    applicationSOLIDUSn_triples = "application/n-triples"
    applicationSOLIDUSoauth_authz_reqPLUS_SIGNjwt = "application/oauth-authz-req+jwt"
    applicationSOLIDUSoblivious_dns_message = "application/oblivious-dns-message"
    applicationSOLIDUSocsp_request = "application/ocsp-request"
    applicationSOLIDUSocsp_response = "application/ocsp-response"
    applicationSOLIDUSoctet_stream = "application/octet-stream"
    applicationSOLIDUSODA = "application/ODA"
    applicationSOLIDUSodmPLUS_SIGNxml = "application/odm+xml"
    applicationSOLIDUSODX = "application/ODX"
    applicationSOLIDUSoebps_packagePLUS_SIGNxml = "application/oebps-package+xml"
    applicationSOLIDUSogg = "application/ogg"
    applicationSOLIDUSohttp_keys = "application/ohttp-keys"
    applicationSOLIDUSopc_nodesetPLUS_SIGNxml = "application/opc-nodeset+xml"
    applicationSOLIDUSoscore = "application/oscore"
    applicationSOLIDUSoxps = "application/oxps"
    applicationSOLIDUSp21 = "application/p21"
    applicationSOLIDUSp21PLUS_SIGNzip = "application/p21+zip"
    applicationSOLIDUSp2p_overlayPLUS_SIGNxml = "application/p2p-overlay+xml"
    applicationSOLIDUSparityfec = "application/parityfec"
    applicationSOLIDUSpassport = "application/passport"
    applicationSOLIDUSpatch_ops_errorPLUS_SIGNxml = "application/patch-ops-error+xml"
    applicationSOLIDUSpdf = "application/pdf"
    applicationSOLIDUSPDX = "application/PDX"
    applicationSOLIDUSpem_certificate_chain = "application/pem-certificate-chain"
    applicationSOLIDUSpgp_encrypted = "application/pgp-encrypted"
    applicationSOLIDUSpgp_keys = "application/pgp-keys"
    applicationSOLIDUSpgp_signature = "application/pgp-signature"
    applicationSOLIDUSpidfPLUS_SIGNxml = "application/pidf+xml"
    applicationSOLIDUSpidf_diffPLUS_SIGNxml = "application/pidf-diff+xml"
    applicationSOLIDUSpkcs10 = "application/pkcs10"
    applicationSOLIDUSpkcs12 = "application/pkcs12"
    applicationSOLIDUSpkcs7_mime = "application/pkcs7-mime"
    applicationSOLIDUSpkcs7_signature = "application/pkcs7-signature"
    applicationSOLIDUSpkcs8 = "application/pkcs8"
    applicationSOLIDUSpkcs8_encrypted = "application/pkcs8-encrypted"
    applicationSOLIDUSpkix_attr_cert = "application/pkix-attr-cert"
    applicationSOLIDUSpkix_cert = "application/pkix-cert"
    applicationSOLIDUSpkixcmp = "application/pkixcmp"
    applicationSOLIDUSpkix_crl = "application/pkix-crl"
    applicationSOLIDUSpkix_pkipath = "application/pkix-pkipath"
    applicationSOLIDUSplsPLUS_SIGNxml = "application/pls+xml"
    applicationSOLIDUSpoc_settingsPLUS_SIGNxml = "application/poc-settings+xml"
    applicationSOLIDUSpostscript = "application/postscript"
    applicationSOLIDUSppsp_trackerPLUS_SIGNjson = "application/ppsp-tracker+json"
    applicationSOLIDUSprivate_token_issuer_directory = (
        "application/private-token-issuer-directory"
    )
    applicationSOLIDUSprivate_token_request = "application/private-token-request"
    applicationSOLIDUSprivate_token_response = "application/private-token-response"
    applicationSOLIDUSproblemPLUS_SIGNjson = "application/problem+json"
    applicationSOLIDUSproblemPLUS_SIGNxml = "application/problem+xml"
    applicationSOLIDUSprovenancePLUS_SIGNxml = "application/provenance+xml"
    applicationSOLIDUSprovided_claimsPLUS_SIGNjwt = "application/provided-claims+jwt"
    applicationSOLIDUSprsFULL_STOPalvestrandFULL_STOPtitrax_sheet = (
        "application/prs.alvestrand.titrax-sheet"
    )
    applicationSOLIDUSprsFULL_STOPcww = "application/prs.cww"
    applicationSOLIDUSprsFULL_STOPcyn = "application/prs.cyn"
    applicationSOLIDUSprsFULL_STOPhpubPLUS_SIGNzip = "application/prs.hpub+zip"
    applicationSOLIDUSprsFULL_STOPimplied_documentPLUS_SIGNxml = (
        "application/prs.implied-document+xml"
    )
    applicationSOLIDUSprsFULL_STOPimplied_executable = (
        "application/prs.implied-executable"
    )
    applicationSOLIDUSprsFULL_STOPimplied_objectPLUS_SIGNjson = (
        "application/prs.implied-object+json"
    )
    applicationSOLIDUSprsFULL_STOPimplied_objectPLUS_SIGNjson_seq = (
        "application/prs.implied-object+json-seq"
    )
    applicationSOLIDUSprsFULL_STOPimplied_objectPLUS_SIGNyaml = (
        "application/prs.implied-object+yaml"
    )
    applicationSOLIDUSprsFULL_STOPimplied_structure = (
        "application/prs.implied-structure"
    )
    applicationSOLIDUSprsFULL_STOPmayfile = "application/prs.mayfile"
    applicationSOLIDUSprsFULL_STOPnprend = "application/prs.nprend"
    applicationSOLIDUSprsFULL_STOPplucker = "application/prs.plucker"
    applicationSOLIDUSprsFULL_STOPrdf_xml_crypt = "application/prs.rdf-xml-crypt"
    applicationSOLIDUSprsFULL_STOPvcfbzip2 = "application/prs.vcfbzip2"
    applicationSOLIDUSprsFULL_STOPxsfPLUS_SIGNxml = "application/prs.xsf+xml"
    applicationSOLIDUSpskcPLUS_SIGNxml = "application/pskc+xml"
    applicationSOLIDUSpvdPLUS_SIGNjson = "application/pvd+json"
    applicationSOLIDUSQSIG = "application/QSIG"
    applicationSOLIDUSraptorfec = "application/raptorfec"
    applicationSOLIDUSrdapPLUS_SIGNjson = "application/rdap+json"
    applicationSOLIDUSrdfPLUS_SIGNxml = "application/rdf+xml"
    applicationSOLIDUSreginfoPLUS_SIGNxml = "application/reginfo+xml"
    applicationSOLIDUSrelax_ng_compact_syntax = "application/relax-ng-compact-syntax"
    applicationSOLIDUSremote_printing = "application/remote-printing"
    applicationSOLIDUSreputonPLUS_SIGNjson = "application/reputon+json"
    applicationSOLIDUSresolve_responsePLUS_SIGNjwt = "application/resolve-response+jwt"
    applicationSOLIDUSresource_listsPLUS_SIGNxml = "application/resource-lists+xml"
    applicationSOLIDUSresource_lists_diffPLUS_SIGNxml = (
        "application/resource-lists-diff+xml"
    )
    applicationSOLIDUSrfcPLUS_SIGNxml = "application/rfc+xml"
    applicationSOLIDUSriscos = "application/riscos"
    applicationSOLIDUSrlmiPLUS_SIGNxml = "application/rlmi+xml"
    applicationSOLIDUSrls_servicesPLUS_SIGNxml = "application/rls-services+xml"
    applicationSOLIDUSroute_apdPLUS_SIGNxml = "application/route-apd+xml"
    applicationSOLIDUSroute_s_tsidPLUS_SIGNxml = "application/route-s-tsid+xml"
    applicationSOLIDUSroute_usdPLUS_SIGNxml = "application/route-usd+xml"
    applicationSOLIDUSrpki_checklist = "application/rpki-checklist"
    applicationSOLIDUSrpki_ghostbusters = "application/rpki-ghostbusters"
    applicationSOLIDUSrpki_manifest = "application/rpki-manifest"
    applicationSOLIDUSrpki_publication = "application/rpki-publication"
    applicationSOLIDUSrpki_roa = "application/rpki-roa"
    applicationSOLIDUSrpki_signed_tal = "application/rpki-signed-tal"
    applicationSOLIDUSrpki_updown = "application/rpki-updown"
    applicationSOLIDUSrtf = "application/rtf"
    applicationSOLIDUSrtploopback = "application/rtploopback"
    applicationSOLIDUSrtx = "application/rtx"
    applicationSOLIDUSsamlassertionPLUS_SIGNxml = "application/samlassertion+xml"
    applicationSOLIDUSsamlmetadataPLUS_SIGNxml = "application/samlmetadata+xml"
    applicationSOLIDUSsarifPLUS_SIGNjson = "application/sarif+json"
    applicationSOLIDUSsarif_external_propertiesPLUS_SIGNjson = (
        "application/sarif-external-properties+json"
    )
    applicationSOLIDUSsbe = "application/sbe"
    applicationSOLIDUSsbmlPLUS_SIGNxml = "application/sbml+xml"
    applicationSOLIDUSscaipPLUS_SIGNxml = "application/scaip+xml"
    applicationSOLIDUSscimPLUS_SIGNjson = "application/scim+json"
    applicationSOLIDUSscvp_cv_request = "application/scvp-cv-request"
    applicationSOLIDUSscvp_cv_response = "application/scvp-cv-response"
    applicationSOLIDUSscvp_vp_request = "application/scvp-vp-request"
    applicationSOLIDUSscvp_vp_response = "application/scvp-vp-response"
    applicationSOLIDUSsdp = "application/sdp"
    applicationSOLIDUSseceventPLUS_SIGNjwt = "application/secevent+jwt"
    applicationSOLIDUSsenmlPLUS_SIGNcbor = "application/senml+cbor"
    applicationSOLIDUSsenmlPLUS_SIGNjson = "application/senml+json"
    applicationSOLIDUSsenmlPLUS_SIGNxml = "application/senml+xml"
    applicationSOLIDUSsenml_etchPLUS_SIGNcbor = "application/senml-etch+cbor"
    applicationSOLIDUSsenml_etchPLUS_SIGNjson = "application/senml-etch+json"
    applicationSOLIDUSsenml_exi = "application/senml-exi"
    applicationSOLIDUSsensmlPLUS_SIGNcbor = "application/sensml+cbor"
    applicationSOLIDUSsensmlPLUS_SIGNjson = "application/sensml+json"
    applicationSOLIDUSsensmlPLUS_SIGNxml = "application/sensml+xml"
    applicationSOLIDUSsensml_exi = "application/sensml-exi"
    applicationSOLIDUSsepPLUS_SIGNxml = "application/sep+xml"
    applicationSOLIDUSsep_exi = "application/sep-exi"
    applicationSOLIDUSsession_info = "application/session-info"
    applicationSOLIDUSset_payment = "application/set-payment"
    applicationSOLIDUSset_payment_initiation = "application/set-payment-initiation"
    applicationSOLIDUSset_registration = "application/set-registration"
    applicationSOLIDUSset_registration_initiation = (
        "application/set-registration-initiation"
    )
    applicationSOLIDUSSGML = "application/SGML"
    applicationSOLIDUSsgml_open_catalog = "application/sgml-open-catalog"
    applicationSOLIDUSshfPLUS_SIGNxml = "application/shf+xml"
    applicationSOLIDUSsieve = "application/sieve"
    applicationSOLIDUSsimple_filterPLUS_SIGNxml = "application/simple-filter+xml"
    applicationSOLIDUSsimple_message_summary = "application/simple-message-summary"
    applicationSOLIDUSsimpleSymbolContainer = "application/simpleSymbolContainer"
    applicationSOLIDUSsipc = "application/sipc"
    applicationSOLIDUSslate = "application/slate"
    applicationSOLIDUSsmil = "application/smil"
    applicationSOLIDUSsmilPLUS_SIGNxml = "application/smil+xml"
    applicationSOLIDUSsmpte336m = "application/smpte336m"
    applicationSOLIDUSsoapPLUS_SIGNfastinfoset = "application/soap+fastinfoset"
    applicationSOLIDUSsoapPLUS_SIGNxml = "application/soap+xml"
    applicationSOLIDUSsparql_query = "application/sparql-query"
    applicationSOLIDUSsparql_resultsPLUS_SIGNxml = "application/sparql-results+xml"
    applicationSOLIDUSspdxPLUS_SIGNjson = "application/spdx+json"
    applicationSOLIDUSspirits_eventPLUS_SIGNxml = "application/spirits-event+xml"
    applicationSOLIDUSsql = "application/sql"
    applicationSOLIDUSsrgs = "application/srgs"
    applicationSOLIDUSsrgsPLUS_SIGNxml = "application/srgs+xml"
    applicationSOLIDUSsruPLUS_SIGNxml = "application/sru+xml"
    applicationSOLIDUSsslkeylogfile = "application/sslkeylogfile"
    applicationSOLIDUSssmlPLUS_SIGNxml = "application/ssml+xml"
    applicationSOLIDUSST2110_41 = "application/ST2110-41"
    applicationSOLIDUSstixPLUS_SIGNjson = "application/stix+json"
    applicationSOLIDUSstratum = "application/stratum"
    applicationSOLIDUSswidPLUS_SIGNcbor = "application/swid+cbor"
    applicationSOLIDUSswidPLUS_SIGNxml = "application/swid+xml"
    applicationSOLIDUStamp_apex_update = "application/tamp-apex-update"
    applicationSOLIDUStamp_apex_update_confirm = "application/tamp-apex-update-confirm"
    applicationSOLIDUStamp_community_update = "application/tamp-community-update"
    applicationSOLIDUStamp_community_update_confirm = (
        "application/tamp-community-update-confirm"
    )
    applicationSOLIDUStamp_error = "application/tamp-error"
    applicationSOLIDUStamp_sequence_adjust = "application/tamp-sequence-adjust"
    applicationSOLIDUStamp_sequence_adjust_confirm = (
        "application/tamp-sequence-adjust-confirm"
    )
    applicationSOLIDUStamp_status_query = "application/tamp-status-query"
    applicationSOLIDUStamp_status_response = "application/tamp-status-response"
    applicationSOLIDUStamp_update = "application/tamp-update"
    applicationSOLIDUStamp_update_confirm = "application/tamp-update-confirm"
    applicationSOLIDUStaxiiPLUS_SIGNjson = "application/taxii+json"
    applicationSOLIDUStdPLUS_SIGNjson = "application/td+json"
    applicationSOLIDUSteiPLUS_SIGNxml = "application/tei+xml"
    applicationSOLIDUSTETRA_ISI = "application/TETRA_ISI"
    applicationSOLIDUSthraudPLUS_SIGNxml = "application/thraud+xml"
    applicationSOLIDUStimestamped_data = "application/timestamped-data"
    applicationSOLIDUStimestamp_query = "application/timestamp-query"
    applicationSOLIDUStimestamp_reply = "application/timestamp-reply"
    applicationSOLIDUStlsrptPLUS_SIGNgzip = "application/tlsrpt+gzip"
    applicationSOLIDUStlsrptPLUS_SIGNjson = "application/tlsrpt+json"
    applicationSOLIDUStmPLUS_SIGNjson = "application/tm+json"
    applicationSOLIDUStnauthlist = "application/tnauthlist"
    applicationSOLIDUStocPLUS_SIGNcbor = "application/toc+cbor"
    applicationSOLIDUStoken_introspectionPLUS_SIGNjwt = (
        "application/token-introspection+jwt"
    )
    applicationSOLIDUStoml = "application/toml"
    applicationSOLIDUStrickle_ice_sdpfrag = "application/trickle-ice-sdpfrag"
    applicationSOLIDUString = "application/trig"
    applicationSOLIDUStrust_chainPLUS_SIGNjson = "application/trust-chain+json"
    applicationSOLIDUStrust_markPLUS_SIGNjwt = "application/trust-mark+jwt"
    applicationSOLIDUStrust_mark_delegationPLUS_SIGNjwt = (
        "application/trust-mark-delegation+jwt"
    )
    applicationSOLIDUSttmlPLUS_SIGNxml = "application/ttml+xml"
    applicationSOLIDUStve_trigger = "application/tve-trigger"
    applicationSOLIDUStzif = "application/tzif"
    applicationSOLIDUStzif_leap = "application/tzif-leap"
    applicationSOLIDUSuccsPLUS_SIGNcbor = "application/uccs+cbor"
    applicationSOLIDUSujcsPLUS_SIGNjson = "application/ujcs+json"
    applicationSOLIDUSulpfec = "application/ulpfec"
    applicationSOLIDUSurc_grpsheetPLUS_SIGNxml = "application/urc-grpsheet+xml"
    applicationSOLIDUSurc_ressheetPLUS_SIGNxml = "application/urc-ressheet+xml"
    applicationSOLIDUSurc_targetdescPLUS_SIGNxml = "application/urc-targetdesc+xml"
    applicationSOLIDUSurc_uisocketdescPLUS_SIGNxml = "application/urc-uisocketdesc+xml"
    applicationSOLIDUSvc = "application/vc"
    applicationSOLIDUSvcPLUS_SIGNcose = "application/vc+cose"
    applicationSOLIDUSvcPLUS_SIGNjwt = "application/vc+jwt"
    applicationSOLIDUSvcardPLUS_SIGNjson = "application/vcard+json"
    applicationSOLIDUSvcardPLUS_SIGNxml = "application/vcard+xml"
    applicationSOLIDUSvemmi = "application/vemmi"
    applicationSOLIDUSvndFULL_STOP1000mindsFULL_STOPdecision_modelPLUS_SIGNxml = (
        "application/vnd.1000minds.decision-model+xml"
    )
    applicationSOLIDUSvndFULL_STOP1ob = "application/vnd.1ob"
    applicationSOLIDUSvndFULL_STOP3gppFULL_STOP5gnas = "application/vnd.3gpp.5gnas"
    applicationSOLIDUSvndFULL_STOP3gppFULL_STOP5gsa2x = "application/vnd.3gpp.5gsa2x"
    applicationSOLIDUSvndFULL_STOP3gppFULL_STOP5gsa2x_local_service_information = (
        "application/vnd.3gpp.5gsa2x-local-service-information"
    )
    applicationSOLIDUSvndFULL_STOP3gppFULL_STOP5gsv2x = "application/vnd.3gpp.5gsv2x"
    applicationSOLIDUSvndFULL_STOP3gppFULL_STOP5gsv2x_local_service_information = (
        "application/vnd.3gpp.5gsv2x-local-service-information"
    )
    applicationSOLIDUSvndFULL_STOP3gppFULL_STOPaccess_transfer_eventsPLUS_SIGNxml = (
        "application/vnd.3gpp.access-transfer-events+xml"
    )
    applicationSOLIDUSvndFULL_STOP3gppFULL_STOPbsfPLUS_SIGNxml = (
        "application/vnd.3gpp.bsf+xml"
    )
    applicationSOLIDUSvndFULL_STOP3gppFULL_STOPcrsPLUS_SIGNxml = (
        "application/vnd.3gpp.crs+xml"
    )
    applicationSOLIDUSvndFULL_STOP3gppFULL_STOPcurrent_location_discoveryPLUS_SIGNxml = "application/vnd.3gpp.current-location-discovery+xml"
    applicationSOLIDUSvndFULL_STOP3gppFULL_STOPGMOPPLUS_SIGNxml = (
        "application/vnd.3gpp.GMOP+xml"
    )
    applicationSOLIDUSvndFULL_STOP3gppFULL_STOPgtpc = "application/vnd.3gpp.gtpc"
    applicationSOLIDUSvndFULL_STOP3gppFULL_STOPinterworking_data = (
        "application/vnd.3gpp.interworking-data"
    )
    applicationSOLIDUSvndFULL_STOP3gppFULL_STOPlpp = "application/vnd.3gpp.lpp"
    applicationSOLIDUSvndFULL_STOP3gppFULL_STOPmcdata_affiliation_commandPLUS_SIGNxml = "application/vnd.3gpp.mcdata-affiliation-command+xml"
    applicationSOLIDUSvndFULL_STOP3gppFULL_STOPmcdata_infoPLUS_SIGNxml = (
        "application/vnd.3gpp.mcdata-info+xml"
    )
    applicationSOLIDUSvndFULL_STOP3gppFULL_STOPmcdata_msgstore_ctrl_requestPLUS_SIGNxml = "application/vnd.3gpp.mcdata-msgstore-ctrl-request+xml"
    applicationSOLIDUSvndFULL_STOP3gppFULL_STOPmcdata_payload = (
        "application/vnd.3gpp.mcdata-payload"
    )
    applicationSOLIDUSvndFULL_STOP3gppFULL_STOPmcdata_regroupPLUS_SIGNxml = (
        "application/vnd.3gpp.mcdata-regroup+xml"
    )
    applicationSOLIDUSvndFULL_STOP3gppFULL_STOPmcdata_service_configPLUS_SIGNxml = (
        "application/vnd.3gpp.mcdata-service-config+xml"
    )
    applicationSOLIDUSvndFULL_STOP3gppFULL_STOPmcdata_signalling = (
        "application/vnd.3gpp.mcdata-signalling"
    )
    applicationSOLIDUSvndFULL_STOP3gppFULL_STOPmcdata_ue_configPLUS_SIGNxml = (
        "application/vnd.3gpp.mcdata-ue-config+xml"
    )
    applicationSOLIDUSvndFULL_STOP3gppFULL_STOPmcdata_user_profilePLUS_SIGNxml = (
        "application/vnd.3gpp.mcdata-user-profile+xml"
    )
    applicationSOLIDUSvndFULL_STOP3gppFULL_STOPmcptt_affiliation_commandPLUS_SIGNxml = (
        "application/vnd.3gpp.mcptt-affiliation-command+xml"
    )
    applicationSOLIDUSvndFULL_STOP3gppFULL_STOPmcptt_floor_requestPLUS_SIGNxml = (
        "application/vnd.3gpp.mcptt-floor-request+xml"
    )
    applicationSOLIDUSvndFULL_STOP3gppFULL_STOPmcptt_infoPLUS_SIGNxml = (
        "application/vnd.3gpp.mcptt-info+xml"
    )
    applicationSOLIDUSvndFULL_STOP3gppFULL_STOPmcptt_location_infoPLUS_SIGNxml = (
        "application/vnd.3gpp.mcptt-location-info+xml"
    )
    applicationSOLIDUSvndFULL_STOP3gppFULL_STOPmcptt_mbms_usage_infoPLUS_SIGNxml = (
        "application/vnd.3gpp.mcptt-mbms-usage-info+xml"
    )
    applicationSOLIDUSvndFULL_STOP3gppFULL_STOPmcptt_regroupPLUS_SIGNxml = (
        "application/vnd.3gpp.mcptt-regroup+xml"
    )
    applicationSOLIDUSvndFULL_STOP3gppFULL_STOPmcptt_service_configPLUS_SIGNxml = (
        "application/vnd.3gpp.mcptt-service-config+xml"
    )
    applicationSOLIDUSvndFULL_STOP3gppFULL_STOPmcptt_signedPLUS_SIGNxml = (
        "application/vnd.3gpp.mcptt-signed+xml"
    )
    applicationSOLIDUSvndFULL_STOP3gppFULL_STOPmcptt_ue_configPLUS_SIGNxml = (
        "application/vnd.3gpp.mcptt-ue-config+xml"
    )
    applicationSOLIDUSvndFULL_STOP3gppFULL_STOPmcptt_ue_init_configPLUS_SIGNxml = (
        "application/vnd.3gpp.mcptt-ue-init-config+xml"
    )
    applicationSOLIDUSvndFULL_STOP3gppFULL_STOPmcptt_user_profilePLUS_SIGNxml = (
        "application/vnd.3gpp.mcptt-user-profile+xml"
    )
    applicationSOLIDUSvndFULL_STOP3gppFULL_STOPmc_signalling_ear = (
        "application/vnd.3gpp.mc-signalling-ear"
    )
    applicationSOLIDUSvndFULL_STOP3gppFULL_STOPmcvideo_affiliation_commandPLUS_SIGNxml = "application/vnd.3gpp.mcvideo-affiliation-command+xml"
    applicationSOLIDUSvndFULL_STOP3gppFULL_STOPmcvideo_affiliation_infoPLUS_SIGNxml = (
        "application/vnd.3gpp.mcvideo-affiliation-info+xml"
    )
    applicationSOLIDUSvndFULL_STOP3gppFULL_STOPmcvideo_infoPLUS_SIGNxml = (
        "application/vnd.3gpp.mcvideo-info+xml"
    )
    applicationSOLIDUSvndFULL_STOP3gppFULL_STOPmcvideo_location_infoPLUS_SIGNxml = (
        "application/vnd.3gpp.mcvideo-location-info+xml"
    )
    applicationSOLIDUSvndFULL_STOP3gppFULL_STOPmcvideo_mbms_usage_infoPLUS_SIGNxml = (
        "application/vnd.3gpp.mcvideo-mbms-usage-info+xml"
    )
    applicationSOLIDUSvndFULL_STOP3gppFULL_STOPmcvideo_regroupPLUS_SIGNxml = (
        "application/vnd.3gpp.mcvideo-regroup+xml"
    )
    applicationSOLIDUSvndFULL_STOP3gppFULL_STOPmcvideo_service_configPLUS_SIGNxml = (
        "application/vnd.3gpp.mcvideo-service-config+xml"
    )
    applicationSOLIDUSvndFULL_STOP3gppFULL_STOPmcvideo_transmission_requestPLUS_SIGNxml = "application/vnd.3gpp.mcvideo-transmission-request+xml"
    applicationSOLIDUSvndFULL_STOP3gppFULL_STOPmcvideo_ue_configPLUS_SIGNxml = (
        "application/vnd.3gpp.mcvideo-ue-config+xml"
    )
    applicationSOLIDUSvndFULL_STOP3gppFULL_STOPmcvideo_user_profilePLUS_SIGNxml = (
        "application/vnd.3gpp.mcvideo-user-profile+xml"
    )
    applicationSOLIDUSvndFULL_STOP3gppFULL_STOPmid_callPLUS_SIGNxml = (
        "application/vnd.3gpp.mid-call+xml"
    )
    applicationSOLIDUSvndFULL_STOP3gppFULL_STOPngap = "application/vnd.3gpp.ngap"
    applicationSOLIDUSvndFULL_STOP3gppFULL_STOPpfcp = "application/vnd.3gpp.pfcp"
    applicationSOLIDUSvndFULL_STOP3gppFULL_STOPpic_bw_large = (
        "application/vnd.3gpp.pic-bw-large"
    )
    applicationSOLIDUSvndFULL_STOP3gppFULL_STOPpic_bw_small = (
        "application/vnd.3gpp.pic-bw-small"
    )
    applicationSOLIDUSvndFULL_STOP3gppFULL_STOPpic_bw_var = (
        "application/vnd.3gpp.pic-bw-var"
    )
    applicationSOLIDUSvndFULL_STOP3gppFULL_STOPpinapp_infoPLUS_SIGNxml = (
        "application/vnd.3gpp.pinapp-info+xml"
    )
    applicationSOLIDUSvndFULL_STOP3gppFULL_STOPs1ap = "application/vnd.3gpp.s1ap"
    applicationSOLIDUSvndFULL_STOP3gppFULL_STOPseal_group_docPLUS_SIGNxml = (
        "application/vnd.3gpp.seal-group-doc+xml"
    )
    applicationSOLIDUSvndFULL_STOP3gppFULL_STOPseal_infoPLUS_SIGNxml = (
        "application/vnd.3gpp.seal-info+xml"
    )
    applicationSOLIDUSvndFULL_STOP3gppFULL_STOPseal_location_infoPLUS_SIGNxml = (
        "application/vnd.3gpp.seal-location-info+xml"
    )
    applicationSOLIDUSvndFULL_STOP3gppFULL_STOPseal_mbms_usage_infoPLUS_SIGNxml = (
        "application/vnd.3gpp.seal-mbms-usage-info+xml"
    )
    applicationSOLIDUSvndFULL_STOP3gppFULL_STOPseal_network_QoS_management_infoPLUS_SIGNxml = "application/vnd.3gpp.seal-network-QoS-management-info+xml"
    applicationSOLIDUSvndFULL_STOP3gppFULL_STOPseal_ue_config_infoPLUS_SIGNxml = (
        "application/vnd.3gpp.seal-ue-config-info+xml"
    )
    applicationSOLIDUSvndFULL_STOP3gppFULL_STOPseal_unicast_infoPLUS_SIGNxml = (
        "application/vnd.3gpp.seal-unicast-info+xml"
    )
    applicationSOLIDUSvndFULL_STOP3gppFULL_STOPseal_user_profile_infoPLUS_SIGNxml = (
        "application/vnd.3gpp.seal-user-profile-info+xml"
    )
    applicationSOLIDUSvndFULL_STOP3gppFULL_STOPsms = "application/vnd.3gpp.sms"
    applicationSOLIDUSvndFULL_STOP3gppFULL_STOPsmsPLUS_SIGNxml = (
        "application/vnd.3gpp.sms+xml"
    )
    applicationSOLIDUSvndFULL_STOP3gppFULL_STOPsrvcc_extPLUS_SIGNxml = (
        "application/vnd.3gpp.srvcc-ext+xml"
    )
    applicationSOLIDUSvndFULL_STOP3gppFULL_STOPSRVCC_infoPLUS_SIGNxml = (
        "application/vnd.3gpp.SRVCC-info+xml"
    )
    applicationSOLIDUSvndFULL_STOP3gppFULL_STOPstate_and_event_infoPLUS_SIGNxml = (
        "application/vnd.3gpp.state-and-event-info+xml"
    )
    applicationSOLIDUSvndFULL_STOP3gppFULL_STOPussdPLUS_SIGNxml = (
        "application/vnd.3gpp.ussd+xml"
    )
    applicationSOLIDUSvndFULL_STOP3gppFULL_STOPv2x = "application/vnd.3gpp.v2x"
    applicationSOLIDUSvndFULL_STOP3gppFULL_STOPvae_infoPLUS_SIGNxml = (
        "application/vnd.3gpp.vae-info+xml"
    )
    applicationSOLIDUSvndFULL_STOP3gpp2FULL_STOPbcmcsinfoPLUS_SIGNxml = (
        "application/vnd.3gpp2.bcmcsinfo+xml"
    )
    applicationSOLIDUSvndFULL_STOP3gpp2FULL_STOPsms = "application/vnd.3gpp2.sms"
    applicationSOLIDUSvndFULL_STOP3gpp2FULL_STOPtcap = "application/vnd.3gpp2.tcap"
    applicationSOLIDUSvndFULL_STOP3gpp_prosePLUS_SIGNxml = (
        "application/vnd.3gpp-prose+xml"
    )
    applicationSOLIDUSvndFULL_STOP3gpp_prose_pc3aPLUS_SIGNxml = (
        "application/vnd.3gpp-prose-pc3a+xml"
    )
    applicationSOLIDUSvndFULL_STOP3gpp_prose_pc3achPLUS_SIGNxml = (
        "application/vnd.3gpp-prose-pc3ach+xml"
    )
    applicationSOLIDUSvndFULL_STOP3gpp_prose_pc3chPLUS_SIGNxml = (
        "application/vnd.3gpp-prose-pc3ch+xml"
    )
    applicationSOLIDUSvndFULL_STOP3gpp_prose_pc8PLUS_SIGNxml = (
        "application/vnd.3gpp-prose-pc8+xml"
    )
    applicationSOLIDUSvndFULL_STOP3gpp_v2x_local_service_information = (
        "application/vnd.3gpp-v2x-local-service-information"
    )
    applicationSOLIDUSvndFULL_STOP3lightssoftwareFULL_STOPimagescal = (
        "application/vnd.3lightssoftware.imagescal"
    )
    applicationSOLIDUSvndFULL_STOP3MFULL_STOPPost_it_Notes = (
        "application/vnd.3M.Post-it-Notes"
    )
    applicationSOLIDUSvndFULL_STOPaccpacFULL_STOPsimplyFULL_STOPaso = (
        "application/vnd.accpac.simply.aso"
    )
    applicationSOLIDUSvndFULL_STOPaccpacFULL_STOPsimplyFULL_STOPimp = (
        "application/vnd.accpac.simply.imp"
    )
    applicationSOLIDUSvndFULL_STOPacmFULL_STOPaddressxferPLUS_SIGNjson = (
        "application/vnd.acm.addressxfer+json"
    )
    applicationSOLIDUSvndFULL_STOPacmFULL_STOPchatbotPLUS_SIGNjson = (
        "application/vnd.acm.chatbot+json"
    )
    applicationSOLIDUSvndFULL_STOPacucobol = "application/vnd.acucobol"
    applicationSOLIDUSvndFULL_STOPacucorp = "application/vnd.acucorp"
    applicationSOLIDUSvndFULL_STOPadobeFULL_STOPflashFULL_STOPmovie = (
        "application/vnd.adobe.flash.movie"
    )
    applicationSOLIDUSvndFULL_STOPadobeFULL_STOPformscentralFULL_STOPfcdt = (
        "application/vnd.adobe.formscentral.fcdt"
    )
    applicationSOLIDUSvndFULL_STOPadobeFULL_STOPfxp = "application/vnd.adobe.fxp"
    applicationSOLIDUSvndFULL_STOPadobeFULL_STOPpartial_upload = (
        "application/vnd.adobe.partial-upload"
    )
    applicationSOLIDUSvndFULL_STOPadobeFULL_STOPxdpPLUS_SIGNxml = (
        "application/vnd.adobe.xdp+xml"
    )
    applicationSOLIDUSvndFULL_STOPaetherFULL_STOPimp = "application/vnd.aether.imp"
    applicationSOLIDUSvndFULL_STOPafpcFULL_STOPafplinedata = (
        "application/vnd.afpc.afplinedata"
    )
    applicationSOLIDUSvndFULL_STOPafpcFULL_STOPafplinedata_pagedef = (
        "application/vnd.afpc.afplinedata-pagedef"
    )
    applicationSOLIDUSvndFULL_STOPafpcFULL_STOPcmoca_cmresource = (
        "application/vnd.afpc.cmoca-cmresource"
    )
    applicationSOLIDUSvndFULL_STOPafpcFULL_STOPfoca_charset = (
        "application/vnd.afpc.foca-charset"
    )
    applicationSOLIDUSvndFULL_STOPafpcFULL_STOPfoca_codedfont = (
        "application/vnd.afpc.foca-codedfont"
    )
    applicationSOLIDUSvndFULL_STOPafpcFULL_STOPfoca_codepage = (
        "application/vnd.afpc.foca-codepage"
    )
    applicationSOLIDUSvndFULL_STOPafpcFULL_STOPmodca = "application/vnd.afpc.modca"
    applicationSOLIDUSvndFULL_STOPafpcFULL_STOPmodca_cmtable = (
        "application/vnd.afpc.modca-cmtable"
    )
    applicationSOLIDUSvndFULL_STOPafpcFULL_STOPmodca_formdef = (
        "application/vnd.afpc.modca-formdef"
    )
    applicationSOLIDUSvndFULL_STOPafpcFULL_STOPmodca_mediummap = (
        "application/vnd.afpc.modca-mediummap"
    )
    applicationSOLIDUSvndFULL_STOPafpcFULL_STOPmodca_objectcontainer = (
        "application/vnd.afpc.modca-objectcontainer"
    )
    applicationSOLIDUSvndFULL_STOPafpcFULL_STOPmodca_overlay = (
        "application/vnd.afpc.modca-overlay"
    )
    applicationSOLIDUSvndFULL_STOPafpcFULL_STOPmodca_pagesegment = (
        "application/vnd.afpc.modca-pagesegment"
    )
    applicationSOLIDUSvndFULL_STOPage = "application/vnd.age"
    applicationSOLIDUSvndFULL_STOPah_barcode = "application/vnd.ah-barcode"
    applicationSOLIDUSvndFULL_STOPaheadFULL_STOPspace = "application/vnd.ahead.space"
    applicationSOLIDUSvndFULL_STOPairzipFULL_STOPfilesecureFULL_STOPazf = (
        "application/vnd.airzip.filesecure.azf"
    )
    applicationSOLIDUSvndFULL_STOPairzipFULL_STOPfilesecureFULL_STOPazs = (
        "application/vnd.airzip.filesecure.azs"
    )
    applicationSOLIDUSvndFULL_STOPamadeusPLUS_SIGNjson = "application/vnd.amadeus+json"
    applicationSOLIDUSvndFULL_STOPamazonFULL_STOPmobi8_ebook = (
        "application/vnd.amazon.mobi8-ebook"
    )
    applicationSOLIDUSvndFULL_STOPamericandynamicsFULL_STOPacc = (
        "application/vnd.americandynamics.acc"
    )
    applicationSOLIDUSvndFULL_STOPamigaFULL_STOPami = "application/vnd.amiga.ami"
    applicationSOLIDUSvndFULL_STOPamundsenFULL_STOPmazePLUS_SIGNxml = (
        "application/vnd.amundsen.maze+xml"
    )
    applicationSOLIDUSvndFULL_STOPandroidFULL_STOPota = "application/vnd.android.ota"
    applicationSOLIDUSvndFULL_STOPanki = "application/vnd.anki"
    applicationSOLIDUSvndFULL_STOPanser_web_certificate_issue_initiation = (
        "application/vnd.anser-web-certificate-issue-initiation"
    )
    applicationSOLIDUSvndFULL_STOPantixFULL_STOPgame_component = (
        "application/vnd.antix.game-component"
    )
    applicationSOLIDUSvndFULL_STOPapacheFULL_STOParrowFULL_STOPfile = (
        "application/vnd.apache.arrow.file"
    )
    applicationSOLIDUSvndFULL_STOPapacheFULL_STOParrowFULL_STOPstream = (
        "application/vnd.apache.arrow.stream"
    )
    applicationSOLIDUSvndFULL_STOPapacheFULL_STOPparquet = (
        "application/vnd.apache.parquet"
    )
    applicationSOLIDUSvndFULL_STOPapacheFULL_STOPthriftFULL_STOPbinary = (
        "application/vnd.apache.thrift.binary"
    )
    applicationSOLIDUSvndFULL_STOPapacheFULL_STOPthriftFULL_STOPcompact = (
        "application/vnd.apache.thrift.compact"
    )
    applicationSOLIDUSvndFULL_STOPapacheFULL_STOPthriftFULL_STOPjson = (
        "application/vnd.apache.thrift.json"
    )
    applicationSOLIDUSvndFULL_STOPapexlang = "application/vnd.apexlang"
    applicationSOLIDUSvndFULL_STOPapiPLUS_SIGNjson = "application/vnd.api+json"
    applicationSOLIDUSvndFULL_STOPaplextorFULL_STOPwarrpPLUS_SIGNjson = (
        "application/vnd.aplextor.warrp+json"
    )
    applicationSOLIDUSvndFULL_STOPapothekendeFULL_STOPreservationPLUS_SIGNjson = (
        "application/vnd.apothekende.reservation+json"
    )
    applicationSOLIDUSvndFULL_STOPappleFULL_STOPinstallerPLUS_SIGNxml = (
        "application/vnd.apple.installer+xml"
    )
    applicationSOLIDUSvndFULL_STOPappleFULL_STOPkeynote = (
        "application/vnd.apple.keynote"
    )
    applicationSOLIDUSvndFULL_STOPappleFULL_STOPmpegurl = (
        "application/vnd.apple.mpegurl"
    )
    applicationSOLIDUSvndFULL_STOPappleFULL_STOPnumbers = (
        "application/vnd.apple.numbers"
    )
    applicationSOLIDUSvndFULL_STOPappleFULL_STOPpages = "application/vnd.apple.pages"
    applicationSOLIDUSvndFULL_STOParastraFULL_STOPswi = "application/vnd.arastra.swi"
    applicationSOLIDUSvndFULL_STOParistanetworksFULL_STOPswi = (
        "application/vnd.aristanetworks.swi"
    )
    applicationSOLIDUSvndFULL_STOPartisanPLUS_SIGNjson = "application/vnd.artisan+json"
    applicationSOLIDUSvndFULL_STOPartsquare = "application/vnd.artsquare"
    applicationSOLIDUSvndFULL_STOPastraea_softwareFULL_STOPiota = (
        "application/vnd.astraea-software.iota"
    )
    applicationSOLIDUSvndFULL_STOPaudiograph = "application/vnd.audiograph"
    applicationSOLIDUSvndFULL_STOPautopackage = "application/vnd.autopackage"
    applicationSOLIDUSvndFULL_STOPavalonPLUS_SIGNjson = "application/vnd.avalon+json"
    applicationSOLIDUSvndFULL_STOPavistarPLUS_SIGNxml = "application/vnd.avistar+xml"
    applicationSOLIDUSvndFULL_STOPbalsamiqFULL_STOPbmmlPLUS_SIGNxml = (
        "application/vnd.balsamiq.bmml+xml"
    )
    applicationSOLIDUSvndFULL_STOPbalsamiqFULL_STOPbmpr = (
        "application/vnd.balsamiq.bmpr"
    )
    applicationSOLIDUSvndFULL_STOPbanana_accounting = (
        "application/vnd.banana-accounting"
    )
    applicationSOLIDUSvndFULL_STOPbbfFULL_STOPuspFULL_STOPerror = (
        "application/vnd.bbf.usp.error"
    )
    applicationSOLIDUSvndFULL_STOPbbfFULL_STOPuspFULL_STOPmsg = (
        "application/vnd.bbf.usp.msg"
    )
    applicationSOLIDUSvndFULL_STOPbbfFULL_STOPuspFULL_STOPmsgPLUS_SIGNjson = (
        "application/vnd.bbf.usp.msg+json"
    )
    applicationSOLIDUSvndFULL_STOPbekitzur_stechPLUS_SIGNjson = (
        "application/vnd.bekitzur-stech+json"
    )
    applicationSOLIDUSvndFULL_STOPbelightsoftFULL_STOPlhzdPLUS_SIGNzip = (
        "application/vnd.belightsoft.lhzd+zip"
    )
    applicationSOLIDUSvndFULL_STOPbelightsoftFULL_STOPlhzlPLUS_SIGNzip = (
        "application/vnd.belightsoft.lhzl+zip"
    )
    applicationSOLIDUSvndFULL_STOPbintFULL_STOPmed_content = (
        "application/vnd.bint.med-content"
    )
    applicationSOLIDUSvndFULL_STOPbiopaxFULL_STOPrdfPLUS_SIGNxml = (
        "application/vnd.biopax.rdf+xml"
    )
    applicationSOLIDUSvndFULL_STOPblink_idb_value_wrapper = (
        "application/vnd.blink-idb-value-wrapper"
    )
    applicationSOLIDUSvndFULL_STOPblueiceFULL_STOPmultipass = (
        "application/vnd.blueice.multipass"
    )
    applicationSOLIDUSvndFULL_STOPbluetoothFULL_STOPepFULL_STOPoob = (
        "application/vnd.bluetooth.ep.oob"
    )
    applicationSOLIDUSvndFULL_STOPbluetoothFULL_STOPleFULL_STOPoob = (
        "application/vnd.bluetooth.le.oob"
    )
    applicationSOLIDUSvndFULL_STOPbmi = "application/vnd.bmi"
    applicationSOLIDUSvndFULL_STOPbpf = "application/vnd.bpf"
    applicationSOLIDUSvndFULL_STOPbpf3 = "application/vnd.bpf3"
    applicationSOLIDUSvndFULL_STOPbusinessobjects = "application/vnd.businessobjects"
    applicationSOLIDUSvndFULL_STOPbyuFULL_STOPuapiPLUS_SIGNjson = (
        "application/vnd.byu.uapi+json"
    )
    applicationSOLIDUSvndFULL_STOPbzip3 = "application/vnd.bzip3"
    applicationSOLIDUSvndFULL_STOPc3vocFULL_STOPschedulePLUS_SIGNxml = (
        "application/vnd.c3voc.schedule+xml"
    )
    applicationSOLIDUSvndFULL_STOPcab_jscript = "application/vnd.cab-jscript"
    applicationSOLIDUSvndFULL_STOPcanon_cpdl = "application/vnd.canon-cpdl"
    applicationSOLIDUSvndFULL_STOPcanon_lips = "application/vnd.canon-lips"
    applicationSOLIDUSvndFULL_STOPcapasystems_pgPLUS_SIGNjson = (
        "application/vnd.capasystems-pg+json"
    )
    applicationSOLIDUSvndFULL_STOPcendioFULL_STOPthinlincFULL_STOPclientconf = (
        "application/vnd.cendio.thinlinc.clientconf"
    )
    applicationSOLIDUSvndFULL_STOPcentury_systemsFULL_STOPtcp_stream = (
        "application/vnd.century-systems.tcp_stream"
    )
    applicationSOLIDUSvndFULL_STOPchemdrawPLUS_SIGNxml = "application/vnd.chemdraw+xml"
    applicationSOLIDUSvndFULL_STOPchess_pgn = "application/vnd.chess-pgn"
    applicationSOLIDUSvndFULL_STOPchipnutsFULL_STOPkaraoke_mmd = (
        "application/vnd.chipnuts.karaoke-mmd"
    )
    applicationSOLIDUSvndFULL_STOPciedi = "application/vnd.ciedi"
    applicationSOLIDUSvndFULL_STOPcinderella = "application/vnd.cinderella"
    applicationSOLIDUSvndFULL_STOPcirpackFULL_STOPisdn_ext = (
        "application/vnd.cirpack.isdn-ext"
    )
    applicationSOLIDUSvndFULL_STOPcitationstylesFULL_STOPstylePLUS_SIGNxml = (
        "application/vnd.citationstyles.style+xml"
    )
    applicationSOLIDUSvndFULL_STOPclaymore = "application/vnd.claymore"
    applicationSOLIDUSvndFULL_STOPcloantoFULL_STOPrp9 = "application/vnd.cloanto.rp9"
    applicationSOLIDUSvndFULL_STOPclonkFULL_STOPc4group = (
        "application/vnd.clonk.c4group"
    )
    applicationSOLIDUSvndFULL_STOPcluetrustFULL_STOPcartomobile_config = (
        "application/vnd.cluetrust.cartomobile-config"
    )
    applicationSOLIDUSvndFULL_STOPcluetrustFULL_STOPcartomobile_config_pkg = (
        "application/vnd.cluetrust.cartomobile-config-pkg"
    )
    applicationSOLIDUSvndFULL_STOPcncfFULL_STOPhelmFULL_STOPchartFULL_STOPcontentFULL_STOPv1FULL_STOPtarPLUS_SIGNgzip = "application/vnd.cncf.helm.chart.content.v1.tar+gzip"
    applicationSOLIDUSvndFULL_STOPcncfFULL_STOPhelmFULL_STOPchartFULL_STOPprovenanceFULL_STOPv1FULL_STOPprov = "application/vnd.cncf.helm.chart.provenance.v1.prov"
    applicationSOLIDUSvndFULL_STOPcncfFULL_STOPhelmFULL_STOPconfigFULL_STOPv1PLUS_SIGNjson = "application/vnd.cncf.helm.config.v1+json"
    applicationSOLIDUSvndFULL_STOPcoffeescript = "application/vnd.coffeescript"
    applicationSOLIDUSvndFULL_STOPcollabioFULL_STOPxodocumentsFULL_STOPdocument = (
        "application/vnd.collabio.xodocuments.document"
    )
    applicationSOLIDUSvndFULL_STOPcollabioFULL_STOPxodocumentsFULL_STOPdocument_template = "application/vnd.collabio.xodocuments.document-template"
    applicationSOLIDUSvndFULL_STOPcollabioFULL_STOPxodocumentsFULL_STOPpresentation = (
        "application/vnd.collabio.xodocuments.presentation"
    )
    applicationSOLIDUSvndFULL_STOPcollabioFULL_STOPxodocumentsFULL_STOPpresentation_template = "application/vnd.collabio.xodocuments.presentation-template"
    applicationSOLIDUSvndFULL_STOPcollabioFULL_STOPxodocumentsFULL_STOPspreadsheet = (
        "application/vnd.collabio.xodocuments.spreadsheet"
    )
    applicationSOLIDUSvndFULL_STOPcollabioFULL_STOPxodocumentsFULL_STOPspreadsheet_template = "application/vnd.collabio.xodocuments.spreadsheet-template"
    applicationSOLIDUSvndFULL_STOPcollectionFULL_STOPdocPLUS_SIGNjson = (
        "application/vnd.collection.doc+json"
    )
    applicationSOLIDUSvndFULL_STOPcollectionFULL_STOPnextPLUS_SIGNjson = (
        "application/vnd.collection.next+json"
    )
    applicationSOLIDUSvndFULL_STOPcollectionPLUS_SIGNjson = (
        "application/vnd.collection+json"
    )
    applicationSOLIDUSvndFULL_STOPcomicbookPLUS_SIGNzip = (
        "application/vnd.comicbook+zip"
    )
    applicationSOLIDUSvndFULL_STOPcomicbook_rar = "application/vnd.comicbook-rar"
    applicationSOLIDUSvndFULL_STOPcommerce_battelle = (
        "application/vnd.commerce-battelle"
    )
    applicationSOLIDUSvndFULL_STOPcommonspace = "application/vnd.commonspace"
    applicationSOLIDUSvndFULL_STOPcontactFULL_STOPcmsg = "application/vnd.contact.cmsg"
    applicationSOLIDUSvndFULL_STOPcoreosFULL_STOPignitionPLUS_SIGNjson = (
        "application/vnd.coreos.ignition+json"
    )
    applicationSOLIDUSvndFULL_STOPcosmocaller = "application/vnd.cosmocaller"
    applicationSOLIDUSvndFULL_STOPcrickFULL_STOPclicker = (
        "application/vnd.crick.clicker"
    )
    applicationSOLIDUSvndFULL_STOPcrickFULL_STOPclickerFULL_STOPkeyboard = (
        "application/vnd.crick.clicker.keyboard"
    )
    applicationSOLIDUSvndFULL_STOPcrickFULL_STOPclickerFULL_STOPpalette = (
        "application/vnd.crick.clicker.palette"
    )
    applicationSOLIDUSvndFULL_STOPcrickFULL_STOPclickerFULL_STOPtemplate = (
        "application/vnd.crick.clicker.template"
    )
    applicationSOLIDUSvndFULL_STOPcrickFULL_STOPclickerFULL_STOPwordbank = (
        "application/vnd.crick.clicker.wordbank"
    )
    applicationSOLIDUSvndFULL_STOPcriticaltoolsFULL_STOPwbsPLUS_SIGNxml = (
        "application/vnd.criticaltools.wbs+xml"
    )
    applicationSOLIDUSvndFULL_STOPcryptiiFULL_STOPpipePLUS_SIGNjson = (
        "application/vnd.cryptii.pipe+json"
    )
    applicationSOLIDUSvndFULL_STOPcryptomatorFULL_STOPencrypted = (
        "application/vnd.cryptomator.encrypted"
    )
    applicationSOLIDUSvndFULL_STOPcryptomatorFULL_STOPvault = (
        "application/vnd.cryptomator.vault"
    )
    applicationSOLIDUSvndFULL_STOPcrypto_shade_file = (
        "application/vnd.crypto-shade-file"
    )
    applicationSOLIDUSvndFULL_STOPctc_posml = "application/vnd.ctc-posml"
    applicationSOLIDUSvndFULL_STOPctctFULL_STOPwsPLUS_SIGNxml = (
        "application/vnd.ctct.ws+xml"
    )
    applicationSOLIDUSvndFULL_STOPcups_pdf = "application/vnd.cups-pdf"
    applicationSOLIDUSvndFULL_STOPcups_postscript = "application/vnd.cups-postscript"
    applicationSOLIDUSvndFULL_STOPcups_ppd = "application/vnd.cups-ppd"
    applicationSOLIDUSvndFULL_STOPcups_raster = "application/vnd.cups-raster"
    applicationSOLIDUSvndFULL_STOPcups_raw = "application/vnd.cups-raw"
    applicationSOLIDUSvndFULL_STOPcurl = "application/vnd.curl"
    applicationSOLIDUSvndFULL_STOPcyanFULL_STOPdeanFULL_STOProotPLUS_SIGNxml = (
        "application/vnd.cyan.dean.root+xml"
    )
    applicationSOLIDUSvndFULL_STOPcybank = "application/vnd.cybank"
    applicationSOLIDUSvndFULL_STOPcyclonedxPLUS_SIGNjson = (
        "application/vnd.cyclonedx+json"
    )
    applicationSOLIDUSvndFULL_STOPcyclonedxPLUS_SIGNxml = (
        "application/vnd.cyclonedx+xml"
    )
    applicationSOLIDUSvndFULL_STOPd2lFULL_STOPcoursepackage1p0PLUS_SIGNzip = (
        "application/vnd.d2l.coursepackage1p0+zip"
    )
    applicationSOLIDUSvndFULL_STOPd3m_dataset = "application/vnd.d3m-dataset"
    applicationSOLIDUSvndFULL_STOPd3m_problem = "application/vnd.d3m-problem"
    applicationSOLIDUSvndFULL_STOPdart = "application/vnd.dart"
    applicationSOLIDUSvndFULL_STOPdatalog = "application/vnd.datalog"
    applicationSOLIDUSvndFULL_STOPdatapackagePLUS_SIGNjson = (
        "application/vnd.datapackage+json"
    )
    applicationSOLIDUSvndFULL_STOPdataresourcePLUS_SIGNjson = (
        "application/vnd.dataresource+json"
    )
    applicationSOLIDUSvndFULL_STOPdata_visionFULL_STOPrdz = (
        "application/vnd.data-vision.rdz"
    )
    applicationSOLIDUSvndFULL_STOPdbf = "application/vnd.dbf"
    applicationSOLIDUSvndFULL_STOPdcmpPLUS_SIGNxml = "application/vnd.dcmp+xml"
    applicationSOLIDUSvndFULL_STOPdebianFULL_STOPbinary_package = (
        "application/vnd.debian.binary-package"
    )
    applicationSOLIDUSvndFULL_STOPdeceFULL_STOPdata = "application/vnd.dece.data"
    applicationSOLIDUSvndFULL_STOPdeceFULL_STOPttmlPLUS_SIGNxml = (
        "application/vnd.dece.ttml+xml"
    )
    applicationSOLIDUSvndFULL_STOPdeceFULL_STOPunspecified = (
        "application/vnd.dece.unspecified"
    )
    applicationSOLIDUSvndFULL_STOPdeceFULL_STOPzip = "application/vnd.dece.zip"
    applicationSOLIDUSvndFULL_STOPdenovoFULL_STOPfcselayout_link = (
        "application/vnd.denovo.fcselayout-link"
    )
    applicationSOLIDUSvndFULL_STOPdesmumeFULL_STOPmovie = (
        "application/vnd.desmume.movie"
    )
    applicationSOLIDUSvndFULL_STOPdir_biFULL_STOPplate_dl_nosuffix = (
        "application/vnd.dir-bi.plate-dl-nosuffix"
    )
    applicationSOLIDUSvndFULL_STOPdmFULL_STOPdelegationPLUS_SIGNxml = (
        "application/vnd.dm.delegation+xml"
    )
    applicationSOLIDUSvndFULL_STOPdna = "application/vnd.dna"
    applicationSOLIDUSvndFULL_STOPdocumentPLUS_SIGNjson = (
        "application/vnd.document+json"
    )
    applicationSOLIDUSvndFULL_STOPdolbyFULL_STOPmobileFULL_STOP1 = (
        "application/vnd.dolby.mobile.1"
    )
    applicationSOLIDUSvndFULL_STOPdolbyFULL_STOPmobileFULL_STOP2 = (
        "application/vnd.dolby.mobile.2"
    )
    applicationSOLIDUSvndFULL_STOPdoremirFULL_STOPscorecloud_binary_document = (
        "application/vnd.doremir.scorecloud-binary-document"
    )
    applicationSOLIDUSvndFULL_STOPdpgraph = "application/vnd.dpgraph"
    applicationSOLIDUSvndFULL_STOPdreamfactory = "application/vnd.dreamfactory"
    applicationSOLIDUSvndFULL_STOPdrivePLUS_SIGNjson = "application/vnd.drive+json"
    applicationSOLIDUSvndFULL_STOPdtgFULL_STOPlocal = "application/vnd.dtg.local"
    applicationSOLIDUSvndFULL_STOPdtgFULL_STOPlocalFULL_STOPflash = (
        "application/vnd.dtg.local.flash"
    )
    applicationSOLIDUSvndFULL_STOPdtgFULL_STOPlocalFULL_STOPhtml = (
        "application/vnd.dtg.local.html"
    )
    applicationSOLIDUSvndFULL_STOPdvbFULL_STOPait = "application/vnd.dvb.ait"
    applicationSOLIDUSvndFULL_STOPdvbFULL_STOPdvbislPLUS_SIGNxml = (
        "application/vnd.dvb.dvbisl+xml"
    )
    applicationSOLIDUSvndFULL_STOPdvbFULL_STOPdvbj = "application/vnd.dvb.dvbj"
    applicationSOLIDUSvndFULL_STOPdvbFULL_STOPesgcontainer = (
        "application/vnd.dvb.esgcontainer"
    )
    applicationSOLIDUSvndFULL_STOPdvbFULL_STOPipdcdftnotifaccess = (
        "application/vnd.dvb.ipdcdftnotifaccess"
    )
    applicationSOLIDUSvndFULL_STOPdvbFULL_STOPipdcesgaccess = (
        "application/vnd.dvb.ipdcesgaccess"
    )
    applicationSOLIDUSvndFULL_STOPdvbFULL_STOPipdcesgaccess2 = (
        "application/vnd.dvb.ipdcesgaccess2"
    )
    applicationSOLIDUSvndFULL_STOPdvbFULL_STOPipdcesgpdd = (
        "application/vnd.dvb.ipdcesgpdd"
    )
    applicationSOLIDUSvndFULL_STOPdvbFULL_STOPipdcroaming = (
        "application/vnd.dvb.ipdcroaming"
    )
    applicationSOLIDUSvndFULL_STOPdvbFULL_STOPiptvFULL_STOPalfec_base = (
        "application/vnd.dvb.iptv.alfec-base"
    )
    applicationSOLIDUSvndFULL_STOPdvbFULL_STOPiptvFULL_STOPalfec_enhancement = (
        "application/vnd.dvb.iptv.alfec-enhancement"
    )
    applicationSOLIDUSvndFULL_STOPdvbFULL_STOPnotif_aggregate_rootPLUS_SIGNxml = (
        "application/vnd.dvb.notif-aggregate-root+xml"
    )
    applicationSOLIDUSvndFULL_STOPdvbFULL_STOPnotif_containerPLUS_SIGNxml = (
        "application/vnd.dvb.notif-container+xml"
    )
    applicationSOLIDUSvndFULL_STOPdvbFULL_STOPnotif_genericPLUS_SIGNxml = (
        "application/vnd.dvb.notif-generic+xml"
    )
    applicationSOLIDUSvndFULL_STOPdvbFULL_STOPnotif_ia_msglistPLUS_SIGNxml = (
        "application/vnd.dvb.notif-ia-msglist+xml"
    )
    applicationSOLIDUSvndFULL_STOPdvbFULL_STOPnotif_ia_registration_requestPLUS_SIGNxml = "application/vnd.dvb.notif-ia-registration-request+xml"
    applicationSOLIDUSvndFULL_STOPdvbFULL_STOPnotif_ia_registration_responsePLUS_SIGNxml = "application/vnd.dvb.notif-ia-registration-response+xml"
    applicationSOLIDUSvndFULL_STOPdvbFULL_STOPnotif_initPLUS_SIGNxml = (
        "application/vnd.dvb.notif-init+xml"
    )
    applicationSOLIDUSvndFULL_STOPdvbFULL_STOPpfr = "application/vnd.dvb.pfr"
    applicationSOLIDUSvndFULL_STOPdvbFULL_STOPservice = "application/vnd.dvb.service"
    applicationSOLIDUSvndFULL_STOPdxr = "application/vnd.dxr"
    applicationSOLIDUSvndFULL_STOPdynageo = "application/vnd.dynageo"
    applicationSOLIDUSvndFULL_STOPdzr = "application/vnd.dzr"
    applicationSOLIDUSvndFULL_STOPeasykaraokeFULL_STOPcdgdownload = (
        "application/vnd.easykaraoke.cdgdownload"
    )
    applicationSOLIDUSvndFULL_STOPecdis_update = "application/vnd.ecdis-update"
    applicationSOLIDUSvndFULL_STOPecipFULL_STOPrlp = "application/vnd.ecip.rlp"
    applicationSOLIDUSvndFULL_STOPeclipseFULL_STOPdittoPLUS_SIGNjson = (
        "application/vnd.eclipse.ditto+json"
    )
    applicationSOLIDUSvndFULL_STOPecowinFULL_STOPchart = "application/vnd.ecowin.chart"
    applicationSOLIDUSvndFULL_STOPecowinFULL_STOPfilerequest = (
        "application/vnd.ecowin.filerequest"
    )
    applicationSOLIDUSvndFULL_STOPecowinFULL_STOPfileupdate = (
        "application/vnd.ecowin.fileupdate"
    )
    applicationSOLIDUSvndFULL_STOPecowinFULL_STOPseries = (
        "application/vnd.ecowin.series"
    )
    applicationSOLIDUSvndFULL_STOPecowinFULL_STOPseriesrequest = (
        "application/vnd.ecowin.seriesrequest"
    )
    applicationSOLIDUSvndFULL_STOPecowinFULL_STOPseriesupdate = (
        "application/vnd.ecowin.seriesupdate"
    )
    applicationSOLIDUSvndFULL_STOPefiFULL_STOPimg = "application/vnd.efi.img"
    applicationSOLIDUSvndFULL_STOPefiFULL_STOPiso = "application/vnd.efi.iso"
    applicationSOLIDUSvndFULL_STOPelnPLUS_SIGNzip = "application/vnd.eln+zip"
    applicationSOLIDUSvndFULL_STOPemclientFULL_STOPaccessrequestPLUS_SIGNxml = (
        "application/vnd.emclient.accessrequest+xml"
    )
    applicationSOLIDUSvndFULL_STOPenliven = "application/vnd.enliven"
    applicationSOLIDUSvndFULL_STOPenphaseFULL_STOPenvoy = (
        "application/vnd.enphase.envoy"
    )
    applicationSOLIDUSvndFULL_STOPeprintsFULL_STOPdataPLUS_SIGNxml = (
        "application/vnd.eprints.data+xml"
    )
    applicationSOLIDUSvndFULL_STOPepsonFULL_STOPesf = "application/vnd.epson.esf"
    applicationSOLIDUSvndFULL_STOPepsonFULL_STOPmsf = "application/vnd.epson.msf"
    applicationSOLIDUSvndFULL_STOPepsonFULL_STOPquickanime = (
        "application/vnd.epson.quickanime"
    )
    applicationSOLIDUSvndFULL_STOPepsonFULL_STOPsalt = "application/vnd.epson.salt"
    applicationSOLIDUSvndFULL_STOPepsonFULL_STOPssf = "application/vnd.epson.ssf"
    applicationSOLIDUSvndFULL_STOPericssonFULL_STOPquickcall = (
        "application/vnd.ericsson.quickcall"
    )
    applicationSOLIDUSvndFULL_STOPerofs = "application/vnd.erofs"
    applicationSOLIDUSvndFULL_STOPespass_espassPLUS_SIGNzip = (
        "application/vnd.espass-espass+zip"
    )
    applicationSOLIDUSvndFULL_STOPeszigno3PLUS_SIGNxml = "application/vnd.eszigno3+xml"
    applicationSOLIDUSvndFULL_STOPetsiFULL_STOPaocPLUS_SIGNxml = (
        "application/vnd.etsi.aoc+xml"
    )
    applicationSOLIDUSvndFULL_STOPetsiFULL_STOPasic_ePLUS_SIGNzip = (
        "application/vnd.etsi.asic-e+zip"
    )
    applicationSOLIDUSvndFULL_STOPetsiFULL_STOPasic_sPLUS_SIGNzip = (
        "application/vnd.etsi.asic-s+zip"
    )
    applicationSOLIDUSvndFULL_STOPetsiFULL_STOPcugPLUS_SIGNxml = (
        "application/vnd.etsi.cug+xml"
    )
    applicationSOLIDUSvndFULL_STOPetsiFULL_STOPiptvcommandPLUS_SIGNxml = (
        "application/vnd.etsi.iptvcommand+xml"
    )
    applicationSOLIDUSvndFULL_STOPetsiFULL_STOPiptvdiscoveryPLUS_SIGNxml = (
        "application/vnd.etsi.iptvdiscovery+xml"
    )
    applicationSOLIDUSvndFULL_STOPetsiFULL_STOPiptvprofilePLUS_SIGNxml = (
        "application/vnd.etsi.iptvprofile+xml"
    )
    applicationSOLIDUSvndFULL_STOPetsiFULL_STOPiptvsad_bcPLUS_SIGNxml = (
        "application/vnd.etsi.iptvsad-bc+xml"
    )
    applicationSOLIDUSvndFULL_STOPetsiFULL_STOPiptvsad_codPLUS_SIGNxml = (
        "application/vnd.etsi.iptvsad-cod+xml"
    )
    applicationSOLIDUSvndFULL_STOPetsiFULL_STOPiptvsad_npvrPLUS_SIGNxml = (
        "application/vnd.etsi.iptvsad-npvr+xml"
    )
    applicationSOLIDUSvndFULL_STOPetsiFULL_STOPiptvservicePLUS_SIGNxml = (
        "application/vnd.etsi.iptvservice+xml"
    )
    applicationSOLIDUSvndFULL_STOPetsiFULL_STOPiptvsyncPLUS_SIGNxml = (
        "application/vnd.etsi.iptvsync+xml"
    )
    applicationSOLIDUSvndFULL_STOPetsiFULL_STOPiptvueprofilePLUS_SIGNxml = (
        "application/vnd.etsi.iptvueprofile+xml"
    )
    applicationSOLIDUSvndFULL_STOPetsiFULL_STOPmcidPLUS_SIGNxml = (
        "application/vnd.etsi.mcid+xml"
    )
    applicationSOLIDUSvndFULL_STOPetsiFULL_STOPmheg5 = "application/vnd.etsi.mheg5"
    applicationSOLIDUSvndFULL_STOPetsiFULL_STOPoverload_control_policy_datasetPLUS_SIGNxml = "application/vnd.etsi.overload-control-policy-dataset+xml"
    applicationSOLIDUSvndFULL_STOPetsiFULL_STOPpstnPLUS_SIGNxml = (
        "application/vnd.etsi.pstn+xml"
    )
    applicationSOLIDUSvndFULL_STOPetsiFULL_STOPsciPLUS_SIGNxml = (
        "application/vnd.etsi.sci+xml"
    )
    applicationSOLIDUSvndFULL_STOPetsiFULL_STOPsimservsPLUS_SIGNxml = (
        "application/vnd.etsi.simservs+xml"
    )
    applicationSOLIDUSvndFULL_STOPetsiFULL_STOPtimestamp_token = (
        "application/vnd.etsi.timestamp-token"
    )
    applicationSOLIDUSvndFULL_STOPetsiFULL_STOPtslFULL_STOPder = (
        "application/vnd.etsi.tsl.der"
    )
    applicationSOLIDUSvndFULL_STOPetsiFULL_STOPtslPLUS_SIGNxml = (
        "application/vnd.etsi.tsl+xml"
    )
    applicationSOLIDUSvndFULL_STOPeuFULL_STOPkasparianFULL_STOPcarPLUS_SIGNjson = (
        "application/vnd.eu.kasparian.car+json"
    )
    applicationSOLIDUSvndFULL_STOPeudoraFULL_STOPdata = "application/vnd.eudora.data"
    applicationSOLIDUSvndFULL_STOPevolvFULL_STOPecigFULL_STOPprofile = (
        "application/vnd.evolv.ecig.profile"
    )
    applicationSOLIDUSvndFULL_STOPevolvFULL_STOPecigFULL_STOPsettings = (
        "application/vnd.evolv.ecig.settings"
    )
    applicationSOLIDUSvndFULL_STOPevolvFULL_STOPecigFULL_STOPtheme = (
        "application/vnd.evolv.ecig.theme"
    )
    applicationSOLIDUSvndFULL_STOPexstream_empowerPLUS_SIGNzip = (
        "application/vnd.exstream-empower+zip"
    )
    applicationSOLIDUSvndFULL_STOPexstream_package = "application/vnd.exstream-package"
    applicationSOLIDUSvndFULL_STOPezpix_album = "application/vnd.ezpix-album"
    applicationSOLIDUSvndFULL_STOPezpix_package = "application/vnd.ezpix-package"
    applicationSOLIDUSvndFULL_STOPfamilysearchFULL_STOPgedcomPLUS_SIGNzip = (
        "application/vnd.familysearch.gedcom+zip"
    )
    applicationSOLIDUSvndFULL_STOPfastcopy_disk_image = (
        "application/vnd.fastcopy-disk-image"
    )
    applicationSOLIDUSvndFULL_STOPfdsnFULL_STOPmseed = "application/vnd.fdsn.mseed"
    applicationSOLIDUSvndFULL_STOPfdsnFULL_STOPseed = "application/vnd.fdsn.seed"
    applicationSOLIDUSvndFULL_STOPfdsnFULL_STOPstationxmlPLUS_SIGNxml = (
        "application/vnd.fdsn.stationxml+xml"
    )
    applicationSOLIDUSvndFULL_STOPffsns = "application/vnd.ffsns"
    applicationSOLIDUSvndFULL_STOPficlabFULL_STOPflbPLUS_SIGNzip = (
        "application/vnd.ficlab.flb+zip"
    )
    applicationSOLIDUSvndFULL_STOPfilmitFULL_STOPzfc = "application/vnd.filmit.zfc"
    applicationSOLIDUSvndFULL_STOPfints = "application/vnd.fints"
    applicationSOLIDUSvndFULL_STOPfiremonkeysFULL_STOPcloudcell = (
        "application/vnd.firemonkeys.cloudcell"
    )
    applicationSOLIDUSvndFULL_STOPFloGraphIt = "application/vnd.FloGraphIt"
    applicationSOLIDUSvndFULL_STOPfluxtimeFULL_STOPclip = (
        "application/vnd.fluxtime.clip"
    )
    applicationSOLIDUSvndFULL_STOPfont_fontforge_sfd = (
        "application/vnd.font-fontforge-sfd"
    )
    applicationSOLIDUSvndFULL_STOPframemaker = "application/vnd.framemaker"
    applicationSOLIDUSvndFULL_STOPfreelogFULL_STOPcomic = (
        "application/vnd.freelog.comic"
    )
    applicationSOLIDUSvndFULL_STOPfrogansFULL_STOPfnc = "application/vnd.frogans.fnc"
    applicationSOLIDUSvndFULL_STOPfrogansFULL_STOPltf = "application/vnd.frogans.ltf"
    applicationSOLIDUSvndFULL_STOPfscFULL_STOPweblaunch = (
        "application/vnd.fsc.weblaunch"
    )
    applicationSOLIDUSvndFULL_STOPf_secureFULL_STOPmobile = (
        "application/vnd.f-secure.mobile"
    )
    applicationSOLIDUSvndFULL_STOPfujifilmFULL_STOPfbFULL_STOPdocuworks = (
        "application/vnd.fujifilm.fb.docuworks"
    )
    applicationSOLIDUSvndFULL_STOPfujifilmFULL_STOPfbFULL_STOPdocuworksFULL_STOPbinder = "application/vnd.fujifilm.fb.docuworks.binder"
    applicationSOLIDUSvndFULL_STOPfujifilmFULL_STOPfbFULL_STOPdocuworksFULL_STOPcontainer = "application/vnd.fujifilm.fb.docuworks.container"
    applicationSOLIDUSvndFULL_STOPfujifilmFULL_STOPfbFULL_STOPjfiPLUS_SIGNxml = (
        "application/vnd.fujifilm.fb.jfi+xml"
    )
    applicationSOLIDUSvndFULL_STOPfujitsuFULL_STOPoasys = (
        "application/vnd.fujitsu.oasys"
    )
    applicationSOLIDUSvndFULL_STOPfujitsuFULL_STOPoasys2 = (
        "application/vnd.fujitsu.oasys2"
    )
    applicationSOLIDUSvndFULL_STOPfujitsuFULL_STOPoasys3 = (
        "application/vnd.fujitsu.oasys3"
    )
    applicationSOLIDUSvndFULL_STOPfujitsuFULL_STOPoasysgp = (
        "application/vnd.fujitsu.oasysgp"
    )
    applicationSOLIDUSvndFULL_STOPfujitsuFULL_STOPoasysprs = (
        "application/vnd.fujitsu.oasysprs"
    )
    applicationSOLIDUSvndFULL_STOPfujixeroxFULL_STOPART4 = (
        "application/vnd.fujixerox.ART4"
    )
    applicationSOLIDUSvndFULL_STOPfujixeroxFULL_STOPART_EX = (
        "application/vnd.fujixerox.ART-EX"
    )
    applicationSOLIDUSvndFULL_STOPfujixeroxFULL_STOPddd = (
        "application/vnd.fujixerox.ddd"
    )
    applicationSOLIDUSvndFULL_STOPfujixeroxFULL_STOPdocuworks = (
        "application/vnd.fujixerox.docuworks"
    )
    applicationSOLIDUSvndFULL_STOPfujixeroxFULL_STOPdocuworksFULL_STOPbinder = (
        "application/vnd.fujixerox.docuworks.binder"
    )
    applicationSOLIDUSvndFULL_STOPfujixeroxFULL_STOPdocuworksFULL_STOPcontainer = (
        "application/vnd.fujixerox.docuworks.container"
    )
    applicationSOLIDUSvndFULL_STOPfujixeroxFULL_STOPHBPL = (
        "application/vnd.fujixerox.HBPL"
    )
    applicationSOLIDUSvndFULL_STOPfut_misnet = "application/vnd.fut-misnet"
    applicationSOLIDUSvndFULL_STOPfutoinPLUS_SIGNcbor = "application/vnd.futoin+cbor"
    applicationSOLIDUSvndFULL_STOPfutoinPLUS_SIGNjson = "application/vnd.futoin+json"
    applicationSOLIDUSvndFULL_STOPfuzzysheet = "application/vnd.fuzzysheet"
    applicationSOLIDUSvndFULL_STOPga4ghFULL_STOPpassportPLUS_SIGNjwt = (
        "application/vnd.ga4gh.passport+jwt"
    )
    applicationSOLIDUSvndFULL_STOPgenomatixFULL_STOPtuxedo = (
        "application/vnd.genomatix.tuxedo"
    )
    applicationSOLIDUSvndFULL_STOPgenozip = "application/vnd.genozip"
    applicationSOLIDUSvndFULL_STOPgenticsFULL_STOPgrdPLUS_SIGNjson = (
        "application/vnd.gentics.grd+json"
    )
    applicationSOLIDUSvndFULL_STOPgentooFULL_STOPcatmetadataPLUS_SIGNxml = (
        "application/vnd.gentoo.catmetadata+xml"
    )
    applicationSOLIDUSvndFULL_STOPgentooFULL_STOPebuild = (
        "application/vnd.gentoo.ebuild"
    )
    applicationSOLIDUSvndFULL_STOPgentooFULL_STOPeclass = (
        "application/vnd.gentoo.eclass"
    )
    applicationSOLIDUSvndFULL_STOPgentooFULL_STOPgpkg = "application/vnd.gentoo.gpkg"
    applicationSOLIDUSvndFULL_STOPgentooFULL_STOPmanifest = (
        "application/vnd.gentoo.manifest"
    )
    applicationSOLIDUSvndFULL_STOPgentooFULL_STOPpkgmetadataPLUS_SIGNxml = (
        "application/vnd.gentoo.pkgmetadata+xml"
    )
    applicationSOLIDUSvndFULL_STOPgentooFULL_STOPxpak = "application/vnd.gentoo.xpak"
    applicationSOLIDUSvndFULL_STOPgeoPLUS_SIGNjson = "application/vnd.geo+json"
    applicationSOLIDUSvndFULL_STOPgeocubePLUS_SIGNxml = "application/vnd.geocube+xml"
    applicationSOLIDUSvndFULL_STOPgeogebraFULL_STOPfile = (
        "application/vnd.geogebra.file"
    )
    applicationSOLIDUSvndFULL_STOPgeogebraFULL_STOPpinboard = (
        "application/vnd.geogebra.pinboard"
    )
    applicationSOLIDUSvndFULL_STOPgeogebraFULL_STOPslides = (
        "application/vnd.geogebra.slides"
    )
    applicationSOLIDUSvndFULL_STOPgeogebraFULL_STOPtool = (
        "application/vnd.geogebra.tool"
    )
    applicationSOLIDUSvndFULL_STOPgeometry_explorer = (
        "application/vnd.geometry-explorer"
    )
    applicationSOLIDUSvndFULL_STOPgeonext = "application/vnd.geonext"
    applicationSOLIDUSvndFULL_STOPgeoplan = "application/vnd.geoplan"
    applicationSOLIDUSvndFULL_STOPgeospace = "application/vnd.geospace"
    applicationSOLIDUSvndFULL_STOPgerber = "application/vnd.gerber"
    applicationSOLIDUSvndFULL_STOPglobalplatformFULL_STOPcard_content_mgt = (
        "application/vnd.globalplatform.card-content-mgt"
    )
    applicationSOLIDUSvndFULL_STOPglobalplatformFULL_STOPcard_content_mgt_response = (
        "application/vnd.globalplatform.card-content-mgt-response"
    )
    applicationSOLIDUSvndFULL_STOPgmx = "application/vnd.gmx"
    applicationSOLIDUSvndFULL_STOPgnuFULL_STOPtalerFULL_STOPexchangePLUS_SIGNjson = (
        "application/vnd.gnu.taler.exchange+json"
    )
    applicationSOLIDUSvndFULL_STOPgnuFULL_STOPtalerFULL_STOPmerchantPLUS_SIGNjson = (
        "application/vnd.gnu.taler.merchant+json"
    )
    applicationSOLIDUSvndFULL_STOPgoogle_earthFULL_STOPkmlPLUS_SIGNxml = (
        "application/vnd.google-earth.kml+xml"
    )
    applicationSOLIDUSvndFULL_STOPgoogle_earthFULL_STOPkmz = (
        "application/vnd.google-earth.kmz"
    )
    applicationSOLIDUSvndFULL_STOPgovFULL_STOPskFULL_STOPe_formPLUS_SIGNxml = (
        "application/vnd.gov.sk.e-form+xml"
    )
    applicationSOLIDUSvndFULL_STOPgovFULL_STOPskFULL_STOPe_formPLUS_SIGNzip = (
        "application/vnd.gov.sk.e-form+zip"
    )
    applicationSOLIDUSvndFULL_STOPgovFULL_STOPskFULL_STOPxmldatacontainerPLUS_SIGNxml = "application/vnd.gov.sk.xmldatacontainer+xml"
    applicationSOLIDUSvndFULL_STOPgpxseeFULL_STOPmapPLUS_SIGNxml = (
        "application/vnd.gpxsee.map+xml"
    )
    applicationSOLIDUSvndFULL_STOPgrafeq = "application/vnd.grafeq"
    applicationSOLIDUSvndFULL_STOPgridmp = "application/vnd.gridmp"
    applicationSOLIDUSvndFULL_STOPgroove_account = "application/vnd.groove-account"
    applicationSOLIDUSvndFULL_STOPgroove_help = "application/vnd.groove-help"
    applicationSOLIDUSvndFULL_STOPgroove_identity_message = (
        "application/vnd.groove-identity-message"
    )
    applicationSOLIDUSvndFULL_STOPgroove_injector = "application/vnd.groove-injector"
    applicationSOLIDUSvndFULL_STOPgroove_tool_message = (
        "application/vnd.groove-tool-message"
    )
    applicationSOLIDUSvndFULL_STOPgroove_tool_template = (
        "application/vnd.groove-tool-template"
    )
    applicationSOLIDUSvndFULL_STOPgroove_vcard = "application/vnd.groove-vcard"
    applicationSOLIDUSvndFULL_STOPhalPLUS_SIGNjson = "application/vnd.hal+json"
    applicationSOLIDUSvndFULL_STOPhalPLUS_SIGNxml = "application/vnd.hal+xml"
    applicationSOLIDUSvndFULL_STOPHandHeld_EntertainmentPLUS_SIGNxml = (
        "application/vnd.HandHeld-Entertainment+xml"
    )
    applicationSOLIDUSvndFULL_STOPhbci = "application/vnd.hbci"
    applicationSOLIDUSvndFULL_STOPhcPLUS_SIGNjson = "application/vnd.hc+json"
    applicationSOLIDUSvndFULL_STOPhcl_bireports = "application/vnd.hcl-bireports"
    applicationSOLIDUSvndFULL_STOPhdt = "application/vnd.hdt"
    applicationSOLIDUSvndFULL_STOPherokuPLUS_SIGNjson = "application/vnd.heroku+json"
    applicationSOLIDUSvndFULL_STOPhheFULL_STOPlesson_player = (
        "application/vnd.hhe.lesson-player"
    )
    applicationSOLIDUSvndFULL_STOPhp_HPGL = "application/vnd.hp-HPGL"
    applicationSOLIDUSvndFULL_STOPhp_hpid = "application/vnd.hp-hpid"
    applicationSOLIDUSvndFULL_STOPhp_hps = "application/vnd.hp-hps"
    applicationSOLIDUSvndFULL_STOPhp_jlyt = "application/vnd.hp-jlyt"
    applicationSOLIDUSvndFULL_STOPhp_PCL = "application/vnd.hp-PCL"
    applicationSOLIDUSvndFULL_STOPhp_PCLXL = "application/vnd.hp-PCLXL"
    applicationSOLIDUSvndFULL_STOPhsl = "application/vnd.hsl"
    applicationSOLIDUSvndFULL_STOPhttphone = "application/vnd.httphone"
    applicationSOLIDUSvndFULL_STOPhydrostatixFULL_STOPsof_data = (
        "application/vnd.hydrostatix.sof-data"
    )
    applicationSOLIDUSvndFULL_STOPhyperPLUS_SIGNjson = "application/vnd.hyper+json"
    applicationSOLIDUSvndFULL_STOPhyperdrivePLUS_SIGNjson = (
        "application/vnd.hyperdrive+json"
    )
    applicationSOLIDUSvndFULL_STOPhyper_itemPLUS_SIGNjson = (
        "application/vnd.hyper-item+json"
    )
    applicationSOLIDUSvndFULL_STOPhzn_3d_crossword = "application/vnd.hzn-3d-crossword"
    applicationSOLIDUSvndFULL_STOPibmFULL_STOPafplinedata = (
        "application/vnd.ibm.afplinedata"
    )
    applicationSOLIDUSvndFULL_STOPibmFULL_STOPelectronic_media = (
        "application/vnd.ibm.electronic-media"
    )
    applicationSOLIDUSvndFULL_STOPibmFULL_STOPMiniPay = "application/vnd.ibm.MiniPay"
    applicationSOLIDUSvndFULL_STOPibmFULL_STOPmodcap = "application/vnd.ibm.modcap"
    applicationSOLIDUSvndFULL_STOPibmFULL_STOPrights_management = (
        "application/vnd.ibm.rights-management"
    )
    applicationSOLIDUSvndFULL_STOPibmFULL_STOPsecure_container = (
        "application/vnd.ibm.secure-container"
    )
    applicationSOLIDUSvndFULL_STOPiccprofile = "application/vnd.iccprofile"
    applicationSOLIDUSvndFULL_STOPieeeFULL_STOP1905 = "application/vnd.ieee.1905"
    applicationSOLIDUSvndFULL_STOPigloader = "application/vnd.igloader"
    applicationSOLIDUSvndFULL_STOPimagemeterFULL_STOPfolderPLUS_SIGNzip = (
        "application/vnd.imagemeter.folder+zip"
    )
    applicationSOLIDUSvndFULL_STOPimagemeterFULL_STOPimagePLUS_SIGNzip = (
        "application/vnd.imagemeter.image+zip"
    )
    applicationSOLIDUSvndFULL_STOPimmervision_ivp = "application/vnd.immervision-ivp"
    applicationSOLIDUSvndFULL_STOPimmervision_ivu = "application/vnd.immervision-ivu"
    applicationSOLIDUSvndFULL_STOPimsFULL_STOPimsccv1p1 = (
        "application/vnd.ims.imsccv1p1"
    )
    applicationSOLIDUSvndFULL_STOPimsFULL_STOPimsccv1p2 = (
        "application/vnd.ims.imsccv1p2"
    )
    applicationSOLIDUSvndFULL_STOPimsFULL_STOPimsccv1p3 = (
        "application/vnd.ims.imsccv1p3"
    )
    applicationSOLIDUSvndFULL_STOPimsFULL_STOPlisFULL_STOPv2FULL_STOPresultPLUS_SIGNjson = "application/vnd.ims.lis.v2.result+json"
    applicationSOLIDUSvndFULL_STOPimsFULL_STOPltiFULL_STOPv2FULL_STOPtoolconsumerprofilePLUS_SIGNjson = "application/vnd.ims.lti.v2.toolconsumerprofile+json"
    applicationSOLIDUSvndFULL_STOPimsFULL_STOPltiFULL_STOPv2FULL_STOPtoolproxyFULL_STOPidPLUS_SIGNjson = "application/vnd.ims.lti.v2.toolproxy.id+json"
    applicationSOLIDUSvndFULL_STOPimsFULL_STOPltiFULL_STOPv2FULL_STOPtoolproxyPLUS_SIGNjson = "application/vnd.ims.lti.v2.toolproxy+json"
    applicationSOLIDUSvndFULL_STOPimsFULL_STOPltiFULL_STOPv2FULL_STOPtoolsettingsFULL_STOPsimplePLUS_SIGNjson = "application/vnd.ims.lti.v2.toolsettings.simple+json"
    applicationSOLIDUSvndFULL_STOPimsFULL_STOPltiFULL_STOPv2FULL_STOPtoolsettingsPLUS_SIGNjson = "application/vnd.ims.lti.v2.toolsettings+json"
    applicationSOLIDUSvndFULL_STOPinformedcontrolFULL_STOPrmsPLUS_SIGNxml = (
        "application/vnd.informedcontrol.rms+xml"
    )
    applicationSOLIDUSvndFULL_STOPinformix_visionary = (
        "application/vnd.informix-visionary"
    )
    applicationSOLIDUSvndFULL_STOPinfotechFULL_STOPproject = (
        "application/vnd.infotech.project"
    )
    applicationSOLIDUSvndFULL_STOPinfotechFULL_STOPprojectPLUS_SIGNxml = (
        "application/vnd.infotech.project+xml"
    )
    applicationSOLIDUSvndFULL_STOPinnopathFULL_STOPwampFULL_STOPnotification = (
        "application/vnd.innopath.wamp.notification"
    )
    applicationSOLIDUSvndFULL_STOPinsorsFULL_STOPigm = "application/vnd.insors.igm"
    applicationSOLIDUSvndFULL_STOPinterconFULL_STOPformnet = (
        "application/vnd.intercon.formnet"
    )
    applicationSOLIDUSvndFULL_STOPintergeo = "application/vnd.intergeo"
    applicationSOLIDUSvndFULL_STOPintertrustFULL_STOPdigibox = (
        "application/vnd.intertrust.digibox"
    )
    applicationSOLIDUSvndFULL_STOPintertrustFULL_STOPnncp = (
        "application/vnd.intertrust.nncp"
    )
    applicationSOLIDUSvndFULL_STOPintuFULL_STOPqbo = "application/vnd.intu.qbo"
    applicationSOLIDUSvndFULL_STOPintuFULL_STOPqfx = "application/vnd.intu.qfx"
    applicationSOLIDUSvndFULL_STOPipfsFULL_STOPipns_record = (
        "application/vnd.ipfs.ipns-record"
    )
    applicationSOLIDUSvndFULL_STOPipldFULL_STOPcar = "application/vnd.ipld.car"
    applicationSOLIDUSvndFULL_STOPipldFULL_STOPdag_cbor = (
        "application/vnd.ipld.dag-cbor"
    )
    applicationSOLIDUSvndFULL_STOPipldFULL_STOPdag_json = (
        "application/vnd.ipld.dag-json"
    )
    applicationSOLIDUSvndFULL_STOPipldFULL_STOPraw = "application/vnd.ipld.raw"
    applicationSOLIDUSvndFULL_STOPiptcFULL_STOPg2FULL_STOPcatalogitemPLUS_SIGNxml = (
        "application/vnd.iptc.g2.catalogitem+xml"
    )
    applicationSOLIDUSvndFULL_STOPiptcFULL_STOPg2FULL_STOPconceptitemPLUS_SIGNxml = (
        "application/vnd.iptc.g2.conceptitem+xml"
    )
    applicationSOLIDUSvndFULL_STOPiptcFULL_STOPg2FULL_STOPknowledgeitemPLUS_SIGNxml = (
        "application/vnd.iptc.g2.knowledgeitem+xml"
    )
    applicationSOLIDUSvndFULL_STOPiptcFULL_STOPg2FULL_STOPnewsitemPLUS_SIGNxml = (
        "application/vnd.iptc.g2.newsitem+xml"
    )
    applicationSOLIDUSvndFULL_STOPiptcFULL_STOPg2FULL_STOPnewsmessagePLUS_SIGNxml = (
        "application/vnd.iptc.g2.newsmessage+xml"
    )
    applicationSOLIDUSvndFULL_STOPiptcFULL_STOPg2FULL_STOPpackageitemPLUS_SIGNxml = (
        "application/vnd.iptc.g2.packageitem+xml"
    )
    applicationSOLIDUSvndFULL_STOPiptcFULL_STOPg2FULL_STOPplanningitemPLUS_SIGNxml = (
        "application/vnd.iptc.g2.planningitem+xml"
    )
    applicationSOLIDUSvndFULL_STOPipunpluggedFULL_STOPrcprofile = (
        "application/vnd.ipunplugged.rcprofile"
    )
    applicationSOLIDUSvndFULL_STOPirepositoryFULL_STOPpackagePLUS_SIGNxml = (
        "application/vnd.irepository.package+xml"
    )
    applicationSOLIDUSvndFULL_STOPisacFULL_STOPfcs = "application/vnd.isac.fcs"
    applicationSOLIDUSvndFULL_STOPiso11783_10PLUS_SIGNzip = (
        "application/vnd.iso11783-10+zip"
    )
    applicationSOLIDUSvndFULL_STOPis_xpr = "application/vnd.is-xpr"
    applicationSOLIDUSvndFULL_STOPjam = "application/vnd.jam"
    applicationSOLIDUSvndFULL_STOPjapannet_directory_service = (
        "application/vnd.japannet-directory-service"
    )
    applicationSOLIDUSvndFULL_STOPjapannet_jpnstore_wakeup = (
        "application/vnd.japannet-jpnstore-wakeup"
    )
    applicationSOLIDUSvndFULL_STOPjapannet_payment_wakeup = (
        "application/vnd.japannet-payment-wakeup"
    )
    applicationSOLIDUSvndFULL_STOPjapannet_registration = (
        "application/vnd.japannet-registration"
    )
    applicationSOLIDUSvndFULL_STOPjapannet_registration_wakeup = (
        "application/vnd.japannet-registration-wakeup"
    )
    applicationSOLIDUSvndFULL_STOPjapannet_setstore_wakeup = (
        "application/vnd.japannet-setstore-wakeup"
    )
    applicationSOLIDUSvndFULL_STOPjapannet_verification = (
        "application/vnd.japannet-verification"
    )
    applicationSOLIDUSvndFULL_STOPjapannet_verification_wakeup = (
        "application/vnd.japannet-verification-wakeup"
    )
    applicationSOLIDUSvndFULL_STOPjcpFULL_STOPjavameFULL_STOPmidlet_rms = (
        "application/vnd.jcp.javame.midlet-rms"
    )
    applicationSOLIDUSvndFULL_STOPjisp = "application/vnd.jisp"
    applicationSOLIDUSvndFULL_STOPjoostFULL_STOPjoda_archive = (
        "application/vnd.joost.joda-archive"
    )
    applicationSOLIDUSvndFULL_STOPjskFULL_STOPisdn_ngn = "application/vnd.jsk.isdn-ngn"
    applicationSOLIDUSvndFULL_STOPkahootz = "application/vnd.kahootz"
    applicationSOLIDUSvndFULL_STOPkdeFULL_STOPkarbon = "application/vnd.kde.karbon"
    applicationSOLIDUSvndFULL_STOPkdeFULL_STOPkchart = "application/vnd.kde.kchart"
    applicationSOLIDUSvndFULL_STOPkdeFULL_STOPkformula = "application/vnd.kde.kformula"
    applicationSOLIDUSvndFULL_STOPkdeFULL_STOPkivio = "application/vnd.kde.kivio"
    applicationSOLIDUSvndFULL_STOPkdeFULL_STOPkontour = "application/vnd.kde.kontour"
    applicationSOLIDUSvndFULL_STOPkdeFULL_STOPkpresenter = (
        "application/vnd.kde.kpresenter"
    )
    applicationSOLIDUSvndFULL_STOPkdeFULL_STOPkspread = "application/vnd.kde.kspread"
    applicationSOLIDUSvndFULL_STOPkdeFULL_STOPkword = "application/vnd.kde.kword"
    applicationSOLIDUSvndFULL_STOPkdl = "application/vnd.kdl"
    applicationSOLIDUSvndFULL_STOPkenameaapp = "application/vnd.kenameaapp"
    applicationSOLIDUSvndFULL_STOPkeymanFULL_STOPkmpPLUS_SIGNzip = (
        "application/vnd.keyman.kmp+zip"
    )
    applicationSOLIDUSvndFULL_STOPkeymanFULL_STOPkmx = "application/vnd.keyman.kmx"
    applicationSOLIDUSvndFULL_STOPkidspiration = "application/vnd.kidspiration"
    applicationSOLIDUSvndFULL_STOPKinar = "application/vnd.Kinar"
    applicationSOLIDUSvndFULL_STOPkoan = "application/vnd.koan"
    applicationSOLIDUSvndFULL_STOPkodak_descriptor = "application/vnd.kodak-descriptor"
    applicationSOLIDUSvndFULL_STOPlays = "application/vnd.las"
    applicationSOLIDUSvndFULL_STOPlaysFULL_STOPlaysPLUS_SIGNjson = (
        "application/vnd.las.las+json"
    )
    applicationSOLIDUSvndFULL_STOPlaysFULL_STOPlaysPLUS_SIGNxml = (
        "application/vnd.las.las+xml"
    )
    applicationSOLIDUSvndFULL_STOPlaszip = "application/vnd.laszip"
    applicationSOLIDUSvndFULL_STOPldevFULL_STOPproductlicensing = (
        "application/vnd.ldev.productlicensing"
    )
    applicationSOLIDUSvndFULL_STOPleapPLUS_SIGNjson = "application/vnd.leap+json"
    applicationSOLIDUSvndFULL_STOPliberty_requestPLUS_SIGNxml = (
        "application/vnd.liberty-request+xml"
    )
    applicationSOLIDUSvndFULL_STOPllamagraphicsFULL_STOPlife_balanceFULL_STOPdesktop = (
        "application/vnd.llamagraphics.life-balance.desktop"
    )
    applicationSOLIDUSvndFULL_STOPllamagraphicsFULL_STOPlife_balanceFULL_STOPexchangePLUS_SIGNxml = "application/vnd.llamagraphics.life-balance.exchange+xml"
    applicationSOLIDUSvndFULL_STOPlogipipeFULL_STOPcircuitPLUS_SIGNzip = (
        "application/vnd.logipipe.circuit+zip"
    )
    applicationSOLIDUSvndFULL_STOPloom = "application/vnd.loom"
    applicationSOLIDUSvndFULL_STOPlotus_1_2_3 = "application/vnd.lotus-1-2-3"
    applicationSOLIDUSvndFULL_STOPlotus_approach = "application/vnd.lotus-approach"
    applicationSOLIDUSvndFULL_STOPlotus_freelance = "application/vnd.lotus-freelance"
    applicationSOLIDUSvndFULL_STOPlotus_notes = "application/vnd.lotus-notes"
    applicationSOLIDUSvndFULL_STOPlotus_organizer = "application/vnd.lotus-organizer"
    applicationSOLIDUSvndFULL_STOPlotus_screencam = "application/vnd.lotus-screencam"
    applicationSOLIDUSvndFULL_STOPlotus_wordpro = "application/vnd.lotus-wordpro"
    applicationSOLIDUSvndFULL_STOPmacportsFULL_STOPportpkg = (
        "application/vnd.macports.portpkg"
    )
    applicationSOLIDUSvndFULL_STOPmapbox_vector_tile = (
        "application/vnd.mapbox-vector-tile"
    )
    applicationSOLIDUSvndFULL_STOPmarlinFULL_STOPdrmFULL_STOPactiontokenPLUS_SIGNxml = (
        "application/vnd.marlin.drm.actiontoken+xml"
    )
    applicationSOLIDUSvndFULL_STOPmarlinFULL_STOPdrmFULL_STOPconftokenPLUS_SIGNxml = (
        "application/vnd.marlin.drm.conftoken+xml"
    )
    applicationSOLIDUSvndFULL_STOPmarlinFULL_STOPdrmFULL_STOPlicensePLUS_SIGNxml = (
        "application/vnd.marlin.drm.license+xml"
    )
    applicationSOLIDUSvndFULL_STOPmarlinFULL_STOPdrmFULL_STOPmdcf = (
        "application/vnd.marlin.drm.mdcf"
    )
    applicationSOLIDUSvndFULL_STOPmasonPLUS_SIGNjson = "application/vnd.mason+json"
    applicationSOLIDUSvndFULL_STOPmaxarFULL_STOParchiveFULL_STOP3tzPLUS_SIGNzip = (
        "application/vnd.maxar.archive.3tz+zip"
    )
    applicationSOLIDUSvndFULL_STOPmaxmindFULL_STOPmaxmind_db = (
        "application/vnd.maxmind.maxmind-db"
    )
    applicationSOLIDUSvndFULL_STOPmcd = "application/vnd.mcd"
    applicationSOLIDUSvndFULL_STOPmdl = "application/vnd.mdl"
    applicationSOLIDUSvndFULL_STOPmdl_mbsdf = "application/vnd.mdl-mbsdf"
    applicationSOLIDUSvndFULL_STOPmedcalcdata = "application/vnd.medcalcdata"
    applicationSOLIDUSvndFULL_STOPmediastationFULL_STOPcdkey = (
        "application/vnd.mediastation.cdkey"
    )
    applicationSOLIDUSvndFULL_STOPmedicalholodeckFULL_STOPrecordxr = (
        "application/vnd.medicalholodeck.recordxr"
    )
    applicationSOLIDUSvndFULL_STOPmeridian_slingshot = (
        "application/vnd.meridian-slingshot"
    )
    applicationSOLIDUSvndFULL_STOPmermaid = "application/vnd.mermaid"
    applicationSOLIDUSvndFULL_STOPMFER = "application/vnd.MFER"
    applicationSOLIDUSvndFULL_STOPmfmp = "application/vnd.mfmp"
    applicationSOLIDUSvndFULL_STOPmicroPLUS_SIGNjson = "application/vnd.micro+json"
    applicationSOLIDUSvndFULL_STOPmicrografxFULL_STOPflo = (
        "application/vnd.micrografx.flo"
    )
    applicationSOLIDUSvndFULL_STOPmicrografxFULL_STOPigx = (
        "application/vnd.micrografx.igx"
    )
    applicationSOLIDUSvndFULL_STOPmicrosoftFULL_STOPportable_executable = (
        "application/vnd.microsoft.portable-executable"
    )
    applicationSOLIDUSvndFULL_STOPmicrosoftFULL_STOPwindowsFULL_STOPthumbnail_cache = (
        "application/vnd.microsoft.windows.thumbnail-cache"
    )
    applicationSOLIDUSvndFULL_STOPmielePLUS_SIGNjson = "application/vnd.miele+json"
    applicationSOLIDUSvndFULL_STOPmif = "application/vnd.mif"
    applicationSOLIDUSvndFULL_STOPminisoft_hp3000_save = (
        "application/vnd.minisoft-hp3000-save"
    )
    applicationSOLIDUSvndFULL_STOPmitsubishiFULL_STOPmisty_guardFULL_STOPtrustweb = (
        "application/vnd.mitsubishi.misty-guard.trustweb"
    )
    applicationSOLIDUSvndFULL_STOPMobiusFULL_STOPDAF = "application/vnd.Mobius.DAF"
    applicationSOLIDUSvndFULL_STOPMobiusFULL_STOPDIS = "application/vnd.Mobius.DIS"
    applicationSOLIDUSvndFULL_STOPMobiusFULL_STOPMBK = "application/vnd.Mobius.MBK"
    applicationSOLIDUSvndFULL_STOPMobiusFULL_STOPMQY = "application/vnd.Mobius.MQY"
    applicationSOLIDUSvndFULL_STOPMobiusFULL_STOPMSL = "application/vnd.Mobius.MSL"
    applicationSOLIDUSvndFULL_STOPMobiusFULL_STOPPLC = "application/vnd.Mobius.PLC"
    applicationSOLIDUSvndFULL_STOPMobiusFULL_STOPTXF = "application/vnd.Mobius.TXF"
    applicationSOLIDUSvndFULL_STOPmodl = "application/vnd.modl"
    applicationSOLIDUSvndFULL_STOPmophunFULL_STOPapplication = (
        "application/vnd.mophun.application"
    )
    applicationSOLIDUSvndFULL_STOPmophunFULL_STOPcertificate = (
        "application/vnd.mophun.certificate"
    )
    applicationSOLIDUSvndFULL_STOPmotorolaFULL_STOPflexsuite = (
        "application/vnd.motorola.flexsuite"
    )
    applicationSOLIDUSvndFULL_STOPmotorolaFULL_STOPflexsuiteFULL_STOPadsi = (
        "application/vnd.motorola.flexsuite.adsi"
    )
    applicationSOLIDUSvndFULL_STOPmotorolaFULL_STOPflexsuiteFULL_STOPfis = (
        "application/vnd.motorola.flexsuite.fis"
    )
    applicationSOLIDUSvndFULL_STOPmotorolaFULL_STOPflexsuiteFULL_STOPgotap = (
        "application/vnd.motorola.flexsuite.gotap"
    )
    applicationSOLIDUSvndFULL_STOPmotorolaFULL_STOPflexsuiteFULL_STOPkmr = (
        "application/vnd.motorola.flexsuite.kmr"
    )
    applicationSOLIDUSvndFULL_STOPmotorolaFULL_STOPflexsuiteFULL_STOPttc = (
        "application/vnd.motorola.flexsuite.ttc"
    )
    applicationSOLIDUSvndFULL_STOPmotorolaFULL_STOPflexsuiteFULL_STOPwem = (
        "application/vnd.motorola.flexsuite.wem"
    )
    applicationSOLIDUSvndFULL_STOPmotorolaFULL_STOPiprm = (
        "application/vnd.motorola.iprm"
    )
    applicationSOLIDUSvndFULL_STOPmozillaFULL_STOPxulPLUS_SIGNxml = (
        "application/vnd.mozilla.xul+xml"
    )
    applicationSOLIDUSvndFULL_STOPms_3mfdocument = "application/vnd.ms-3mfdocument"
    applicationSOLIDUSvndFULL_STOPmsa_disk_image = "application/vnd.msa-disk-image"
    applicationSOLIDUSvndFULL_STOPms_artgalry = "application/vnd.ms-artgalry"
    applicationSOLIDUSvndFULL_STOPms_asf = "application/vnd.ms-asf"
    applicationSOLIDUSvndFULL_STOPms_cab_compressed = (
        "application/vnd.ms-cab-compressed"
    )
    applicationSOLIDUSvndFULL_STOPmseq = "application/vnd.mseq"
    applicationSOLIDUSvndFULL_STOPms_excel = "application/vnd.ms-excel"
    applicationSOLIDUSvndFULL_STOPms_excelFULL_STOPaddingFULL_STOPmacroEnabledFULL_STOP12 = "application/vnd.ms-excel.addin.macroEnabled.12"
    applicationSOLIDUSvndFULL_STOPms_excelFULL_STOPsheetFULL_STOPbinaryFULL_STOPmacroEnabledFULL_STOP12 = "application/vnd.ms-excel.sheet.binary.macroEnabled.12"
    applicationSOLIDUSvndFULL_STOPms_excelFULL_STOPsheetFULL_STOPmacroEnabledFULL_STOP12 = "application/vnd.ms-excel.sheet.macroEnabled.12"
    applicationSOLIDUSvndFULL_STOPms_excelFULL_STOPtemplateFULL_STOPmacroEnabledFULL_STOP12 = "application/vnd.ms-excel.template.macroEnabled.12"
    applicationSOLIDUSvndFULL_STOPms_fontobject = "application/vnd.ms-fontobject"
    applicationSOLIDUSvndFULL_STOPmsgpack = "application/vnd.msgpack"
    applicationSOLIDUSvndFULL_STOPms_htmlhelp = "application/vnd.ms-htmlhelp"
    applicationSOLIDUSvndFULL_STOPmsign = "application/vnd.msign"
    applicationSOLIDUSvndFULL_STOPms_ims = "application/vnd.ms-ims"
    applicationSOLIDUSvndFULL_STOPms_lrm = "application/vnd.ms-lrm"
    applicationSOLIDUSvndFULL_STOPms_officeFULL_STOPactiveXPLUS_SIGNxml = (
        "application/vnd.ms-office.activeX+xml"
    )
    applicationSOLIDUSvndFULL_STOPms_officetheme = "application/vnd.ms-officetheme"
    applicationSOLIDUSvndFULL_STOPms_playreadyFULL_STOPinitiatorPLUS_SIGNxml = (
        "application/vnd.ms-playready.initiator+xml"
    )
    applicationSOLIDUSvndFULL_STOPms_powerpoint = "application/vnd.ms-powerpoint"
    applicationSOLIDUSvndFULL_STOPms_powerpointFULL_STOPaddingFULL_STOPmacroEnabledFULL_STOP12 = "application/vnd.ms-powerpoint.addin.macroEnabled.12"
    applicationSOLIDUSvndFULL_STOPms_powerpointFULL_STOPpresentationFULL_STOPmacroEnabledFULL_STOP12 = "application/vnd.ms-powerpoint.presentation.macroEnabled.12"
    applicationSOLIDUSvndFULL_STOPms_powerpointFULL_STOPslideFULL_STOPmacroEnabledFULL_STOP12 = "application/vnd.ms-powerpoint.slide.macroEnabled.12"
    applicationSOLIDUSvndFULL_STOPms_powerpointFULL_STOPslideshowFULL_STOPmacroEnabledFULL_STOP12 = "application/vnd.ms-powerpoint.slideshow.macroEnabled.12"
    applicationSOLIDUSvndFULL_STOPms_powerpointFULL_STOPtemplateFULL_STOPmacroEnabledFULL_STOP12 = "application/vnd.ms-powerpoint.template.macroEnabled.12"
    applicationSOLIDUSvndFULL_STOPms_PrintDeviceCapabilitiesPLUS_SIGNxml = (
        "application/vnd.ms-PrintDeviceCapabilities+xml"
    )
    applicationSOLIDUSvndFULL_STOPms_PrintSchemaTicketPLUS_SIGNxml = (
        "application/vnd.ms-PrintSchemaTicket+xml"
    )
    applicationSOLIDUSvndFULL_STOPms_project = "application/vnd.ms-project"
    applicationSOLIDUSvndFULL_STOPms_tnef = "application/vnd.ms-tnef"
    applicationSOLIDUSvndFULL_STOPms_windowsFULL_STOPdevicepairing = (
        "application/vnd.ms-windows.devicepairing"
    )
    applicationSOLIDUSvndFULL_STOPms_windowsFULL_STOPnwprintingFULL_STOPoob = (
        "application/vnd.ms-windows.nwprinting.oob"
    )
    applicationSOLIDUSvndFULL_STOPms_windowsFULL_STOPprinterpairing = (
        "application/vnd.ms-windows.printerpairing"
    )
    applicationSOLIDUSvndFULL_STOPms_windowsFULL_STOPwsdFULL_STOPoob = (
        "application/vnd.ms-windows.wsd.oob"
    )
    applicationSOLIDUSvndFULL_STOPms_wmdrmFULL_STOPlic_chlg_req = (
        "application/vnd.ms-wmdrm.lic-chlg-req"
    )
    applicationSOLIDUSvndFULL_STOPms_wmdrmFULL_STOPlic_resp = (
        "application/vnd.ms-wmdrm.lic-resp"
    )
    applicationSOLIDUSvndFULL_STOPms_wmdrmFULL_STOPmeter_chlg_req = (
        "application/vnd.ms-wmdrm.meter-chlg-req"
    )
    applicationSOLIDUSvndFULL_STOPms_wmdrmFULL_STOPmeter_resp = (
        "application/vnd.ms-wmdrm.meter-resp"
    )
    applicationSOLIDUSvndFULL_STOPms_wordFULL_STOPdocumentFULL_STOPmacroEnabledFULL_STOP12 = "application/vnd.ms-word.document.macroEnabled.12"
    applicationSOLIDUSvndFULL_STOPms_wordFULL_STOPtemplateFULL_STOPmacroEnabledFULL_STOP12 = "application/vnd.ms-word.template.macroEnabled.12"
    applicationSOLIDUSvndFULL_STOPms_works = "application/vnd.ms-works"
    applicationSOLIDUSvndFULL_STOPms_wpl = "application/vnd.ms-wpl"
    applicationSOLIDUSvndFULL_STOPms_xpsdocument = "application/vnd.ms-xpsdocument"
    applicationSOLIDUSvndFULL_STOPmultiadFULL_STOPcreator = (
        "application/vnd.multiad.creator"
    )
    applicationSOLIDUSvndFULL_STOPmultiadFULL_STOPcreatorFULL_STOPcif = (
        "application/vnd.multiad.creator.cif"
    )
    applicationSOLIDUSvndFULL_STOPmusician = "application/vnd.musician"
    applicationSOLIDUSvndFULL_STOPmusic_niff = "application/vnd.music-niff"
    applicationSOLIDUSvndFULL_STOPmuveeFULL_STOPstyle = "application/vnd.muvee.style"
    applicationSOLIDUSvndFULL_STOPmynfc = "application/vnd.mynfc"
    applicationSOLIDUSvndFULL_STOPnacamarFULL_STOPybridPLUS_SIGNjson = (
        "application/vnd.nacamar.ybrid+json"
    )
    applicationSOLIDUSvndFULL_STOPnatoFULL_STOPbindingdataobjectPLUS_SIGNcbor = (
        "application/vnd.nato.bindingdataobject+cbor"
    )
    applicationSOLIDUSvndFULL_STOPnatoFULL_STOPbindingdataobjectPLUS_SIGNjson = (
        "application/vnd.nato.bindingdataobject+json"
    )
    applicationSOLIDUSvndFULL_STOPnatoFULL_STOPbindingdataobjectPLUS_SIGNxml = (
        "application/vnd.nato.bindingdataobject+xml"
    )
    applicationSOLIDUSvndFULL_STOPnatoFULL_STOPopenxmlformats_packageFULL_STOPiepdPLUS_SIGNzip = "application/vnd.nato.openxmlformats-package.iepd+zip"
    applicationSOLIDUSvndFULL_STOPncdFULL_STOPcontrol = "application/vnd.ncd.control"
    applicationSOLIDUSvndFULL_STOPncdFULL_STOPreference = (
        "application/vnd.ncd.reference"
    )
    applicationSOLIDUSvndFULL_STOPnearstFULL_STOPinvPLUS_SIGNjson = (
        "application/vnd.nearst.inv+json"
    )
    applicationSOLIDUSvndFULL_STOPnebumindFULL_STOPline = (
        "application/vnd.nebumind.line"
    )
    applicationSOLIDUSvndFULL_STOPnervana = "application/vnd.nervana"
    applicationSOLIDUSvndFULL_STOPnetfpx = "application/vnd.netfpx"
    applicationSOLIDUSvndFULL_STOPneurolanguageFULL_STOPnlu = (
        "application/vnd.neurolanguage.nlu"
    )
    applicationSOLIDUSvndFULL_STOPnimn = "application/vnd.nimn"
    applicationSOLIDUSvndFULL_STOPnintendoFULL_STOPnitroFULL_STOProm = (
        "application/vnd.nintendo.nitro.rom"
    )
    applicationSOLIDUSvndFULL_STOPnintendoFULL_STOPsnesFULL_STOProm = (
        "application/vnd.nintendo.snes.rom"
    )
    applicationSOLIDUSvndFULL_STOPnitf = "application/vnd.nitf"
    applicationSOLIDUSvndFULL_STOPnoblenet_directory = (
        "application/vnd.noblenet-directory"
    )
    applicationSOLIDUSvndFULL_STOPnoblenet_sealer = "application/vnd.noblenet-sealer"
    applicationSOLIDUSvndFULL_STOPnoblenet_web = "application/vnd.noblenet-web"
    applicationSOLIDUSvndFULL_STOPnokiaFULL_STOPcatalogs = (
        "application/vnd.nokia.catalogs"
    )
    applicationSOLIDUSvndFULL_STOPnokiaFULL_STOPconmlPLUS_SIGNwbxml = (
        "application/vnd.nokia.conml+wbxml"
    )
    applicationSOLIDUSvndFULL_STOPnokiaFULL_STOPconmlPLUS_SIGNxml = (
        "application/vnd.nokia.conml+xml"
    )
    applicationSOLIDUSvndFULL_STOPnokiaFULL_STOPiptvFULL_STOPconfigPLUS_SIGNxml = (
        "application/vnd.nokia.iptv.config+xml"
    )
    applicationSOLIDUSvndFULL_STOPnokiaFULL_STOPiSDS_radio_presets = (
        "application/vnd.nokia.iSDS-radio-presets"
    )
    applicationSOLIDUSvndFULL_STOPnokiaFULL_STOPlandmarkPLUS_SIGNwbxml = (
        "application/vnd.nokia.landmark+wbxml"
    )
    applicationSOLIDUSvndFULL_STOPnokiaFULL_STOPlandmarkPLUS_SIGNxml = (
        "application/vnd.nokia.landmark+xml"
    )
    applicationSOLIDUSvndFULL_STOPnokiaFULL_STOPlandmarkcollectionPLUS_SIGNxml = (
        "application/vnd.nokia.landmarkcollection+xml"
    )
    applicationSOLIDUSvndFULL_STOPnokiaFULL_STOPncd = "application/vnd.nokia.ncd"
    applicationSOLIDUSvndFULL_STOPnokiaFULL_STOOn_gageFULL_STOPacPLUS_SIGNxml = (
        "application/vnd.nokia.n-gage.ac+xml"
    )
    applicationSOLIDUSvndFULL_STOPnokiaFULL_STOOn_gageFULL_STOPdata = (
        "application/vnd.nokia.n-gage.data"
    )
    applicationSOLIDUSvndFULL_STOPnokiaFULL_STOOn_gageFULL_STOPsymbianFULL_STOPinstall = "application/vnd.nokia.n-gage.symbian.install"
    applicationSOLIDUSvndFULL_STOPnokiaFULL_STOPpcdPLUS_SIGNwbxml = (
        "application/vnd.nokia.pcd+wbxml"
    )
    applicationSOLIDUSvndFULL_STOPnokiaFULL_STOPpcdPLUS_SIGNxml = (
        "application/vnd.nokia.pcd+xml"
    )
    applicationSOLIDUSvndFULL_STOPnokiaFULL_STOPradio_preset = (
        "application/vnd.nokia.radio-preset"
    )
    applicationSOLIDUSvndFULL_STOPnokiaFULL_STOPradio_presets = (
        "application/vnd.nokia.radio-presets"
    )
    applicationSOLIDUSvndFULL_STOPnovadigmFULL_STOPEDM = "application/vnd.novadigm.EDM"
    applicationSOLIDUSvndFULL_STOPnovadigmFULL_STOPEDX = "application/vnd.novadigm.EDX"
    applicationSOLIDUSvndFULL_STOPnovadigmFULL_STOPEXT = "application/vnd.novadigm.EXT"
    applicationSOLIDUSvndFULL_STOPntt_localFULL_STOPcontent_share = (
        "application/vnd.ntt-local.content-share"
    )
    applicationSOLIDUSvndFULL_STOPntt_localFULL_STOPfile_transfer = (
        "application/vnd.ntt-local.file-transfer"
    )
    applicationSOLIDUSvndFULL_STOPntt_localFULL_STOPogw_remote_access = (
        "application/vnd.ntt-local.ogw_remote-access"
    )
    applicationSOLIDUSvndFULL_STOPntt_localFULL_STOPsip_ta_remote = (
        "application/vnd.ntt-local.sip-ta_remote"
    )
    applicationSOLIDUSvndFULL_STOPntt_localFULL_STOPsip_ta_tcp_stream = (
        "application/vnd.ntt-local.sip-ta_tcp_stream"
    )
    applicationSOLIDUSvndFULL_STOPoaiFULL_STOPworkflows = (
        "application/vnd.oai.workflows"
    )
    applicationSOLIDUSvndFULL_STOPoaiFULL_STOPworkflowsPLUS_SIGNjson = (
        "application/vnd.oai.workflows+json"
    )
    applicationSOLIDUSvndFULL_STOPoaiFULL_STOPworkflowsPLUS_SIGNyaml = (
        "application/vnd.oai.workflows+yaml"
    )
    applicationSOLIDUSvndFULL_STOPoasisFULL_STOPopendocumentFULL_STOPbase = (
        "application/vnd.oasis.opendocument.base"
    )
    applicationSOLIDUSvndFULL_STOPoasisFULL_STOPopendocumentFULL_STOPchart = (
        "application/vnd.oasis.opendocument.chart"
    )
    applicationSOLIDUSvndFULL_STOPoasisFULL_STOPopendocumentFULL_STOPchart_template = (
        "application/vnd.oasis.opendocument.chart-template"
    )
    applicationSOLIDUSvndFULL_STOPoasisFULL_STOPopendocumentFULL_STOPdatabase = (
        "application/vnd.oasis.opendocument.database"
    )
    applicationSOLIDUSvndFULL_STOPoasisFULL_STOPopendocumentFULL_STOPformula = (
        "application/vnd.oasis.opendocument.formula"
    )
    applicationSOLIDUSvndFULL_STOPoasisFULL_STOPopendocumentFULL_STOPformula_template = "application/vnd.oasis.opendocument.formula-template"
    applicationSOLIDUSvndFULL_STOPoasisFULL_STOPopendocumentFULL_STOPgraphics = (
        "application/vnd.oasis.opendocument.graphics"
    )
    applicationSOLIDUSvndFULL_STOPoasisFULL_STOPopendocumentFULL_STOPgraphics_template = "application/vnd.oasis.opendocument.graphics-template"
    applicationSOLIDUSvndFULL_STOPoasisFULL_STOPopendocumentFULL_STOPimage = (
        "application/vnd.oasis.opendocument.image"
    )
    applicationSOLIDUSvndFULL_STOPoasisFULL_STOPopendocumentFULL_STOPimage_template = (
        "application/vnd.oasis.opendocument.image-template"
    )
    applicationSOLIDUSvndFULL_STOPoasisFULL_STOPopendocumentFULL_STOPpresentation = (
        "application/vnd.oasis.opendocument.presentation"
    )
    applicationSOLIDUSvndFULL_STOPoasisFULL_STOPopendocumentFULL_STOPpresentation_template = "application/vnd.oasis.opendocument.presentation-template"
    applicationSOLIDUSvndFULL_STOPoasisFULL_STOPopendocumentFULL_STOPspreadsheet = (
        "application/vnd.oasis.opendocument.spreadsheet"
    )
    applicationSOLIDUSvndFULL_STOPoasisFULL_STOPopendocumentFULL_STOPspreadsheet_template = "application/vnd.oasis.opendocument.spreadsheet-template"
    applicationSOLIDUSvndFULL_STOPoasisFULL_STOPopendocumentFULL_STOPtext = (
        "application/vnd.oasis.opendocument.text"
    )
    applicationSOLIDUSvndFULL_STOPoasisFULL_STOPopendocumentFULL_STOPtext_master = (
        "application/vnd.oasis.opendocument.text-master"
    )
    applicationSOLIDUSvndFULL_STOPoasisFULL_STOPopendocumentFULL_STOPtext_master_template = "application/vnd.oasis.opendocument.text-master-template"
    applicationSOLIDUSvndFULL_STOPoasisFULL_STOPopendocumentFULL_STOPtext_template = (
        "application/vnd.oasis.opendocument.text-template"
    )
    applicationSOLIDUSvndFULL_STOPoasisFULL_STOPopendocumentFULL_STOPtext_web = (
        "application/vnd.oasis.opendocument.text-web"
    )
    applicationSOLIDUSvndFULL_STOPobn = "application/vnd.obn"
    applicationSOLIDUSvndFULL_STOPocfPLUS_SIGNcbor = "application/vnd.ocf+cbor"
    applicationSOLIDUSvndFULL_STOPociFULL_STOPimageFULL_STOPmanifestFULL_STOPv1PLUS_SIGNjson = "application/vnd.oci.image.manifest.v1+json"
    applicationSOLIDUSvndFULL_STOPoftnFULL_STOPl10nPLUS_SIGNjson = (
        "application/vnd.oftn.l10n+json"
    )
    applicationSOLIDUSvndFULL_STOPoipfFULL_STOPcontentaccessdownloadPLUS_SIGNxml = (
        "application/vnd.oipf.contentaccessdownload+xml"
    )
    applicationSOLIDUSvndFULL_STOPoipfFULL_STOPcontentaccessstreamingPLUS_SIGNxml = (
        "application/vnd.oipf.contentaccessstreaming+xml"
    )
    applicationSOLIDUSvndFULL_STOPoipfFULL_STOPcspg_hexbinary = (
        "application/vnd.oipf.cspg-hexbinary"
    )
    applicationSOLIDUSvndFULL_STOPoipfFULL_STOPdaeFULL_STOPsvgPLUS_SIGNxml = (
        "application/vnd.oipf.dae.svg+xml"
    )
    applicationSOLIDUSvndFULL_STOPoipfFULL_STOPdaeFULL_STOPxhtmlPLUS_SIGNxml = (
        "application/vnd.oipf.dae.xhtml+xml"
    )
    applicationSOLIDUSvndFULL_STOPoipfFULL_STOPmippvcontrolmessagePLUS_SIGNxml = (
        "application/vnd.oipf.mippvcontrolmessage+xml"
    )
    applicationSOLIDUSvndFULL_STOPoipfFULL_STOPpaeFULL_STOPgem = (
        "application/vnd.oipf.pae.gem"
    )
    applicationSOLIDUSvndFULL_STOPoipfFULL_STOPspdiscoveryPLUS_SIGNxml = (
        "application/vnd.oipf.spdiscovery+xml"
    )
    applicationSOLIDUSvndFULL_STOPoipfFULL_STOPspdlistPLUS_SIGNxml = (
        "application/vnd.oipf.spdlist+xml"
    )
    applicationSOLIDUSvndFULL_STOPoipfFULL_STOPueprofilePLUS_SIGNxml = (
        "application/vnd.oipf.ueprofile+xml"
    )
    applicationSOLIDUSvndFULL_STOPoipfFULL_STOPuserprofilePLUS_SIGNxml = (
        "application/vnd.oipf.userprofile+xml"
    )
    applicationSOLIDUSvndFULL_STOPolpc_sugar = "application/vnd.olpc-sugar"
    applicationSOLIDUSvndFULL_STOPomaFULL_STOPbcastFULL_STOPassociated_procedure_parameterPLUS_SIGNxml = "application/vnd.oma.bcast.associated-procedure-parameter+xml"
    applicationSOLIDUSvndFULL_STOPomaFULL_STOPbcastFULL_STOPdrm_triggerPLUS_SIGNxml = (
        "application/vnd.oma.bcast.drm-trigger+xml"
    )
    applicationSOLIDUSvndFULL_STOPomaFULL_STOPbcastFULL_STOPimdPLUS_SIGNxml = (
        "application/vnd.oma.bcast.imd+xml"
    )
    applicationSOLIDUSvndFULL_STOPomaFULL_STOPbcastFULL_STOPltkm = (
        "application/vnd.oma.bcast.ltkm"
    )
    applicationSOLIDUSvndFULL_STOPomaFULL_STOPbcastFULL_STOPnotificationPLUS_SIGNxml = (
        "application/vnd.oma.bcast.notification+xml"
    )
    applicationSOLIDUSvndFULL_STOPomaFULL_STOPbcastFULL_STOPprovisioningtrigger = (
        "application/vnd.oma.bcast.provisioningtrigger"
    )
    applicationSOLIDUSvndFULL_STOPomaFULL_STOPbcastFULL_STOPsgboot = (
        "application/vnd.oma.bcast.sgboot"
    )
    applicationSOLIDUSvndFULL_STOPomaFULL_STOPbcastFULL_STOPsgddPLUS_SIGNxml = (
        "application/vnd.oma.bcast.sgdd+xml"
    )
    applicationSOLIDUSvndFULL_STOPomaFULL_STOPbcastFULL_STOPsgdu = (
        "application/vnd.oma.bcast.sgdu"
    )
    applicationSOLIDUSvndFULL_STOPomaFULL_STOPbcastFULL_STOPsimple_symbol_container = (
        "application/vnd.oma.bcast.simple-symbol-container"
    )
    applicationSOLIDUSvndFULL_STOPomaFULL_STOPbcastFULL_STOPsmartcard_triggerPLUS_SIGNxml = "application/vnd.oma.bcast.smartcard-trigger+xml"
    applicationSOLIDUSvndFULL_STOPomaFULL_STOPbcastFULL_STOPsprovPLUS_SIGNxml = (
        "application/vnd.oma.bcast.sprov+xml"
    )
    applicationSOLIDUSvndFULL_STOPomaFULL_STOPbcastFULL_STOPstkm = (
        "application/vnd.oma.bcast.stkm"
    )
    applicationSOLIDUSvndFULL_STOPomaFULL_STOPcab_address_bookPLUS_SIGNxml = (
        "application/vnd.oma.cab-address-book+xml"
    )
    applicationSOLIDUSvndFULL_STOPomaFULL_STOPcab_feature_handlerPLUS_SIGNxml = (
        "application/vnd.oma.cab-feature-handler+xml"
    )
    applicationSOLIDUSvndFULL_STOPomaFULL_STOPcab_pccPLUS_SIGNxml = (
        "application/vnd.oma.cab-pcc+xml"
    )
    applicationSOLIDUSvndFULL_STOPomaFULL_STOPcab_subs_invitePLUS_SIGNxml = (
        "application/vnd.oma.cab-subs-invite+xml"
    )
    applicationSOLIDUSvndFULL_STOPomaFULL_STOPcab_user_prefsPLUS_SIGNxml = (
        "application/vnd.oma.cab-user-prefs+xml"
    )
    applicationSOLIDUSvndFULL_STOPomaFULL_STOPdcd = "application/vnd.oma.dcd"
    applicationSOLIDUSvndFULL_STOPomaFULL_STOPdcdc = "application/vnd.oma.dcdc"
    applicationSOLIDUSvndFULL_STOPomaFULL_STOPdd2PLUS_SIGNxml = (
        "application/vnd.oma.dd2+xml"
    )
    applicationSOLIDUSvndFULL_STOPomaFULL_STOPdrmFULL_STOPrisdPLUS_SIGNxml = (
        "application/vnd.oma.drm.risd+xml"
    )
    applicationSOLIDUSvndFULL_STOPomaFULL_STOPgroup_usage_listPLUS_SIGNxml = (
        "application/vnd.oma.group-usage-list+xml"
    )
    applicationSOLIDUSvndFULL_STOPomaFULL_STOPlwm2mPLUS_SIGNcbor = (
        "application/vnd.oma.lwm2m+cbor"
    )
    applicationSOLIDUSvndFULL_STOPomaFULL_STOPlwm2mPLUS_SIGNjson = (
        "application/vnd.oma.lwm2m+json"
    )
    applicationSOLIDUSvndFULL_STOPomaFULL_STOPlwm2mPLUS_SIGNtlv = (
        "application/vnd.oma.lwm2m+tlv"
    )
    applicationSOLIDUSvndFULL_STOPomaFULL_STOPpalPLUS_SIGNxml = (
        "application/vnd.oma.pal+xml"
    )
    applicationSOLIDUSvndFULL_STOPomaFULL_STOPpocFULL_STOPdetailed_progress_reportPLUS_SIGNxml = "application/vnd.oma.poc.detailed-progress-report+xml"
    applicationSOLIDUSvndFULL_STOPomaFULL_STOPpocFULL_STOPfinal_reportPLUS_SIGNxml = (
        "application/vnd.oma.poc.final-report+xml"
    )
    applicationSOLIDUSvndFULL_STOPomaFULL_STOPpocFULL_STOPgroupsPLUS_SIGNxml = (
        "application/vnd.oma.poc.groups+xml"
    )
    applicationSOLIDUSvndFULL_STOPomaFULL_STOPpocFULL_STOPinvocation_descriptorPLUS_SIGNxml = "application/vnd.oma.poc.invocation-descriptor+xml"
    applicationSOLIDUSvndFULL_STOPomaFULL_STOPpocFULL_STOPoptimized_progress_reportPLUS_SIGNxml = "application/vnd.oma.poc.optimized-progress-report+xml"
    applicationSOLIDUSvndFULL_STOPomaFULL_STOPpush = "application/vnd.oma.push"
    applicationSOLIDUSvndFULL_STOPomaFULL_STOPscidmFULL_STOPmessagesPLUS_SIGNxml = (
        "application/vnd.oma.scidm.messages+xml"
    )
    applicationSOLIDUSvndFULL_STOPomaFULL_STOPxcap_directoryPLUS_SIGNxml = (
        "application/vnd.oma.xcap-directory+xml"
    )
    applicationSOLIDUSvndFULL_STOPomads_emailPLUS_SIGNxml = (
        "application/vnd.omads-email+xml"
    )
    applicationSOLIDUSvndFULL_STOPomads_filePLUS_SIGNxml = (
        "application/vnd.omads-file+xml"
    )
    applicationSOLIDUSvndFULL_STOPomads_folderPLUS_SIGNxml = (
        "application/vnd.omads-folder+xml"
    )
    applicationSOLIDUSvndFULL_STOPomaloc_supl_init = "application/vnd.omaloc-supl-init"
    applicationSOLIDUSvndFULL_STOPoma_scws_config = "application/vnd.oma-scws-config"
    applicationSOLIDUSvndFULL_STOPoma_scws_http_request = (
        "application/vnd.oma-scws-http-request"
    )
    applicationSOLIDUSvndFULL_STOPoma_scws_http_response = (
        "application/vnd.oma-scws-http-response"
    )
    applicationSOLIDUSvndFULL_STOPonepager = "application/vnd.onepager"
    applicationSOLIDUSvndFULL_STOPonepagertamp = "application/vnd.onepagertamp"
    applicationSOLIDUSvndFULL_STOPonepagertamx = "application/vnd.onepagertamx"
    applicationSOLIDUSvndFULL_STOPonepagertat = "application/vnd.onepagertat"
    applicationSOLIDUSvndFULL_STOPonepagertatp = "application/vnd.onepagertatp"
    applicationSOLIDUSvndFULL_STOPonepagertatx = "application/vnd.onepagertatx"
    applicationSOLIDUSvndFULL_STOPonvifFULL_STOPmetadata = (
        "application/vnd.onvif.metadata"
    )
    applicationSOLIDUSvndFULL_STOPopenbloxFULL_STOPgamePLUS_SIGNxml = (
        "application/vnd.openblox.game+xml"
    )
    applicationSOLIDUSvndFULL_STOPopenbloxFULL_STOPgame_binary = (
        "application/vnd.openblox.game-binary"
    )
    applicationSOLIDUSvndFULL_STOPopeneyeFULL_STOPoeb = "application/vnd.openeye.oeb"
    applicationSOLIDUSvndFULL_STOPopenstreetmapFULL_STOPdataPLUS_SIGNxml = (
        "application/vnd.openstreetmap.data+xml"
    )
    applicationSOLIDUSvndFULL_STOPopentimestampsFULL_STOPots = (
        "application/vnd.opentimestamps.ots"
    )
    applicationSOLIDUSvndFULL_STOPopenvpiFULL_STOPdspxPLUS_SIGNjson = (
        "application/vnd.openvpi.dspx+json"
    )
    applicationSOLIDUSvndFULL_STOPopenxmlformats_officedocumentFULL_STOPcustom_propertiesPLUS_SIGNxml = "application/vnd.openxmlformats-officedocument.custom-properties+xml"
    applicationSOLIDUSvndFULL_STOPopenxmlformats_officedocumentFULL_STOPcustomXmlPropertiesPLUS_SIGNxml = "application/vnd.openxmlformats-officedocument.customXmlProperties+xml"
    applicationSOLIDUSvndFULL_STOPopenxmlformats_officedocumentFULL_STOPdrawingPLUS_SIGNxml = "application/vnd.openxmlformats-officedocument.drawing+xml"
    applicationSOLIDUSvndFULL_STOPopenxmlformats_officedocumentFULL_STOPdrawingmlFULL_STOPchartPLUS_SIGNxml = "application/vnd.openxmlformats-officedocument.drawingml.chart+xml"
    applicationSOLIDUSvndFULL_STOPopenxmlformats_officedocumentFULL_STOPdrawingmlFULL_STOPchartshapesPLUS_SIGNxml = "application/vnd.openxmlformats-officedocument.drawingml.chartshapes+xml"
    applicationSOLIDUSvndFULL_STOPopenxmlformats_officedocumentFULL_STOPdrawingmlFULL_STOPdiagramColorsPLUS_SIGNxml = "application/vnd.openxmlformats-officedocument.drawingml.diagramColors+xml"
    applicationSOLIDUSvndFULL_STOPopenxmlformats_officedocumentFULL_STOPdrawingmlFULL_STOPdiagramDataPLUS_SIGNxml = "application/vnd.openxmlformats-officedocument.drawingml.diagramData+xml"
    applicationSOLIDUSvndFULL_STOPopenxmlformats_officedocumentFULL_STOPdrawingmlFULL_STOPdiagramLayoutPLUS_SIGNxml = "application/vnd.openxmlformats-officedocument.drawingml.diagramLayout+xml"
    applicationSOLIDUSvndFULL_STOPopenxmlformats_officedocumentFULL_STOPdrawingmlFULL_STOPdiagramStylePLUS_SIGNxml = "application/vnd.openxmlformats-officedocument.drawingml.diagramStyle+xml"
    applicationSOLIDUSvndFULL_STOPopenxmlformats_officedocumentFULL_STOPextended_propertiesPLUS_SIGNxml = "application/vnd.openxmlformats-officedocument.extended-properties+xml"
    applicationSOLIDUSvndFULL_STOPopenxmlformats_officedocumentFULL_STOPpresentationmlFULL_STOPcommentAuthorsPLUS_SIGNxml = "application/vnd.openxmlformats-officedocument.presentationml.commentAuthors+xml"
    applicationSOLIDUSvndFULL_STOPopenxmlformats_officedocumentFULL_STOPpresentationmlFULL_STOPcommentsPLUS_SIGNxml = "application/vnd.openxmlformats-officedocument.presentationml.comments+xml"
    applicationSOLIDUSvndFULL_STOPopenxmlformats_officedocumentFULL_STOPpresentationmlFULL_STOPhandoutMasterPLUS_SIGNxml = "application/vnd.openxmlformats-officedocument.presentationml.handoutMaster+xml"
    applicationSOLIDUSvndFULL_STOPopenxmlformats_officedocumentFULL_STOPpresentationmlFULL_STOPnotesMasterPLUS_SIGNxml = "application/vnd.openxmlformats-officedocument.presentationml.notesMaster+xml"
    applicationSOLIDUSvndFULL_STOPopenxmlformats_officedocumentFULL_STOPpresentationmlFULL_STOPnotesSlidePLUS_SIGNxml = "application/vnd.openxmlformats-officedocument.presentationml.notesSlide+xml"
    applicationSOLIDUSvndFULL_STOPopenxmlformats_officedocumentFULL_STOPpresentationmlFULL_STOPpresentation = "application/vnd.openxmlformats-officedocument.presentationml.presentation"
    applicationSOLIDUSvndFULL_STOPopenxmlformats_officedocumentFULL_STOPpresentationmlFULL_STOPpresentationFULL_STOPmainPLUS_SIGNxml = "application/vnd.openxmlformats-officedocument.presentationml.presentation.main+xml"
    applicationSOLIDUSvndFULL_STOPopenxmlformats_officedocumentFULL_STOPpresentationmlFULL_STOPpresPropsPLUS_SIGNxml = "application/vnd.openxmlformats-officedocument.presentationml.presProps+xml"
    applicationSOLIDUSvndFULL_STOPopenxmlformats_officedocumentFULL_STOPpresentationmlFULL_STOPslide = "application/vnd.openxmlformats-officedocument.presentationml.slide"
    applicationSOLIDUSvndFULL_STOPopenxmlformats_officedocumentFULL_STOPpresentationmlFULL_STOPslidePLUS_SIGNxml = "application/vnd.openxmlformats-officedocument.presentationml.slide+xml"
    applicationSOLIDUSvndFULL_STOPopenxmlformats_officedocumentFULL_STOPpresentationmlFULL_STOPslideLayoutPLUS_SIGNxml = "application/vnd.openxmlformats-officedocument.presentationml.slideLayout+xml"
    applicationSOLIDUSvndFULL_STOPopenxmlformats_officedocumentFULL_STOPpresentationmlFULL_STOPslideMasterPLUS_SIGNxml = "application/vnd.openxmlformats-officedocument.presentationml.slideMaster+xml"
    applicationSOLIDUSvndFULL_STOPopenxmlformats_officedocumentFULL_STOPpresentationmlFULL_STOPslideshow = "application/vnd.openxmlformats-officedocument.presentationml.slideshow"
    applicationSOLIDUSvndFULL_STOPopenxmlformats_officedocumentFULL_STOPpresentationmlFULL_STOPslideshowFULL_STOPmainPLUS_SIGNxml = "application/vnd.openxmlformats-officedocument.presentationml.slideshow.main+xml"
    applicationSOLIDUSvndFULL_STOPopenxmlformats_officedocumentFULL_STOPpresentationmlFULL_STOPslideUpdateInfoPLUS_SIGNxml = "application/vnd.openxmlformats-officedocument.presentationml.slideUpdateInfo+xml"
    applicationSOLIDUSvndFULL_STOPopenxmlformats_officedocumentFULL_STOPpresentationmlFULL_STOPtableStylesPLUS_SIGNxml = "application/vnd.openxmlformats-officedocument.presentationml.tableStyles+xml"
    applicationSOLIDUSvndFULL_STOPopenxmlformats_officedocumentFULL_STOPpresentationmlFULL_STOPtagsPLUS_SIGNxml = "application/vnd.openxmlformats-officedocument.presentationml.tags+xml"
    applicationSOLIDUSvndFULL_STOPopenxmlformats_officedocumentFULL_STOPpresentationmlFULL_STOPtemplate = "application/vnd.openxmlformats-officedocument.presentationml.template"
    applicationSOLIDUSvndFULL_STOPopenxmlformats_officedocumentFULL_STOPpresentationmlFULL_STOPtemplateFULL_STOPmainPLUS_SIGNxml = "application/vnd.openxmlformats-officedocument.presentationml.template.main+xml"
    applicationSOLIDUSvndFULL_STOPopenxmlformats_officedocumentFULL_STOPpresentationmlFULL_STOPviewPropsPLUS_SIGNxml = "application/vnd.openxmlformats-officedocument.presentationml.viewProps+xml"
    applicationSOLIDUSvndFULL_STOPopenxmlformats_officedocumentFULL_STOPspreadsheetmlFULL_STOPcalcChainPLUS_SIGNxml = "application/vnd.openxmlformats-officedocument.spreadsheetml.calcChain+xml"
    applicationSOLIDUSvndFULL_STOPopenxmlformats_officedocumentFULL_STOPspreadsheetmlFULL_STOPchartsheetPLUS_SIGNxml = "application/vnd.openxmlformats-officedocument.spreadsheetml.chartsheet+xml"
    applicationSOLIDUSvndFULL_STOPopenxmlformats_officedocumentFULL_STOPspreadsheetmlFULL_STOPcommentsPLUS_SIGNxml = "application/vnd.openxmlformats-officedocument.spreadsheetml.comments+xml"
    applicationSOLIDUSvndFULL_STOPopenxmlformats_officedocumentFULL_STOPspreadsheetmlFULL_STOPconnectionsPLUS_SIGNxml = "application/vnd.openxmlformats-officedocument.spreadsheetml.connections+xml"
    applicationSOLIDUSvndFULL_STOPopenxmlformats_officedocumentFULL_STOPspreadsheetmlFULL_STOPdialogsheetPLUS_SIGNxml = "application/vnd.openxmlformats-officedocument.spreadsheetml.dialogsheet+xml"
    applicationSOLIDUSvndFULL_STOPopenxmlformats_officedocumentFULL_STOPspreadsheetmlFULL_STOPexternalLinkPLUS_SIGNxml = "application/vnd.openxmlformats-officedocument.spreadsheetml.externalLink+xml"
    applicationSOLIDUSvndFULL_STOPopenxmlformats_officedocumentFULL_STOPspreadsheetmlFULL_STOPpivotCacheDefinitionPLUS_SIGNxml = "application/vnd.openxmlformats-officedocument.spreadsheetml.pivotCacheDefinition+xml"
    applicationSOLIDUSvndFULL_STOPopenxmlformats_officedocumentFULL_STOPspreadsheetmlFULL_STOPpivotCacheRecordsPLUS_SIGNxml = "application/vnd.openxmlformats-officedocument.spreadsheetml.pivotCacheRecords+xml"
    applicationSOLIDUSvndFULL_STOPopenxmlformats_officedocumentFULL_STOPspreadsheetmlFULL_STOPpivotTablePLUS_SIGNxml = "application/vnd.openxmlformats-officedocument.spreadsheetml.pivotTable+xml"
    applicationSOLIDUSvndFULL_STOPopenxmlformats_officedocumentFULL_STOPspreadsheetmlFULL_STOPqueryTablePLUS_SIGNxml = "application/vnd.openxmlformats-officedocument.spreadsheetml.queryTable+xml"
    applicationSOLIDUSvndFULL_STOPopenxmlformats_officedocumentFULL_STOPspreadsheetmlFULL_STOPrevisionHeadersPLUS_SIGNxml = "application/vnd.openxmlformats-officedocument.spreadsheetml.revisionHeaders+xml"
    applicationSOLIDUSvndFULL_STOPopenxmlformats_officedocumentFULL_STOPspreadsheetmlFULL_STOPrevisionLogPLUS_SIGNxml = "application/vnd.openxmlformats-officedocument.spreadsheetml.revisionLog+xml"
    applicationSOLIDUSvndFULL_STOPopenxmlformats_officedocumentFULL_STOPspreadsheetmlFULL_STOPsharedStringsPLUS_SIGNxml = "application/vnd.openxmlformats-officedocument.spreadsheetml.sharedStrings+xml"
    applicationSOLIDUSvndFULL_STOPopenxmlformats_officedocumentFULL_STOPspreadsheetmlFULL_STOPsheet = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    applicationSOLIDUSvndFULL_STOPopenxmlformats_officedocumentFULL_STOPspreadsheetmlFULL_STOPsheetFULL_STOPmainPLUS_SIGNxml = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"
    applicationSOLIDUSvndFULL_STOPopenxmlformats_officedocumentFULL_STOPspreadsheetmlFULL_STOPsheetMetadataPLUS_SIGNxml = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheetMetadata+xml"
    applicationSOLIDUSvndFULL_STOPopenxmlformats_officedocumentFULL_STOPspreadsheetmlFULL_STOPstylesPLUS_SIGNxml = "application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml"
    applicationSOLIDUSvndFULL_STOPopenxmlformats_officedocumentFULL_STOPspreadsheetmlFULL_STOPtablePLUS_SIGNxml = "application/vnd.openxmlformats-officedocument.spreadsheetml.table+xml"
    applicationSOLIDUSvndFULL_STOPopenxmlformats_officedocumentFULL_STOPspreadsheetmlFULL_STOPtableSingleCellsPLUS_SIGNxml = "application/vnd.openxmlformats-officedocument.spreadsheetml.tableSingleCells+xml"
    applicationSOLIDUSvndFULL_STOPopenxmlformats_officedocumentFULL_STOPspreadsheetmlFULL_STOPtemplate = "application/vnd.openxmlformats-officedocument.spreadsheetml.template"
    applicationSOLIDUSvndFULL_STOPopenxmlformats_officedocumentFULL_STOPspreadsheetmlFULL_STOPtemplateFULL_STOPmainPLUS_SIGNxml = "application/vnd.openxmlformats-officedocument.spreadsheetml.template.main+xml"
    applicationSOLIDUSvndFULL_STOPopenxmlformats_officedocumentFULL_STOPspreadsheetmlFULL_STOPuserNamesPLUS_SIGNxml = "application/vnd.openxmlformats-officedocument.spreadsheetml.userNames+xml"
    applicationSOLIDUSvndFULL_STOPopenxmlformats_officedocumentFULL_STOPspreadsheetmlFULL_STOPvolatileDependenciesPLUS_SIGNxml = "application/vnd.openxmlformats-officedocument.spreadsheetml.volatileDependencies+xml"
    applicationSOLIDUSvndFULL_STOPopenxmlformats_officedocumentFULL_STOPspreadsheetmlFULL_STOPworksheetPLUS_SIGNxml = "application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"
    applicationSOLIDUSvndFULL_STOPopenxmlformats_officedocumentFULL_STOPthemePLUS_SIGNxml = "application/vnd.openxmlformats-officedocument.theme+xml"
    applicationSOLIDUSvndFULL_STOPopenxmlformats_officedocumentFULL_STOPthemeOverridePLUS_SIGNxml = "application/vnd.openxmlformats-officedocument.themeOverride+xml"
    applicationSOLIDUSvndFULL_STOPopenxmlformats_officedocumentFULL_STOPvmlDrawing = (
        "application/vnd.openxmlformats-officedocument.vmlDrawing"
    )
    applicationSOLIDUSvndFULL_STOPopenxmlformats_officedocumentFULL_STOPwordprocessingmlFULL_STOPcommentsPLUS_SIGNxml = "application/vnd.openxmlformats-officedocument.wordprocessingml.comments+xml"
    applicationSOLIDUSvndFULL_STOPopenxmlformats_officedocumentFULL_STOPwordprocessingmlFULL_STOPdocument = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    applicationSOLIDUSvndFULL_STOPopenxmlformats_officedocumentFULL_STOPwordprocessingmlFULL_STOPdocumentFULL_STOPglossaryPLUS_SIGNxml = "application/vnd.openxmlformats-officedocument.wordprocessingml.document.glossary+xml"
    applicationSOLIDUSvndFULL_STOPopenxmlformats_officedocumentFULL_STOPwordprocessingmlFULL_STOPdocumentFULL_STOPmainPLUS_SIGNxml = "application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"
    applicationSOLIDUSvndFULL_STOPopenxmlformats_officedocumentFULL_STOPwordprocessingmlFULL_STOPendnotesPLUS_SIGNxml = "application/vnd.openxmlformats-officedocument.wordprocessingml.endnotes+xml"
    applicationSOLIDUSvndFULL_STOPopenxmlformats_officedocumentFULL_STOPwordprocessingmlFULL_STOPfontTablePLUS_SIGNxml = "application/vnd.openxmlformats-officedocument.wordprocessingml.fontTable+xml"
    applicationSOLIDUSvndFULL_STOPopenxmlformats_officedocumentFULL_STOPwordprocessingmlFULL_STOPfooterPLUS_SIGNxml = "application/vnd.openxmlformats-officedocument.wordprocessingml.footer+xml"
    applicationSOLIDUSvndFULL_STOPopenxmlformats_officedocumentFULL_STOPwordprocessingmlFULL_STOPfootnotesPLUS_SIGNxml = "application/vnd.openxmlformats-officedocument.wordprocessingml.footnotes+xml"
    applicationSOLIDUSvndFULL_STOPopenxmlformats_officedocumentFULL_STOPwordprocessingmlFULL_STOPnumberingPLUS_SIGNxml = "application/vnd.openxmlformats-officedocument.wordprocessingml.numbering+xml"
    applicationSOLIDUSvndFULL_STOPopenxmlformats_officedocumentFULL_STOPwordprocessingmlFULL_STOPsettingsPLUS_SIGNxml = "application/vnd.openxmlformats-officedocument.wordprocessingml.settings+xml"
    applicationSOLIDUSvndFULL_STOPopenxmlformats_officedocumentFULL_STOPwordprocessingmlFULL_STOPstylesPLUS_SIGNxml = "application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"
    applicationSOLIDUSvndFULL_STOPopenxmlformats_officedocumentFULL_STOPwordprocessingmlFULL_STOPtemplate = "application/vnd.openxmlformats-officedocument.wordprocessingml.template"
    applicationSOLIDUSvndFULL_STOPopenxmlformats_officedocumentFULL_STOPwordprocessingmlFULL_STOPtemplateFULL_STOPmainPLUS_SIGNxml = "application/vnd.openxmlformats-officedocument.wordprocessingml.template.main+xml"
    applicationSOLIDUSvndFULL_STOPopenxmlformats_officedocumentFULL_STOPwordprocessingmlFULL_STOPwebSettingsPLUS_SIGNxml = "application/vnd.openxmlformats-officedocument.wordprocessingml.webSettings+xml"
    applicationSOLIDUSvndFULL_STOPopenxmlformats_packageFULL_STOPcore_propertiesPLUS_SIGNxml = "application/vnd.openxmlformats-package.core-properties+xml"
    applicationSOLIDUSvndFULL_STOPopenxmlformats_packageFULL_STOPdigital_signature_xmlsignaturePLUS_SIGNxml = "application/vnd.openxmlformats-package.digital-signature-xmlsignature+xml"
    applicationSOLIDUSvndFULL_STOPopenxmlformats_packageFULL_STOPrelationshipsPLUS_SIGNxml = "application/vnd.openxmlformats-package.relationships+xml"
    applicationSOLIDUSvndFULL_STOPoracleFULL_STOPresourcePLUS_SIGNjson = (
        "application/vnd.oracle.resource+json"
    )
    applicationSOLIDUSvndFULL_STOPorangeFULL_STOPindata = (
        "application/vnd.orange.indata"
    )
    applicationSOLIDUSvndFULL_STOPosaFULL_STOPnetdeploy = (
        "application/vnd.osa.netdeploy"
    )
    applicationSOLIDUSvndFULL_STOPosgeoFULL_STOPmapguideFULL_STOPpackage = (
        "application/vnd.osgeo.mapguide.package"
    )
    applicationSOLIDUSvndFULL_STOPosgiFULL_STOPbundle = "application/vnd.osgi.bundle"
    applicationSOLIDUSvndFULL_STOPosgiFULL_STOPdp = "application/vnd.osgi.dp"
    applicationSOLIDUSvndFULL_STOPosgiFULL_STOPsubsystem = (
        "application/vnd.osgi.subsystem"
    )
    applicationSOLIDUSvndFULL_STOPotpsFULL_STOPct_kipPLUS_SIGNxml = (
        "application/vnd.otps.ct-kip+xml"
    )
    applicationSOLIDUSvndFULL_STOPoxliFULL_STOPcountgraph = (
        "application/vnd.oxli.countgraph"
    )
    applicationSOLIDUSvndFULL_STOPpagerdutyPLUS_SIGNjson = (
        "application/vnd.pagerduty+json"
    )
    applicationSOLIDUSvndFULL_STOPpalm = "application/vnd.palm"
    applicationSOLIDUSvndFULL_STOPpanoply = "application/vnd.panoply"
    applicationSOLIDUSvndFULL_STOPpaosFULL_STOPxml = "application/vnd.paos.xml"
    applicationSOLIDUSvndFULL_STOPpatentdive = "application/vnd.patentdive"
    applicationSOLIDUSvndFULL_STOPpatientecommsdoc = "application/vnd.patientecommsdoc"
    applicationSOLIDUSvndFULL_STOPpawaafile = "application/vnd.pawaafile"
    applicationSOLIDUSvndFULL_STOPpcos = "application/vnd.pcos"
    applicationSOLIDUSvndFULL_STOPpgFULL_STOPformat = "application/vnd.pg.format"
    applicationSOLIDUSvndFULL_STOPpgFULL_STOPosasli = "application/vnd.pg.osasli"
    applicationSOLIDUSvndFULL_STOPpiaccessFULL_STOPapplication_licence = (
        "application/vnd.piaccess.application-licence"
    )
    applicationSOLIDUSvndFULL_STOPpicsel = "application/vnd.picsel"
    applicationSOLIDUSvndFULL_STOPpmiFULL_STOPwidget = "application/vnd.pmi.widget"
    applicationSOLIDUSvndFULL_STOPpocFULL_STOPgroup_advertisementPLUS_SIGNxml = (
        "application/vnd.poc.group-advertisement+xml"
    )
    applicationSOLIDUSvndFULL_STOPpocketlearn = "application/vnd.pocketlearn"
    applicationSOLIDUSvndFULL_STOPpowerbuilder6 = "application/vnd.powerbuilder6"
    applicationSOLIDUSvndFULL_STOPpowerbuilder6_s = "application/vnd.powerbuilder6-s"
    applicationSOLIDUSvndFULL_STOPpowerbuilder7 = "application/vnd.powerbuilder7"
    applicationSOLIDUSvndFULL_STOPpowerbuilder75 = "application/vnd.powerbuilder75"
    applicationSOLIDUSvndFULL_STOPpowerbuilder75_s = "application/vnd.powerbuilder75-s"
    applicationSOLIDUSvndFULL_STOPpowerbuilder7_s = "application/vnd.powerbuilder7-s"
    applicationSOLIDUSvndFULL_STOPpreminet = "application/vnd.preminet"
    applicationSOLIDUSvndFULL_STOPpreviewsystemsFULL_STOPbox = (
        "application/vnd.previewsystems.box"
    )
    applicationSOLIDUSvndFULL_STOPproteusFULL_STOPmagazine = (
        "application/vnd.proteus.magazine"
    )
    applicationSOLIDUSvndFULL_STOPpsfs = "application/vnd.psfs"
    applicationSOLIDUSvndFULL_STOPptFULL_STOPmundusmundi = (
        "application/vnd.pt.mundusmundi"
    )
    applicationSOLIDUSvndFULL_STOPpublishare_delta_tree = (
        "application/vnd.publishare-delta-tree"
    )
    applicationSOLIDUSvndFULL_STOPpviFULL_STOPptid1 = "application/vnd.pvi.ptid1"
    applicationSOLIDUSvndFULL_STOPpwg_multiplexed = "application/vnd.pwg-multiplexed"
    applicationSOLIDUSvndFULL_STOPpwg_xhtml_printPLUS_SIGNxml = (
        "application/vnd.pwg-xhtml-print+xml"
    )
    applicationSOLIDUSvndFULL_STOPqualcommFULL_STOPbrew_app_res = (
        "application/vnd.qualcomm.brew-app-res"
    )
    applicationSOLIDUSvndFULL_STOPquarantainenet = "application/vnd.quarantainenet"
    applicationSOLIDUSvndFULL_STOPQuarkFULL_STOPQuarkXPress = (
        "application/vnd.Quark.QuarkXPress"
    )
    applicationSOLIDUSvndFULL_STOPquobject_quoxdocument = (
        "application/vnd.quobject-quoxdocument"
    )
    applicationSOLIDUSvndFULL_STOPradisysFULL_STOPmomlPLUS_SIGNxml = (
        "application/vnd.radisys.moml+xml"
    )
    applicationSOLIDUSvndFULL_STOPradisysFULL_STOPmsmlPLUS_SIGNxml = (
        "application/vnd.radisys.msml+xml"
    )
    applicationSOLIDUSvndFULL_STOPradisysFULL_STOPmsml_auditPLUS_SIGNxml = (
        "application/vnd.radisys.msml-audit+xml"
    )
    applicationSOLIDUSvndFULL_STOPradisysFULL_STOPmsml_audit_confPLUS_SIGNxml = (
        "application/vnd.radisys.msml-audit-conf+xml"
    )
    applicationSOLIDUSvndFULL_STOPradisysFULL_STOPmsml_audit_connPLUS_SIGNxml = (
        "application/vnd.radisys.msml-audit-conn+xml"
    )
    applicationSOLIDUSvndFULL_STOPradisysFULL_STOPmsml_audit_dialogPLUS_SIGNxml = (
        "application/vnd.radisys.msml-audit-dialog+xml"
    )
    applicationSOLIDUSvndFULL_STOPradisysFULL_STOPmsml_audit_streamPLUS_SIGNxml = (
        "application/vnd.radisys.msml-audit-stream+xml"
    )
    applicationSOLIDUSvndFULL_STOPradisysFULL_STOPmsml_confPLUS_SIGNxml = (
        "application/vnd.radisys.msml-conf+xml"
    )
    applicationSOLIDUSvndFULL_STOPradisysFULL_STOPmsml_dialogPLUS_SIGNxml = (
        "application/vnd.radisys.msml-dialog+xml"
    )
    applicationSOLIDUSvndFULL_STOPradisysFULL_STOPmsml_dialog_basePLUS_SIGNxml = (
        "application/vnd.radisys.msml-dialog-base+xml"
    )
    applicationSOLIDUSvndFULL_STOPradisysFULL_STOPmsml_dialog_fax_detectPLUS_SIGNxml = (
        "application/vnd.radisys.msml-dialog-fax-detect+xml"
    )
    applicationSOLIDUSvndFULL_STOPradisysFULL_STOPmsml_dialog_fax_sendrecvPLUS_SIGNxml = "application/vnd.radisys.msml-dialog-fax-sendrecv+xml"
    applicationSOLIDUSvndFULL_STOPradisysFULL_STOPmsml_dialog_groupPLUS_SIGNxml = (
        "application/vnd.radisys.msml-dialog-group+xml"
    )
    applicationSOLIDUSvndFULL_STOPradisysFULL_STOPmsml_dialog_speechPLUS_SIGNxml = (
        "application/vnd.radisys.msml-dialog-speech+xml"
    )
    applicationSOLIDUSvndFULL_STOPradisysFULL_STOPmsml_dialog_transformPLUS_SIGNxml = (
        "application/vnd.radisys.msml-dialog-transform+xml"
    )
    applicationSOLIDUSvndFULL_STOPrainstorFULL_STOPdata = (
        "application/vnd.rainstor.data"
    )
    applicationSOLIDUSvndFULL_STOPrapid = "application/vnd.rapid"
    applicationSOLIDUSvndFULL_STOPrar = "application/vnd.rar"
    applicationSOLIDUSvndFULL_STOPrealvncFULL_STOPbed = "application/vnd.realvnc.bed"
    applicationSOLIDUSvndFULL_STOPrecordareFULL_STOPmusicxml = (
        "application/vnd.recordare.musicxml"
    )
    applicationSOLIDUSvndFULL_STOPrecordareFULL_STOPmusicxmlPLUS_SIGNxml = (
        "application/vnd.recordare.musicxml+xml"
    )
    applicationSOLIDUSvndFULL_STOPrelpipe = "application/vnd.relpipe"
    applicationSOLIDUSvndFULL_STOPRenLearnFULL_STOPrlprint = (
        "application/vnd.RenLearn.rlprint"
    )
    applicationSOLIDUSvndFULL_STOPresilientFULL_STOPlogic = (
        "application/vnd.resilient.logic"
    )
    applicationSOLIDUSvndFULL_STOPrestfulPLUS_SIGNjson = "application/vnd.restful+json"
    applicationSOLIDUSvndFULL_STOPrigFULL_STOPcryptonote = (
        "application/vnd.rig.cryptonote"
    )
    applicationSOLIDUSvndFULL_STOProute66FULL_STOPlink66PLUS_SIGNxml = (
        "application/vnd.route66.link66+xml"
    )
    applicationSOLIDUSvndFULL_STOPrs_274x = "application/vnd.rs-274x"
    applicationSOLIDUSvndFULL_STOPruckusFULL_STOPdownload = (
        "application/vnd.ruckus.download"
    )
    applicationSOLIDUSvndFULL_STOPs3sms = "application/vnd.s3sms"
    applicationSOLIDUSvndFULL_STOPsailingtrackerFULL_STOPtrack = (
        "application/vnd.sailingtracker.track"
    )
    applicationSOLIDUSvndFULL_STOPsar = "application/vnd.sar"
    applicationSOLIDUSvndFULL_STOPsbmFULL_STOPcid = "application/vnd.sbm.cid"
    applicationSOLIDUSvndFULL_STOPsbmFULL_STOPmid2 = "application/vnd.sbm.mid2"
    applicationSOLIDUSvndFULL_STOPscribus = "application/vnd.scribus"
    applicationSOLIDUSvndFULL_STOPsealedFULL_STOP3df = "application/vnd.sealed.3df"
    applicationSOLIDUSvndFULL_STOPsealedFULL_STOPcsf = "application/vnd.sealed.csf"
    applicationSOLIDUSvndFULL_STOPsealedFULL_STOPdoc = "application/vnd.sealed.doc"
    applicationSOLIDUSvndFULL_STOPsealedFULL_STOPeml = "application/vnd.sealed.eml"
    applicationSOLIDUSvndFULL_STOPsealedFULL_STOPmht = "application/vnd.sealed.mht"
    applicationSOLIDUSvndFULL_STOPsealedFULL_STOPnet = "application/vnd.sealed.net"
    applicationSOLIDUSvndFULL_STOPsealedFULL_STOPppt = "application/vnd.sealed.ppt"
    applicationSOLIDUSvndFULL_STOPsealedFULL_STOPtiff = "application/vnd.sealed.tiff"
    applicationSOLIDUSvndFULL_STOPsealedFULL_STOPxls = "application/vnd.sealed.xls"
    applicationSOLIDUSvndFULL_STOPsealedmediaFULL_STOPsoftsealFULL_STOPhtml = (
        "application/vnd.sealedmedia.softseal.html"
    )
    applicationSOLIDUSvndFULL_STOPsealedmediaFULL_STOPsoftsealFULL_STOPpdf = (
        "application/vnd.sealedmedia.softseal.pdf"
    )
    applicationSOLIDUSvndFULL_STOPseemail = "application/vnd.seemail"
    applicationSOLIDUSvndFULL_STOPseisPLUS_SIGNjson = "application/vnd.seis+json"
    applicationSOLIDUSvndFULL_STOPsema = "application/vnd.sema"
    applicationSOLIDUSvndFULL_STOPsemd = "application/vnd.semd"
    applicationSOLIDUSvndFULL_STOPsemf = "application/vnd.semf"
    applicationSOLIDUSvndFULL_STOPshade_save_file = "application/vnd.shade-save-file"
    applicationSOLIDUSvndFULL_STOPshanaFULL_STOPinformedFULL_STOPformdata = (
        "application/vnd.shana.informed.formdata"
    )
    applicationSOLIDUSvndFULL_STOPshanaFULL_STOPinformedFULL_STOPformtemplate = (
        "application/vnd.shana.informed.formtemplate"
    )
    applicationSOLIDUSvndFULL_STOPshanaFULL_STOPinformedFULL_STOPinterchange = (
        "application/vnd.shana.informed.interchange"
    )
    applicationSOLIDUSvndFULL_STOPshanaFULL_STOPinformedFULL_STOPpackage = (
        "application/vnd.shana.informed.package"
    )
    applicationSOLIDUSvndFULL_STOPshootproofPLUS_SIGNjson = (
        "application/vnd.shootproof+json"
    )
    applicationSOLIDUSvndFULL_STOPshopkickPLUS_SIGNjson = (
        "application/vnd.shopkick+json"
    )
    applicationSOLIDUSvndFULL_STOPshp = "application/vnd.shp"
    applicationSOLIDUSvndFULL_STOPshx = "application/vnd.shx"
    applicationSOLIDUSvndFULL_STOPsigrokFULL_STOPsession = (
        "application/vnd.sigrok.session"
    )
    applicationSOLIDUSvndFULL_STOPSimTech_MindMapper = (
        "application/vnd.SimTech-MindMapper"
    )
    applicationSOLIDUSvndFULL_STOPsirenPLUS_SIGNjson = "application/vnd.siren+json"
    applicationSOLIDUSvndFULL_STOPsketchometry = "application/vnd.sketchometry"
    applicationSOLIDUSvndFULL_STOPsmaf = "application/vnd.smaf"
    applicationSOLIDUSvndFULL_STOPsmartFULL_STOPnotebook = (
        "application/vnd.smart.notebook"
    )
    applicationSOLIDUSvndFULL_STOPsmartFULL_STOPteacher = (
        "application/vnd.smart.teacher"
    )
    applicationSOLIDUSvndFULL_STOPsmintioFULL_STOPportalsFULL_STOParchive = (
        "application/vnd.smintio.portals.archive"
    )
    applicationSOLIDUSvndFULL_STOPsnesdev_page_table = (
        "application/vnd.snesdev-page-table"
    )
    applicationSOLIDUSvndFULL_STOPsoftware602FULL_STOPfillerFULL_STOPformPLUS_SIGNxml = "application/vnd.software602.filler.form+xml"
    applicationSOLIDUSvndFULL_STOPsoftware602FULL_STOPfillerFULL_STOPform_xml_zip = (
        "application/vnd.software602.filler.form-xml-zip"
    )
    applicationSOLIDUSvndFULL_STOPsolentFULL_STOPsdkmPLUS_SIGNxml = (
        "application/vnd.solent.sdkm+xml"
    )
    applicationSOLIDUSvndFULL_STOPspotfireFULL_STOPdxp = "application/vnd.spotfire.dxp"
    applicationSOLIDUSvndFULL_STOPspotfireFULL_STOPsfs = "application/vnd.spotfire.sfs"
    applicationSOLIDUSvndFULL_STOPsqlite3 = "application/vnd.sqlite3"
    applicationSOLIDUSvndFULL_STOPsss_cod = "application/vnd.sss-cod"
    applicationSOLIDUSvndFULL_STOPsss_dtf = "application/vnd.sss-dtf"
    applicationSOLIDUSvndFULL_STOPsss_ntf = "application/vnd.sss-ntf"
    applicationSOLIDUSvndFULL_STOPstepmaniaFULL_STOPpackage = (
        "application/vnd.stepmania.package"
    )
    applicationSOLIDUSvndFULL_STOPstepmaniaFULL_STOPstepchart = (
        "application/vnd.stepmania.stepchart"
    )
    applicationSOLIDUSvndFULL_STOPstreet_stream = "application/vnd.street-stream"
    applicationSOLIDUSvndFULL_STOPsunFULL_STOPwadlPLUS_SIGNxml = (
        "application/vnd.sun.wadl+xml"
    )
    applicationSOLIDUSvndFULL_STOPsus_calendar = "application/vnd.sus-calendar"
    applicationSOLIDUSvndFULL_STOPsvd = "application/vnd.svd"
    applicationSOLIDUSvndFULL_STOPswiftview_ics = "application/vnd.swiftview-ics"
    applicationSOLIDUSvndFULL_STOPsybylFULL_STOPmol2 = "application/vnd.sybyl.mol2"
    applicationSOLIDUSvndFULL_STOPsyclePLUS_SIGNxml = "application/vnd.sycle+xml"
    applicationSOLIDUSvndFULL_STOPsyftPLUS_SIGNjson = "application/vnd.syft+json"
    applicationSOLIDUSvndFULL_STOPsyncmlFULL_STOPdmFULL_STOPnotification = (
        "application/vnd.syncml.dm.notification"
    )
    applicationSOLIDUSvndFULL_STOPsyncmlFULL_STOPdmPLUS_SIGNwbxml = (
        "application/vnd.syncml.dm+wbxml"
    )
    applicationSOLIDUSvndFULL_STOPsyncmlFULL_STOPdmPLUS_SIGNxml = (
        "application/vnd.syncml.dm+xml"
    )
    applicationSOLIDUSvndFULL_STOPsyncmlFULL_STOPdmddfPLUS_SIGNwbxml = (
        "application/vnd.syncml.dmddf+wbxml"
    )
    applicationSOLIDUSvndFULL_STOPsyncmlFULL_STOPdmddfPLUS_SIGNxml = (
        "application/vnd.syncml.dmddf+xml"
    )
    applicationSOLIDUSvndFULL_STOPsyncmlFULL_STOPdmtndsPLUS_SIGNwbxml = (
        "application/vnd.syncml.dmtnds+wbxml"
    )
    applicationSOLIDUSvndFULL_STOPsyncmlFULL_STOPdmtndsPLUS_SIGNxml = (
        "application/vnd.syncml.dmtnds+xml"
    )
    applicationSOLIDUSvndFULL_STOPsyncmlFULL_STOPdsFULL_STOPnotification = (
        "application/vnd.syncml.ds.notification"
    )
    applicationSOLIDUSvndFULL_STOPsyncmlPLUS_SIGNxml = "application/vnd.syncml+xml"
    applicationSOLIDUSvndFULL_STOPtableschemaPLUS_SIGNjson = (
        "application/vnd.tableschema+json"
    )
    applicationSOLIDUSvndFULL_STOPtaoFULL_STOPintent_module_archive = (
        "application/vnd.tao.intent-module-archive"
    )
    applicationSOLIDUSvndFULL_STOPtcpdumpFULL_STOPpcap = "application/vnd.tcpdump.pcap"
    applicationSOLIDUSvndFULL_STOPthink_cellFULL_STOPppttcPLUS_SIGNjson = (
        "application/vnd.think-cell.ppttc+json"
    )
    applicationSOLIDUSvndFULL_STOPtmdFULL_STOPmediaflexFULL_STOPapiPLUS_SIGNxml = (
        "application/vnd.tmd.mediaflex.api+xml"
    )
    applicationSOLIDUSvndFULL_STOPtml = "application/vnd.tml"
    applicationSOLIDUSvndFULL_STOPtmobile_livetv = "application/vnd.tmobile-livetv"
    applicationSOLIDUSvndFULL_STOPtriFULL_STOPonesource = (
        "application/vnd.tri.onesource"
    )
    applicationSOLIDUSvndFULL_STOPtridFULL_STOPtpt = "application/vnd.trid.tpt"
    applicationSOLIDUSvndFULL_STOPtriscapeFULL_STOPmxs = "application/vnd.triscape.mxs"
    applicationSOLIDUSvndFULL_STOPtrueapp = "application/vnd.trueapp"
    applicationSOLIDUSvndFULL_STOPtruedoc = "application/vnd.truedoc"
    applicationSOLIDUSvndFULL_STOPubisoftFULL_STOPwebplayer = (
        "application/vnd.ubisoft.webplayer"
    )
    applicationSOLIDUSvndFULL_STOPufdl = "application/vnd.ufdl"
    applicationSOLIDUSvndFULL_STOPuicFULL_STOPosdmPLUS_SIGNjson = (
        "application/vnd.uic.osdm+json"
    )
    applicationSOLIDUSvndFULL_STOPuiqFULL_STOPtheme = "application/vnd.uiq.theme"
    applicationSOLIDUSvndFULL_STOPumajin = "application/vnd.umajin"
    applicationSOLIDUSvndFULL_STOPunity = "application/vnd.unity"
    applicationSOLIDUSvndFULL_STOPuomlPLUS_SIGNxml = "application/vnd.uoml+xml"
    applicationSOLIDUSvndFULL_STOPuplanetFULL_STOPalert = (
        "application/vnd.uplanet.alert"
    )
    applicationSOLIDUSvndFULL_STOPuplanetFULL_STOPalert_wbxml = (
        "application/vnd.uplanet.alert-wbxml"
    )
    applicationSOLIDUSvndFULL_STOPuplanetFULL_STOPbearer_choice = (
        "application/vnd.uplanet.bearer-choice"
    )
    applicationSOLIDUSvndFULL_STOPuplanetFULL_STOPbearer_choice_wbxml = (
        "application/vnd.uplanet.bearer-choice-wbxml"
    )
    applicationSOLIDUSvndFULL_STOPuplanetFULL_STOPcacheop = (
        "application/vnd.uplanet.cacheop"
    )
    applicationSOLIDUSvndFULL_STOPuplanetFULL_STOPcacheop_wbxml = (
        "application/vnd.uplanet.cacheop-wbxml"
    )
    applicationSOLIDUSvndFULL_STOPuplanetFULL_STOPchannel = (
        "application/vnd.uplanet.channel"
    )
    applicationSOLIDUSvndFULL_STOPuplanetFULL_STOPchannel_wbxml = (
        "application/vnd.uplanet.channel-wbxml"
    )
    applicationSOLIDUSvndFULL_STOPuplanetFULL_STOPlist = "application/vnd.uplanet.list"
    applicationSOLIDUSvndFULL_STOPuplanetFULL_STOPlistcmd = (
        "application/vnd.uplanet.listcmd"
    )
    applicationSOLIDUSvndFULL_STOPuplanetFULL_STOPlistcmd_wbxml = (
        "application/vnd.uplanet.listcmd-wbxml"
    )
    applicationSOLIDUSvndFULL_STOPuplanetFULL_STOPlist_wbxml = (
        "application/vnd.uplanet.list-wbxml"
    )
    applicationSOLIDUSvndFULL_STOPuplanetFULL_STOPsignal = (
        "application/vnd.uplanet.signal"
    )
    applicationSOLIDUSvndFULL_STOPuri_map = "application/vnd.uri-map"
    applicationSOLIDUSvndFULL_STOPvalveFULL_STOPsourceFULL_STOPmaterial = (
        "application/vnd.valve.source.material"
    )
    applicationSOLIDUSvndFULL_STOPvcx = "application/vnd.vcx"
    applicationSOLIDUSvndFULL_STOPvd_study = "application/vnd.vd-study"
    applicationSOLIDUSvndFULL_STOPvectorworks = "application/vnd.vectorworks"
    applicationSOLIDUSvndFULL_STOPvelPLUS_SIGNjson = "application/vnd.vel+json"
    applicationSOLIDUSvndFULL_STOPveraisonFULL_STOPtsm_reportPLUS_SIGNcbor = (
        "application/vnd.veraison.tsm-report+cbor"
    )
    applicationSOLIDUSvndFULL_STOPveraisonFULL_STOPtsm_reportPLUS_SIGNjson = (
        "application/vnd.veraison.tsm-report+json"
    )
    applicationSOLIDUSvndFULL_STOPverimatrixFULL_STOPvcas = (
        "application/vnd.verimatrix.vcas"
    )
    applicationSOLIDUSvndFULL_STOPveritoneFULL_STOPaionPLUS_SIGNjson = (
        "application/vnd.veritone.aion+json"
    )
    applicationSOLIDUSvndFULL_STOPveryantFULL_STOPthin = "application/vnd.veryant.thin"
    applicationSOLIDUSvndFULL_STOPvesFULL_STOPencrypted = (
        "application/vnd.ves.encrypted"
    )
    applicationSOLIDUSvndFULL_STOPvidsoftFULL_STOPvidconference = (
        "application/vnd.vidsoft.vidconference"
    )
    applicationSOLIDUSvndFULL_STOPvisio = "application/vnd.visio"
    applicationSOLIDUSvndFULL_STOPvisionary = "application/vnd.visionary"
    applicationSOLIDUSvndFULL_STOPvividenceFULL_STOPscriptfile = (
        "application/vnd.vividence.scriptfile"
    )
    applicationSOLIDUSvndFULL_STOPvocalshaperFULL_STOPvsp4 = (
        "application/vnd.vocalshaper.vsp4"
    )
    applicationSOLIDUSvndFULL_STOPvsf = "application/vnd.vsf"
    applicationSOLIDUSvndFULL_STOPwapFULL_STOPsic = "application/vnd.wap.sic"
    applicationSOLIDUSvndFULL_STOPwapFULL_STOPslc = "application/vnd.wap.slc"
    applicationSOLIDUSvndFULL_STOPwapFULL_STOPwbxml = "application/vnd.wap.wbxml"
    applicationSOLIDUSvndFULL_STOPwapFULL_STOPwmlc = "application/vnd.wap.wmlc"
    applicationSOLIDUSvndFULL_STOPwapFULL_STOPwmlscriptc = (
        "application/vnd.wap.wmlscriptc"
    )
    applicationSOLIDUSvndFULL_STOPwasmflowFULL_STOPwafl = (
        "application/vnd.wasmflow.wafl"
    )
    applicationSOLIDUSvndFULL_STOPwebturbo = "application/vnd.webturbo"
    applicationSOLIDUSvndFULL_STOPwfaFULL_STOPdpp = "application/vnd.wfa.dpp"
    applicationSOLIDUSvndFULL_STOPwfaFULL_STOPp2p = "application/vnd.wfa.p2p"
    applicationSOLIDUSvndFULL_STOPwfaFULL_STOPwsc = "application/vnd.wfa.wsc"
    applicationSOLIDUSvndFULL_STOPwindowsFULL_STOPdevicepairing = (
        "application/vnd.windows.devicepairing"
    )
    applicationSOLIDUSvndFULL_STOPwmc = "application/vnd.wmc"
    applicationSOLIDUSvndFULL_STOPwmfFULL_STOPbootstrap = (
        "application/vnd.wmf.bootstrap"
    )
    applicationSOLIDUSvndFULL_STOPwolframFULL_STOPmathematica = (
        "application/vnd.wolfram.mathematica"
    )
    applicationSOLIDUSvndFULL_STOPwolframFULL_STOPmathematicaFULL_STOPpackage = (
        "application/vnd.wolfram.mathematica.package"
    )
    applicationSOLIDUSvndFULL_STOPwolframFULL_STOPplayer = (
        "application/vnd.wolfram.player"
    )
    applicationSOLIDUSvndFULL_STOPwordlift = "application/vnd.wordlift"
    applicationSOLIDUSvndFULL_STOPwordperfect = "application/vnd.wordperfect"
    applicationSOLIDUSvndFULL_STOPwqd = "application/vnd.wqd"
    applicationSOLIDUSvndFULL_STOPwrq_hp3000_labelled = (
        "application/vnd.wrq-hp3000-labelled"
    )
    applicationSOLIDUSvndFULL_STOPwtFULL_STOPstf = "application/vnd.wt.stf"
    applicationSOLIDUSvndFULL_STOPwvFULL_STOPcspPLUS_SIGNwbxml = (
        "application/vnd.wv.csp+wbxml"
    )
    applicationSOLIDUSvndFULL_STOPwvFULL_STOPcspPLUS_SIGNxml = (
        "application/vnd.wv.csp+xml"
    )
    applicationSOLIDUSvndFULL_STOPwvFULL_STOPsspPLUS_SIGNxml = (
        "application/vnd.wv.ssp+xml"
    )
    applicationSOLIDUSvndFULL_STOPxacmlPLUS_SIGNjson = "application/vnd.xacml+json"
    applicationSOLIDUSvndFULL_STOPxara = "application/vnd.xara"
    applicationSOLIDUSvndFULL_STOPxarinFULL_STOPcpj = "application/vnd.xarin.cpj"
    applicationSOLIDUSvndFULL_STOPxecrets_encrypted = (
        "application/vnd.xecrets-encrypted"
    )
    applicationSOLIDUSvndFULL_STOPxfdl = "application/vnd.xfdl"
    applicationSOLIDUSvndFULL_STOPxfdlFULL_STOPwebform = "application/vnd.xfdl.webform"
    applicationSOLIDUSvndFULL_STOPxmiPLUS_SIGNxml = "application/vnd.xmi+xml"
    applicationSOLIDUSvndFULL_STOPxmpieFULL_STOPcpkg = "application/vnd.xmpie.cpkg"
    applicationSOLIDUSvndFULL_STOPxmpieFULL_STOPdpkg = "application/vnd.xmpie.dpkg"
    applicationSOLIDUSvndFULL_STOPxmpieFULL_STOPplan = "application/vnd.xmpie.plan"
    applicationSOLIDUSvndFULL_STOPxmpieFULL_STOPppkg = "application/vnd.xmpie.ppkg"
    applicationSOLIDUSvndFULL_STOPxmpieFULL_STOPxlim = "application/vnd.xmpie.xlim"
    applicationSOLIDUSvndFULL_STOPyamahaFULL_STOPhv_dic = (
        "application/vnd.yamaha.hv-dic"
    )
    applicationSOLIDUSvndFULL_STOPyamahaFULL_STOPhv_script = (
        "application/vnd.yamaha.hv-script"
    )
    applicationSOLIDUSvndFULL_STOPyamahaFULL_STOPhv_voice = (
        "application/vnd.yamaha.hv-voice"
    )
    applicationSOLIDUSvndFULL_STOPyamahaFULL_STOPopenscoreformat = (
        "application/vnd.yamaha.openscoreformat"
    )
    applicationSOLIDUSvndFULL_STOPyamahaFULL_STOPopenscoreformatFULL_STOPosfpvgPLUS_SIGNxml = "application/vnd.yamaha.openscoreformat.osfpvg+xml"
    applicationSOLIDUSvndFULL_STOPyamahaFULL_STOPremote_setup = (
        "application/vnd.yamaha.remote-setup"
    )
    applicationSOLIDUSvndFULL_STOPyamahaFULL_STOPsmaf_audio = (
        "application/vnd.yamaha.smaf-audio"
    )
    applicationSOLIDUSvndFULL_STOPyamahaFULL_STOPsmaf_phrase = (
        "application/vnd.yamaha.smaf-phrase"
    )
    applicationSOLIDUSvndFULL_STOPyamahaFULL_STOPthrough_ngn = (
        "application/vnd.yamaha.through-ngn"
    )
    applicationSOLIDUSvndFULL_STOPyamahaFULL_STOPtunnel_udpencap = (
        "application/vnd.yamaha.tunnel-udpencap"
    )
    applicationSOLIDUSvndFULL_STOPyaoweme = "application/vnd.yaoweme"
    applicationSOLIDUSvndFULL_STOPyellowriver_custom_menu = (
        "application/vnd.yellowriver-custom-menu"
    )
    applicationSOLIDUSvndFULL_STOPyoutubeFULL_STOPyt = "application/vnd.youtube.yt"
    applicationSOLIDUSvndFULL_STOPzul = "application/vnd.zul"
    applicationSOLIDUSvndFULL_STOPzzazzFULL_STOPdeckPLUS_SIGNxml = (
        "application/vnd.zzazz.deck+xml"
    )
    applicationSOLIDUSvoicexmlPLUS_SIGNxml = "application/voicexml+xml"
    applicationSOLIDUSvoucher_cmsPLUS_SIGNjson = "application/voucher-cms+json"
    applicationSOLIDUSvoucher_jwsPLUS_SIGNjson = "application/voucher-jws+json"
    applicationSOLIDUSvp = "application/vp"
    applicationSOLIDUSvpPLUS_SIGNcose = "application/vp+cose"
    applicationSOLIDUSvpPLUS_SIGNjwt = "application/vp+jwt"
    applicationSOLIDUSvq_rtcpxr = "application/vq-rtcpxr"
    applicationSOLIDUSwasm = "application/wasm"
    applicationSOLIDUSwatcherinfoPLUS_SIGNxml = "application/watcherinfo+xml"
    applicationSOLIDUSwebpush_optionsPLUS_SIGNjson = "application/webpush-options+json"
    applicationSOLIDUSwhoispp_query = "application/whoispp-query"
    applicationSOLIDUSwhoispp_response = "application/whoispp-response"
    applicationSOLIDUSwidget = "application/widget"
    applicationSOLIDUSwita = "application/wita"
    applicationSOLIDUSwordperfect5FULL_STOP1 = "application/wordperfect5.1"
    applicationSOLIDUSwsdlPLUS_SIGNxml = "application/wsdl+xml"
    applicationSOLIDUSwspolicyPLUS_SIGNxml = "application/wspolicy+xml"
    applicationSOLIDUSx400_bp = "application/x400-bp"
    applicationSOLIDUSxacmlPLUS_SIGNxml = "application/xacml+xml"
    applicationSOLIDUSxcap_attPLUS_SIGNxml = "application/xcap-att+xml"
    applicationSOLIDUSxcap_capsPLUS_SIGNxml = "application/xcap-caps+xml"
    applicationSOLIDUSxcap_diffPLUS_SIGNxml = "application/xcap-diff+xml"
    applicationSOLIDUSxcap_elPLUS_SIGNxml = "application/xcap-el+xml"
    applicationSOLIDUSxcap_errorPLUS_SIGNxml = "application/xcap-error+xml"
    applicationSOLIDUSxcap_nsPLUS_SIGNxml = "application/xcap-ns+xml"
    applicationSOLIDUSxcon_conference_infoPLUS_SIGNxml = (
        "application/xcon-conference-info+xml"
    )
    applicationSOLIDUSxcon_conference_info_diffPLUS_SIGNxml = (
        "application/xcon-conference-info-diff+xml"
    )
    applicationSOLIDUSxencPLUS_SIGNxml = "application/xenc+xml"
    applicationSOLIDUSxfdf = "application/xfdf"
    applicationSOLIDUSxhtmlPLUS_SIGNxml = "application/xhtml+xml"
    applicationSOLIDUSxliffPLUS_SIGNxml = "application/xliff+xml"
    applicationSOLIDUSxml = "application/xml"
    applicationSOLIDUSxml_dtd = "application/xml-dtd"
    applicationSOLIDUSxml_external_parsed_entity = (
        "application/xml-external-parsed-entity"
    )
    applicationSOLIDUSxml_patchPLUS_SIGNxml = "application/xml-patch+xml"
    applicationSOLIDUSxmppPLUS_SIGNxml = "application/xmpp+xml"
    applicationSOLIDUSxopPLUS_SIGNxml = "application/xop+xml"
    applicationSOLIDUSx_pki_message = "application/x-pki-message"
    applicationSOLIDUSxsltPLUS_SIGNxml = "application/xslt+xml"
    applicationSOLIDUSxvPLUS_SIGNxml = "application/xv+xml"
    applicationSOLIDUSx_www_form_urlencoded = "application/x-www-form-urlencoded"
    applicationSOLIDUSx_x509_ca_cert = "application/x-x509-ca-cert"
    applicationSOLIDUSx_x509_ca_ra_cert = "application/x-x509-ca-ra-cert"
    applicationSOLIDUSx_x509_next_ca_cert = "application/x-x509-next-ca-cert"
    applicationSOLIDUSyaml = "application/yaml"
    applicationSOLIDUSyang = "application/yang"
    applicationSOLIDUSyang_dataPLUS_SIGNcbor = "application/yang-data+cbor"
    applicationSOLIDUSyang_dataPLUS_SIGNjson = "application/yang-data+json"
    applicationSOLIDUSyang_dataPLUS_SIGNxml = "application/yang-data+xml"
    applicationSOLIDUSyang_patchPLUS_SIGNjson = "application/yang-patch+json"
    applicationSOLIDUSyang_patchPLUS_SIGNxml = "application/yang-patch+xml"
    applicationSOLIDUSyang_sidPLUS_SIGNjson = "application/yang-sid+json"
    applicationSOLIDUSyinPLUS_SIGNxml = "application/yin+xml"
    applicationSOLIDUSzip = "application/zip"
    applicationSOLIDUSzlib = "application/zlib"
    applicationSOLIDUSzstd = "application/zstd"
    audioSOLIDUS1d_interleaved_parityfec = "audio/1d-interleaved-parityfec"
    audioSOLIDUS32kadpcm = "audio/32kadpcm"
    audioSOLIDUS3gpp = "audio/3gpp"
    audioSOLIDUS3gpp2 = "audio/3gpp2"
    audioSOLIDUSaac = "audio/aac"
    audioSOLIDUSac3 = "audio/ac3"
    audioSOLIDUSAMR = "audio/AMR"
    audioSOLIDUSAMR_WB = "audio/AMR-WB"
    audioSOLIDUSamr_wbPLUS_SIGN = "audio/amr-wb+"
    audioSOLIDUSaptx = "audio/aptx"
    audioSOLIDUSasc = "audio/asc"
    audioSOLIDUSATRAC3 = "audio/ATRAC3"
    audioSOLIDUSATRAC_ADVANCED_LOSSLESS = "audio/ATRAC-ADVANCED-LOSSLESS"
    audioSOLIDUSATRAC_X = "audio/ATRAC-X"
    audioSOLIDUSbasic = "audio/basic"
    audioSOLIDUSBV16 = "audio/BV16"
    audioSOLIDUSBV32 = "audio/BV32"
    audioSOLIDUSclearmode = "audio/clearmode"
    audioSOLIDUSCN = "audio/CN"
    audioSOLIDUSDAT12 = "audio/DAT12"
    audioSOLIDUSdls = "audio/dls"
    audioSOLIDUSdsr_es201108 = "audio/dsr-es201108"
    audioSOLIDUSdsr_es202050 = "audio/dsr-es202050"
    audioSOLIDUSdsr_es202211 = "audio/dsr-es202211"
    audioSOLIDUSdsr_es202212 = "audio/dsr-es202212"
    audioSOLIDUSDV = "audio/DV"
    audioSOLIDUSDVI4 = "audio/DVI4"
    audioSOLIDUSeac3 = "audio/eac3"
    audioSOLIDUSencaprtp = "audio/encaprtp"
    audioSOLIDUSEVRC = "audio/EVRC"
    audioSOLIDUSEVRC0 = "audio/EVRC0"
    audioSOLIDUSEVRC1 = "audio/EVRC1"
    audioSOLIDUSEVRCB = "audio/EVRCB"
    audioSOLIDUSEVRCB0 = "audio/EVRCB0"
    audioSOLIDUSEVRCB1 = "audio/EVRCB1"
    audioSOLIDUSEVRCNW = "audio/EVRCNW"
    audioSOLIDUSEVRCNW0 = "audio/EVRCNW0"
    audioSOLIDUSEVRCNW1 = "audio/EVRCNW1"
    audioSOLIDUSEVRC_QCP = "audio/EVRC-QCP"
    audioSOLIDUSEVRCWB = "audio/EVRCWB"
    audioSOLIDUSEVRCWB0 = "audio/EVRCWB0"
    audioSOLIDUSEVRCWB1 = "audio/EVRCWB1"
    audioSOLIDUSEVS = "audio/EVS"
    audioSOLIDUSexample = "audio/example"
    audioSOLIDUSflac = "audio/flac"
    audioSOLIDUSflexfec = "audio/flexfec"
    audioSOLIDUSfwdred = "audio/fwdred"
    audioSOLIDUSG711_0 = "audio/G711-0"
    audioSOLIDUSG719 = "audio/G719"
    audioSOLIDUSG722 = "audio/G722"
    audioSOLIDUSG7221 = "audio/G7221"
    audioSOLIDUSG723 = "audio/G723"
    audioSOLIDUSG726_16 = "audio/G726-16"
    audioSOLIDUSG726_24 = "audio/G726-24"
    audioSOLIDUSG726_32 = "audio/G726-32"
    audioSOLIDUSG726_40 = "audio/G726-40"
    audioSOLIDUSG728 = "audio/G728"
    audioSOLIDUSG729 = "audio/G729"
    audioSOLIDUSG7291 = "audio/G7291"
    audioSOLIDUSG729D = "audio/G729D"
    audioSOLIDUSG729E = "audio/G729E"
    audioSOLIDUSGSM = "audio/GSM"
    audioSOLIDUSGSM_EFR = "audio/GSM-EFR"
    audioSOLIDUSGSM_HR_08 = "audio/GSM-HR-08"
    audioSOLIDUSiLBC = "audio/iLBC"
    audioSOLIDUSip_mr_v2FULL_STOP5 = "audio/ip-mr_v2.5"
    audioSOLIDUSL16 = "audio/L16"
    audioSOLIDUSL20 = "audio/L20"
    audioSOLIDUSL24 = "audio/L24"
    audioSOLIDUSL8 = "audio/L8"
    audioSOLIDUSLPC = "audio/LPC"
    audioSOLIDUSmatroska = "audio/matroska"
    audioSOLIDUSMELP = "audio/MELP"
    audioSOLIDUSMELP1200 = "audio/MELP1200"
    audioSOLIDUSMELP2400 = "audio/MELP2400"
    audioSOLIDUSMELP600 = "audio/MELP600"
    audioSOLIDUSmhas = "audio/mhas"
    audioSOLIDUSmidi_clip = "audio/midi-clip"
    audioSOLIDUSmobile_xmf = "audio/mobile-xmf"
    audioSOLIDUSmp4 = "audio/mp4"
    audioSOLIDUSMP4A_LATM = "audio/MP4A-LATM"
    audioSOLIDUSMPA = "audio/MPA"
    audioSOLIDUSmpa_robust = "audio/mpa-robust"
    audioSOLIDUSmpeg = "audio/mpeg"
    audioSOLIDUSmpeg4_generic = "audio/mpeg4-generic"
    audioSOLIDUSogg = "audio/ogg"
    audioSOLIDUSopus = "audio/opus"
    audioSOLIDUSparityfec = "audio/parityfec"
    audioSOLIDUSPCMA = "audio/PCMA"
    audioSOLIDUSPCMA_WB = "audio/PCMA-WB"
    audioSOLIDUSPCMU = "audio/PCMU"
    audioSOLIDUSPCMU_WB = "audio/PCMU-WB"
    audioSOLIDUSprsFULL_STOPsid = "audio/prs.sid"
    audioSOLIDUSQCELP = "audio/QCELP"
    audioSOLIDUSraptorfec = "audio/raptorfec"
    audioSOLIDUSRED = "audio/RED"
    audioSOLIDUSrtp_enc_aescm128 = "audio/rtp-enc-aescm128"
    audioSOLIDUSrtploopback = "audio/rtploopback"
    audioSOLIDUSrtp_midi = "audio/rtp-midi"
    audioSOLIDUSrtx = "audio/rtx"
    audioSOLIDUSscip = "audio/scip"
    audioSOLIDUSSMV = "audio/SMV"
    audioSOLIDUSSMV0 = "audio/SMV0"
    audioSOLIDUSSMV_QCP = "audio/SMV-QCP"
    audioSOLIDUSsofa = "audio/sofa"
    audioSOLIDUSspeex = "audio/speex"
    audioSOLIDUSsp_midi = "audio/sp-midi"
    audioSOLIDUSt140c = "audio/t140c"
    audioSOLIDUSt38 = "audio/t38"
    audioSOLIDUStelephone_event = "audio/telephone-event"
    audioSOLIDUSTETRA_ACELP = "audio/TETRA_ACELP"
    audioSOLIDUSTETRA_ACELP_BB = "audio/TETRA_ACELP_BB"
    audioSOLIDUStone = "audio/tone"
    audioSOLIDUSTSVCIS = "audio/TSVCIS"
    audioSOLIDUSUEMCLIP = "audio/UEMCLIP"
    audioSOLIDUSulpfec = "audio/ulpfec"
    audioSOLIDUSusac = "audio/usac"
    audioSOLIDUSVDVI = "audio/VDVI"
    audioSOLIDUSVMR_WB = "audio/VMR-WB"
    audioSOLIDUSvndFULL_STOP3gppFULL_STOPiufp = "audio/vnd.3gpp.iufp"
    audioSOLIDUSvndFULL_STOP4SB = "audio/vnd.4SB"
    audioSOLIDUSvndFULL_STOPaudiokoz = "audio/vnd.audiokoz"
    audioSOLIDUSvndFULL_STOPCELP = "audio/vnd.CELP"
    audioSOLIDUSvndFULL_STOPciscoFULL_STOPnse = "audio/vnd.cisco.nse"
    audioSOLIDUSvndFULL_STOPcmlesFULL_STOPradio_events = "audio/vnd.cmles.radio-events"
    audioSOLIDUSvndFULL_STOPcnsFULL_STOPanp1 = "audio/vnd.cns.anp1"
    audioSOLIDUSvndFULL_STOPcnsFULL_STOPinf1 = "audio/vnd.cns.inf1"
    audioSOLIDUSvndFULL_STOPdeceFULL_STOPaudio = "audio/vnd.dece.audio"
    audioSOLIDUSvndFULL_STOPdigital_winds = "audio/vnd.digital-winds"
    audioSOLIDUSvndFULL_STOPdlnaFULL_STOPadts = "audio/vnd.dlna.adts"
    audioSOLIDUSvndFULL_STOPdolbyFULL_STOPheaacFULL_STOP1 = "audio/vnd.dolby.heaac.1"
    audioSOLIDUSvndFULL_STOPdolbyFULL_STOPheaacFULL_STOP2 = "audio/vnd.dolby.heaac.2"
    audioSOLIDUSvndFULL_STOPdolbyFULL_STOPmlp = "audio/vnd.dolby.mlp"
    audioSOLIDUSvndFULL_STOPdolbyFULL_STOPmps = "audio/vnd.dolby.mps"
    audioSOLIDUSvndFULL_STOPdolbyFULL_STOPpl2 = "audio/vnd.dolby.pl2"
    audioSOLIDUSvndFULL_STOPdolbyFULL_STOPpl2x = "audio/vnd.dolby.pl2x"
    audioSOLIDUSvndFULL_STOPdolbyFULL_STOPpl2z = "audio/vnd.dolby.pl2z"
    audioSOLIDUSvndFULL_STOPdolbyFULL_STOPpulseFULL_STOP1 = "audio/vnd.dolby.pulse.1"
    audioSOLIDUSvndFULL_STOPdra = "audio/vnd.dra"
    audioSOLIDUSvndFULL_STOPdts = "audio/vnd.dts"
    audioSOLIDUSvndFULL_STOPdtsFULL_STOPhd = "audio/vnd.dts.hd"
    audioSOLIDUSvndFULL_STOPdtsFULL_STOPuhd = "audio/vnd.dts.uhd"
    audioSOLIDUSvndFULL_STOPdvbFULL_STOPfile = "audio/vnd.dvb.file"
    audioSOLIDUSvndFULL_STOPeveradFULL_STOPplj = "audio/vnd.everad.plj"
    audioSOLIDUSvndFULL_STOPhnsFULL_STOPaudio = "audio/vnd.hns.audio"
    audioSOLIDUSvndFULL_STOPlucentFULL_STOPvoice = "audio/vnd.lucent.voice"
    audioSOLIDUSvndFULL_STOPms_playreadyFULL_STOPmediaFULL_STOPpya = (
        "audio/vnd.ms-playready.media.pya"
    )
    audioSOLIDUSvndFULL_STOPnokiaFULL_STOPmobile_xmf = "audio/vnd.nokia.mobile-xmf"
    audioSOLIDUSvndFULL_STOPnortelFULL_STOPvbk = "audio/vnd.nortel.vbk"
    audioSOLIDUSvndFULL_STOPnueraFULL_STOPecelp4800 = "audio/vnd.nuera.ecelp4800"
    audioSOLIDUSvndFULL_STOPnueraFULL_STOPecelp7470 = "audio/vnd.nuera.ecelp7470"
    audioSOLIDUSvndFULL_STOPnueraFULL_STOPecelp9600 = "audio/vnd.nuera.ecelp9600"
    audioSOLIDUSvndFULL_STOPoctelFULL_STOPsbc = "audio/vnd.octel.sbc"
    audioSOLIDUSvndFULL_STOPpresonusFULL_STOPmultitrack = (
        "audio/vnd.presonus.multitrack"
    )
    audioSOLIDUSvndFULL_STOPqcelp = "audio/vnd.qcelp"
    audioSOLIDUSvndFULL_STOPrhetorexFULL_STOP32kadpcm = "audio/vnd.rhetorex.32kadpcm"
    audioSOLIDUSvndFULL_STOPrip = "audio/vnd.rip"
    audioSOLIDUSvndFULL_STOPsealedmediaFULL_STOPsoftsealFULL_STOPmpeg = (
        "audio/vnd.sealedmedia.softseal.mpeg"
    )
    audioSOLIDUSvndFULL_STOPvmxFULL_STOPcvsd = "audio/vnd.vmx.cvsd"
    audioSOLIDUSvorbis = "audio/vorbis"
    audioSOLIDUSvorbis_config = "audio/vorbis-config"
    fontSOLIDUScollection = "font/collection"
    fontSOLIDUSotf = "font/otf"
    fontSOLIDUSsfnt = "font/sfnt"
    fontSOLIDUSttf = "font/ttf"
    fontSOLIDUSwoff = "font/woff"
    fontSOLIDUSwoff2 = "font/woff2"
    hapticsSOLIDUShjif = "haptics/hjif"
    hapticsSOLIDUShmpg = "haptics/hmpg"
    hapticsSOLIDUSivs = "haptics/ivs"
    imageSOLIDUSaces = "image/aces"
    imageSOLIDUSapng = "image/apng"
    imageSOLIDUSavci = "image/avci"
    imageSOLIDUSavcs = "image/avcs"
    imageSOLIDUSavif = "image/avif"
    imageSOLIDUSbmp = "image/bmp"
    imageSOLIDUScgm = "image/cgm"
    imageSOLIDUSdicom_rle = "image/dicom-rle"
    imageSOLIDUSdpx = "image/dpx"
    imageSOLIDUSemf = "image/emf"
    imageSOLIDUSexample = "image/example"
    imageSOLIDUSfits = "image/fits"
    imageSOLIDUSg3fax = "image/g3fax"
    imageSOLIDUSgif = "image/gif"
    imageSOLIDUSheic = "image/heic"
    imageSOLIDUSheic_sequence = "image/heic-sequence"
    imageSOLIDUSheif = "image/heif"
    imageSOLIDUSheif_sequence = "image/heif-sequence"
    imageSOLIDUShej2k = "image/hej2k"
    imageSOLIDUShsj2 = "image/hsj2"
    imageSOLIDUSief = "image/ief"
    imageSOLIDUSj2c = "image/j2c"
    imageSOLIDUSjaii = "image/jaii"
    imageSOLIDUSjais = "image/jais"
    imageSOLIDUSjls = "image/jls"
    imageSOLIDUSjp2 = "image/jp2"
    imageSOLIDUSjpeg = "image/jpeg"
    imageSOLIDUSjph = "image/jph"
    imageSOLIDUSjphc = "image/jphc"
    imageSOLIDUSjpm = "image/jpm"
    imageSOLIDUSjpx = "image/jpx"
    imageSOLIDUSjxl = "image/jxl"
    imageSOLIDUSjxr = "image/jxr"
    imageSOLIDUSjxrA = "image/jxrA"
    imageSOLIDUSjxrS = "image/jxrS"
    imageSOLIDUSjxs = "image/jxs"
    imageSOLIDUSjxsc = "image/jxsc"
    imageSOLIDUSjxsi = "image/jxsi"
    imageSOLIDUSjxss = "image/jxss"
    imageSOLIDUSktx = "image/ktx"
    imageSOLIDUSktx2 = "image/ktx2"
    imageSOLIDUSnaplps = "image/naplps"
    imageSOLIDUSpng = "image/png"
    imageSOLIDUSprsFULL_STOPbtif = "image/prs.btif"
    imageSOLIDUSprsFULL_STOPpti = "image/prs.pti"
    imageSOLIDUSpwg_raster = "image/pwg-raster"
    imageSOLIDUSsvgPLUS_SIGNxml = "image/svg+xml"
    imageSOLIDUSt38 = "image/t38"
    imageSOLIDUStiff = "image/tiff"
    imageSOLIDUStiff_fx = "image/tiff-fx"
    imageSOLIDUSvndFULL_STOPadobeFULL_STOPphotoshop = "image/vnd.adobe.photoshop"
    imageSOLIDUSvndFULL_STOPairzipFULL_STOPacceleratorFULL_STOPazv = (
        "image/vnd.airzip.accelerator.azv"
    )
    imageSOLIDUSvndFULL_STOPcnsFULL_STOPinf2 = "image/vnd.cns.inf2"
    imageSOLIDUSvndFULL_STOPdeceFULL_STOPgraphic = "image/vnd.dece.graphic"
    imageSOLIDUSvndFULL_STOPdjvu = "image/vnd.djvu"
    imageSOLIDUSvndFULL_STOPdvbFULL_STOPsubtitle = "image/vnd.dvb.subtitle"
    imageSOLIDUSvndFULL_STOPdwg = "image/vnd.dwg"
    imageSOLIDUSvndFULL_STOPdxf = "image/vnd.dxf"
    imageSOLIDUSvndFULL_STOPfastbidsheet = "image/vnd.fastbidsheet"
    imageSOLIDUSvndFULL_STOPfpx = "image/vnd.fpx"
    imageSOLIDUSvndFULL_STOPfst = "image/vnd.fst"
    imageSOLIDUSvndFULL_STOPfujixeroxFULL_STOPedmics_mmr = (
        "image/vnd.fujixerox.edmics-mmr"
    )
    imageSOLIDUSvndFULL_STOPfujixeroxFULL_STOPedmics_rlc = (
        "image/vnd.fujixerox.edmics-rlc"
    )
    imageSOLIDUSvndFULL_STOPglobalgraphicsFULL_STOPpgb = "image/vnd.globalgraphics.pgb"
    imageSOLIDUSvndFULL_STOPmicrosoftFULL_STOPicon = "image/vnd.microsoft.icon"
    imageSOLIDUSvndFULL_STOPmix = "image/vnd.mix"
    imageSOLIDUSvndFULL_STOPmozillaFULL_STOPapng = "image/vnd.mozilla.apng"
    imageSOLIDUSvndFULL_STOPms_modi = "image/vnd.ms-modi"
    imageSOLIDUSvndFULL_STOPnet_fpx = "image/vnd.net-fpx"
    imageSOLIDUSvndFULL_STOPpcoFULL_STOPb16 = "image/vnd.pco.b16"
    imageSOLIDUSvndFULL_STOPradiance = "image/vnd.radiance"
    imageSOLIDUSvndFULL_STOPsealedFULL_STOPpng = "image/vnd.sealed.png"
    imageSOLIDUSvndFULL_STOPsealedmediaFULL_STOPsoftsealFULL_STOPgif = (
        "image/vnd.sealedmedia.softseal.gif"
    )
    imageSOLIDUSvndFULL_STOPsealedmediaFULL_STOPsoftsealFULL_STOPjpg = (
        "image/vnd.sealedmedia.softseal.jpg"
    )
    imageSOLIDUSvndFULL_STOPsvf = "image/vnd.svf"
    imageSOLIDUSvndFULL_STOPtencentFULL_STOPtap = "image/vnd.tencent.tap"
    imageSOLIDUSvndFULL_STOPvalveFULL_STOPsourceFULL_STOPtexture = (
        "image/vnd.valve.source.texture"
    )
    imageSOLIDUSvndFULL_STOPwapFULL_STOPwbmp = "image/vnd.wap.wbmp"
    imageSOLIDUSvndFULL_STOPxiff = "image/vnd.xiff"
    imageSOLIDUSvndFULL_STOPzbrushFULL_STOPpcx = "image/vnd.zbrush.pcx"
    imageSOLIDUSwebp = "image/webp"
    imageSOLIDUSwmf = "image/wmf"
    imageSOLIDUSx_emf = "image/x-emf"
    imageSOLIDUSx_wmf = "image/x-wmf"
    messageSOLIDUSbhttp = "message/bhttp"
    messageSOLIDUSCPIM = "message/CPIM"
    messageSOLIDUSdelivery_status = "message/delivery-status"
    messageSOLIDUSdisposition_notification = "message/disposition-notification"
    messageSOLIDUSexample = "message/example"
    messageSOLIDUSexternal_body = "message/external-body"
    messageSOLIDUSfeedback_report = "message/feedback-report"
    messageSOLIDUSglobal = "message/global"
    messageSOLIDUSglobal_delivery_status = "message/global-delivery-status"
    messageSOLIDUSglobal_disposition_notification = (
        "message/global-disposition-notification"
    )
    messageSOLIDUSglobal_headers = "message/global-headers"
    messageSOLIDUShttp = "message/http"
    messageSOLIDUSimdnPLUS_SIGNxml = "message/imdn+xml"
    messageSOLIDUSmls = "message/mls"
    messageSOLIDUSnews = "message/news"
    messageSOLIDUSohttp_req = "message/ohttp-req"
    messageSOLIDUSohttp_res = "message/ohttp-res"
    messageSOLIDUSpartial = "message/partial"
    messageSOLIDUSrfc822 = "message/rfc822"
    messageSOLIDUSs_http = "message/s-http"
    messageSOLIDUSsip = "message/sip"
    messageSOLIDUSsipfrag = "message/sipfrag"
    messageSOLIDUStracking_status = "message/tracking-status"
    messageSOLIDUSvndFULL_STOPsiFULL_STOPsimp = "message/vnd.si.simp"
    messageSOLIDUSvndFULL_STOPwfaFULL_STOPwsc = "message/vnd.wfa.wsc"
    modelSOLIDUS3mf = "model/3mf"
    modelSOLIDUSe57 = "model/e57"
    modelSOLIDUSexample = "model/example"
    modelSOLIDUSgltfPLUS_SIGNjson = "model/gltf+json"
    modelSOLIDUSgltf_binary = "model/gltf-binary"
    modelSOLIDUSiges = "model/iges"
    modelSOLIDUSJT = "model/JT"
    modelSOLIDUSmesh = "model/mesh"
    modelSOLIDUSmtl = "model/mtl"
    modelSOLIDUSobj = "model/obj"
    modelSOLIDUSprc = "model/prc"
    modelSOLIDUSstep = "model/step"
    modelSOLIDUSstepPLUS_SIGNxml = "model/step+xml"
    modelSOLIDUSstepPLUS_SIGNzip = "model/step+zip"
    modelSOLIDUSstep_xmlPLUS_SIGNzip = "model/step-xml+zip"
    modelSOLIDUSstl = "model/stl"
    modelSOLIDUSu3d = "model/u3d"
    modelSOLIDUSvndFULL_STOPbary = "model/vnd.bary"
    modelSOLIDUSvndFULL_STOPcld = "model/vnd.cld"
    modelSOLIDUSvndFULL_STOPcolladaPLUS_SIGNxml = "model/vnd.collada+xml"
    modelSOLIDUSvndFULL_STOPdwf = "model/vnd.dwf"
    modelSOLIDUSvndFULL_STOPflatlandFULL_STOP3dml = "model/vnd.flatland.3dml"
    modelSOLIDUSvndFULL_STOPgdl = "model/vnd.gdl"
    modelSOLIDUSvndFULL_STOPgs_gdl = "model/vnd.gs-gdl"
    modelSOLIDUSvndFULL_STOPgtw = "model/vnd.gtw"
    modelSOLIDUSvndFULL_STOPmomlPLUS_SIGNxml = "model/vnd.moml+xml"
    modelSOLIDUSvndFULL_STOPmts = "model/vnd.mts"
    modelSOLIDUSvndFULL_STOPopengex = "model/vnd.opengex"
    modelSOLIDUSvndFULL_STOPparasolidFULL_STOPtransmitFULL_STOPbinary = (
        "model/vnd.parasolid.transmit.binary"
    )
    modelSOLIDUSvndFULL_STOPparasolidFULL_STOPtransmitFULL_STOPtext = (
        "model/vnd.parasolid.transmit.text"
    )
    modelSOLIDUSvndFULL_STOPpythaFULL_STOPpyox = "model/vnd.pytha.pyox"
    modelSOLIDUSvndFULL_STOProsetteFULL_STOPannotated_data_model = (
        "model/vnd.rosette.annotated-data-model"
    )
    modelSOLIDUSvndFULL_STOPsapFULL_STOPvds = "model/vnd.sap.vds"
    modelSOLIDUSvndFULL_STOPusda = "model/vnd.usda"
    modelSOLIDUSvndFULL_STOPusdzPLUS_SIGNzip = "model/vnd.usdz+zip"
    modelSOLIDUSvndFULL_STOPvalveFULL_STOPsourceFULL_STOPcompiled_map = (
        "model/vnd.valve.source.compiled-map"
    )
    modelSOLIDUSvndFULL_STOPvtu = "model/vnd.vtu"
    modelSOLIDUSvrml = "model/vrml"
    modelSOLIDUSx3dPLUS_SIGNfastinfoset = "model/x3d+fastinfoset"
    modelSOLIDUSx3dPLUS_SIGNxml = "model/x3d+xml"
    modelSOLIDUSx3d_vrml = "model/x3d-vrml"
    multipartSOLIDUSalternative = "multipart/alternative"
    multipartSOLIDUSappledouble = "multipart/appledouble"
    multipartSOLIDUSbyteranges = "multipart/byteranges"
    multipartSOLIDUSdigest = "multipart/digest"
    multipartSOLIDUSencrypted = "multipart/encrypted"
    multipartSOLIDUSexample = "multipart/example"
    multipartSOLIDUSform_data = "multipart/form-data"
    multipartSOLIDUSheader_set = "multipart/header-set"
    multipartSOLIDUSmixed = "multipart/mixed"
    multipartSOLIDUSmultilingual = "multipart/multilingual"
    multipartSOLIDUSparallel = "multipart/parallel"
    multipartSOLIDUSrelated = "multipart/related"
    multipartSOLIDUSreport = "multipart/report"
    multipartSOLIDUSsigned = "multipart/signed"
    multipartSOLIDUSvndFULL_STOPbintFULL_STOPmed_plus = "multipart/vnd.bint.med-plus"
    multipartSOLIDUSvoice_message = "multipart/voice-message"
    multipartSOLIDUSx_mixed_replace = "multipart/x-mixed-replace"
    textSOLIDUS1d_interleaved_parityfec = "text/1d-interleaved-parityfec"
    textSOLIDUScache_manifest = "text/cache-manifest"
    textSOLIDUScalendar = "text/calendar"
    textSOLIDUScql = "text/cql"
    textSOLIDUScql_expression = "text/cql-expression"
    textSOLIDUScql_identifier = "text/cql-identifier"
    textSOLIDUScss = "text/css"
    textSOLIDUScsv = "text/csv"
    textSOLIDUScsv_schema = "text/csv-schema"
    textSOLIDUSdirectory = "text/directory"
    textSOLIDUSdns = "text/dns"
    textSOLIDUSecmascript = "text/ecmascript"
    textSOLIDUSencaprtp = "text/encaprtp"
    textSOLIDUSenriched = "text/enriched"
    textSOLIDUSexample = "text/example"
    textSOLIDUSfhirpath = "text/fhirpath"
    textSOLIDUSflexfec = "text/flexfec"
    textSOLIDUSfwdred = "text/fwdred"
    textSOLIDUSgff3 = "text/gff3"
    textSOLIDUSgrammar_ref_list = "text/grammar-ref-list"
    textSOLIDUShl7v2 = "text/hl7v2"
    textSOLIDUShtml = "text/html"
    textSOLIDUSjavascript = "text/javascript"
    textSOLIDUSjcr_cnd = "text/jcr-cnd"
    textSOLIDUSmarkdown = "text/markdown"
    textSOLIDUSmizar = "text/mizar"
    textSOLIDUSn3 = "text/n3"
    textSOLIDUSparameters = "text/parameters"
    textSOLIDUSparityfec = "text/parityfec"
    textSOLIDUSplain = "text/plain"
    textSOLIDUSprovenance_notation = "text/provenance-notation"
    textSOLIDUSprsFULL_STOPfallensteinFULL_STOPrst = "text/prs.fallenstein.rst"
    textSOLIDUSprsFULL_STOPlinesFULL_STOPtag = "text/prs.lines.tag"
    textSOLIDUSprsFULL_STOPpropFULL_STOPlogic = "text/prs.prop.logic"
    textSOLIDUSprsFULL_STOPtexi = "text/prs.texi"
    textSOLIDUSraptorfec = "text/raptorfec"
    textSOLIDUSRED = "text/RED"
    textSOLIDUSrfc822_headers = "text/rfc822-headers"
    textSOLIDUSrichtext = "text/richtext"
    textSOLIDUSrtf = "text/rtf"
    textSOLIDUSrtp_enc_aescm128 = "text/rtp-enc-aescm128"
    textSOLIDUSrtploopback = "text/rtploopback"
    textSOLIDUSrtx = "text/rtx"
    textSOLIDUSSGML = "text/SGML"
    textSOLIDUSshaclc = "text/shaclc"
    textSOLIDUSshex = "text/shex"
    textSOLIDUSspdx = "text/spdx"
    textSOLIDUSstrings = "text/strings"
    textSOLIDUSt140 = "text/t140"
    textSOLIDUStab_separated_values = "text/tab-separated-values"
    textSOLIDUStroff = "text/troff"
    textSOLIDUSturtle = "text/turtle"
    textSOLIDUSulpfec = "text/ulpfec"
    textSOLIDUSuri_list = "text/uri-list"
    textSOLIDUSvcard = "text/vcard"
    textSOLIDUSvndFULL_STOPa = "text/vnd.a"
    textSOLIDUSvndFULL_STOPabc = "text/vnd.abc"
    textSOLIDUSvndFULL_STOPascii_art = "text/vnd.ascii-art"
    textSOLIDUSvndFULL_STOPcurl = "text/vnd.curl"
    textSOLIDUSvndFULL_STOPdebianFULL_STOPcopyright = "text/vnd.debian.copyright"
    textSOLIDUSvndFULL_STOPDMClientScript = "text/vnd.DMClientScript"
    textSOLIDUSvndFULL_STOPdvbFULL_STOPsubtitle = "text/vnd.dvb.subtitle"
    textSOLIDUSvndFULL_STOPesmertecFULL_STOPtheme_descriptor = (
        "text/vnd.esmertec.theme-descriptor"
    )
    textSOLIDUSvndFULL_STOPexchangeable = "text/vnd.exchangeable"
    textSOLIDUSvndFULL_STOPfamilysearchFULL_STOPgedcom = "text/vnd.familysearch.gedcom"
    textSOLIDUSvndFULL_STOPficlabFULL_STOPflt = "text/vnd.ficlab.flt"
    textSOLIDUSvndFULL_STOPfly = "text/vnd.fly"
    textSOLIDUSvndFULL_STOPfmiFULL_STOPflexstor = "text/vnd.fmi.flexstor"
    textSOLIDUSvndFULL_STOPgml = "text/vnd.gml"
    textSOLIDUSvndFULL_STOPgraphviz = "text/vnd.graphviz"
    textSOLIDUSvndFULL_STOPhans = "text/vnd.hans"
    textSOLIDUSvndFULL_STOPhgl = "text/vnd.hgl"
    textSOLIDUSvndFULL_STOPin3dFULL_STOP3dml = "text/vnd.in3d.3dml"
    textSOLIDUSvndFULL_STOPin3dFULL_STOPspot = "text/vnd.in3d.spot"
    textSOLIDUSvndFULL_STOPIPTCFULL_STOPNewsML = "text/vnd.IPTC.NewsML"
    textSOLIDUSvndFULL_STOPIPTCFULL_STOPNITF = "text/vnd.IPTC.NITF"
    textSOLIDUSvndFULL_STOPlatex_z = "text/vnd.latex-z"
    textSOLIDUSvndFULL_STOPmotorolaFULL_STOPreflex = "text/vnd.motorola.reflex"
    textSOLIDUSvndFULL_STOPms_mediapackage = "text/vnd.ms-mediapackage"
    textSOLIDUSvndFULL_STOPnet2phoneFULL_STOPcommcenterFULL_STOPcommand = (
        "text/vnd.net2phone.commcenter.command"
    )
    textSOLIDUSvndFULL_STOPradisysFULL_STOPmsml_basic_layout = (
        "text/vnd.radisys.msml-basic-layout"
    )
    textSOLIDUSvndFULL_STOPsenxFULL_STOPwarpscript = "text/vnd.senx.warpscript"
    textSOLIDUSvndFULL_STOPsiFULL_STOPuricatalogue = "text/vnd.si.uricatalogue"
    textSOLIDUSvndFULL_STOPsosi = "text/vnd.sosi"
    textSOLIDUSvndFULL_STOPsunFULL_STOPj2meFULL_STOPapp_descriptor = (
        "text/vnd.sun.j2me.app-descriptor"
    )
    textSOLIDUSvndFULL_STOPtrolltechFULL_STOPlinguist = "text/vnd.trolltech.linguist"
    textSOLIDUSvndFULL_STOPvcf = "text/vnd.vcf"
    textSOLIDUSvndFULL_STOPwapFULL_STOPsi = "text/vnd.wap.si"
    textSOLIDUSvndFULL_STOPwapFULL_STOPsl = "text/vnd.wap.sl"
    textSOLIDUSvndFULL_STOPwapFULL_STOPwml = "text/vnd.wap.wml"
    textSOLIDUSvndFULL_STOPwapFULL_STOPwmlscript = "text/vnd.wap.wmlscript"
    textSOLIDUSvndFULL_STOPzooFULL_STOPkcl = "text/vnd.zoo.kcl"
    textSOLIDUSvtt = "text/vtt"
    textSOLIDUSwgsl = "text/wgsl"
    textSOLIDUSxml = "text/xml"
    textSOLIDUSxml_external_parsed_entity = "text/xml-external-parsed-entity"
    videoSOLIDUS1d_interleaved_parityfec = "video/1d-interleaved-parityfec"
    videoSOLIDUS3gpp = "video/3gpp"
    videoSOLIDUS3gpp2 = "video/3gpp2"
    videoSOLIDUS3gpp_tt = "video/3gpp-tt"
    videoSOLIDUSAV1 = "video/AV1"
    videoSOLIDUSBMPEG = "video/BMPEG"
    videoSOLIDUSBT656 = "video/BT656"
    videoSOLIDUSCelB = "video/CelB"
    videoSOLIDUSDV = "video/DV"
    videoSOLIDUSencaprtp = "video/encaprtp"
    videoSOLIDUSevc = "video/evc"
    videoSOLIDUSexample = "video/example"
    videoSOLIDUSFFV1 = "video/FFV1"
    videoSOLIDUSflexfec = "video/flexfec"
    videoSOLIDUSH261 = "video/H261"
    videoSOLIDUSH263 = "video/H263"
    videoSOLIDUSH263_1998 = "video/H263-1998"
    videoSOLIDUSH263_2000 = "video/H263-2000"
    videoSOLIDUSH264 = "video/H264"
    videoSOLIDUSH264_RCDO = "video/H264-RCDO"
    videoSOLIDUSH264_SVC = "video/H264-SVC"
    videoSOLIDUSH265 = "video/H265"
    videoSOLIDUSH266 = "video/H266"
    videoSOLIDUSisoFULL_STOPsegment = "video/iso.segment"
    videoSOLIDUSJPEG = "video/JPEG"
    videoSOLIDUSjpeg2000 = "video/jpeg2000"
    videoSOLIDUSjxsv = "video/jxsv"
    videoSOLIDUSmatroska = "video/matroska"
    videoSOLIDUSmatroska_3d = "video/matroska-3d"
    videoSOLIDUSmj2 = "video/mj2"
    videoSOLIDUSMP1S = "video/MP1S"
    videoSOLIDUSMP2P = "video/MP2P"
    videoSOLIDUSMP2T = "video/MP2T"
    videoSOLIDUSmp4 = "video/mp4"
    videoSOLIDUSMP4V_ES = "video/MP4V-ES"
    videoSOLIDUSmpeg = "video/mpeg"
    videoSOLIDUSmpeg4_generic = "video/mpeg4-generic"
    videoSOLIDUSMPV = "video/MPV"
    videoSOLIDUSnv = "video/nv"
    videoSOLIDUSogg = "video/ogg"
    videoSOLIDUSparityfec = "video/parityfec"
    videoSOLIDUSpointer = "video/pointer"
    videoSOLIDUSquicktime = "video/quicktime"
    videoSOLIDUSraptorfec = "video/raptorfec"
    videoSOLIDUSraw = "video/raw"
    videoSOLIDUSrtp_enc_aescm128 = "video/rtp-enc-aescm128"
    videoSOLIDUSrtploopback = "video/rtploopback"
    videoSOLIDUSrtx = "video/rtx"
    videoSOLIDUSscip = "video/scip"
    videoSOLIDUSsmpte291 = "video/smpte291"
    videoSOLIDUSSMPTE292M = "video/SMPTE292M"
    videoSOLIDUSulpfec = "video/ulpfec"
    videoSOLIDUSvc1 = "video/vc1"
    videoSOLIDUSvc2 = "video/vc2"
    videoSOLIDUSvndFULL_STOPCCTV = "video/vnd.CCTV"
    videoSOLIDUSvndFULL_STOPdeceFULL_STOPhd = "video/vnd.dece.hd"
    videoSOLIDUSvndFULL_STOPdeceFULL_STOPmobile = "video/vnd.dece.mobile"
    videoSOLIDUSvndFULL_STOPdeceFULL_STOPmp4 = "video/vnd.dece.mp4"
    videoSOLIDUSvndFULL_STOPdeceFULL_STOPpd = "video/vnd.dece.pd"
    videoSOLIDUSvndFULL_STOPdeceFULL_STOPsd = "video/vnd.dece.sd"
    videoSOLIDUSvndFULL_STOPdeceFULL_STOPvideo = "video/vnd.dece.video"
    videoSOLIDUSvndFULL_STOPdirectvFULL_STOPmpeg = "video/vnd.directv.mpeg"
    videoSOLIDUSvndFULL_STOPdirectvFULL_STOPmpeg_tts = "video/vnd.directv.mpeg-tts"
    videoSOLIDUSvndFULL_STOPdlnaFULL_STOPmpeg_tts = "video/vnd.dlna.mpeg-tts"
    videoSOLIDUSvndFULL_STOPdvbFULL_STOPfile = "video/vnd.dvb.file"
    videoSOLIDUSvndFULL_STOPfvt = "video/vnd.fvt"
    videoSOLIDUSvndFULL_STOPhnsFULL_STOPvideo = "video/vnd.hns.video"
    videoSOLIDUSvndFULL_STOPiptvforumFULL_STOP1dparityfec_1010 = (
        "video/vnd.iptvforum.1dparityfec-1010"
    )
    videoSOLIDUSvndFULL_STOPiptvforumFULL_STOP1dparityfec_2005 = (
        "video/vnd.iptvforum.1dparityfec-2005"
    )
    videoSOLIDUSvndFULL_STOPiptvforumFULL_STOP2dparityfec_1010 = (
        "video/vnd.iptvforum.2dparityfec-1010"
    )
    videoSOLIDUSvndFULL_STOPiptvforumFULL_STOP2dparityfec_2005 = (
        "video/vnd.iptvforum.2dparityfec-2005"
    )
    videoSOLIDUSvndFULL_STOPiptvforumFULL_STOPttsavc = "video/vnd.iptvforum.ttsavc"
    videoSOLIDUSvndFULL_STOPiptvforumFULL_STOPttsmpeg2 = "video/vnd.iptvforum.ttsmpeg2"
    videoSOLIDUSvndFULL_STOPmotorolaFULL_STOPvideo = "video/vnd.motorola.video"
    videoSOLIDUSvndFULL_STOPmotorolaFULL_STOPvideop = "video/vnd.motorola.videop"
    videoSOLIDUSvndFULL_STOPmpegurl = "video/vnd.mpegurl"
    videoSOLIDUSvndFULL_STOPms_playreadyFULL_STOPmediaFULL_STOPpyv = (
        "video/vnd.ms-playready.media.pyv"
    )
    videoSOLIDUSvndFULL_STOPnokiaFULL_STOPinterleaved_multimedia = (
        "video/vnd.nokia.interleaved-multimedia"
    )
    videoSOLIDUSvndFULL_STOPnokiaFULL_STOPmp4vr = "video/vnd.nokia.mp4vr"
    videoSOLIDUSvndFULL_STOPnokiaFULL_STOPvideovoip = "video/vnd.nokia.videovoip"
    videoSOLIDUSvndFULL_STOPobjectvideo = "video/vnd.objectvideo"
    videoSOLIDUSvndFULL_STOPradgamettoolsFULL_STOPbink = "video/vnd.radgamettools.bink"
    videoSOLIDUSvndFULL_STOPradgamettoolsFULL_STOPsmacker = (
        "video/vnd.radgamettools.smacker"
    )
    videoSOLIDUSvndFULL_STOPsealedFULL_STOPmpeg1 = "video/vnd.sealed.mpeg1"
    videoSOLIDUSvndFULL_STOPsealedFULL_STOPmpeg4 = "video/vnd.sealed.mpeg4"
    videoSOLIDUSvndFULL_STOPsealedFULL_STOPswf = "video/vnd.sealed.swf"
    videoSOLIDUSvndFULL_STOPsealedmediaFULL_STOPsoftsealFULL_STOPmov = (
        "video/vnd.sealedmedia.softseal.mov"
    )
    videoSOLIDUSvndFULL_STOPuvvuFULL_STOPmp4 = "video/vnd.uvvu.mp4"
    videoSOLIDUSvndFULL_STOPvivo = "video/vnd.vivo"
    videoSOLIDUSvndFULL_STOPyoutubeFULL_STOPyt = "video/vnd.youtube.yt"
    videoSOLIDUSVP8 = "video/VP8"
    videoSOLIDUSVP9 = "video/VP9"


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
    # The resource has a version.
    HAS_VERSION = "HAS_VERSION"
    # The resource is a version of another resource. This is useful to refer to an abstract resource that has different versions, for example, "Python 3.12 is a version of Python".
    IS_VERSION_OF = "IS_VERSION_OF"
    # The resource is a new version of another resource.
    IS_NEW_VERSION_OF = "IS_NEW_VERSION_OF"
    # The resource is a previous version of another resource.
    IS_PREVIOUS_VERSION_OF = "IS_PREVIOUS_VERSION_OF"
    # The resource is part of another resource.
    IS_PART_OF = "IS_PART_OF"
    # The resource has part another resource.
    HAS_PART = "HAS_PART"
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
    # The resource is obsoleted by another resource.
    IS_OBSOLETED_BY = "IS_OBSOLETED_BY"
    # The resource obsoletes another resource.
    OBSOLETES = "OBSOLETES"


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
        {"from_schema": "https://w3id.org/nfdi4cat/pid4cat-model"}
    )

    responseCode: Optional[int] = Field(
        None,
        description="""The response code of the handle API.""",
        json_schema_extra={
            "linkml_meta": {"alias": "responseCode", "domain_of": ["HandleAPIRecord"]}
        },
    )
    handle: str = Field(
        ...,
        description="""The handle of the pid4cat record.""",
        json_schema_extra={
            "linkml_meta": {"alias": "handle", "domain_of": ["HandleAPIRecord"]}
        },
    )
    values: Optional[
        List[
            Union[
                HandleRecord,
                URL,
                STATUS,
                SCHEMAVER,
                LICENSE,
                EMAIL,
                RESOURCEINFO,
                RELATED,
                LOG,
            ]
        ]
    ] = Field(
        None,
        description="""The values of the pid4cat record.""",
        json_schema_extra={
            "linkml_meta": {"alias": "values", "domain_of": ["HandleAPIRecord"]}
        },
    )


class HandleRecord(ConfiguredBaseModel):
    """
    A class representing a handle record in the same way as in the REST (json) API of a handle server.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://w3id.org/nfdi4cat/pid4cat-model",
            "slot_usage": {
                "type": {
                    "description": "The type of handledata stored in the "
                    "handle record.",
                    "designates_type": True,
                    "name": "type",
                }
            },
        }
    )

    ttl: Optional[int] = Field(
        None,
        description="""A time to live in seconds for the handle record. Typically: 86400 => 1 day
TODO: Research details of ttl meaning for handle API.
""",
        json_schema_extra={
            "linkml_meta": {"alias": "ttl", "domain_of": ["HandleRecord"]}
        },
    )
    timestamp: Optional[datetime] = Field(
        None,
        description="""The iso datetime for the last update of the handle data.""",
        json_schema_extra={
            "linkml_meta": {"alias": "timestamp", "domain_of": ["HandleRecord"]}
        },
    )
    type: Literal["HandleRecord"] = Field(
        "HandleRecord",
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
        {"from_schema": "https://w3id.org/nfdi4cat/pid4cat-model"}
    )

    index: Optional[int] = Field(
        None,
        ge=1,
        le=1,
        json_schema_extra={
            "linkml_meta": {
                "alias": "index",
                "domain_of": [
                    "URL",
                    "STATUS",
                    "SCHEMA_VER",
                    "LICENSE",
                    "EMAIL",
                    "RESOURCE_INFO",
                    "RELATED",
                    "LOG",
                ],
            }
        },
    )
    data: Optional[HdlDataUrl] = Field(
        None,
        json_schema_extra={
            "linkml_meta": {
                "alias": "data",
                "domain_of": [
                    "URL",
                    "STATUS",
                    "SCHEMA_VER",
                    "LICENSE",
                    "EMAIL",
                    "RESOURCE_INFO",
                    "RELATED",
                    "LOG",
                ],
            }
        },
    )
    ttl: Optional[int] = Field(
        None,
        description="""A time to live in seconds for the handle record. Typically: 86400 => 1 day
TODO: Research details of ttl meaning for handle API.
""",
        json_schema_extra={
            "linkml_meta": {"alias": "ttl", "domain_of": ["HandleRecord"]}
        },
    )
    timestamp: Optional[datetime] = Field(
        None,
        description="""The iso datetime for the last update of the handle data.""",
        json_schema_extra={
            "linkml_meta": {"alias": "timestamp", "domain_of": ["HandleRecord"]}
        },
    )
    type: Literal["URL"] = Field(
        "URL",
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
    The data element in the handle API for the redirect url.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://w3id.org/nfdi4cat/pid4cat-model",
            "slot_usage": {
                "format": {"equals_string": "string", "name": "format"},
                "value": {"name": "value", "pattern": "^https?:\\/\\/.*$"},
            },
        }
    )

    format: Optional[Literal["string"]] = Field(
        None,
        description="""The format of the handle data.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "format",
                "domain_of": [
                    "HdlDataUrl",
                    "HdlDataStatus",
                    "HdlDataSchemaVer",
                    "HdlDataLicense",
                    "HdlDataContact",
                    "HdlDataResourceInfo",
                    "HdlDataRelated",
                    "HdlDataLog",
                ],
                "equals_string": "string",
            }
        },
    )
    value: Optional[str] = Field(
        None,
        description="""The value of the handle data.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "value",
                "domain_of": [
                    "HdlDataUrl",
                    "HdlDataStatus",
                    "HdlDataSchemaVer",
                    "HdlDataLicense",
                    "HdlDataContact",
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


class STATUS(HandleRecord):
    """
    A data element in the handle API.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://w3id.org/nfdi4cat/pid4cat-model"}
    )

    index: Optional[int] = Field(
        None,
        ge=2,
        le=2,
        json_schema_extra={
            "linkml_meta": {
                "alias": "index",
                "domain_of": [
                    "URL",
                    "STATUS",
                    "SCHEMA_VER",
                    "LICENSE",
                    "EMAIL",
                    "RESOURCE_INFO",
                    "RELATED",
                    "LOG",
                ],
            }
        },
    )
    data: Optional[HdlDataStatus] = Field(
        None,
        json_schema_extra={
            "linkml_meta": {
                "alias": "data",
                "domain_of": [
                    "URL",
                    "STATUS",
                    "SCHEMA_VER",
                    "LICENSE",
                    "EMAIL",
                    "RESOURCE_INFO",
                    "RELATED",
                    "LOG",
                ],
            }
        },
    )
    ttl: Optional[int] = Field(
        None,
        description="""A time to live in seconds for the handle record. Typically: 86400 => 1 day
TODO: Research details of ttl meaning for handle API.
""",
        json_schema_extra={
            "linkml_meta": {"alias": "ttl", "domain_of": ["HandleRecord"]}
        },
    )
    timestamp: Optional[datetime] = Field(
        None,
        description="""The iso datetime for the last update of the handle data.""",
        json_schema_extra={
            "linkml_meta": {"alias": "timestamp", "domain_of": ["HandleRecord"]}
        },
    )
    type: Literal["STATUS"] = Field(
        "STATUS",
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
    The data element in the handle API for the status.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://w3id.org/nfdi4cat/pid4cat-model",
            "slot_usage": {
                "format": {"equals_string": "string", "name": "format"},
                "value": {"name": "value", "range": "Pid4CatStatus"},
            },
        }
    )

    format: Optional[Literal["string"]] = Field(
        None,
        description="""The format of the handle data.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "format",
                "domain_of": [
                    "HdlDataUrl",
                    "HdlDataStatus",
                    "HdlDataSchemaVer",
                    "HdlDataLicense",
                    "HdlDataContact",
                    "HdlDataResourceInfo",
                    "HdlDataRelated",
                    "HdlDataLog",
                ],
                "equals_string": "string",
            }
        },
    )
    value: Optional[Pid4CatStatus] = Field(
        None,
        description="""The value of the handle data.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "value",
                "domain_of": [
                    "HdlDataUrl",
                    "HdlDataStatus",
                    "HdlDataSchemaVer",
                    "HdlDataLicense",
                    "HdlDataContact",
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
        {"from_schema": "https://w3id.org/nfdi4cat/pid4cat-model"}
    )

    index: Optional[int] = Field(
        None,
        ge=3,
        le=3,
        json_schema_extra={
            "linkml_meta": {
                "alias": "index",
                "domain_of": [
                    "URL",
                    "STATUS",
                    "SCHEMA_VER",
                    "LICENSE",
                    "EMAIL",
                    "RESOURCE_INFO",
                    "RELATED",
                    "LOG",
                ],
            }
        },
    )
    data: Optional[HdlDataSchemaVer] = Field(
        None,
        json_schema_extra={
            "linkml_meta": {
                "alias": "data",
                "domain_of": [
                    "URL",
                    "STATUS",
                    "SCHEMA_VER",
                    "LICENSE",
                    "EMAIL",
                    "RESOURCE_INFO",
                    "RELATED",
                    "LOG",
                ],
            }
        },
    )
    ttl: Optional[int] = Field(
        None,
        description="""A time to live in seconds for the handle record. Typically: 86400 => 1 day
TODO: Research details of ttl meaning for handle API.
""",
        json_schema_extra={
            "linkml_meta": {"alias": "ttl", "domain_of": ["HandleRecord"]}
        },
    )
    timestamp: Optional[datetime] = Field(
        None,
        description="""The iso datetime for the last update of the handle data.""",
        json_schema_extra={
            "linkml_meta": {"alias": "timestamp", "domain_of": ["HandleRecord"]}
        },
    )
    type: Literal["SCHEMA_VER"] = Field(
        "SCHEMA_VER",
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
    The data element in the handle API for the schema version.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://w3id.org/nfdi4cat/pid4cat-model",
            "slot_usage": {
                "format": {"equals_string": "string", "name": "format"},
                "value": {"name": "value", "pattern": "^v\\d+\\.\\d+\\.\\d+$"},
            },
        }
    )

    format: Optional[Literal["string"]] = Field(
        None,
        description="""The format of the handle data.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "format",
                "domain_of": [
                    "HdlDataUrl",
                    "HdlDataStatus",
                    "HdlDataSchemaVer",
                    "HdlDataLicense",
                    "HdlDataContact",
                    "HdlDataResourceInfo",
                    "HdlDataRelated",
                    "HdlDataLog",
                ],
                "equals_string": "string",
            }
        },
    )
    value: Optional[str] = Field(
        None,
        description="""The value of the handle data.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "value",
                "domain_of": [
                    "HdlDataUrl",
                    "HdlDataStatus",
                    "HdlDataSchemaVer",
                    "HdlDataLicense",
                    "HdlDataContact",
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


class LICENSE(HandleRecord):
    """
    The data element in the handle API for the schema version.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://w3id.org/nfdi4cat/pid4cat-model"}
    )

    index: Optional[int] = Field(
        None,
        ge=4,
        le=4,
        json_schema_extra={
            "linkml_meta": {
                "alias": "index",
                "domain_of": [
                    "URL",
                    "STATUS",
                    "SCHEMA_VER",
                    "LICENSE",
                    "EMAIL",
                    "RESOURCE_INFO",
                    "RELATED",
                    "LOG",
                ],
            }
        },
    )
    data: Optional[HdlDataLicense] = Field(
        None,
        json_schema_extra={
            "linkml_meta": {
                "alias": "data",
                "domain_of": [
                    "URL",
                    "STATUS",
                    "SCHEMA_VER",
                    "LICENSE",
                    "EMAIL",
                    "RESOURCE_INFO",
                    "RELATED",
                    "LOG",
                ],
            }
        },
    )
    ttl: Optional[int] = Field(
        None,
        description="""A time to live in seconds for the handle record. Typically: 86400 => 1 day
TODO: Research details of ttl meaning for handle API.
""",
        json_schema_extra={
            "linkml_meta": {"alias": "ttl", "domain_of": ["HandleRecord"]}
        },
    )
    timestamp: Optional[datetime] = Field(
        None,
        description="""The iso datetime for the last update of the handle data.""",
        json_schema_extra={
            "linkml_meta": {"alias": "timestamp", "domain_of": ["HandleRecord"]}
        },
    )
    type: Literal["LICENSE"] = Field(
        "LICENSE",
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
    The data element in the handle API for the license.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://w3id.org/nfdi4cat/pid4cat-model",
            "slot_usage": {
                "format": {"equals_string": "string", "name": "format"},
                "value": {"equals_string": "CC0-1.0", "name": "value"},
            },
        }
    )

    format: Optional[Literal["string"]] = Field(
        None,
        description="""The format of the handle data.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "format",
                "domain_of": [
                    "HdlDataUrl",
                    "HdlDataStatus",
                    "HdlDataSchemaVer",
                    "HdlDataLicense",
                    "HdlDataContact",
                    "HdlDataResourceInfo",
                    "HdlDataRelated",
                    "HdlDataLog",
                ],
                "equals_string": "string",
            }
        },
    )
    value: Optional[Literal["CC0-1.0"]] = Field(
        None,
        description="""The value of the handle data.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "value",
                "domain_of": [
                    "HdlDataUrl",
                    "HdlDataStatus",
                    "HdlDataSchemaVer",
                    "HdlDataLicense",
                    "HdlDataContact",
                    "HdlDataResourceInfo",
                    "HdlDataRelated",
                    "HdlDataLog",
                ],
                "equals_string": "CC0-1.0",
            }
        },
    )


class EMAIL(HandleRecord):
    """
    The data element in the handle API for the contact email.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://w3id.org/nfdi4cat/pid4cat-model"}
    )

    index: Optional[int] = Field(
        None,
        ge=5,
        le=5,
        json_schema_extra={
            "linkml_meta": {
                "alias": "index",
                "domain_of": [
                    "URL",
                    "STATUS",
                    "SCHEMA_VER",
                    "LICENSE",
                    "EMAIL",
                    "RESOURCE_INFO",
                    "RELATED",
                    "LOG",
                ],
            }
        },
    )
    data: Optional[HdlDataContact] = Field(
        None,
        json_schema_extra={
            "linkml_meta": {
                "alias": "data",
                "domain_of": [
                    "URL",
                    "STATUS",
                    "SCHEMA_VER",
                    "LICENSE",
                    "EMAIL",
                    "RESOURCE_INFO",
                    "RELATED",
                    "LOG",
                ],
            }
        },
    )
    ttl: Optional[int] = Field(
        None,
        description="""A time to live in seconds for the handle record. Typically: 86400 => 1 day
TODO: Research details of ttl meaning for handle API.
""",
        json_schema_extra={
            "linkml_meta": {"alias": "ttl", "domain_of": ["HandleRecord"]}
        },
    )
    timestamp: Optional[datetime] = Field(
        None,
        description="""The iso datetime for the last update of the handle data.""",
        json_schema_extra={
            "linkml_meta": {"alias": "timestamp", "domain_of": ["HandleRecord"]}
        },
    )
    type: Literal["EMAIL"] = Field(
        "EMAIL",
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
    The data element in the handle API for the contact email.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://w3id.org/nfdi4cat/pid4cat-model",
            "slot_usage": {
                "format": {"equals_string": "string", "name": "format"},
                "value": {"name": "value", "pattern": "^\\S+@[\\S+\\.]+\\S+"},
            },
        }
    )

    format: Optional[Literal["string"]] = Field(
        None,
        description="""The format of the handle data.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "format",
                "domain_of": [
                    "HdlDataUrl",
                    "HdlDataStatus",
                    "HdlDataSchemaVer",
                    "HdlDataLicense",
                    "HdlDataContact",
                    "HdlDataResourceInfo",
                    "HdlDataRelated",
                    "HdlDataLog",
                ],
                "equals_string": "string",
            }
        },
    )
    value: Optional[str] = Field(
        None,
        description="""The value of the handle data.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "value",
                "domain_of": [
                    "HdlDataUrl",
                    "HdlDataStatus",
                    "HdlDataSchemaVer",
                    "HdlDataLicense",
                    "HdlDataContact",
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


class RESOURCEINFO(HandleRecord):
    """
    The data element in the handle API for the resource info.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://w3id.org/nfdi4cat/pid4cat-model"}
    )

    index: Optional[int] = Field(
        None,
        ge=6,
        le=6,
        json_schema_extra={
            "linkml_meta": {
                "alias": "index",
                "domain_of": [
                    "URL",
                    "STATUS",
                    "SCHEMA_VER",
                    "LICENSE",
                    "EMAIL",
                    "RESOURCE_INFO",
                    "RELATED",
                    "LOG",
                ],
            }
        },
    )
    data: Optional[HdlDataResourceInfo] = Field(
        None,
        json_schema_extra={
            "linkml_meta": {
                "alias": "data",
                "domain_of": [
                    "URL",
                    "STATUS",
                    "SCHEMA_VER",
                    "LICENSE",
                    "EMAIL",
                    "RESOURCE_INFO",
                    "RELATED",
                    "LOG",
                ],
            }
        },
    )
    ttl: Optional[int] = Field(
        None,
        description="""A time to live in seconds for the handle record. Typically: 86400 => 1 day
TODO: Research details of ttl meaning for handle API.
""",
        json_schema_extra={
            "linkml_meta": {"alias": "ttl", "domain_of": ["HandleRecord"]}
        },
    )
    timestamp: Optional[datetime] = Field(
        None,
        description="""The iso datetime for the last update of the handle data.""",
        json_schema_extra={
            "linkml_meta": {"alias": "timestamp", "domain_of": ["HandleRecord"]}
        },
    )
    type: Literal["RESOURCE_INFO"] = Field(
        "RESOURCE_INFO",
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
    The data element in the handle API for the resource info.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://w3id.org/nfdi4cat/pid4cat-model",
            "slot_usage": {
                "format": {"equals_string": "string", "name": "format"},
                "value": {"name": "value", "range": "ResourceInfo"},
            },
        }
    )

    format: Optional[Literal["string"]] = Field(
        None,
        description="""The format of the handle data.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "format",
                "domain_of": [
                    "HdlDataUrl",
                    "HdlDataStatus",
                    "HdlDataSchemaVer",
                    "HdlDataLicense",
                    "HdlDataContact",
                    "HdlDataResourceInfo",
                    "HdlDataRelated",
                    "HdlDataLog",
                ],
                "equals_string": "string",
            }
        },
    )
    value: Optional[ResourceInfo] = Field(
        None,
        description="""The value of the handle data.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "value",
                "domain_of": [
                    "HdlDataUrl",
                    "HdlDataStatus",
                    "HdlDataSchemaVer",
                    "HdlDataLicense",
                    "HdlDataContact",
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
        {"from_schema": "https://w3id.org/nfdi4cat/pid4cat-model"}
    )

    index: Optional[int] = Field(
        None,
        ge=7,
        le=7,
        json_schema_extra={
            "linkml_meta": {
                "alias": "index",
                "domain_of": [
                    "URL",
                    "STATUS",
                    "SCHEMA_VER",
                    "LICENSE",
                    "EMAIL",
                    "RESOURCE_INFO",
                    "RELATED",
                    "LOG",
                ],
            }
        },
    )
    data: Optional[HdlDataRelated] = Field(
        None,
        json_schema_extra={
            "linkml_meta": {
                "alias": "data",
                "domain_of": [
                    "URL",
                    "STATUS",
                    "SCHEMA_VER",
                    "LICENSE",
                    "EMAIL",
                    "RESOURCE_INFO",
                    "RELATED",
                    "LOG",
                ],
            }
        },
    )
    ttl: Optional[int] = Field(
        None,
        description="""A time to live in seconds for the handle record. Typically: 86400 => 1 day
TODO: Research details of ttl meaning for handle API.
""",
        json_schema_extra={
            "linkml_meta": {"alias": "ttl", "domain_of": ["HandleRecord"]}
        },
    )
    timestamp: Optional[datetime] = Field(
        None,
        description="""The iso datetime for the last update of the handle data.""",
        json_schema_extra={
            "linkml_meta": {"alias": "timestamp", "domain_of": ["HandleRecord"]}
        },
    )
    type: Literal["RELATED"] = Field(
        "RELATED",
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
    The data element in the handle API for related identifiers.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://w3id.org/nfdi4cat/pid4cat-model",
            "slot_usage": {
                "format": {"equals_string": "string", "name": "format"},
                "value": {
                    "multivalued": True,
                    "name": "value",
                    "range": "Pid4CatRelation",
                },
            },
        }
    )

    format: Optional[Literal["string"]] = Field(
        None,
        description="""The format of the handle data.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "format",
                "domain_of": [
                    "HdlDataUrl",
                    "HdlDataStatus",
                    "HdlDataSchemaVer",
                    "HdlDataLicense",
                    "HdlDataContact",
                    "HdlDataResourceInfo",
                    "HdlDataRelated",
                    "HdlDataLog",
                ],
                "equals_string": "string",
            }
        },
    )
    value: Optional[List[Pid4CatRelation]] = Field(
        None,
        description="""The value of the handle data.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "value",
                "domain_of": [
                    "HdlDataUrl",
                    "HdlDataStatus",
                    "HdlDataSchemaVer",
                    "HdlDataLicense",
                    "HdlDataContact",
                    "HdlDataResourceInfo",
                    "HdlDataRelated",
                    "HdlDataLog",
                ],
            }
        },
    )


class LOG(HandleRecord):
    """
    The data element in the handle API for the change log.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://w3id.org/nfdi4cat/pid4cat-model"}
    )

    index: Optional[int] = Field(
        None,
        ge=8,
        le=8,
        json_schema_extra={
            "linkml_meta": {
                "alias": "index",
                "domain_of": [
                    "URL",
                    "STATUS",
                    "SCHEMA_VER",
                    "LICENSE",
                    "EMAIL",
                    "RESOURCE_INFO",
                    "RELATED",
                    "LOG",
                ],
            }
        },
    )
    data: Optional[HdlDataLog] = Field(
        None,
        json_schema_extra={
            "linkml_meta": {
                "alias": "data",
                "domain_of": [
                    "URL",
                    "STATUS",
                    "SCHEMA_VER",
                    "LICENSE",
                    "EMAIL",
                    "RESOURCE_INFO",
                    "RELATED",
                    "LOG",
                ],
            }
        },
    )
    ttl: Optional[int] = Field(
        None,
        description="""A time to live in seconds for the handle record. Typically: 86400 => 1 day
TODO: Research details of ttl meaning for handle API.
""",
        json_schema_extra={
            "linkml_meta": {"alias": "ttl", "domain_of": ["HandleRecord"]}
        },
    )
    timestamp: Optional[datetime] = Field(
        None,
        description="""The iso datetime for the last update of the handle data.""",
        json_schema_extra={
            "linkml_meta": {"alias": "timestamp", "domain_of": ["HandleRecord"]}
        },
    )
    type: Literal["LOG"] = Field(
        "LOG",
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
    The data element in the handle API for the change log.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://w3id.org/nfdi4cat/pid4cat-model",
            "slot_usage": {
                "format": {"equals_string": "string", "name": "format"},
                "value": {"multivalued": True, "name": "value", "range": "LogRecord"},
            },
        }
    )

    format: Optional[Literal["string"]] = Field(
        None,
        description="""The format of the handle data.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "format",
                "domain_of": [
                    "HdlDataUrl",
                    "HdlDataStatus",
                    "HdlDataSchemaVer",
                    "HdlDataLicense",
                    "HdlDataContact",
                    "HdlDataResourceInfo",
                    "HdlDataRelated",
                    "HdlDataLog",
                ],
                "equals_string": "string",
            }
        },
    )
    value: Optional[List[LogRecord]] = Field(
        None,
        description="""The value of the handle data.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "value",
                "domain_of": [
                    "HdlDataUrl",
                    "HdlDataStatus",
                    "HdlDataSchemaVer",
                    "HdlDataLicense",
                    "HdlDataContact",
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
        None,
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
    A relation between pid4cat handles or between a pid4cat handle and other resources identified by a PID.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://w3id.org/nfdi4cat/pid4cat-model"}
    )

    relation_type: Optional[RelationType] = Field(
        None,
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
        None,
        description="""The related identifier.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "related_identifier",
                "domain_of": ["Pid4CatRelation"],
            }
        },
    )
    datetime_log: Optional[datetime] = Field(
        None,
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
    Data object to hold information about the resource and its representation.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://w3id.org/nfdi4cat/pid4cat-model"}
    )

    label: Optional[str] = Field(
        None,
        description="""A human-readable name for a resource.""",
        json_schema_extra={
            "linkml_meta": {"alias": "label", "domain_of": ["ResourceInfo"]}
        },
    )
    description: Optional[str] = Field(
        None,
        description="""A human-readable description for a resource.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "description",
                "domain_of": ["ResourceInfo", "LogRecord"],
            }
        },
    )
    resource_category: Optional[ResourceCategory] = Field(
        None,
        description="""The category of the resource.""",
        json_schema_extra={
            "linkml_meta": {"alias": "resource_category", "domain_of": ["ResourceInfo"]}
        },
    )
    representation_variants: Optional[List[RepresentationVariant]] = Field(
        None,
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
    A log record for changes made in a pid4cat handle record starting from registration.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://w3id.org/nfdi4cat/pid4cat-model"}
    )

    datetime_log: Optional[datetime] = Field(
        None,
        description="""The date and time of a log record.""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "datetime_log",
                "domain_of": ["Pid4CatRelation", "LogRecord"],
            }
        },
    )
    has_agent: Optional[Agent] = Field(
        None,
        description="""The person who registered or modified the PID record.""",
        json_schema_extra={
            "linkml_meta": {"alias": "has_agent", "domain_of": ["LogRecord"]}
        },
    )
    changed_field: Optional[ChangeLogField] = Field(
        None,
        description="""The field that was changed""",
        json_schema_extra={
            "linkml_meta": {"alias": "changed_field", "domain_of": ["LogRecord"]}
        },
    )
    description: Optional[str] = Field(
        None,
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
    Person who plays a role relative to PID creation or curation.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "class_uri": "prov:Agent",
            "from_schema": "https://w3id.org/nfdi4cat/pid4cat-model",
            "slot_usage": {
                "email": {"name": "email", "pattern": "^\\S+@[\\S+\\.]+\\S+"}
            },
        }
    )

    name: Optional[str] = Field(
        None,
        description="""The name of the agent that created or modified the PID record.""",
        json_schema_extra={"linkml_meta": {"alias": "name", "domain_of": ["Agent"]}},
    )
    email: Optional[str] = Field(
        None,
        description="""Email address of the agent that created or modified the PID record.""",
        json_schema_extra={"linkml_meta": {"alias": "email", "domain_of": ["Agent"]}},
    )
    orcid: Optional[str] = Field(
        None,
        description="""The ORCID of the person""",
        json_schema_extra={"linkml_meta": {"alias": "orcid", "domain_of": ["Agent"]}},
    )
    affiliation_ror: Optional[str] = Field(
        None,
        description="""The ROR of the agent's affiliation.""",
        json_schema_extra={
            "linkml_meta": {"alias": "affiliation_ror", "domain_of": ["Agent"]}
        },
    )
    role: Optional[Pid4CatAgentRole] = Field(
        None,
        description="""The role of the agent relative to the resource""",
        json_schema_extra={"linkml_meta": {"alias": "role", "domain_of": ["Agent"]}},
    )

    @field_validator("email")
    def pattern_email(cls, v):
        pattern = re.compile(r"^\S+@[\S+\.]+\S+")
        if isinstance(v, list):
            for element in v:
                if isinstance(v, str) and not pattern.match(element):
                    raise ValueError(f"Invalid email format: {element}")
        elif isinstance(v, str):
            if not pattern.match(v):
                raise ValueError(f"Invalid email format: {v}")
        return v


class RepresentationVariant(ConfiguredBaseModel):
    """
    A representation of the resource in other media types than text/html which is the default for landing_page_url.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://w3id.org/nfdi4cat/pid4cat-model"}
    )

    url: Optional[str] = Field(
        None,
        description="""The URL of the representation.""",
        json_schema_extra={
            "linkml_meta": {"alias": "url", "domain_of": ["RepresentationVariant"]}
        },
    )
    media_type: Optional[MEDIATypes] = Field(
        None,
        description="""The media type of the representation as defined by [IANA](https://www.iana.org/assignments/media-types/media-types.xhtml)""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "media_type",
                "domain_of": ["RepresentationVariant"],
            }
        },
    )
    encoding_format: Optional[str] = Field(
        None,
        description="""The encoding of the representation. https://encoding.spec.whatwg.org/#names-and-labels""",
        json_schema_extra={
            "linkml_meta": {
                "alias": "encoding_format",
                "domain_of": ["RepresentationVariant"],
            }
        },
    )
    size: Optional[int] = Field(
        None,
        description="""The size of the representation in bytes.""",
        ge=0,
        json_schema_extra={
            "linkml_meta": {"alias": "size", "domain_of": ["RepresentationVariant"]}
        },
    )


class RelatedIdentifier(ConfiguredBaseModel):
    """
    A class for all types pf related identifiers.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://w3id.org/nfdi4cat/pid4cat-model"}
    )

    type: Literal["RelatedIdentifier"] = Field(
        "RelatedIdentifier",
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
                }
            },
        }
    )

    resolving_url: Optional[str] = Field(
        None,
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
        "PurlIdentifier",
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
                "identifier": {
                    "name": "identifier",
                    "pattern": "^doi:10\\.\\d{4,}\\/.*$",
                },
                "resolving_url": {
                    "name": "resolving_url",
                    "pattern": "^https:\\/\\/doi\\.org\\/10.*$",
                },
            },
        }
    )

    resolving_url: Optional[str] = Field(
        None,
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
        None,
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
        "DoiIdentifier",
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
        pattern = re.compile(r"^doi:10\.\d{4,}\/.*$")
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
                    "pattern": "^(hdl|handle):\\d{2}\\.\\d{4,}\\/.*$",
                },
                "resolving_url": {
                    "name": "resolving_url",
                    "pattern": "^https:\\/\\/hdl\\.handle\\.net\\/\\d{2}\\.\\d{4,}\\/.*$",
                },
            },
        }
    )

    resolving_url: Optional[str] = Field(
        None,
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
        None,
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
        "HandleIdentifier",
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
        pattern = re.compile(r"^https:\/\/hdl\.handle\.net\/\d{2}\.\d{4,}\/.*$")
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
        pattern = re.compile(r"^(hdl|handle):\d{2}\.\d{4,}\/.*$")
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
                },
            },
        }
    )

    identifier: Optional[str] = Field(
        None,
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
        None,
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
        "ArkIdentifier",
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
                }
            },
        }
    )

    identifier: Optional[str] = Field(
        None,
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
        "UrnIdentifier",
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
    A  Global Trade Item Number (GTIN) previously called European Article Number (EAN) often encoded as EAN13 barcode. The identifier is used to identify products. GTINs don't have a resolvable URL.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://w3id.org/nfdi4cat/pid4cat-model",
            "slot_usage": {
                "identifier": {"name": "identifier", "pattern": "^\\d{13}$"}
            },
        }
    )

    identifier: Optional[str] = Field(
        None,
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
        "GtinIdentifier",
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
        None,
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
        None,
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
        "ExampleIdentifier",
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


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
HandleAPIRecord.model_rebuild()
HandleRecord.model_rebuild()
URL.model_rebuild()
HdlDataUrl.model_rebuild()
STATUS.model_rebuild()
HdlDataStatus.model_rebuild()
SCHEMAVER.model_rebuild()
HdlDataSchemaVer.model_rebuild()
LICENSE.model_rebuild()
HdlDataLicense.model_rebuild()
EMAIL.model_rebuild()
HdlDataContact.model_rebuild()
RESOURCEINFO.model_rebuild()
HdlDataResourceInfo.model_rebuild()
RELATED.model_rebuild()
HdlDataRelated.model_rebuild()
LOG.model_rebuild()
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
