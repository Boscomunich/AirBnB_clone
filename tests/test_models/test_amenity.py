#!/usr/bin/python3
""" Unittest for Amenity class """
import unittest
import json
import os
from models.base_model import BaseModel
from models.amenity import Amenity
from datetime import datetime, timedelta


class TestAmenity(unittest.TestCase):
    """Test case for Amenity class"""
    def setUp(self):
        """SetUp method"""
        self.amenity1 = Amenity()
        self.amenity1.name = "juan"

    def test_docstring(self):
        """test docstring in the file"""
        self.assertIsNotNone(Amenity.__doc__)

    def test_is_instance(self):
        """Test for instantiation"""
        self.assertIsInstance(self.amenity1, Amenity)

    def test_attributes(self):
        """Test to check attributes"""
        self.amenity1.save()
        amenity1_json = self.amenity1.to_dict()
        my_new_amenity = Amenity(**amenity1_json)
        self.assertEqual(my_new_amenity.id, self.amenity1.id)
        self.assertEqual(my_new_amenity.created_at, self.amenity1.created_at)
        self.assertEqual(my_new_amenity.updated_at, self.amenity1.updated_at)
        self.assertIsNot(self.amenity1, my_new_amenity)

    def test_subclass(self):
        """Test to check the inheritance"""
        self.assertTrue(issubclass(self.amenity1.__class__, BaseModel), True)

    def test_save(self):
        """Test to check save method and check if updated_at is updated"""
        self.amenity1.updated_at = datetime.now() - timedelta(days=1)
        variable_update = self.amenity1.updated_at
        self.amenity1.save()
        self.amenity1.updated_at = datetime.now()
        self.amenity1.save()
        self.assertNotEqual(variable_update, self.amenity1.updated_at)

    def test_to_dict(self):
        """Test to check to_dict method"""
        self.amenity1.name = "juan"
        amenity1_dict = self.amenity1.to_dict()
        self.assertEqual(self.amenity1.__class__.__name__, 'Amenity')
        self.assertIsInstance(amenity1_dict['created_at'], str)
        self.assertIsInstance(amenity1_dict['updated_at'], str)
        self.assertIsInstance(amenity1_dict['name'], str)
