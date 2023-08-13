#!/usr/bin/python3
"""Unit tests for the `city` module.
"""
# Import the 'os' module
import os
# Import the 'unittest' module                  
import unittest
# Import the 'FileStorage' class from the 'models.engine.file_storage' module            
from models.engine.file_storage import FileStorage
# Import the 'storage' module from the 'models' package   
from models import storage
# Import the 'City' class from the 'models.city' module   
from models.city import City
# Import the 'datetime' class from the 'datetime' module   
from datetime import datetime   

# Create instances of City class with different parameters
c1 = City()
c2 = City(**c1.to_dict())
c3 = City("hello", "wait", "in")

# Define a class for testing the 'City' class
class TestCity(unittest.TestCase):
    """Test cases for the `City` class."""

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
        # Construct a key based on the instance's class name and ID
        k = f"{type(c1).__name__}.{c1.id}"
        # Validate instance attribute types and values
        self.assertIsInstance(c1.name, str)
        self.assertEqual(c3.name, "")
        c1.name = "Abuja"
        self.assertEqual(c1.name, "Abuja")

    # Test method for public instance attributes
    def test_init(self):
        """Test method for public instances"""
        # Validate instance attribute types and consistency
        self.assertIsInstance(c1.id, str)
        self.assertIsInstance(c1.created_at, datetime)
        self.assertIsInstance(c1.updated_at, datetime)
        self.assertEqual(c1.updated_at, c2.updated_at)

    # Test method for 'save'
    def test_save(self):
        """Test method for save"""
        # Record the current 'updated_at' attribute value
        old_update = c1.updated_at
        # Call the 'save' method
        c1.save()
        # Validate that 'updated_at' attribute changed
        self.assertNotEqual(c1.updated_at, old_update)

    # Test method for 'to_dict'
    def test_todict(self):
        """Test method for dict"""
        # Obtain the dictionary representation using 'to_dict'
        a_dict = c2.to_dict()
        # Validate the dictionary representation
        self.assertIsInstance(a_dict, dict)
        self.assertEqual(a_dict['__class__'], type(c2).__name__)
        self.assertIn('created_at', a_dict.keys())
        self.assertIn('updated_at', a_dict.keys())
        self.assertNotEqual(c1, c2)

# Execute the tests if this script is the main program
if __name__ == "__main__":
    unittest.main()
