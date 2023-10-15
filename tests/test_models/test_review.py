#!/usr/bin/python3
""" Unittest for Review class """
import unittest
import json
import os
from models.base_model import BaseModel
from models.review import Review
from datetime import datetime, timedelta


class TestReview(unittest.TestCase):
    """Test case for the Review class"""
    def setUp(self):
        """SetUp method"""
        self.review1 = Review()
        self.review1.place_id = "ad45ad61as6d1"
        self.review1.user_id = "yt33t3tg4vhg43"
        self.review1.text = "That place is awesome"

    def test_docstring(self):
        """test docstring in the file"""
        self.assertIsNotNone(Review.__doc__)

    def test_is_instance(self):
        """Test for instantiation"""
        self.assertIsInstance(self.review1, Review)

    def test_attributes(self):
        """Test to check attributes"""
        self.review1.save()
        review1_json = self.review1.to_dict()
        my_new_review = Review(**review1_json)
        self.assertEqual(my_new_review.id, self.review1.id)
        self.assertEqual(my_new_review.created_at, self.review1.created_at)
        self.assertEqual(my_new_review.updated_at, self.review1.updated_at)
        self.assertIsNot(self.review1, my_new_review)

    def test_subclass(self):
        """Test to check the inheritance"""
        self.assertTrue(issubclass(self.review1.__class__, BaseModel), True)

    def test_save(self):
        """Test to check save method and check if updated_at is updated"""
        self.review1.updated_at = datetime.now() - timedelta(days=1)
        variable_update = self.review1.updated_at
        self.review1.save()
        self.review1.updated_at = datetime.now()
        self.review1.save()
        self.assertNotEqual(variable_update, self.review1.updated_at)

    def test_to_dict(self):
        """test to check to_dict method"""
        self.assertEqual('to_dict' in dir(self.review1), True)
