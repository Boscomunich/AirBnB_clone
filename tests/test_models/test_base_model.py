#!/usr/bin/python3
""" Unittest for BaseModel class """
import unittest
import os
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
"""Test BaseModel class"""
class TestBaseModel(unittest.TestCase):
    """Test class for BaseModel

    Args:
        unittest ([type]): [description]
    """
    def setUp(self):
        """SetUp method"""
        self.bm_instance1 = BaseModel()
        self.bm_instance2 = BaseModel()

    def test_docstring(self):
        """Test docstring"""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_is_instance(self):
        """Test the instance of the class"""
        self.assertIsInstance(self.bm_instance1, BaseModel)
        self.assertIsInstance(self.bm_instance1.created_at, datetime)
        self.assertIsInstance(self.bm_instance1.updated_at, datetime)

    def test_id(self):
        """Test id of the instance"""
        self.assertNotEqual(self.bm_instance1.id, self.bm_instance2.id)
        self.assertTrue(hasattr(self.bm_instance1, "id"))
        self.assertEqual(type(self.bm_instance1.id), str)
        self.assertEqual(type(self.bm_instance2.id), str)

    def test_attributes(self):
        """Test the attr of the instance"""
        self.bm_instance1.name = "Solomon"
        self.bm_instance1.my_number = 46
        self.bm_instance1.save()
        bm_instance1_json = self.bm_instance1.to_dict()
        self.bm_instance2 = BaseModel(**bm_instance1_json)
        self.assertEqual(self.bm_instance2.id, self.bm_instance1.id)
        self.assertEqual(self.bm_instance2.name, self.bm_instance1.name)
        self.assertEqual(self.bm_instance2.my_number, self.bm_instance1.my_number)
