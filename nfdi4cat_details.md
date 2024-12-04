# PIDs in NFDI4Cat

> *This document is work in progress (and not yet a reference).*

Persistent identifiers (PIDs) play an important role in achieving FAIR data.
This text is about the different use cases for PIDs in NFDI4Cat and how each case is solved technically.

## PIDs for Data Portals

According to the [architecture document](https://zenodo.org/doi/10.5281/zenodo.10391090), different repositories are considered for the NFDI4Cat data infra structure:

- **Repo4Cat**, the central global repository for publishing data and collaborating on data.
- Local repositories hosted at various institutions, e.g. BasCat or LARA

Since Researchers expect DOIs for their data publications,
the data sets published in Repo4Cat should get a DOIs from DataCite as PID.

However, DOIs are not a good fit for earlier stages of research due to the metadata requirements and associated costs.
Nevertheless researchers want to share research artifacts already in the early stage with collaborators and having PIDs already at this stage would be very useful. 
Therefore, NFDI4Cat will in addition to DOIs use a handle-based solution **PID4Cat** (see below) 
to address the need for PIDs in the early phase when data are shared in private with collaborators. Repo4Cat seeks to support this private sharing between collaborators.

NFDI4cat has selected Dataverse as software for Repo4Cat, the global data portal.
Dataverse supports two types of PIDs: DOIs and handles.
It is however not possible to use handles and DOIs at the same time in a single Dataverse installation.

To address this limitations, two possible solutions are discussed:

- [preferred] Use one Dataverse instance and PID4Cat-handles as primary PID. For data sets being published DOIs will be minted (and linked to the handle).
- Use two Dataverse instances, one for published data that is configured to use DOIs and another one for early-stage data that is configured to use PID4-Cat-handles.

For the handle-PIDs in Dataverse, it is suggested

- To generate individual PIDs for all files in a dataset.
  
  Configuration
  - [:DataFilePIDFormat](https://guides.dataverse.org/en/latest/installation/config.html#datafilepidformat) = independent

- To generate the ID-part via a procedure stored in the DB.
  What scheme is used does not matter much, but clashes with PID4Cat-handles or other Dataverse (BasCat) must be avoided.
  Via a stored procedure UUID4 (or UUID7) identifiers could be created.
  An alternative is to add a prefix to the numeric ID used by default.
  The numeric ID may be base32 encoded to shorten the ID length.
  In this case the start ID should maybe not set to 1 but to 1001 to make the numeric part stick out.
  For example:
  - r4c-9OH    (prefix and base32 encoded integer number)
    - "9OH" is 10001 using [base-32 alphabet](https://en.wikipedia.org/wiki/Base32#base-32)
  - r4c-10001  (prefix & integer number)
  
  Preferred is the first scheme, because it is shorter.
  
  It is suggested to not use RFC4648 base32 (letters A to Z and numbers 2 to 7) but another, more human-friendly alphabet, preferably z-base-32.
  The z-base-32 encoding avoids human reading problems by excluding 0, l, v, 2 
  (number 0 may be confused with letter o, letter l with number 1 or letter i, letter v is close to u or r especially in handwriting, also number 2 is close to z in handwriting).
  The z-base-32 alphabet is optimized for lowercase letters so should be represented in this form.

  Configuration:
  - [:IdentifierGenerationStyle](https://guides.dataverse.org/en/latest/installation/config.html#identifiergenerationstyle) = storedProcGenerated

Related Dataverse documentation:

- [General Dataverse PID documentation](https://guides.dataverse.org/en/latest/installation/config.html#persistent-identifiers-and-publishing-datasets)
- [Dataverse handle configuration](https://guides.dataverse.org/en/latest/installation/config.html#configuring-your-dataverse-installation-for-handles)


## PIDs for Catalysis Research Resources (PID4Cat)

PIDs like the well known DOIs require a certain set of metadata (see DataCite Schema).
DOIs are based on handles, which in principle allow to store additional data in the record.
However, DOI metadata are stored in a different service and have to be requested via the DataCite API
which is a different service than the handle-system used for resolving a DOI.
The reason for DataCite`s approach is performance(?).

For NFDI4Cat a simpler system that reduces complexity is more attractive.
Therefore, PID4Cat handles are similar to [ePIC](http://www.pidconsortium.net/)-handles in that they use the handle record itself to store metadata.
This has the advantage that these metadata are available directly from the resolver.

PID4Cat comes with a well-defined schema for how and which metadata to store in the handle record. 
The schema is defined in [LinkML](https://linkml.io/linkml/) and developed in this repo ([NFDI4Cat/PID4Cat](https://github.com/nfdi4cat/pid4cat-model/)).
The schema does only require a minimum of information; it does not disclose anything about the resource except its type. Moreover, it is not required to specify an owner/creator but only a curator. Therefore, PID4Cat-handles do not mandate to put resources into context if this is undesired for whatever reasons.

### Mapping of PID4Cat schema to handle record

The PID4Cat schema is mapped to the handle record as follows:

**Table** Example record for a PID4Cat handle with the suffix "lik-dfi345", URL: https://hdl.handle.net/20.1000/lik-dfi345 <BR> The *PID4CatRecord* column contains the slot name of the LinkML model that is written to the respective line of the handle record; this column is not part of the handle record.

| Index | Type | Timestamp | Data | *PID4CatRecord* |
|-------|------|-----------|------|-----------|
|     1 | URL  | 2024-01-01 10:47:38Z | https://pid4cat.example.org/lik-dfi345 | *landing pageURL* |
|     2 | STATUS | 2024-02-19 13:40:02Z | REGISTERED | *status* |
|     3 | SCHEMA_VER | 2024-01-01 10:47:38Z | 1.0.0 | *pid_schema_version* |
|     4 | LICENSE | 2024-01-01 10:47:38Z | CC0-1.0 | *license* |
|     5 | EMAIL | 2024-01-01 10:47:38Z | datafuzzi@example.org | *curation_contact_email* |
|     6 | RESOURCE_INFO | 2024-01-01 10:47:38Z | {json} | *resource_info* |
|     7 | RELATED | 2024-02-19 13:40:02Z | {json} | *related_identifiers* |
|     8 | CHANGES | 2024-02-19 13:40:02Z | {json} | *change_log* |

In a future version, the non-standard values the in **Type**-column may be replaced by references to type declarations in a datatype registry (DTR).
Such DTRs are still under development and not yet widely used.

The LICENSE specifies the licence for the metadata in the PID-record.
It will be fixed to CC0-1.0 in the NFDICat service to facilitate reuse.

Since PID4Cat is a linkML-model we have all tools at hand to create records or an API.
For example, we can use the pydantic-model created from the PID4cat schema to create the json-objects for the PID record above, for example the *resource_info* json-object:

```python
from linkml_runtime.dumpers import json_dumper
from pid4cat_model.datamodel import pid4cat_model_pydantic as p4c

pid1_resource_info = p4c.ResourceInfo(
    label="Resource label",
    description="Resource description",
    resource_category=p4c.ResourceCategory.SAMPLE,
    rdf_url="https://example.org/resource/pid1",
    rdf_type="TURTLE",
    schema_url="https://example.org/resource_schema",
    schema_type="XSD",
)

print(json_dumper.dumps(pid1_resource_info, inject_type=False))
```

which will print the json-object to be stored under index 7 in the handle-record:

```json
{                                            
  "label": "Resource label",                 
  "description": "Resource description",     
  "resource_category": "SAMPLE",             
  "rdf_url": "https://example.org/resource", 
  "rdf_type": "TURTLE",                      
  "schema_url": "https://example.org/schema",
  "schema_type": "XSD"                       
}                                            
```
The pydantic model can also be used to create web APIs with other Python-based tools like django-ninja or fastapi.

### Handle-suffix design

*This text is based on the proposal "PID-suffix, Version 2" made in NFDI4Cat-openproject on 2023-12-07*

Two handle-suffix schemes are supported:

- **UUID4** (_uuid pid4cat_)
  - Can be either supplied from the PID-applicant when minting a new PID or can be generated by the gateway (both ways should be possible).
  UUID7 should also be accepted.
- **namespace_of_agent/local_ID** (_name-spaced pid4cat_)
  - The handle-gateway should only validate the uniqueness of `namespace_of_agent/local_ID`-combinations.
   It is suggested to use 3 characters from a human-friendly base32-alphabet as namespaces (e.g. **z-base-32**, see above). This gives 3**32 prefixes and if ever necessary we can switch to 4 chars.
  - The uniqueness of the `local_ID` has to be taken care of by the namespace owner.
  - The `local_ID` can be freely chosen by the namespace owner but is limited to ASCII letters [a-zA-Z], numbers [0-9] and symbols `.-`. *OK or too restrictive?*
  - The request for becoming the owner of a new namespace should be made by email.

Examples for PID4Cat handles (non-resolvable):

- **UUID4 pid4cat**: `https://hdl.handle.net/21.T11978/pid4cat/7e82d892-6acf-41a8-9c91-df826f67a806`
- **name-spaced pid4cat** in the example-namespace &quot;`k3a`&quot;:
  - `https://hdl.handle.net/21.T11978/pid4cat/k3a/123-456`
  - The corresponding regex in Python syntax is:   
    `re.compile(r"21\.T11978/pid4cat/(?P<namespace>k3a)/(?P<local_ID>\d{3}-\d{3})")`<BR>
    ...which extracts "k3a" as group "namespace" and "123-456" as group "local_ID".

  > Note, the `pid4cat`-part in the above URLs/suffixes has no functional meaning.
  > It is only present to make pid4cat-handles easily recognizable.
  > We should consider registering `pid4cat` as a prefix on bioregistry.io just like we registered the [voc4cat:](https://bioregistry.io/registry/voc4cat) prefix.

### API of handle server gateway

> This section is work in progress! It does not yet reflect the final implementation.

The role of the handle-server-gateway (HSG) is to restrict and manage write access to the handle-server and to add PID4Cat-specific validation for the handles.
The HSG provides an API only.
Create and updating PID4Cat-handles will exclusively managed via the HSG. 
Suggested URLs for the HSG are https://pid4cat.nfdi4cat.org or https://pid.nfdi4cat.org

> Note: Dataverse will not use the HSG but interface the handle-server directly.

The HSG controls which users are allowed to create and update handle records.
Except for sysadmins, HSG users will only be allowed to create and update handles for named-spaced PIDs.
All PID name-spaces will have at least one name-space admin user.
Institutions that like to manage a PID4Cat-PID-namespace need to register a PID-namespace admin with NFDI4Cat.

Suggested minimal API of the HSG:

*[unedited copy from internal OpenProject]*

Here is a tentative minimal API (to be discussed). 
API access is limited to special users &quot;namespace-owners&quot; (read-write), and &quot;viewers&quot; (read-only).
Anonymous users have no access.

* _Regarding permissions and the minimal API we like to get your feedback. Is this OK? Do you see gaps or need more functionality?_

#### List all PIDs records of owner [GET] or create new PID [PUT]:

`https://pid.nfdi4cat.org/<api-version>/<name-space> [GET,PUT]`

- `https://pid.nfdi4cat.org/` is the base url of the gateway server.
- `api-version` (e.g. `v1.0.0`) is a version specifier for the API (it is recommended  to version APIs)
- `name-space` is the first part of the suffix of name-spaced PID.
- Special notes on create [PUT]:
  - HSG should set "record_version" automatically on create
  - *...and some more validation & consistency checks*

#### Show PID record [GET] or update PID record [PUT]

`https://pid.nfdi4cat.org/<api-version>/<name-space>/<local-ID-of-pid> [GET,PUT]`

where `<name-space>/<local-ID-of-pid>` form the suffix of the handle to get or update. For the examples above it is `k3a/123-456` and `7e82d892-6acf-41a8-9c91-df826f67a806`, respectively.

- Special notes on updates [PUT]:
  - The data are supplied as PID4Cat-schema-conform json object in the body of the request.
  - each handle record update needs an update of the changelog (append)
  - HSG should set/increment "record_version" automatically on updates
  - *...and some more validation & consistency checks*

We could allow [DELETE] but we should not perform any true delete of a handle. Instead the record should be modified to state "OBSOLETE" (see PID4CatStatus enum in schema).

#### Possible API Extensions

The API may be extended to make the information in the handle record more accessible, for example

- Routes to retrieve all PIDs by category [GET]
- Routes to retrieve all PIDs by status [GET]

## Permanent IRIs for terminology or ontology terms

For linked-data applications permanent IRIs are required.
Several services exists that provide a stable base URL and
a redirect service that can be configured to redirect 
to the actual resource location.

Such services should support serving different data to humans and to machines.
One way to do this is via content-negotiation. Depending on the request that
is send to the redirect service, the client is redirected to human-oriented representation of the resource of to a machine-oriented one.

NFDI4Cat has selected [w3id.org](https://w3id.org/) for this service. Comparable services are [purl.org](https://purl.org/) or [pida.org](https://purls.helmholtz-metadaten.de/) which work in the same way.

In principle, it would also be possible to use handle-based PIDs for the terms in ontologies.
However, the additional features and the more reliable redundant network of the handle-system are of minor importance for this application.
