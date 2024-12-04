from linkml_runtime.dumpers import json_dumper, yaml_dumper
from pid4cat_model.datamodel import pid4cat_model_pydantic as p4c

p1_Agent = p4c.Agent(
    name="Data Fuzzi",
    email=None,
    orcid="0000-0000-0000-0000",
    affiliation_ror=None,
    role=p4c.PID4CatAgentRole.TRUSTEE,
)

p1_log = p4c.LogRecord(
    datetime_log="2024-02-19T00:00:00Z",
    has_agent=p1_Agent,
    changed_field=p4c.ChangeLogField.STATUS,
    description="as requested in issue #234",
)

p1_resource_info = p4c.ResourceInfo(
    label="Resource label",
    description="Resource description",
    resource_category=p4c.ResourceCategory.SAMPLE,
    rdf_url="https://example.org/resource",
    rdf_type="TURTLE",
    schema_url="https://example.org/schema",
    schema_type="XSD",
)

p1 = p4c.PID4CatRecord(
    id="lik-123",
    change_log=[p1_log],
    landing_page_url="https://pid4cat.example.org/lik-123",
    status=p4c.PID4CatStatus.REGISTERED,
    pid_schema_version="0.1.0",
    resource_info=p1_resource_info,
    related_identifiers=None,
    license="CC0-1.0",
    curation_contact_email="datafuzzi@example.org",
)

c = p4c.Container(contains_pids=[p1])

print(p1)

print(json_dumper.dumps(p1))

print(yaml_dumper.dumps(c))
