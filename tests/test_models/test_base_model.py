#!/usr/bin/python3
"""
Test Module - contains tests for the BaseModel class
"""

from models.base_model import BaseModel
import unittest


class TestBaseModel(unittest.TestCase):
    """Defines the class tests"""

    @classmethod
    def setUpClass(cls):
        """Defines class objects before running tests"""
        cls.base1 = BaseModel()

    def test_new_instance(self):
        """Tests the creation of new instance"""
        self.assertIs(type(self.base1.id), str)

    def test_str(self):
        """Tests the string representation of the object"""
        expected = "[BaseModel] ({}) {}".format(self.base1.id,
                                                self.base1.__dict__)
        self.assertEqual(str(self.base1), expected)

    def test_to_dict(self):
        """Tests to_dict method"""
        dic = self.base1.to_dict()
        self.assertIs(type(dic), dict)
        self.assertTrue('__class__' in dic)
        self.assertIs(type(dic['created_at']), str)
        self.assertIs(type(dic['updated_at']), str)
