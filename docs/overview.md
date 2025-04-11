# Overview

## What is a Persistent Identifier and what is pid4cat?

A Persistent Identifier (PID) is a long-lasting reference to a digital resource that remains valid regardless of changes in the resource's location or ownership.

pid4cat is a persistent identifier service designed specifically for the needs of the catalysis research community.
The pid4cat service builds upon existing PID infrastructure ([Handle System](https://www.handle.net/)) while providing enhanced capabilities for metadata management and namespace delegation.
It enables partner organizations to manage their own sub-namespaces while maintaining a consistent approach to identifier creation and metadata management.
It consists of three main components:

1. **pid4cat-model**: A data model for metadata of persistent identifiers
2. **pid4cat API**: A REST API for creating, updating, and retrieving PIDs and their associated metadata
3. **pid4cat hosting**: Operation of a production handle system with an officially registered permanent handle-prefix 21.11165 and of an analogous test system with the demo prefix 21.T11978.

## Design goals

For the PID system:

- Provide PIDs for NFDI4Cat and its tools & services
- Low cost per PID
- Managed and operated by one main authority (HLRS)
- Sub ID-spaces for sub name assigning authorities (SNAA)
- Allow each SNAA to create IDs according to self-defined patterns
  (with some constraints on allowed characters)
- Custom REST-API access with authorization for PID-management by SNAAs
- Use of a single common handle prefix
- Open tools & open data (CC-0 for PID metadata, MIT or Apache-2-license for code)

For the PID metadata model:

- Predominantly metadata about the PID (status, changes, contact)
- Low post-creation update work for metadata
- Minimum information about the resource
  - What is identified? (selection among few types)
  - How to access the resource? (for example which other media type than html can be requested)
- Relations to other PIDs (reuse relations from DataCite [metadata schema](https://datacite-metadata-schema.readthedocs.io/))
- linked-data conform to facilitate PID-graph integration/creation

For the pid4cat pattern:

- Recognizable as pid4cat
- Short meaningless identifier for the namespaces of SNAAs.
- Best-practice guidelines for identifier patterns to help the SNAAs.
- Within the prefix space, only the combination of identifier for the namespace
  and SNAA-created ID must be unique to allow offline (uncoordinated & de-centralized) minting of identifiers.

## Handle System Basics

Every handle consists of two parts:
its naming authority, otherwise known as its prefix,
and a unique local name under the naming authority, otherwise known as its suffix:[^1]

`<Handle> ::= <Handle Naming Authority> "/" <Handle Local Name>`

The naming authority and local name are separated by the ASCII character "/".

```ascii
21.zzzzz/4cat/638s-k9dx
\______/\_____________/
   |           |
 prefix      suffix
```

The collection of local names under a naming authority defines the local handle namespace for that naming authority.
Any local name must be unique under its local namespace.
The uniqueness of a naming authority and a local name under that authority ensures that any handle is globally unique within the context of the Handle System.

The naming authority for pid4cat handles is HLRS.

[^1]:
  Larry Lannom and Lt. Col. Brian P. Boesch and Sam Sun, RFC 3650: Handle System Overview, 2003.
  https://datatracker.ietf.org/doc/html/rfc3650

## Identifier pattern

The handle-suffix part has to fulfill different roles in pid4cat handles.
First, it should allow the minting of PIDs by different institutions.
This requires that a part of the PID suffix is used as an identifier for an organization using a sub-PID-namespace.
Second, the suffix must contain an identifier part that makes it unique in each sub-PID-namespace.
Third, the suffix should make pid4cat handles easily distinguishable from other handles (for humans).

The following scheme was selected for pid4cat handles:

- `<handle-prefix> / <branding-suffix> / <ns-suffix> / <id-suffix>`

```ascii
21.zzzzz/4cat/xxx/723-hk-09
        \___/\__/\________/
          |    |      |
   branding    |     id-suffix
     suffix   ns-suffix
```

As a branding label we use `4cat` to make pid4cat handles easily distinguishable.[^4]
This has as already been implemented for NFDI4Cat´s [data repository](https://repository.nfdi4cat.org).
Next comes an identifier `ns-suffix` for the namespace of sub-authorities associated with the PID-subspace followed by the ID-suffix part.
Regarding uniqueness, it is important to note that only the combination of ns-suffix and id-suffix must be unique.
Due to this all SNAAs are independent in the IDs they generate.
The same id-suffix may be present in different sub namespaces.
The different parts are separated by the ASCII character "/".

Rules for the `<ns-suffix>`:

- To identify the sub-authority, opaque (meaningless) IDs should be used.
  It is suggested to keep the sub-authority identifier short (3 chars)
  and use only the crockford-32 alphabet. This gives 32**3 = 32768 combinations.
- Sub-namespaces have to be requested at HLRS.
- The ns-suffixes are generated randomly and should have no meaning (for example they should not match abbreviations of institutions).[^2]


Rules for the `<id-suffix>`:

- The local-IDs are managed by the responsible SNAA.
  It may contain letters [A-Za-z], numbers [0-9] and symbols [./] as part of the identifier.
- Dashes in this part are ignored.
- The local-IDs should be kept short and not exceed 36 chars including dashes (which is the length of UUID4).
- If an optional checksum is included, it must be calculated including the `<ns-suffix>` and ignoring dashes.

Suggested checksum calculations:

- **The ISO 7064 Mod 97, 10 algorithm.** It evaluates the whole identifier as an integer which is valid if the number modulo 97 is 1.
  It has two check digits and is easy to compute. Strings may be handled by replacing the letters with a number, e.g. its ascii-code,
  before applying the algorithm.
  It is for example used by [ROR](https://ror.org/) and [DataCite](https://datacite.org/).
- **The ISO 7064 Mod 37, 36 algorithm.** It uses one alphanumeric check digit and the identifier itself may also be alphanumeric (digit or char).
  Hence, it is well suited to detect error in alphanumeric identification numbers.
  This algorithm is for example used by the [Global Release Identifier](https://en.wikipedia.org/wiki/Global_Release_Identifier).

Implementation of these algorithms are available in many languages (for example in [python-stdnum](https://arthurdejong.org/python-stdnum/doc/1.20/stdnum.iso7064),
[base32-lib](https://pypi.org/project/base32-lib/) for Python or [cdigit](https://github.com/LiosK/cdigit) for JavaScript).

!!! warning "Open question on supporting case sensitivity for identifier suffix."

    TODO: Update after poll: [Do you need case-sensitive ID handling?](https://github.com/nfdi4cat/pid4cat-model/issues/114)

    While case sensitive strings would not be required for numeric, hex or base32 encoded IDs,
    case sensitivity would be essential to support also base64 encoded ID-suffixes.
    Case-insensitivity could only be enabled for certain sub-namespaces upon SNAA request.
    It should not be enforced for all created identifiers and case-insensitive should be the default.

[^2]: Fenner, M. (2016). ‘Cool DOI's’, DataCite Blog, https://doi.org/10.5438/55E5-T5C0

## Use case: PIDs for samples, devices etc.

pid4cat identifiers can be used for various resources in the catalysis research domain:

| Category   | Definition | Description of use  |
| :----------- | :-------------- | :------------------------------------------------------------------------------- |
| COLLECTION   | [voc4cat:0005012](https://w3id.org/nfdi4cat/voc4cat_0005012) | A collection is a group of resources and/or other collections |
| SAMPLE       | [voc4cat:0005013](https://w3id.org/nfdi4cat/voc4cat_0005013) | A representative part of a material of interest on which observations are made. |
| MATERIAL     | [voc4cat:0005014](https://w3id.org/nfdi4cat/voc4cat_0005014) | A material used in the research process (except samples). |
| DEVICE       | [voc4cat:0005015](https://w3id.org/nfdi4cat/voc4cat_0005015) | A physical device used in a research or manufacturing process. |
| DATA_OBJECT  | [voc4cat:0005016](https://w3id.org/nfdi4cat/voc4cat_0005016) | A collection of data available for access or download. A data object might be a data file, a data set, a data collection. |
| DATA_SERVICE | [voc4cat:0005017](https://w3id.org/nfdi4cat/voc4cat_0005017) | An organized system of operations that provide data processing functions or access to datasets. |

The categories are linked to SKOS concepts defined in the [Voc4Cat](https://nfdi4cat.github.io/voc4cat/) vocabulary.
Such mapping to machine readable terminologies facilitate the use of pid4cat PIDs in linked-data applications and are key to fully realize FAIR data.

## Use case: repo4cat

[Repo4cat](https://repository.nfdi4cat.org/) is the data sharing portal created and operated by NFDI4Cat.
It is built upon [Dataverse](https://dataverse.org/).
Repo4cat makes use of pid4cat handles to persistently identify the stored resources.

Example handle PID for data in the production instance of [repo4cat](https://repository.nfdi4cat.org/):

- [https://hdl.handle.net/21.11165/4cat/638s-k9dx](https://hdl.handle.net/21.11165/4cat/638s-k9dx?noredirect)
- The shoulder `4cat/` is also used as "PID-namespace" for repo4cat PIDs.
- The `<ns-suffix>` is not present in repo4cat PIDs.

Currently the PIDs minted by repo4cat lack the rich metadata that are attached to other pid4cat PIDs due to limitations of Dataverse.

## PID resolution methods

pid4cat identifiers can be resolved using multiple methods:

### Direct Handle System resolution

```http
https://hdl.handle.net/<prefix>/4cat/<ns-suffix>/<id-suffix>
```

### pid4cat resolver

```http
https://pid.nfdi4cat.org/<prefix>/4cat/<ns-suffix>/<id-suffix>
```

or alternatively

```http
https://handle.nfdi4cat.org/<prefix>/4cat/<ns-suffix>/<id-suffix>
```

### DOI proxy

The DOI resolver also works with other handles than the DOI 10.*-handles.

```http
https://doi.org/<prefix>/4cat/<ns-suffix>/<id-suffix>
```

## Logos & display guidelines

The pid4cat identifier should be displayed consistently across all platforms to ensure recognition and proper use.

### Display Format

When displaying pid4cat identifiers in text:

- Use the full handle identifier including prefix, branding suffix, namespace suffix, and local identifier part
- Do not abbreviate any part of the identifier
- Maintain the case sensitivity of the identifier

Example: `21.11165/4cat/ABC/SAMPLE-2023-001`

When creating hyperlinks use the handle.net resolver URL:

- `https://hdl.handle.net/21.11165/4cat/ABC/SAMPLE-23-001`

For using pid4cat identifies in linked-data application we plan to register `pid4cat` as the _preferable prefix_ for `https://pid.nfdi4cat.org/21.11165/4cat/` in [Bioregistry](https://bioregistry.io/). This allows to use the CURIE (compact URI) notation:

- `pid4cat:ABC/SAMPLE-23-001`

### Logo Usage

When referencing pid4cat in applications, websites, or publications, the following logo guidelines apply:

- The official pid4cat logo should be used when possible
- Maintain the aspect ratio of the logo
- Do not modify or alter the logo
- Ensure sufficient clear space around the logo
- Use the full-color version on light backgrounds and the inverted version on dark backgrounds

The official pid4cat logos can be downloaded from [URL to be provided].

## Best Practices

### Local Identifier Design

SNAAs are encouraged to follow these best practices when designing their local identifier scheme:

1. **Consistency**: Adopt a consistent pattern across all identifiers within your namespace
2. **Documentation**: Document your identifier pattern for future reference
3. **Avoid semantics**: Minimize semantic content that might become outdated.
   - Semantic identifiers contain meaningful information (e.g., `JoeMiller-Sample-LiMg-001`)
   - Opaque identifiers have no inherent meaning (e.g., `x7z-9q2`)
4. **Validation**: Implement validation to ensure identifiers conform to your pattern
5. **Checksums**: Consider incorporating checksums for error detection
6. **Future-proofing**: Design for scalability and longevity

If the resources that you want to assign identifiers to, have already identifiers in a local system (for example an electronic lab notebook),
it is strongly suggested to reuse these locally unique identifiers for the identifier part in the pid4cat identifier.
Often these are just integer numbers or type-number combinations.

If you design a new scheme, consider how the IDs are used.
For example, whenever reading and typing of the IDs by humans is important, consider using character sets (alphabets) designed for this purpose and/or using a checksum.

- **Base32-encoded sequential number with checksum**:

For example, base32-encoding the number "123456789" with ISO 7064-Mod97-10 checksum gives the ID:

  ```ascii
  3FZ-2J9
  ```

For pure machine use and if global uniqueness is important consider using

- **UUID4-based identifiers** (unordered):

  ```ascii
  40944082-40ed-4f66-9e8f-66fbcd3908a9
  ```

- **UUID7-based identifiers** (time-ordered):

  ```ascii
  0195c559-4b8a-7201-a7ab-f1a5d06687e0
  ```

See also suffix design in [identifier pattern](#identifier-pattern) section and PID literature[^3]^,^[^4].

[^3]:
  McMurry JA, Juty N, Blomberg N, Burdett T, Conlin T, Conte N, et al. (2017) ‘Identifiers for the 21stcentury: How to design, provision, andreuse persistent identifiers to maximize utility and impact of lifescience data’. PLoS Biol15(6): e2001414. https://doi.org/10.1371/journal.pbio.2001414

[^4]:
  Philipson, Joakim. ‘Identifying PIDs Playing FAIR’. Data Science 2, no. 1–2 (1 January 2019): 229–44. https://doi.org/10.3233/DS-190024.


### Landing Pages

Landing pages should:

1. **Be persistent**: Remain accessible for as long as the identifier exists
2. **Provide metadata**: Display key metadata about the resource
3. **Offer access information**: Provide direct access to the resource or clear instructions for obtaining access
4. **Include citation information**: Show how the resource should be cited
5. **Show provenance**: Include information about the origin and history of the resource
6. **Be human-readable**: Present information in a user-friendly format
7. **Be machine-readable**: Include structured metadata (e.g., JSON-LD, RDFa)

### Metadata Quality

To maintain high-quality metadata:

1. **Completeness**: Provide as many relevant metadata elements as possible
2. **Accuracy**: Ensure metadata correctly describes the resource
3. **Timeliness**: Update metadata when the resource changes
4. **Relationships**: Document relationships to other resources

### Integrating with Local Systems

Recommendations for integrating pid4cat with local systems:

1. **Automated workflows**: Implement workflows that automatically create identifiers at appropriate points in research data lifecycles
2. **Metadata harvesting**: Set up processes to harvest metadata from local systems for pid4cat
3. **User interfaces**: Provide user-friendly interfaces for creating and managing identifiers
4. **Authentication integration**: Integrate local authentication systems with pid4cat API access
5. **Monitoring**: Implement monitoring to ensure identifiers remain resolvable

### Security and Access Control

The SNAAs ensure the security and access control of the data and must secure it with sufficient technical and organisational measures.

#### API Key Management

1. Keep your API key secure
2. Rotate keys periodically (recommended every 90 days)
3. Use separate keys for different environments (development, production)
4. Revoke compromised keys immediately

#### Access Policies

1. Only authorized personnel should have access to create and modify PIDs
2. Implement internal approval workflows for PID creation
3. Maintain an audit log of all PID operations
4. Review access permissions quarterly

## Roadmap

The development and expansion of pid4cat is planned in several phases:

### Phase 1: Infrastructure Establishment (Completed)

- Handle prefix registration
- Basic API implementation
- Core metadata model development
- Initial documentation

### Phase 2: Service Expansion (Current)

- Enhance API capabilities
- Improve metadata model
- Integration with related services
- Expansion of user and developer documentation
- Onboarding of initial SNAAs

### Phase 3: Community Growth (Upcoming)

- Outreach to potential SNAAs
- Development of additional tools and services
- Integration with the broader PID ecosystem
- Community building activities

### Phase 4: Sustainability (Future)

- Establish a sustainable funding model
- Plan long-term preservation
- Evaluation and improvement of governance model

## History

The pid4cat service has been developed within NFDI4Cat, a project funded by the German Research Foundation (DFG) to establish a research data infrastructure for catalysis research (see [About](./about.md)).

Key milestones in the development of pid4cat:

- **2023**: Initial conceptualization of pid4cat
- **2024**: Launch of the production handle server
- **2025**: Launch of pid4cat service; Onboarding of initial SNAAs
