#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from datetime import datetime
"""Test BaseModel class"""

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        """Set up test methods"""
        self.model = BaseModel()

    def test_init_with_kwargs(self):
        """Test __init__ method with kwargs"""
        created_at = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')
        updated_at = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')
        model = BaseModel(id="123", created_at=created_at, updated_at=updated_at)
        self.assertEqual(model.id, "123")
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_init_with_no_kwargs(self):
        """Test __init__ method with no kwargs"""
        model = BaseModel()
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_to_dict_with_no_args(self):
        """Test to_dict method with no arguments"""
        model_dict = self.model.to_dict()
        self.assertEqual(model_dict['id'], self.model.id)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)

    def test_save_with_no_changes(self):
        """Test save method with no changes"""
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertEqual(old_updated_at, self.model.updated_at)

    def test_str_method(self):
        """Test __str__ method"""
        string = str(self.model)
        self.assertIsInstance(string, str)
        self.assertIn('BaseModel', string)
        self.assertIn('id', string)
        self.assertIn('created_at', string)
        self.assertIn('updated_at', string)

    def test_to_dict_method(self):
        """Test to_dict method"""
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertIn('__class__', model_dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
