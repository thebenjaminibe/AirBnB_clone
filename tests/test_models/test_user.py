#!/usr/bin/env python3
"""Test model for User class"""

import unittest
import os
from models.user import User
from models.base_model import BaseModel
import uuid


class TestUser(unittest.TestCase):
    """User model class test case"""

    @classmethod
    def setUpClass(cls):
        """Setup the unittest"""
        cls.user = User()
        cls.user.email = "me@example.com"
        cls.user.password = "123i123"
        cls.user.first_name = "John"
        cls.user.last_name = "Swag"

    @classmethod
    def tearDownClass(cls):
        """Clean up the dirt"""
        del cls.user
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_is_subclass(self):
        self.assertTrue(issubclass(self.user.__class__, BaseModel))

    def checking_for_doc(self):
        self.assertIsNotNone(User.__doc__)

    def test_has_attributes(self):
        self.assertTrue('id' in self.user.__dict__)
        self.assertTrue('created_at' in self.user.__dict__)
        self.assertTrue('updated_at' in self.user.__dict__)
        self.assertTrue('email' in self.user.__dict__)
        self.assertTrue('password' in self.user.__dict__)
        self.assertTrue('first_name' in self.user.__dict__)
        self.assertTrue('last_name' in self.user.__dict__)

    def test_attributes_are_string(self):
        self.assertIs(type(self.user.email), str)
        self.assertIs(type(self.user.password), str)
        self.assertIs(type(self.user.first_name), str)
        self.assertIs(type(self.user.last_name), str)

    def test_save(self):
        self.user.save()
        self.assertNotEqual(self.user.created_at, self.user.updated_at)

    def test_to_dict(self):
        self.assertTrue('to_dict' in dir(self.user))


if __name__ == "__main__":
    unittest.main()
