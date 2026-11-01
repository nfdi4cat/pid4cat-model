import json
from pathlib import Path

from pydantic import ValidationError
import pytest
from pid4cat_model.datamodel.pid4cat_model_pydantic import (
    HandleAPIRecord,
    RepresentationVariant,
)


def test_load_json_from_handle_net():
    with Path("tests/data/21.T11978_hdlnet_api/TEST-D4Y_kbka-bem9_decoded.json").open(
        mode="r", encoding="utf-8"
    ) as f:
        data = json.load(f)
    pid = HandleAPIRecord(**data)
    assert pid.handle == "21.T11978/4cat/TEST-D4Y/kbka-bem9"


@pytest.mark.parametrize(
    "handle",
    [
        "21.T11978/TEST/KBKA-BEM9",  # no 4cat segment
        "21.T11978/4cat/TEST-D4Y/batch-1/kbka-bem9",  # "/" in the id-suffix
        "21.T11978/4cat/TEST-D4Y/KBKA-BEM9",  # upper case in the id-suffix
        "21.T11978/4cat/TEST-I4Y/kbka-bem9",  # I is not in Crockford Base32
    ],
)
def test_handle_outside_the_pid4cat_structure(handle):
    data = {"responseCode": 1, "handle": handle, "values": []}

    with pytest.raises(ValidationError, match="handle"):
        HandleAPIRecord(**data)


def test_representation_variant_requires_media_type():
    with pytest.raises(ValidationError, match="media_type"):
        RepresentationVariant(variant_url="https://example.org/resource.ttl")


def test_load_json_from_handle_net_invalid():
    """
    Load data with invalid media type "textturtle". Check for validation error.

    The validation error message is long and misleading: "25 validation errors
    for HandleAPIRecord" - The pydantic model does not help to detect that only
    the mediatype is invalid (it should be "text/turtle").
    """
    with Path("tests/data/21.T11978_hdlnet_api/TEST-D4Y_kbka-bem9_invalid.json").open(
        mode="r", encoding="utf-8"
    ) as f:
        data = json.load(f)

    with pytest.raises(ValidationError):
        _pid = HandleAPIRecord(**data)
