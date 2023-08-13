#!/usr/bin/python3
"""Defines unittests for models/engine/file_storage.py.
Unittest classes:
    TestFileStorage_instantiation
    TestFileStorage_methods
"""
# Import necessary modules

# Import the 'os' module for operating system-related functionality
import os

# Import the 'models' module (assuming it contains various classes)
import models

# Import the 'unittest' module for unit testing functionality
import unittest

# Import specific classes from different modules within the 'models' package
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


# Define a test class for testing FileStorage instantiation
class TestFileStorage_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the FileStorage class."""

    # Test instantiation of FileStorage with no arguments
    def test_FileStorage_instantiation_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    # Test instantiation of FileStorage with an argument
    def test_FileStorage_instantiation_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    # Test that the file path attribute is a private string
    def test_FileStorage_file_path_is_private_str(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    # Test that the objects attribute is a private dictionary
    def testFileStorage_objects_is_private_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    # Test that the models.storage attribute is an instance of FileStorage
    def test_storage_initializes(self):
        self.assertEqual(type(models.storage), FileStorage)

# Define a test class for testing FileStorage methods
class TestFileStorage_methods(unittest.TestCase):
    """Unittests for testing methods of the FileStorage class."""

    # Set up the test environment (not implemented here)
    def setUp(self):
        pass

    # Teardown the test environment and reset FileStorage data
    def tearDown(self) -> None:
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    # Test the 'all' method of models.storage
    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))

    # Test the 'all' method of models.storage with an argument
    def test_all_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    # Test the 'new' method of models.storage
    def test_new(self):
        # Create instances of various classes
        bm = BaseModel()
        us = User()
        st = State()
        pl = Place()
        cy = City()
        am = Amenity()
        rv = Review()

        # Add instances to storage and check their presence
        models.storage.new(bm)
        models.storage.new(us)
        # ... (similar lines for other instances)
        self.assertIn("BaseModel." + bm.id, models.storage.all().keys())
        self.assertIn(bm, models.storage.all().values())
        # ... (similar lines for other instances)

    # Test the 'new' method of models.storage with arguments
    def test_new_with_args(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    # Test the 'new' method of models.storage with None
    def test_new_with_None(self):
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    # Test the 'save' method of models.storage
    def test_save(self):
        # Create instances and add them to storage
        # ... (similar lines as in the 'test_new' method)
        models.storage.save()

        # Check if instances are saved in the file
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            # ... (similar lines to check for each instance)

    # Test the 'save' method of models.storage with an argument
    def test_save_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)

    # Test the 'reload' method of models.storage
    def test_reload(self):
        # Create instances, add them to storage, save and reload
        # ... (similar lines as in the 'test_save' method)
        models.storage.reload()

        # Check if instances are reloaded
        objs = FileStorage._FileStorage__objects
        # ... (similar lines to check for each instance)

    # Test the 'reload' method of models.storage with an argument
    def test_reload_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)

# Entry point for running the unittests
if __name__ == "__main__":
    unittest.main()

