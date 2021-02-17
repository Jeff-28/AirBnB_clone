#!/usr/bin/python3
"""
Test Module - contains tests for the Test class
"""

import unittest
from models.state import State
import datetime


class TestState(unittest.TestCase):
    """Defines the tests for the class"""

    @classmethod
    def setUpClass(cls):
        """Sets the objects to be tested"""
        cls.state1 = State()

    def test_new_instance(self):
        """Tests the creation of a new instance"""
        self.assertIs(type(self.state1.id), str)
        self.assertIs(type(self.state1.created_at), datetime.datetime)
        self.assertIs(type(self.state1.updated_at), datetime.datetime)
