#!/usr/bin/env python3
"""Test module for file storage engine"""

import unittest
from models.base_model import BaseModel
from models import storage
import os

class TestFileStorageEngine(unittest.TestCase):
    """Class for for Unittesting file storage engine"""

    @classmethod
    def setUpClass(cls):
        """Setup the test case"""
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    @classmethod
    def tearDownClass(cls):
        """Cleanup after tests done"""
        try:
            os.remove(storage._FileStorage__file_path)
        except Exception:
            pass

    def test_storage_save_objects(self):
        """Test storage.new method"""
        storage.clear()
        storage.reload()
        objects = storage.all()

        self.assertEqual(len(objects), 0)

        obj1 = BaseModel()
        obj2 = BaseModel()

        obj1.save()
        obj2.save()

        self.assertIs(type(storage.all()), dict)
        self.assertEqual(len(storage.all()), 2)

        storage.reload()
        self.assertEqual(len(storage.all()), 2)
