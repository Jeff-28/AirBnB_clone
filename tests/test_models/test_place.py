#!/usr/bin/python3
"""
Test Module - contains tests for the Place class
"""

import unittest
from models.place import Place
import datetime


class TestState(unittest.TestCase):
    """Defines the tests for the class"""

    @classmethod
    def setUpClass(cls):
        """Sets the objects to be tested"""
        cls.place1 = Place()
        cls.place1.name = "betty"

    def test_new_instance(self):
        """Tests the creation of a new instance"""
        self.assertIs(type(self.place1.name), str)
        self.assertIs(type(self.place1.id), str)
        self.assertIs(type(self.place1.created_at), datetime.datetime)
        self.assertIs(type(self.place1.updated_at), datetime.datetime)
