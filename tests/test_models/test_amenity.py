#!/usr/bin/python3
"""
Test Module - contains tests for the Amenity class
"""

import unittest
from models.amenity import Amenity
import datetime


class TestAmenity(unittest.TestCase):
    """Defines the tests for the class"""

    @classmethod
    def setUpClass(cls):
        """Sets the objects to be tested"""
        cls.amen1 = Amenity()
        cls.amen1.name = "betty"

    def test_new_instance(self):
        """Tests the creation of a new instance"""
        self.assertIs(type(self.amen1.name), str)
        self.assertIs(type(self.amen1.id), str)
        self.assertIs(type(self.amen1.created_at), datetime.datetime)
        self.assertIs(type(self.amen1.updated_at), datetime.datetime)
