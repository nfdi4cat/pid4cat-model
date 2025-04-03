import json
import logging
import re

import httpx
from dataclasses import dataclass, field

from pydantic import ValidationError

from pid4cat_model.datamodel.pid4cat_model_pydantic import (
    HandleAPIRecord,
    Pid4CatRecord,
)

logger = logging.getLogger(__name__)

# Regex to check if a string is either a json array [...] or a json object {...}
json_str = re.compile(r"(^\{.*\}$)|(^\[.*\]$)")


@dataclass
class HandleConfig:
    """
    Configuration for the HandleNet API client.
    """

    api_url: str = "https://hdl.handle.net/api/handles/"
    prefix: str = "21.T11978"
    ns_suffix: str = "test"
    base_url: str = field(init=False)

    def __post_init__(self):
        self.base_url = f"{self.api_url}{self.prefix}/{self.ns_suffix}/"


class HandleNetAPI:
    """
    Client to retrieve data for pid4cat handles with the HandleNet API.
    """

    def __init__(self, config: HandleConfig, client: httpx.Client):
        """
        Initialize a HandleNetAPI client with the given configuration.
        """
        self.config = config
        self.client = client

    def get_metadata_for_id(self, id_suffix: str) -> dict:
        """
        Load metadata for a given id from HandleNet API or from local file.
        """
        url = f"{self.config.base_url}{id_suffix}"
        response = self.client.get(url)
        data = response.json()
        logger.debug(f"Response: {data}")

        # decode records that contain escaped json syntax
        for rec in data.get("values", []):
            value = rec["data"]["value"].strip()
            if json_str.match(value):
                try:
                    parsed = json.loads(value)
                    rec["data"]["value"] = parsed
                except json.JSONDecodeError as e:
                    print(f"Invalid json! Error: {e}")

        return data


def pid4cat_record_factory(pid_metadata: dict | None) -> Pid4CatRecord:
    """
    Factory function to create a Pid4CatRecord from the API response.
    """
    if pid_metadata is None:
        raise ValueError("pid_metadata is None")
    # First create a HandleAPIRecord instance
    hdl = HandleAPIRecord.model_validate(pid_metadata)
    # Create a Pid4CatRecord instance using the HandleAPIRecord
    data = {}
    for rec in hdl.values:
        match rec.type:
            case "URL":
                data["landing_page_url"] = rec.data.value
            case "EMAIL":
                data["curation_contact"] = rec.data.value
            case "STATUS":
                data["status"] = rec.data.value
            case "SCHEMA_VER":
                data["schema_version"] = rec.data.value
            case "METADATA_LICENSE":
                data["metadata_license"] = rec.data.value
            case "RESOURCE":
                data["resource_info"] = rec.data.value
            case "RELATED":
                data["related_identifiers"] = rec.data.value
            case "CHANGES":
                data["change_log"] = rec.data.value

    try:
        rec = Pid4CatRecord.model_validate(data)
    except ValidationError as e:
        logger.error(f"Validation error: {e}")
        raise
    return rec


if __name__ == "__main__":
    # Set logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    logging.basicConfig(level=logging.INFO)

    config = HandleConfig()
    api = HandleNetAPI(config, client=httpx.Client())
    metadata = api.get_metadata_for_id("KBKA-BEM9")

    print("\nTrying to create a HandleAPIRecord object", end="... ")
    hdl_rec = HandleAPIRecord.model_validate(metadata)
    print("success!")
    print(hdl_rec.model_dump_json(indent=2))

    print("\nTrying to create a Pid4CatRecord object", end="... ")
    pid_rec = pid4cat_record_factory(metadata)
    print("success!")
    print(f"-> Landing page: {pid_rec.landing_page_url}")
