# Documentation

**Draft** of a structure for the pid4cat documentation.

# Basics

## What is pid4cat?

xxx

- Operation of a production system (with aregistered pemananent handle-suffix) and an analogous test system (with a demo handle-prefix)
- Costs may have to be shared by SNAAs in post-NFDI times

## Design goals

For the PID system:

- Provide PIDs for NFDI4Cat and its tool & services
- Low cost per PID
- Managed and operated by one main authority (HLRS)
- Sub ID-spaces for sub name assigning authorities SNAA
- Allow each SNAA to create IDs according to own pattern
  (with some constraints on allowed characters)
- Custom REST-API-access with authorisation for PID-management by SNAAs
- Use of a single common handle prefix
- Open tools & open data (CC-0 fir PID metadata, MIT/Apache-2-license for code)

For the PID meta data model:

- Pre-dominantly metadata about the PID (status, changes, contact)
- Low post-creation update work for metadata
- Minimum information about the resource
  - What is identified? (selection among few types)
  - How to access the resource? (for example which other media type than html can be requested)
- Relations to other PIDs (reuse relations from DataCite)
- linked-data conform to facilitate PID-graph integration/creation

For the pid4cat-pattern:

- Recognisable as pid4cat
- Short meaningless identifier for the namespaces of sub name assigning authorities (which are provided from MA to SNNAs)
- Best-practice guidelines for identifier patterns to help SNAAs (sub name assigning authorities)
- Within the prefix space, only the combination of identifier for the namespace and SNAA-created ID must be unique to allow offline (uncoordinated) ID minting.

## Identifier pattern

## Handle System Basics

Every handle consists of two parts:
its naming authority, otherwise known as its prefix,
and a unique local name under the naming
authority, otherwise known as its suffix:

`<Handle> ::= <Handle Naming Authority> "/" <Handle Local Name>`

The naming authority and local name are separated by the ASCII
character "/".

```ascii
21.zzzzz/4cat/638s-k9dx
\______/\_____________/
   |           |
 prefix      suffix
```

The collection of local names under a naming
authority defines the local handle namespace for that naming
authority.  Any local name must be unique under its local namespace.
The uniqueness of a naming authority and a local name under that
authority ensures that any handle is globally unique within the
context of the Handle System.

The naming authority for pid4cat handles is HLRS.

Ref.: https://datatracker.ietf.org/doc/html/rfc3650

## pid4cat suffix design

The suffix has to fulfill different roles in pid4cat handles.
First, it should allow the minting of PIDs by different institutions.
This requires that a part of the PID suffix is used as identifier for an organisation using a sub-PID-namespace.
Second, the suffix must contain an identifier part the makes it unique in a sub-PID-namespace.
Third, the suffix should make pid4cat-handles easily distiguishable from other handles (for humans) [ref?].

The following scheme was selected for pid4cat handles:

- `<handle-prefix> / <branding-suffix> / <ns-suffix> / <id-suffix>`

```ascii
21.zzzzz/4cat/xxx/723-hk-09
        \___/\__/\________/
          |    |      |
   branding    |     id-suffix
     suffix   ns-suffix
```

As branding label we use `4cat` as already done for the dataverse data repository.
Next comes an identifier `ns-suffix` for the namesspace of sub-authorities associated with the PID-subspace followed by the ID-suffix part.
Regarding uniqueness, it is important to note that only the combination of ns-suffix and id-suffix must be unique. Due to this all sub-NAAs are independent in the IDs they generate. The same id-suffix may be present in different sub namespaces. The different parts are separated by the ASCII character "/".

Rules for the `<ns-suffix>`:

- For identifying the sub-authority IDs without meaning should be used.
  It is suggested to keep the sub-authority identifier short (3 chars)
  and use only the crockford-32 alphabet. This gives 32**3 = 32768 combinations.
- Sub-namespaces have to be requested at HLRS.
- The ns-suffixes are generated radomly and should have no meaning (for example they should not match abbreviations of insititutions). [ref.]

Rules for the `<id-suffix>`:

- The local-ID is managed by the NAA for the sub-namespace.
  It may contain letters [A-Za-z], numbers [0-9] and symbols [./] as part if the identifier.
- Dashes in this part are ignored.
- If an optional checksum is included, it must be calculated including the `<ns-suffix>` and ignoring dashes.

Suggested checksum calculations:

- **The ISO 7064 Mod 97, 10 algorithm.** It evaluates the whole identifier as an integer which is valid if the number modulo 97 is 1. It has two check digits and is easy to compute. It is for example used by ROR and DataCite.
- **The ISO 7064 Mod 37, 36 algorithm.** It uses one alphanumeric check digit and the identifier itself may also be alphanumeric (digit or char). Hence, it is well suited to detect error in  alphanumeric identification numbers. This algorithm is for example used by the [Global Release Identifier](https://en.wikipedia.org/wiki/Global_Release_Identifier).

Open question:

- should the ID-suffix be case sensitive? While this would not be required for numeric, hex or base32 encoded IDs, case sensitivity would be essential to support also base64 encoded ID-suffixes.
  - Proposal: support case-sensitive IDs -

LGPL lib: https://arthurdejong.org/python-stdnum/doc/1.20/stdnum.iso7064

## Uses

Example handle PID for data in the production instance of [repo4cat](https://repository.nfdi4cat.org/):

- https://hdl.handle.net/21.11165/4cat/638s-k9dx
- The shoulder "4cat" is used as "PID-namespace" for all handles minted by the production dataverse.

## Logos & display guidelines

## Suffix guidelines

- guidelines on schemes for suffix2 to help sub name assigning authorities
  - hard: allowed chars, checksum algorithm, checksum positioning
  - open: use of a checksum
  - on registration: description of pattern and information if a checksum is used. part of suffix2; if a custom pattern is used a regex must be provided which includes the ns-suffix.

## Governance

## Roadmap

## History

# Metadata

For pid4cat handles metadata are stored directly in the handle record in contrast to the DOI-system where metadata are hosted by the DOI-providers like DataCite.

The metadata for pid4cat include mainly data about the pid and its relation to other pids. The relation information should be relate the new PID to relevant existing PIDs. pid4cat allows but does not mandate that PIDs are updated with new relations that come into existence only later after the PID assignment to a resource.

The metadata schema for pid4cat is defined as a LinkML schema. From this LinkML schema various representations can be created.

The schema is documenented under [overview](/overview).

The Python package derived from the schema is described in the section [Tools and Services](#Tools-and-services) below.

# REST APIs

HLRS API (create, read, update)

Standard handle.net REST API (read only)

# Tools and Services

Python package based on LinkML pid4cat-model.

django app (?)

# Open Data

We plan to make a PID meta data dump available as FAIR data in the future.
