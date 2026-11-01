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
    with Path("tests/data/21.T11978_hdlnet_api/TEST-D4Y_kbka-bem9.json").open(
        mode="r", encoding="utf-8"
    ) as f:
        api_data_raw = json.load(f)
    with Path("tests/data/21.T11978_hdlnet_api/TEST-D4Y_kbka-bem9_decoded.json").open(
        mode="r", encoding="utf-8"
    ) as f:
        api_data_decoded = json.load(f)

    # Create a configuration object
    config = HandleConfig(ns_suffix="TEST-D4Y")
    requested_urls = []

    def respond(request):
        requested_urls.append(str(request.url))
        return httpx.Response(HTTPStatus.OK, json=api_data_raw)

    # Mock httpx request, https://www.python-httpx.org/advanced/transports/#mock-transports
    my_test_client = httpx.Client(transport=httpx.MockTransport(respond))
    # Create an instance of HandleNetAPI
    handle_api = HandleNetAPI(config, my_test_client)

    # Check if the instance is created successfully
    assert isinstance(handle_api, HandleNetAPI)

    assert handle_api.get_metadata_for_id("kbka-bem9") == api_data_decoded
    assert requested_urls == [
        "https://hdl.handle.net/api/handles/21.T11978/4cat/TEST-D4Y/kbka-bem9"
    ]


def test_pid4cat_record_factory():
    """
    Test the pid4cat_record_factory function.
    """
    with Path("tests/data/21.T11978_hdlnet_api/TEST-D4Y_kbka-bem9_decoded.json").open(
        mode="r", encoding="utf-8"
    ) as f:
        data = json.load(f)

    record = pid4cat_record_factory(data)
    assert isinstance(record, Pid4CatRecord)
    assert record.landing_page_url == "http://Mytest2.com"
