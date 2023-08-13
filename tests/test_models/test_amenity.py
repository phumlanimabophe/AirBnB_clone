#!/usr/bin/python3
"""Unit tests for the `amenity` module."""
# Import the 'os' module
import os
# Import the 'unittest' module
import unittest
# Import the 'storage' module from the 'models' package
from models import storage
# Import the 'datetime' class from the 'datetime' module
from datetime import datetime
# Import the 'Amenity' class from the 'models.amenity' module
from models.amenity import Amenity
# Import the 'FileStorage' class from the 'models.engine.file_storage' module
from models.engine.file_storage import FileStorage

# Define a class for testing the 'Amenity' class
class TestAmenity(unittest.TestCase):
    """Test cases for the `Amenity` class."""

    # Set up any initial conditions for the tests
    def setUp(self):
        pass

    # Perform cleanup after each test
    def tearDown(self) -> None:
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    # Test method for class attributes
    def test_params(self):
        """Test method for class attributes"""

        # Create instances of Amenity class with different parameters
        a1 = Amenity()
        a2 = Amenity(**a1.to_dict())
        a3 = Amenity("hello", "wait", "in")

        # Construct a key based on the instance's class name and ID
        k = f"{type(a1).__name__}.{a1.id}"
        # Validate instance attribute types and presence in storage
        self.assertIsInstance(a1.name, str)
        self.assertIn(k, storage.all())
        self.assertEqual(a3.name, "")

    # Test method for public instance attributes
    def test_init(self):
        """Test method for public instances"""
        # Create instances of Amenity class
        a1 = Amenity()
        a2 = Amenity(**a1.to_dict())
        # Validate instance attribute types and consistency
        self.assertIsInstance(a1.id, str)
        self.assertIsInstance(a1.created_at, datetime)
        self.assertIsInstance(a1.updated_at, datetime)
        self.assertEqual(a1.updated_at, a2.updated_at)

    # Test method for string representation
    def test_str(self):
        """Test method for str representation"""
        # Create an instance of Amenity class
        a1 = Amenity()
        # Construct the expected string representation
        string = f"[{type(a1).__name__}] ({a1.id}) {a1.__dict__}"
        # Validate the instance's string representation
        self.assertEqual(a1.__str__(), string)

    # Test method for the 'save' method
    def test_save(self):
        """Test method for save"""
        # Create an instance of Amenity class
        a1 = Amenity()
        # Record the current 'updated_at' attribute value
        old_update = a1.updated_at
        # Call the 'save' method
        a1.save()
        # Validate that 'updated_at' attribute changed
        self.assertNotEqual(a1.updated_at, old_update)

    # Test method for the 'to_dict' method
    def test_todict(self):
        """Test method for dict"""
        # Create instances of Amenity class
        a1 = Amenity()
        a2 = Amenity(**a1.to_dict())
        # Obtain the dictionary representation using 'to_dict'
        a_dict = a2.to_dict()
        # Validate the dictionary representation
        self.assertIsInstance(a_dict, dict)
        self.assertEqual(a_dict['__class__'], type(a2).__name__)
        self.assertIn('created_at', a_dict.keys())
        self.assertIn('updated_at', a_dict.keys())
        self.assertNotEqual(a1, a2)

# Execute the tests if this script is the main program
if __name__ == "__main__":
    unittest.main()
