#!/usr/bin/python3
""" Unittest for Place class """
import unittest
import json
import os
from models.base_model import BaseModel
from models.place import Place
from datetime import datetime, timedelta


class TestPlace(unittest.TestCase):
    """Test case for Place class"""
    def setUp(self):
        """SetUp method"""
        self.place1 = Place()
        self.place1.city_id = "Yaba"
        self.place1.user_id = "5rfy6t7u8i9o"
        self.place1.name = "Lagos"
        self.place1.description = "Apartment"
        self.place1.number_rooms = 2
        self.place1.number_bathrooms = 1
        self.place1.max_guest = 7
        self.place1.price_by_night = 20000
        self.place1.latitude = 6.5
        self.place1.longitude = 33.4
        self.place1.amenity_ids = ["d15s64sd", "4asdad"]

    def test_docstring(self):
        """test docstring in the file"""
        self.assertIsNotNone(Place.__doc__)

    def test_is_instance(self):
        """Test for instantiation"""
        self.assertIsInstance(self.place1, Place)

    def test_attributes(self):
        """Test to check attributes"""
        self.place1.save()
        place1_json = self.place1.to_dict()
        my_new_place = Place(**place1_json)
        self.assertEqual(my_new_place.id, self.place1.id)
        self.assertEqual(my_new_place.created_at, self.place1.created_at)
        self.assertEqual(my_new_place.updated_at, self.place1.updated_at)
        self.assertIsNot(self.place1, my_new_place)

    def test_subclass(self):
        """Test to check the inheritance"""
        self.assertTrue(issubclass(self.place1.__class__, BaseModel), True)

    def test_save(self):
        """Test to check save method and check if updated_at is updated"""
        self.place1.updated_at = datetime.now() - timedelta(days=1)
        variable_update = self.place1.updated_at
        self.place1.save()
        self.place1.updated_at = datetime.now()
        self.place1.save()
        self.assertNotEqual(variable_update, self.place1.updated_at)

    def test_to_dict(self):
        """Test to check to_dict method"""
        self.place1_dict = self.place1.to_dict()
        self.assertIsInstance(self.place1_dict, dict)
        self.assertEqual(type(self.place1_dict['created_at']), str)
        self.assertEqual(type(self.place1_dict['updated_at']), str)
