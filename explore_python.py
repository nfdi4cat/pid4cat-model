from linkml_runtime.dumpers import json_dumper
from pid4cat_model.datamodel import pid4cat_model as p4c


p1_Agent = p4c.Agent(
    orcid="0000-0000-0000-0000",
    name="Data Fuzzi",
    role="TRUSTEE",
)

p1_log = p4c.LogRecord(
    datetime_log="2024-02-19T00:00:00Z",
    has_agent=p1_Agent,
    changed_field=p4c.ChangeLogField.STATUS,  # "STATUS",
    description="as requested in issue #234",
)

p1 = p4c.PID4CatRecord(
    id="lik-1",
    change_log=p1_log,
    landing_page_url="https://pid4cat.example.org/lik-1",
    status=p4c.PID4CatStatus.REGISTERED,  # "REGISTERED",
    resource_info={},
    related_identifiers=None,
    license="CC0-1.0",
    curation_contact_email="datafuzzi@example.org",
)

print(p1)

print(json_dumper.dumps(p1))

c = p4c.Container(contains_pids=[p1])
