
# PIDs in NFDI4Cat

*David Linke, LIKAT, 2024-02-23 (first draft)*

## Permanent IRIs for terminology or ontology terms

For linked-data applications permanent IRIs are required.
Several services exists that provide a stable base URL and
a redirect service that can be configured to redirect 
to the actual resource location.

Such services should support serving different data to humans vs. machines.
One way to do this is via content-negotiation. Depending on the request that
is send to the redirect service, the client is redirected to human-oriented representation of the resource of to a machine-oriented one.

NFDI4Cat has selected w3id.org for this service. Comparable services are purl.org or pida.org which work in exactly the same way.

In principle, it would also be possible to use handle-based PIDs for the terms in ontologies.
However, the additional features and the more reliable redundant network of the handle-system are of minor importance for this application.

## PIDs for Data Portals

NFDI4cat has selected Dataverse as software for the data portal(s). 
Dataverse supports two types of PIDs: DOIs and handles. It is not possible to
use handles and DOIs at the same time.

According to the architecture document, different repositories are considered
for the NFDI4Cat data infra structure.
Since Researchers expect DOIs for the data publications that they make,
the Dataverse for publishing final data should use DOIs.
However, DOIs are not a good fit for earlier stages of research due to
the metadata requirements and associated costs.
Therefore, another Dataverse is offered for data shared in an early phase of research
which uses handle-PIDs. This Dataverse is especially targeted at helping 
researchers to collaboratively work with data in joint projects.

To summarize, HLRS offers two central Dataverse installations:

- "Data4Cat" for publishing final datasets that using DataCite DOIs
- "Colab4Cat" - A Dataverse that uses PID4Cat-Handles. Its purpose is to allow early sharing of data and collaborating on data prior to publishing.

In addition there may be other local Dataverse installation like at BasCat
which also have an interest to use the PID4Cat handle server to mint PIDs.

Things to think about:

- If a data set is published it will get a DOI in addition to the handle.
  Could this be a problem? For example, can the handle record be updated
  to point to the same landing page as the DOI. This is probably not 
  a standard functionality in Dataverse so requires a custom solution.
- more?

For the handle-PIDs in Dataverse it is suggested:

- To generate individual PIDs for all files in a dataset.
  
  Configuration
  - [:DataFilePIDFormat](https://guides.dataverse.org/en/latest/installation/config.html#datafilepidformat) = independent

- It is suggested to generate the ID-part via a procedure stored in the DB.
  What scheme is used does not matter much,
  but clashes with PID4Cat-handles or other Dataverse (BasCat) must be avoided,
  for example by adding a prefix to the numeric ID. 
  The start ID should maybe not set to 1 but to 1001 to make the numeric part stick out. 
  Numeric-IDs may be encoded to shorten the ID length. For example:
  - d4c-3yS    (prefix and base58 encoded integer number)
    - "3yS" is 10001 in [Base58 encoding](https://de.wikipedia.org/wiki/Base58) using alphabet [1-9A-HJ-NP-Za-km-z]
  - d4c-10001  (prefix & integer number)
  
  Preferred is the first scheme, because it is shorter. 
  The advantage of the base58 encoding (vs. base 36 or base 64) is that it avoids reading problems by excluding O, 0, I, l.

  Configuration:
  - [:IdentifierGenerationStyle](https://guides.dataverse.org/en/latest/installation/config.html#identifiergenerationstyle) = storedProcGenerated

Related documentation:

- [General Dataverse PID documentation](https://guides.dataverse.org/en/latest/installation/config.html#persistent-identifiers-and-publishing-datasets)
- [Dataverse handle configuration](https://guides.dataverse.org/en/latest/installation/config.html#configuring-your-dataverse-installation-for-handles)


## PIDs for Catalysis Research Resources (PID4Cat)

PIDs like the well known DOIs require a certain set of metadata (see DataCite Schema).
DOIs are based on handles, which in principle allow to store additional data in the record.
However, DOI metadata are stored in a different service and have to be requested via the DataCite API
which is a different service than the handle-system used for resolving a DOI.
The reason for DataCite`s approach is performance(? - need to check!).

For NFDI4Cat a simpler system that reduces complexity is more attractive.
Therefore, PID4Cat handles are similar to [ePIC](http://www.pidconsortium.net/)-handles in that they use the handle record itself to store metadata.
This has the advantage that these metadata are available directly from the resolver.

PID4Cat comes with a well-defined schema for how and which metadata to store in the handle record. The schema is defined in [LinkML](https://linkml.io/linkml/) and developed here ([NFDI4Cat/PID4Cat](https://github.com/dalito/pid4cat-model/)).

The PID4Cat schema is mapped to the handle record as follows:

**Table** Example record for a PID4Cat handle with the suffix "lik-dfi345", URL: https://hdl.handle.net/20.1000/lik-dfi345 <BR> The *PID4CatRecord* column contains the slot name of the LinkML model that is written to the respective line of the handle record.

| Index | Type | Timestamp | Data | *PID4CatRecord* |
|-------|------|-----------|------|-----------|
|     1 | URL  | ...       | https://pid4cat.example.org/lik-dfi345 | *landing pageURL* |
|     2 |   | ...       | REGISTERED | *status* |
|     3 |   | ...       | 20240219v0 | *record_version* |
|     4 |   | ...       | 1.0.0 | *pid_schema_version* |
|     5 |   | ...       | CC0-1.0 | *dc_rights* |
|     6 |   | ...       | datafuzzi@example.org | *curation_contact* |
|     7 |   | ...       | {json} | *resource_info* |
|     8 |   | ...       | {json} | *related_identifiers* |
|     9 |   | ...       | {json} | *change_log* |

In a future version the Type-column could reference type declarations in a datatype registry (DTR). Such DTRs are still under development and not yet open for general use.
