from http import HTTPStatus
import json
from pathlib import Path
import httpx
from pid4cat_model.handle_api import HandleNetAPI, HandleConfig
from pid4cat_model.datamodel.pid4cat_model_pydantic import Pid4CatRecord
from pid4cat_model.handle_api import pid4cat_record_factory


def test_HandleNetApi():
    """
    Test the HandleNetAPI class.
    """
    with Path("tests/data/21.T11978_hdlnet_api/TEST_KBKA-BEM9.json").open(
        mode="r", encoding="utf-8"
    ) as f:
        api_data_raw = json.load(f)
    with Path("tests/data/21.T11978_hdlnet_api/TEST_KBKA-BEM9_decoded.json").open(
        mode="r", encoding="utf-8"
    ) as f:
        api_data_decoded = json.load(f)

    # Create a configuration object
    config = HandleConfig()

    # Mock httpx request, https://www.python-httpx.org/advanced/transports/#mock-transports
    my_test_client = httpx.Client(
        transport=httpx.MockTransport(
            lambda request: httpx.Response(HTTPStatus.OK, json=api_data_raw)
        )
    )
    # Create an instance of HandleNetAPI
    handle_api = HandleNetAPI(config, my_test_client)

    # Check if the instance is created successfully
    assert isinstance(handle_api, HandleNetAPI)

    # Check if the base URL is set correctly
    assert (
        handle_api.config.base_url
        == f"{config.api_url}{config.prefix}/{config.ns_suffix}/"
    )
    assert handle_api.get_metadata_for_id("TEST/KBKA-BEM9") == api_data_decoded


def test_pid4cat_record_factory():
    """
    Test the pid4cat_record_factory function.
    """
    with Path("tests/data/21.T11978_hdlnet_api/TEST_KBKA-BEM9_decoded.json").open(
        mode="r", encoding="utf-8"
    ) as f:
        data = json.load(f)

    record = pid4cat_record_factory(data)
    assert isinstance(record, Pid4CatRecord)
    assert record.landing_page_url == "http://Mytest2.com"
