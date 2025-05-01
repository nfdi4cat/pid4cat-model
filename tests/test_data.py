import os
import glob

from linkml_runtime.loaders import yaml_loader, json_loader
from pid4cat_model.datamodel.pid4cat_model import HandleAPIRecord, HandleRecordContainer

ROOT = os.path.join(os.path.dirname(__file__), "..")
DATA_DIR = os.path.join(ROOT, "tests", "data", "valid")


def test_yaml_data():
    """Yaml data test."""
    for path in glob.glob(os.path.join(DATA_DIR, "HandleAPIRecord*.yaml")):
        obj = yaml_loader.load(path, target_class=HandleAPIRecord)
        assert obj

    for path in glob.glob(os.path.join(DATA_DIR, "HandleRecordContainer*.yaml")):
        obj = yaml_loader.load(path, target_class=HandleRecordContainer)
        assert obj


def test_json_data():
    """Json data test."""
    for path in glob.glob(os.path.join(DATA_DIR, "HandleAPIRecord*.json")):
        obj = json_loader.load(path, target_class=HandleAPIRecord)
        assert obj
