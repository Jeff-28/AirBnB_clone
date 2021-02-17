#!/usr/bin/python3
"""
Test Module - contains tests for the Review class
"""

import unittest
from models.review import Review
import datetime


class TestReview(unittest.TestCase):
    """Defines the tests for the class"""

    @classmethod
    def setUpClass(cls):
        """Sets the objects to be tested"""
        cls.rev1 = Review()
        cls.rev1.name = "betty"

    def test_new_instance(self):
        """Tests the creation of a new instance"""
        self.assertIs(type(self.rev1.name), str)
        self.assertIs(type(self.rev1.id), str)
        self.assertIs(type(self.rev1.created_at), datetime.datetime)
        self.assertIs(type(self.rev1.updated_at), datetime.datetime)
