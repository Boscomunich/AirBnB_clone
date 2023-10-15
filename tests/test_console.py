#!/usr/bin/python3
"""Unittest for Airbnb console"""
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """Test class for console"""
    def setUp(self):
        """SetUp method"""
        self.console = HBNBCommand()

    def tearDown(self):
        """TearDown method"""
        pass

    def test_create(self):
        """Test create method"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            self.assertTrue(len(f.getvalue().strip()) == 36)

    def test_show(self):
        """Test show method"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            self.console.onecmd("show BaseModel {}".format(obj_id))
            self.assertTrue(obj_id in f.getvalue())

    def test_destroy(self):
        """Test destroy method"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            self.console.onecmd("destroy BaseModel {}".format(obj_id))
            self.console.onecmd("show BaseModel {}".format(obj_id))
            self.assertTrue("** no instance found **" in f.getvalue())

    def test_all(self):
        """Test all method"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            self.console.onecmd("create User")
            self.console.onecmd("all")
            self.assertTrue("BaseModel" in f.getvalue())
            self.assertTrue("User" in f.getvalue())

    def test_update(self):
        """Test update method"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            self.console.onecmd(
                    "update BaseModel {} name 'test'".format(obj_id))
            self.console.onecmd("show BaseModel {}".format(obj_id))
            self.assertTrue("test" in f.getvalue())

    def test_count(self):
        """Test count method"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            self.console.onecmd("create BaseModel")
            self.console.onecmd("create BaseModel")
            self.console.onecmd("count BaseModel")
            self.assertTrue("3" in f.getvalue())


if __name__ == '__main__':
    unittest.main()
