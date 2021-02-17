#!/usr/bin/python3
"""
Test Module - contains tests for the Test class
"""

import unittest
from models.city import City
import datetime


class TestState(unittest.TestCase):
    """Defines the tests for the class"""

    @classmethod
    def setUpClass(cls):
        """Sets the objects to be tested"""
        cls.city1 = City()
        cls.city1.name = "betty"

    def test_new_instance(self):
        """Tests the creation of a new instance"""
        self.assertIs(type(self.city1.name), str)
        self.assertIs(type(self.city1.id), str)
        self.assertIs(type(self.city1.created_at), datetime.datetime)
        self.assertIs(type(self.city1.updated_at), datetime.datetime)
