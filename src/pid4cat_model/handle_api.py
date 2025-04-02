import json
import logging
import re

import httpx
from dataclasses import dataclass, field

from pid4cat_model.datamodel.pid4cat_model_pydantic import (
    HandleAPIRecord,
    Pid4CatRecord,
)


logger = logging.getLogger(__name__)

# Regex to check if a string could be a json array [...] or json object {...}
json_str = re.compile(r"(^\{.*\}$)|(^\[.*\]$)")


@dataclass
class HandleConfig:
    api_url: str = "https://hdl.handle.net/api/handles/"
    prefix: str = "21.T11978"
    ns_suffix: str = "test"
    base_url: str = field(init=False)

    def __post_init__(self):
        self.base_url = f"{self.api_url}{self.prefix}/{self.ns_suffix}/"


# TODO Removed function after the record is corrected.
def fix_record_bug(parsed):
    """Fix media_type in the metadata"""
    if "representation_variants" in parsed:
        for i, el in enumerate(parsed["representation_variants"]):
            if el.get("media_type", "") == "textturtle":
                parsed["representation_variants"][i]["media_type"] = "text/turtle"
    return parsed


class HandleNetAPI:
    def __init__(self, config: HandleConfig):
        self.config = config
        self.client = httpx.Client()
        self.metadata = None

    def get_metadata_for_id(self, id_suffix: str):
        url = f"{self.config.base_url}{id_suffix}"
        response = self.client.get(url)
        data = response.json()
        logger.debug(f"Response: {data}")
        # decode strings containing json
        for rec in data.get("values", []):
            value = rec["data"]["value"].strip()
            if json_str.match(value):
                try:
                    parsed = json.loads(value)
                    # TODO Removed after the record is corrected.
                    if id_suffix == "KBKA-BEM9":
                        parsed = fix_record_bug(parsed)
                    rec["data"]["value"] = parsed
                except json.JSONDecodeError as e:
                    print(f"Invalid json! Error: {e}")
        self.metadata = data


class Pid4CatMetaData(Pid4CatRecord):
    pass


if __name__ == "__main__":
    config = HandleConfig()
    print(config.base_url)
    api = HandleNetAPI(config)
    api.get_metadata_for_id("KBKA-BEM9")
    rec = HandleAPIRecord.model_validate(api.metadata)
    print(rec.model_dump_json(indent=2))
