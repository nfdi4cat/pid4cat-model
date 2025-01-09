import sys
from datetime import datetime
from linkml_runtime.dumpers import json_dumper
from pid4cat_model.datamodel import pid4cat_model as p4c

# Demonstrate the use of Python DataClass-based model

if sys.version_info < (3, 11):
    raise RuntimeError("Python 3.11 or higher is required due to the use of datetime.fromisoformat")

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

p1 = p4c.PID4CatRecord(
    id="lik-1",
    landing_page_url="https://pid4cat.example.org/lik-1",
    status=p4c.PID4CatStatus.REGISTERED,
    pid_schema_version="0.1.0",
    license="CC0-1.0",
    curation_contact_email="datafuzzi@example.org",
    resource_info=p1_res_info,
    related_identifiers=p1_related,
    change_log=p1_log,
)

print(p1)

print(json_dumper.dumps(p1))

c = p4c.Container(contains_pids=[p1])
