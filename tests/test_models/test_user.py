#!/usr/bin/python3
""" Unittest for User class """
import unittest
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage
from datetime import datetime, timedelta


class TestUser(unittest.TestCase):
    """Test case for User class"""
    def setUp(self):
        """Method to set the environment"""
        self.user1 = User()
        self.user1.email = "solomonodunusi@gmail.com"
        self.user1.password = "qwerty12345"
        self.user1.first_name = "Solomon"
        self.user1.last_name = "Odunusi"

    def test_docstring(self):
        """Test docstring in the file"""
        self.assertIsNotNone(User.__doc__)

    def test_is_instance(self):
        """Test for instantiation"""
        self.assertIsInstance(self.user1, User)

    def test_attributes(self):
        """Test to check attr"""
        self.user1.save()
        user1_json = self.user1.to_dict()
        my_new_user = User(**user1_json)
        self.assertEqual(my_new_user.id, self.user1.id)
        self.assertEqual(my_new_user.created_at, self.user1.created_at)
        self.assertEqual(my_new_user.updated_at, self.user1.updated_at)
        self.assertIsNot(self.user1, my_new_user)

    def test_subclass(self):
        """Test to check the inheritance"""
        self.assertTrue(issubclass(self.user1.__class__, BaseModel), True)

    def test_save(self):
        """Test to check save method"""
        self.user1.updated_at = datetime.now() - timedelta(days=1)
        variable_update = self.user1.updated_at
        self.user1.save()
        self.user1.updated_at = datetime.now()
        self.user1.save()
        self.assertNotEqual(variable_update, self.user1.updated_at)

    def test_password(self):
        """Test password"""
        self.assertEqual(self.user1.password, "qwerty12345")


if __name__ == '__main__':
    unittest.main()
