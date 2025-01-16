"""Data test."""

import os
import glob
import unittest

from linkml_runtime.loaders import yaml_loader, json_loader
from pid4cat_model.datamodel.pid4cat_model import HandleRecordContainer

ROOT = os.path.join(os.path.dirname(__file__), "..")
DATA_DIR = os.path.join(ROOT, "src", "data", "examples")

EXAMPLE_FILES_YAML = glob.glob(os.path.join(DATA_DIR, "*.yaml"))
EXAMPLE_FILES_JSON = glob.glob(os.path.join(DATA_DIR, "*.json"))


class TestData(unittest.TestCase):
    """Test data and datamodel."""

    def test_yaml_data(self):
        """Yaml data test."""
        for path in EXAMPLE_FILES_YAML:
            obj = yaml_loader.load(path, target_class=HandleRecordContainer)
            assert obj

    def test_json_data(self):
        """Json data test."""
        for path in EXAMPLE_FILES_JSON:
            obj = json_loader.load(path, target_class=HandleRecordContainer)
            assert obj
