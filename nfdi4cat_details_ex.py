from linkml_runtime.dumpers import json_dumper
from pid4cat_model.datamodel import pid4cat_model_pydantic as p4c

p1_repr_variants = [
    p4c.RepresentationVariant(
        variant_url="https://example.org/resource",
        media_type="text/turtle",
        encoding_format="UTF-8",
        size=12345,
    ),
    # could be more than one representation variant
]

pid1_resource_info = p4c.ResourceInfo(
    label="Resource label",
    description="Resource description",
    resource_category=p4c.ResourceCategory.SAMPLE,
    representation_variants=p1_repr_variants,
)

print(json_dumper.dumps(pid1_resource_info, inject_type=False))
