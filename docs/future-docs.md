# Documentation

**Draft** of a structure for the pid4cat documentation.

# Basics

## What is pid4cat?

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
 -  What is identified? (selection among few types)
 -  How to access the resource? (for example which other media type than html can be requested)
- Relations to other PIDs (reuse relations from DataCite)
- linked-data conform to facilitate PID-graph integration/creation

For the pid4cat-pattern:

- Recognisable as pid4cat
- Short meaningless identifier for the namespaces of sub name assigning authorities (which are provided from MA to SNNAs)
- Best-practice guidelines for identifier patterns to help SNAAs (sub name assigning authorities)
- Within the prefix space, only the combination of identifier for the namespace and SNAA-created ID must be unique to allow offline (uncoordinated) ID minting.

## Identifier pattern

## Handle System Basics

Every handle consists of two parts: its naming authority, otherwise
   known as its prefix, and a unique local name under the naming
   authority, otherwise known as its suffix:
   
<Handle> ::= <Handle Naming Authority> "/" <Handle Local Name>

   The naming authority and local name are separated by the ASCII
   character "/". 

   The collection of local names under a naming
   authority defines the local handle namespace for that naming
   authority.  Any local name must be unique under its local namespace.
   The uniqueness of a naming authority and a local name under that
   authority ensures that any handle is globally unique within the
   context of the Handle System.

```   
21.zzzzz/4cat/638s-k9dx
\______/\_____________/
   |           |
 prefix      suffix
```

Ref.: https://datatracker.ietf.org/doc/html/rfc3650

## pid4cat suffix design

The shoulders will comprise of two parts. The first "pid4cat" will provide
namespace that separates all handles under the prefix that conforming to the
pid4cat-model from other handles, e.g. created by dataverse. The second part
is used to create sub-namespaces that may be managed by other NFDI4Cat-related
institutions/services that will act as name assigning authority (NAA) for the
sub-namespace (e.g. LIKAT, U Greifswald, KIT).

Suffix-design:

- `<handle-prefix> / <branding-suffix> / <ns-suffix> / <id-suffix>`

```
21.zzzzz/4cat/xxx/723-hk-09
        \___/\__/\________/
          |      |      |
    branding     |     id-suffix
      suffix    ns-suffix
```

For identifying the sub-authority IDs without meaning should be used.
It is suggested to keep the sub-authority identifier short (3 chars) 
and use only lower case ascii letters a-z and numbers 0-9. 
Sub-namespaces have to be requested at HLRS.

The local-ID is managed by the NAA for the sub-namespace. It may contain
letters [A-Za-z], numbers [0-9] and the symbols [.-/].

Rules for the `<ns-suffix>`:
- Random three chars out of crockford-32 alphabet. This gives 32**3 = 32768 combinations.

Rules for the `<id-suffix>`:
- Dashes in this part are ignored.
- If an optional checksum is included, it must be calculated including the <ns-suffix> and ignoring dashes.

Suggested checksum calculations:
- The ISO 7064 Mod 97, 10 algorithm. It evaluates the whole identifier as an integer which is valid if the number modulo 97 is 1. It has two check digits and is easy to compute. (used by ROR and DataCite)
- The ISO 7064 Mod 37, 36 algorithm. The Mod 37, 36 algorithm uses an alphanumeric check digit and the number itself may also contain letters. Gives one check character (digit or char). Useful to detect error in  alphanumeric identification numbers. Used by Global_Release_Identifier (Music).

Example handle PID for data in the production instance of [repo4cat](https://repository.nfdi4cat.org/):

* https://hdl.handle.net/21.11165/4cat/638s-k9dx
* The shoulder "4cat" is used as "PID-namespace" for all handles minted by the production dataverse.

LGPL lib: https://arthurdejong.org/python-stdnum/doc/1.20/stdnum.iso7064

## Uses

## Logos & display guidelines

## Suffix guidelines

- guidelines on schemes for suffix2 to help sub name assigning authorities
  - hard: allowed chars, checksum algorithm, checksum positioning
  - open: use of a checksum
  - on registration: description of pattern and information if a checksum is used. part of suffix2; if a custom pattern is used a regex must be provided

## Governance

## Roadmap

## History

# Metadata

LinkML schema

# REST APIs

HLRS API (create, read, update)

Standard handle.net REST API (read only)

# Tools and Services

Python package based on LinkML pid4cat-model.

django app (?)

# Open Data

PID data dump download
