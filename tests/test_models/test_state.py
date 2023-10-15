#!/usr/bin/python3
""" Unittest for State class """
import unittest
import json
import os
from models.base_model import BaseModel
from models.state import State
from datetime import datetime, timedelta


class TestState(unittest.TestCase):
    """Test case for the State class"""
    def setUp(self):
        """SetUp method"""
        self.state1 = State()
        self.state1.name = "Lagos"

    def test_docstring(self):
        """test docstring in the file"""
        self.assertIsNotNone(State.__doc__)

    def test_is_instance(self):
        """Test for instantiation"""
        self.assertIsInstance(self.state1, State)

    def test_attributes(self):
        """Test to check attributes"""
        self.state1.save()
        state1_json = self.state1.to_dict()
        my_new_state = State(**state1_json)
        self.assertEqual(my_new_state.id, self.state1.id)
        self.assertEqual(my_new_state.created_at, self.state1.created_at)
        self.assertEqual(my_new_state.updated_at, self.state1.updated_at)
        self.assertIsNot(self.state1, my_new_state)

    def test_subclass(self):
        """Test to check the inheritance"""
        self.assertTrue(issubclass(self.state1.__class__, BaseModel), True)

    def test_save(self):
        """Test to check save method and check if updated_at is updated"""
        self.state1.updated_at = datetime.now() - timedelta(days=1)
        variable_update = self.state1.updated_at
        self.state1.save()
        self.state1.updated_at = datetime.now()
        self.state1.save()
        self.assertNotEqual(variable_update, self.state1.updated_at)

    def test_to_dict(self):
        """test to check to_dict method"""
        self.assertEqual('to_dict' in dir(self.state1), True)
