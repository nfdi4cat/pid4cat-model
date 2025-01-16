import sys
from datetime import datetime
from pathlib import Path
from linkml_runtime.dumpers import json_dumper, yaml_dumper
from pid4cat_model.datamodel import pid4cat_model_pydantic as p4c

# Demonstrate the use of Pydantic models

if sys.version_info < (3, 11):
    raise RuntimeError(
        "Python >= 3.11 is required until merging of https://github.com/linkml/linkml-runtime/pull/357"
    )

p1_Agent = p4c.Agent(
    name="Data Fuzzi",
    email="data.fuzzi@example.org",
    orcid="0000-0000-0000-0000",
    affiliation_ror="https://ror.org/01abcde",
    role=p4c.PID4CatAgentRole.TRUSTEE,
)

p1_related = [
    p4c.PID4CatRelation(
        relation_type=p4c.RelationType.IS_PART_OF,
        related_identifier="https://example.org/collection",
        datetime_log=datetime.fromisoformat("2024-02-19T00:00:00Z"),
    ),
    p4c.PID4CatRelation(
        relation_type=p4c.RelationType.IS_REFERENCED_BY,
        related_identifier="https://example.org/referenced",
        datetime_log=datetime.fromisoformat("2024-02-19T00:00:00Z"),
    ),
]

p1_repr_variants = [
    p4c.RepresentationVariant(
        url="https://example.org/resource",
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
    responseCode = 1,
    handle = "21.T12995/lik-1",
    values = [
        p4c.HandleRecord(
            index = 1,
            type = p4c.HandleDataType.URL,
            ttl = 86400,
            timestamp = datetime.fromisoformat("2024-05-15T15:51:15Z"),
            data = p4c.HandleData(
                format = "string",
                value = "https://pid4cat.example.org/lik-1",
            ),
        ),
        p4c.HandleRecord(
            index = 2,
            type = p4c.HandleDataType.STATUS,
            ttl = 86400,
            timestamp = datetime.fromisoformat("2024-05-15T15:51:15Z"),
            data = p4c.HandleData(
                format = "string",
                value = p4c.PID4CatStatus.REGISTERED,
            ),
        ),
        p4c.HandleRecord(
            index = 3,
            type = p4c.HandleDataType.SCHEMA_VER,
            ttl = 86400,
            timestamp = datetime.fromisoformat("2024-05-15T15:51:15Z"),
            data = p4c.HandleData(
                format = "string",
                value = "v0.1.0",
            ),
        ),
        p4c.HandleRecord(
            index = 4,
            type = p4c.HandleDataType.LICENSE,
            ttl = 86400,
            timestamp = datetime.fromisoformat("2024-05-15T15:51:15Z"),
            data = p4c.HandleData(
                format = "string",
                value = "CC0-1.0",
            ),
        ),
        p4c.HandleRecord(
            index = 5,
            type = p4c.HandleDataType.EMAIL,
            ttl = 86400,
            timestamp = datetime.fromisoformat("2024-05-15T15:51:15Z"),
            data = p4c.HandleData(
                format = "string",
                value = "datafuzzi@example.org",
            ),
        ),
        p4c.HandleRecord(
            index = 6,
            type = p4c.HandleDataType.RESOURCE_INFO,
            ttl = 86400,
            timestamp = datetime.fromisoformat("2024-05-15T15:51:15Z"),
            data = p4c.HandleData(
                format = "string",
                value = p1_res_info,
            ),
        ),
        p4c.HandleRecord(
            index = 7,
            type = p4c.HandleDataType.RELATED,
            ttl = 86400,
            timestamp = datetime.fromisoformat("2024-05-15T15:51:15Z"),
            data = p4c.HandleData(
                format = "string",
                value = p1_related,
            ),
        ),
        p4c.HandleRecord(
            index = 8,
            type = p4c.HandleDataType.LOG,
            ttl = 86400,
            timestamp = datetime.fromisoformat("2024-05-15T15:51:15Z"),
            data = p4c.HandleData(
                format = "string",
                value = p1_log,
            ),
        ),
    ],
)

c = p4c.Container(contains_pids=[p1_api])

print(p1_api)

print(yaml_dumper.dumps(c))

print(json_dumper.dumps(p1_api))

# write json to file
script_folder = Path(__file__).parent
with open(script_folder / "example_p1.json", "w", encoding="utf-8") as f:
    f.write(json_dumper.dumps(p1_api))
