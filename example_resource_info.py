from linkml_runtime.dumpers import json_dumper
from pid4cat_model.datamodel import pid4cat_model_pydantic as p4c

pid1_resource_info = p4c.ResourceInfo(
    label="Resource label",
    description="Resource description",
    resource_category=p4c.ResourceCategory.SAMPLE,
    rdf_url="https://example.org/resource",
    rdf_type="TURTLE",
    schema_url="https://example.org/schema",
    schema_type="XSD",
)

print(json_dumper.dumps(pid1_resource_info, inject_type=False))
