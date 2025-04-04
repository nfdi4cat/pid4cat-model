import json
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
    email_address="data.fuzzi@example.org",
    orcid="0000-0000-0000-0000",
    affiliation_ror="https://ror.org/029hg0311",
    role=p4c.Pid4CatAgentRole.TRUSTEE,
)

p1_related = [
    p4c.Pid4CatRelation(
        relation_type=p4c.RelationType.IS_PART_OF,
        # pydantic complains if using RelatedIdentifier directly instead of
        # the designated classes. - A bug? (observed with linkml 1.8.5)
        # related_identifier=p4c.RelatedIdentifier(
        #     type="ExampleIdentifier",
        #     identifier="ex:collection1",
        #     resolving_url="https://example.org/collection1",
        # ),
        related_identifier=p4c.ExampleIdentifier(
            type="ExampleIdentifier",
            identifier="ex:collection1",
            resolving_url="https://example.org/collection1",
        ),
        datetime_log=datetime.fromisoformat("2024-02-19T00:00:00Z"),
    ),
    p4c.Pid4CatRelation(
        relation_type=p4c.RelationType.IS_REFERENCED_BY,
        related_identifier=p4c.ExampleIdentifier(
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
        # As above, pydantic complains if using HandleRecord directly instead
        # of the designated classes. - A bug? (observed with linkml 1.8.5)
        p4c.URL(
            index=1,
            type="URL",
            ttl=86400,
            timestamp=datetime.fromisoformat("2024-05-15T15:51:15Z"),
            data=p4c.HdlDataUrl(
                format="string",
                value="https://pid4cat.example.org/lik-1",
            ),
        ),
        p4c.EMAIL(
            index=10,
            type="EMAIL",
            ttl=86400,
            timestamp=datetime.fromisoformat("2024-05-15T15:51:15Z"),
            data=p4c.HdlDataContact(
                format="string",
                value="datafuzzi@example.org",
            ),
        ),
        p4c.STATUS(
            index=11,
            type="STATUS",
            ttl=86400,
            timestamp=datetime.fromisoformat("2024-05-15T15:51:15Z"),
            data=p4c.HdlDataStatus(
                format="string",
                value=p4c.Pid4CatStatus.REGISTERED,
            ),
        ),
        p4c.SCHEMAVER(  # gen-pydantic replaces SCHEMA_VER with SCHEMAVER in linkml 1.8.5
            index=12,
            type="SCHEMA_VER",
            ttl=86400,
            timestamp=datetime.fromisoformat("2024-05-15T15:51:15Z"),
            data=p4c.HdlDataSchemaVer(
                format="string",
                value="v0.1.0",
            ),
        ),
        p4c.METADATALICENSE(
            index=13,
            type="METADATA_LICENSE",
            ttl=86400,
            timestamp=datetime.fromisoformat("2024-05-15T15:51:15Z"),
            data=p4c.HdlDataLicense(
                format="string",
                value="CC0-1.0",
            ),
        ),
        p4c.RESOURCE(
            index=14,
            type="RESOURCE",
            ttl=86400,
            timestamp=datetime.fromisoformat("2024-05-15T15:51:15Z"),
            data=p4c.HdlDataResourceInfo(
                format="string",
                value=p1_res_info,
            ),
        ),
        p4c.RELATED(
            index=15,
            type="RELATED",
            ttl=86400,
            timestamp=datetime.fromisoformat("2024-05-15T15:51:15Z"),
            data=p4c.HdlDataRelated(
                format="string",
                value=p1_related,
            ),
        ),
        p4c.CHANGES(
            index=16,
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

c = p4c.HandleRecordContainer(contains_pids=[p1_api])

# print(p1_api)
print(yaml_dumper.dumps(c))

script_folder = Path(__file__).parent
with open(script_folder / "example_p1.yaml", "w", encoding="utf-8") as f:
    f.write(yaml_dumper.dumps(c))

try:
    # Next line fails with linkML 1.8.5 due to a bug in json_dumper.py
    # which does not convert datetime objects to strings
    json_dump = json_dumper.dumps(p1_api, inject_type=False)
    print(json_dump)
    # write json to file
    with open(script_folder / "example_p1.json", "w", encoding="utf-8") as f:
        f.write(json_dump)
except Exception as e:
    print(f"Failed to dump to JSON: {e}")
    print("Please use a fixed version of linkml_runtime")

data_json = p1_api.model_dump_json(indent=2)
with open(script_folder / "example_p1_pydantic.json", "w", encoding="utf-8") as f:
    f.write(data_json)

print("Dumped to example_p1_pydantic.json")

# Load the data again to pydantic class

print("\nReloading data from JSON")

d = json.loads(data_json)

with Path("tests/data/21.T11978_hdlnet_api/TEST_KBKA-BEM9_decoded.json").open(
    mode="r", encoding="utf-8"
) as f:
    d = json.load(f)
p1_api_reloaded = p4c.HandleAPIRecord(**d)
print(p1_api_reloaded)

# Create a Pid4CatRecord object from the data
data = {}
data["landing_page_url"] = "https://pid4cat.example.org/lik-1"
data["curation_contact"] = "datafuzzi@example.org"
data["status"] = p4c.Pid4CatStatus.REGISTERED
data["schema_version"] = "v0.1.0"
data["metadata_license"] = "CC0-1.0"
data["resource_info"] = p1_res_info
data["related_identifiers"] = p1_related
data["change_log"] = p1_log

print("\nTrying to create a Pid4CatRecord object", end="... ")
rec = p4c.Pid4CatRecord.model_validate(data)
print("success!")
print(f"-> Landing page: {rec.landing_page_url}")
