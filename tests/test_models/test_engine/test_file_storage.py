#!/usr/bin/python3
"""
    Test Module - contains tests for the FileStorage class
"""

import unittest
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage

base1 = BaseModel()


class TestFileStorage(unittest.TestCase):
    """Defines the class tests"""

    def test_all(self):
        """ Test all() method """
        self.assertIs(type(storage.all()), dict)

    def test_new(self):
        """ Test new() method """
        key = "{:s}.{:s}".format(base1.__class__.__name__, base1.id)
        self.assertTrue(key in storage.all())

    def test_save(self):
        """ Test save() method """
        json_copy = {}
        obj = storage.all()
        for key in obj:
            json_copy[key] = obj[key].to_dict()
        load = json.dumps(json_copy)
        with open("file.json", "r") as f:
            to_obj = f.read()
        self.assertEqual(json.loads(load), json.loads(to_obj))
