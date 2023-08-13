#!/usr/bin/python3
"""Unit tests for the `state` module.
"""
# Import the 'os' module
import os
# Import the 'unittest' module                  
import unittest  
# Import the 'FileStorage' class from the 'models.engine.file_storage' module          
from models.engine.file_storage import FileStorage 
# Import the 'State' class from the 'models.state' module  
from models.state import State
# Import the 'storage' module from the 'models' package   
from models import storage
# Import the 'datetime' class from the 'datetime' module   
from datetime import datetime   

# Define a class for testing the 'State' class
class TestState(unittest.TestCase):
    """Test cases for the `State` class."""

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
        # Create instances of State class with different parameters
        s1 = State()
        s3 = State("hello", "wait", "in")
        # Construct a key based on the instance's class name and ID
        k = f"{type(s1).__name__}.{s1.id}"
        # Validate instance attribute types and values
        self.assertIsInstance(s1.name, str)
        self.assertEqual(s3.name, "")
        s1.name = "Chicago"
        self.assertEqual(s1.name, "Chicago")
        self.assertIn(k, storage.all())

    # Test method for public instance attributes
    def test_init(self):
        """Test method for public instances"""
        # Create instances of State class
        s1 = State()
        s2 = State(**s1.to_dict())
        # Validate instance attribute types and consistency
        self.assertIsInstance(s1.id, str)
        self.assertIsInstance(s1.created_at, datetime)
        self.assertIsInstance(s1.updated_at, datetime)
        self.assertEqual(s1.updated_at, s2.updated_at)

    # Test method for str representation
    def test_str(self):
        """Test method for str representation"""
        # Create an instance of State class
        s1 = State()
        # Construct the expected string representation
        string = f"[{type(s1).__name__}] ({s1.id}) {s1.__dict__}"
        # Validate the instance's string representation
        self.assertEqual(s1.__str__(), string)

    # Test method for 'save'
    def test_save(self):
        """Test method for save"""
        # Create an instance of State class
        s1 = State()
        # Record the current 'updated_at' attribute value
        old_update = s1.updated_at
        # Call the 'save' method
        s1.save()
        # Validate that 'updated_at' attribute changed
        self.assertNotEqual(s1.updated_at, old_update)

    # Test method for 'to_dict'
    def test_todict(self):
        """Test method for dict"""
        # Create instances of State class
        s1 = State()
        s2 = State(**s1.to_dict())
        # Obtain the dictionary representation using 'to_dict'
        a_dict = s2.to_dict()
        # Validate the dictionary representation
        self.assertIsInstance(a_dict, dict)
        self.assertEqual(a_dict['__class__'], type(s2).__name__)
        self.assertIn('created_at', a_dict.keys())
        self.assertIn('updated_at', a_dict.keys())
        self.assertNotEqual(s1, s2)

# Execute the tests if this script is the main program
if __name__ == "__main__":
    unittest.main()
