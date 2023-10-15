#!/usr/bin/python3
""" Unittest for City class """
import unittest
import json
import os
from models.base_model import BaseModel
from models.city import City
from datetime import datetime, timedelta


class TestCity(unittest.TestCase):
    """Test case for City class"""
    def setUp(self):
        """SetUp method"""
        self.city1 = City()
        self.city1.state_id = "5gfchgcghy"
        self.city1.name = "Yaba"

    def test_docstring(self):
        """test docstring in the file"""
        self.assertIsNotNone(City.__doc__)

    def test_is_instance(self):
        """Test for instantiation"""
        self.assertIsInstance(self.city1, City)

    def test_attributes(self):
        """Test to check attributes"""
        self.city1.save()
        city1_json = self.city1.to_dict()
        my_new_city = City(**city1_json)
        self.assertEqual(my_new_city.id, self.city1.id)
        self.assertEqual(my_new_city.created_at, self.city1.created_at)
        self.assertEqual(my_new_city.updated_at, self.city1.updated_at)
        self.assertIsNot(self.city1, my_new_city)

    def test_subclass(self):
        """Test to check the inheritance"""
        self.assertTrue(issubclass(self.city1.__class__, BaseModel), True)

    def test_save(self):
        """Test to check save method and check if updated_at is updated"""
        self.city1.updated_at = datetime.now() - timedelta(days=1)
        variable_update = self.city1.updated_at
        self.city1.save()
        self.city1.updated_at = datetime.now()
        self.city1.save()
        self.assertNotEqual(variable_update, self.city1.updated_at)

    def test_to_dict(self):
        """test to check to_dict method"""
        self.assertEqual('to_dict' in dir(self.city1), True)
