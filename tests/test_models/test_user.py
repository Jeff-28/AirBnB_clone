#!/usr/bin/python3
"""
Test Module - contains tests for the User class
"""

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Defines the tests for the class"""

    @classmethod
    def setUpClass(cls):
        """Sets the objects to be tested"""
        cls.user1 = User(email="betty@holbertonschool.com",
                         password="betty", first_name="Betty",
                         last_name="Holbie")

    def test_new_instance(self):
        """Tests the creation of a new instance"""
        self.assertIs(type(self.user1.email), str)
        self.assertIs(type(self.user1.password), str)
        self.assertIs(type(self.user1.first_name), str)
        self.assertIs(type(self.user1.last_name), str)
        self.assertIs(type(self.user1.id), str)
        self.assertIs(type(self.user1.created_at), str)
