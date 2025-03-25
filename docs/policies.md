# Policies

## Governance

pid4cat is governed by a two-tiered structure:

1. **pid4cat Core Organization**: Responsible for the overall governance, technical operation, and sustainability of the pid4cat service
2. **Sub-Name Assigning Authorities (SNAAs)**: Partner organizations responsible for managing identifiers within their assigned sub-namespaces

## Governance Principles

1. **Transparency**: All policies, procedures, and decisions are documented and publicly available
2. **Inclusivity**: The governance process includes input from all stakeholders
3. **Sustainability**: Governance structures are designed to ensure the long-term viability of the service
4. **Accountability**: Clear responsibilities and reporting mechanisms are established
5. **Community-driven**: Governance is responsive to community needs and priorities

## Registration as SNAA

To become a Sub-Name Assigning Authority (SNAA), an organization must:

1. Submit an application to the Core Organization (HLRS)
2. Demonstrate the capability to maintain identified resources
3. Agree to the pid4cat policies
4. Designate technical and administrative contacts

## Identifier Persistence

pid4cat is committed to the persistence of identifiers. Once created, an identifier should remain resolvable indefinitely. This implies:

1. **No deletion**: Identifiers should not be deleted, even if the identified resource is no longer available
2. **Tombstones**: If a resource becomes unavailable, a tombstone page should be provided with information about the resource and its status
3. **Responsibility**: SNAAs are responsible for maintaining the resolution of identifiers they create

In exceptional circumstances, identifiers may be deleted or transferred, but only with the approval of the pid4cat Core Organization.

## Metadata

Metadata associated with identifiers can be updated to reflect changes in the resource or to correct errors.

1. **Metadata Quality**: SNAAs must provide accurate and complete metadata
2. **Metadata Updates**: Metadata may be updated to correct errors or reflect changes in the resource
3. **Core Organization Rights**: The Core Organization reserves the right to update metadata to ensure policy compliance
4. **Provenance**: All metadata updates are recorded with provenance information
5. **Metadata License**: All metadata is made available under CC0 1.0 Universal Public Domain Dedication

## Access Policy

1. **Landing Pages**: All identifiers must resolve to a landing page or point directly to the resource.
2. **Resource Access**: If a resource has access restrictions, a landing pages must provide clear information about how to access the resource.
3. **Metadata Access**: Metadata associated with identifiers should be openly accessible.

## Resource Access

pid4cat does not mandate that identified resources be openly accessible. However:

1. **Landing page requirement**: All identifiers must resolve to a landing page with basic metadata about the resource or point directly to the resource.
2. **Access information**: If access to the resource is restricted, the landing page must provide information about the restrictions and if/how access can be obtained.
3. **Metadata accessibility**: Metadata associated with identifiers should be openly accessible, even if the resource itself is not

## SNAA Responsibilities

Each SNAA is responsible for:

1. **Identifier Management**: Creating and maintaining identifiers within their sub-namespace
2. **Resource Maintenance**: Ensuring identified resources remain accessible or providing appropriate tombstone pages
3. **Metadata Accuracy**: Providing and maintaining accurate metadata
4. **Policy Compliance**: Adhering to all pid4cat policies
5. **Contact Information**: Maintaining up-to-date technical and administrative contacts
6. **Sustainability**: Contributing to the long-term sustainability of pid4cat

## Resource Access

pid4cat does not mandate that identified resources be openly accessible. However:

1. **Landing page requirement**: All identifiers must resolve to a landing page with basic metadata about the resource
2. **Access information**: If access to the resource is restricted, the landing page must provide clear information about the restrictions and how access can be obtained
3. **Metadata accessibility**: Metadata associated with identifiers should be openly accessible, even if the resource itself is not

## Licensing

pid4cat adopts the following licensing policies:

1. **Service licensing**: The pid4cat service is operated under [specific license]
2. **Metadata licensing**:
   - Metadata submitted to pid4cat is made available under the CC0 1.0 Universal Public Domain Dedication
   - This allows for unrestricted reuse of metadata, promoting interoperability and discovery
3. **Resource licensing**:
   - pid4cat does not mandate specific licenses for identified resources
   - SNAAs should include clear license information in the metadata
   - Recommended licenses include Creative Commons licenses, Open Data Commons licenses, and other open licenses

## Sustainability

To ensure the long-term sustainability of the pid4cat service:

1. **Succession planning**: The pid4cat Core Organization has established succession plans to ensure continuity of service
2. **SNAA succession**: SNAAs must designate a successor organization or return control of their sub-namespace to the Core Organization if they can no longer fulfill their responsibilities
3. **Financial model**: [Details about the financial model supporting pid4cat]
4. **Data preservation**: All identifier metadata is regularly backed up and preserved in multiple locations
