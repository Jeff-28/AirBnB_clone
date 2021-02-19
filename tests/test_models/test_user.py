#!/usr/bin/python3
"""
Test Module - contains tests for the User class
"""

import unittest
from models.user import User
from models.base_model import BaseModel


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

    def test_inheritance(self):
        """Tests that user inherits from BaseModel"""
        user = User()
        self.assertIsInstance(user, BaseModel)
        self.assertTrue(hasattr(user, "id"))
        self.assertTrue(hasattr(user, "created_at"))
        self.assertTrue(hasattr(user, "updated_at"))
