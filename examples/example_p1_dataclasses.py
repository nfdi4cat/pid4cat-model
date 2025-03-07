from pathlib import Path
import sys
from datetime import datetime
from linkml_runtime.dumpers import json_dumper, yaml_dumper
from pid4cat_model.datamodel import pid4cat_model as p4c

# Demonstrate the use of Python DataClass-based model

if sys.version_info < (3, 11):
    raise RuntimeError(
        "Python >= 3.11 is required until merging of https://github.com/linkml/linkml-runtime/pull/357"
    )

p1_Agent = p4c.Agent(
    name="Data Fuzzi",
    email_address="data.fuzzi@example.org",
    orcid="0000-0000-0000-0000",
    affiliation_ror="https://ror.org/029hg0311",
    role=p4c.Pid4CatAgentRole.TRUSTEE,
)

p1_related = [
    p4c.Pid4CatRelation(
        relation_type=p4c.RelationType.IS_PART_OF,
        related_identifier=p4c.RelatedIdentifier(
            type="ExampleIdentifier",
            identifier="ex:collection1",
            resolving_url="https://example.org/collection1",
        ),
        datetime_log=datetime.fromisoformat("2024-02-19T00:00:00Z"),
    ),
    p4c.Pid4CatRelation(
        relation_type=p4c.RelationType.IS_REFERENCED_BY,
        related_identifier=p4c.RelatedIdentifier(
            type="ExampleIdentifier",
            identifier="ex:referenced1",
            resolving_url="https://example.org/referenced1",
        ),
        datetime_log=datetime.fromisoformat("2024-02-19T00:00:00Z"),
    ),
]

p1_repr_variants = [
    p4c.RepresentationVariant(
        variant_url="https://example.org/resource",
        media_type="text/turtle",
        encoding_format="UTF-8",
        size=12345,
    ),
    # could be more than one representation variant
]

p1_res_info = p4c.ResourceInfo(
    label="Resource label",
    description="Resource description",
    resource_category=p4c.ResourceCategory.SAMPLE,
    representation_variants=p1_repr_variants,
)

p1_log = [
    p4c.LogRecord(
        datetime_log=datetime.fromisoformat("2024-02-19T00:00:00Z"),
        has_agent=p1_Agent,
        changed_field=p4c.ChangeLogField.STATUS,
        description="Registration completed.",
    ),
    p4c.LogRecord(
        datetime_log=datetime.fromisoformat("2024-05-15T15:51:15Z"),
        has_agent=p1_Agent,
        changed_field=p4c.ChangeLogField.RESOURCE_INFO,
        description="as requested in issue #234",
    ),
]

# HandleData

p1_api = p4c.HandleAPIRecord(
    responseCode=1,
    handle="21.T12995/lik-1",
    values=[
        p4c.HandleRecord(
            index=1,
            type="URL",
            ttl=86400,
            timestamp=datetime.fromisoformat("2024-05-15T15:51:15Z"),
            data=p4c.HdlDataUrl(
                format="string",
                value="https://pid4cat.example.org/lik-1",
            ),
        ),
        p4c.HandleRecord(
            index=2,
            type="STATUS",
            ttl=86400,
            timestamp=datetime.fromisoformat("2024-05-15T15:51:15Z"),
            data=p4c.HdlDataStatus(
                format="string",
                value=p4c.Pid4CatStatus.REGISTERED,
            ),
        ),
        p4c.HandleRecord(
            index=3,
            type="SCHEMA_VER",
            ttl=86400,
            timestamp=datetime.fromisoformat("2024-05-15T15:51:15Z"),
            data=p4c.HdlDataSchemaVer(
                format="string",
                value="v0.1.0",
            ),
        ),
        p4c.HandleRecord(
            index=4,
            type="LICENSE",
            ttl=86400,
            timestamp=datetime.fromisoformat("2024-05-15T15:51:15Z"),
            data=p4c.HdlDataLicense(
                format="string",
                value="CC0-1.0",
            ),
        ),
        p4c.HandleRecord(
            index=5,
            type="EMAIL",
            ttl=86400,
            timestamp=datetime.fromisoformat("2024-05-15T15:51:15Z"),
            data=p4c.HdlDataContact(
                format="string",
                value="datafuzzi@example.org",
            ),
        ),
        p4c.HandleRecord(
            index=6,
            type="RESOURCE",
            ttl=86400,
            timestamp=datetime.fromisoformat("2024-05-15T15:51:15Z"),
            data=p4c.HdlDataResourceInfo(
                format="string",
                value=p1_res_info,
            ),
        ),
        p4c.HandleRecord(
            index=7,
            type="RELATED",
            ttl=86400,
            timestamp=datetime.fromisoformat("2024-05-15T15:51:15Z"),
            data=p4c.HdlDataRelated(
                format="string",
                value=p1_related,
            ),
        ),
        p4c.HandleRecord(
            index=8,
            type="CHANGES",
            ttl=86400,
            timestamp=datetime.fromisoformat("2024-05-15T15:51:15Z"),
            data=p4c.HdlDataLog(
                format="string",
                value=p1_log,
            ),
        ),
    ],
)

print(p1_api)

print(json_dumper.dumps(p1_api))

container = p4c.HandleRecordContainer(contains_pids=[p1_api])

# write json to file
script_folder = Path(__file__).parent
with open(script_folder / "example_p1.json", "w", encoding="utf-8") as f:
    f.write(json_dumper.dumps(container, inject_type=False))
with open(script_folder / "example_p1.yaml", "w", encoding="utf-8") as f:
    f.write(yaml_dumper.dumps(container))
