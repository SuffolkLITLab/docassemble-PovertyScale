# do not pre-load

import runpy
import sys
import unittest
from types import ModuleType
from unittest.mock import patch

from flask import Flask
import docassemble.webapp

# Load dependencies before patching sys.modules so they remain cached afterward.
from . import poverty


class TestAppCompatibility(unittest.TestCase):
    def test_routes_with_old_and_new_docassemble_app_names(self):
        for attribute in ("app", "flaskapp"):
            with self.subTest(attribute=attribute):
                app = Flask(attribute)
                app_object = ModuleType("docassemble.webapp.app_object")
                setattr(app_object, attribute, app)
                with patch.object(docassemble.webapp, "app_object", app_object, create=True):
                    with patch.dict(sys.modules, {"docassemble.webapp.app_object": app_object}):
                        runpy.run_module("docassemble.PovertyScale.poverty_endpoint")

                client = app.test_client()
                response = client.get("/poverty_guidelines")
                self.assertEqual(response.status_code, 200)
                self.assertEqual(response.get_json(), poverty.get_poverty_scale_data())

                response = client.get("/poverty_guidelines/household_size/1")
                self.assertEqual(response.status_code, 200)
                self.assertEqual(
                    response.get_json()["amount"], poverty.poverty_scale_get_income_limit(1)
                )

                response = client.get("/poverty_guidelines/qualifies/household_size/1?income=0")
                self.assertEqual(response.status_code, 200)
                self.assertTrue(response.get_json()["qualifies"])
