import re
from importlib.metadata import version

import yaml

import pid4cat_model
from pid4cat_model.datamodel import MAIN_SCHEMA_PATH
from pid4cat_model.datamodel import pid4cat_model as dataclass_model


def test_package_version_is_the_installed_distribution_version():
    assert pid4cat_model.__version__ == version("pid4cat-model")


def test_schema_version_is_the_version_of_the_packaged_schema():
    schema = yaml.safe_load(MAIN_SCHEMA_PATH.read_text(encoding="utf-8"))
    assert pid4cat_model.SCHEMA_VERSION == f"v{schema['version']}"


def test_schema_version_has_the_three_parts_of_schemaver():
    # A package version here (e.g. 0.4.3.1.post1.dev0+abc) means the schema
    # file was version-stamped by the build.
    assert re.fullmatch(r"v\d+\.\d+\.\d+", pid4cat_model.SCHEMA_VERSION)


def test_generated_dataclasses_match_the_schema_version():
    assert f"v{dataclass_model.version}" == pid4cat_model.SCHEMA_VERSION


def test_version_tuple_splits_the_package_version_into_ints_and_strs():
    version_tuple = pid4cat_model.__version_tuple__
    assert ".".join(str(part) for part in version_tuple) == (
        pid4cat_model.__version__.replace("+", ".")
    )
    assert all(isinstance(part, int) for part in version_tuple if str(part).isdigit())
