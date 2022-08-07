#!/usr/bin/env python3
"""Test model for Review class"""

import unittest
import os
from models.review import Review
from models.base_model import BaseModel
import uuid


class TestReview(unittest.TestCase):
    """Review model class test case"""

    @classmethod
    def setUpClass(cls):
        """Setup the unittest"""
        cls.review = Review()
        cls.review.user_id = str(uuid.uuid4())
        cls.review.place_id = str(uuid.uuid4())
        cls.review.text = "St. Petesburg"

    @classmethod
    def tearDownClass(cls):
        """Clean up the dirt"""
        del cls.review
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_is_subclass(self):
        self.assertTrue(issubclass(self.review.__class__, BaseModel))

    def checking_for_doc(self):
        self.assertIsNotNone(Review.__doc__)

    def test_has_attributes(self):
        self.assertTrue('id' in self.review.__dict__)
        self.assertTrue('created_at' in self.review.__dict__)
        self.assertTrue('updated_at' in self.review.__dict__)
        self.assertTrue('user_id' in self.review.__dict__)
        self.assertTrue('place_id' in self.review.__dict__)
        self.assertTrue('text' in self.review.__dict__)

    def test_attributes_are_string(self):
        self.assertIs(type(self.review.user_id), str)
        self.assertIs(type(self.review.place_id), str)
        self.assertIs(type(self.review.text), str)

    def test_save(self):
        self.review.save()
        self.assertNotEqual(self.review.created_at, self.review.updated_at)

    def test_to_dict(self):
        self.assertTrue('to_dict' in dir(self.review))


if __name__ == "__main__":
    unittest.main()
