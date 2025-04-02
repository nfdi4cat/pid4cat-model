import json
from pathlib import Path

from pydantic import ValidationError
import pytest
from pid4cat_model.datamodel.pid4cat_model_pydantic import HandleAPIRecord


def test_load_json_from_handle_net():
    with Path("tests/data/21.T11978_hdlnet_api/TEST_KBKA-BEM9_decoded.json").open(
        mode="r", encoding="utf-8"
    ) as f:
        data = json.load(f)
    pid = HandleAPIRecord(**data)
    assert pid.handle == "21.T11978/TEST/KBKA-BEM9"


def test_load_json_from_handle_net_invalid():
    """
    Load data with invalid media type "textturtle". Check for validation error.

    The validation error message is long and misleading: "25 validation errors
    for HandleAPIRecord" - The pydantic model does not help to detect that only
    the mediatype is invalid (it should be "text/turtle").
    """
    with Path("tests/data/21.T11978_hdlnet_api/TEST_KBKA-BEM9_invalid.json").open(
        mode="r", encoding="utf-8"
    ) as f:
        data = json.load(f)

    with pytest.raises(ValidationError):
        _pid = HandleAPIRecord(**data)
