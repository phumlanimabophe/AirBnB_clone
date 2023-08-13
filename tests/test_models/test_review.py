#!/usr/bin/python3
"""Unit tests for the `review` module.
"""
# Import the 'os' module
import os   
# Import the 'unittest' module               
import unittest
# Import the 'Review' class from the 'models.review' module            
from models.review import Review 
# Import the 'storage' module from the 'models' package  
from models import storage
# Import the 'datetime' class from the 'datetime' module   
from datetime import datetime
# Import the 'FileStorage' class from the 'models.engine.file_storage' module
from models.engine.file_storage import FileStorage   

# Define a class for testing the 'Review' class
class TestReview(unittest.TestCase):
    """Test cases for the `Review` class."""

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
        # Create instances of Review class with different parameters
        r1 = Review()
        r3 = Review("hello", "wait", "in")
        # Construct a key based on the instance's class name and ID
        k = f"{type(r1).__name__}.{r1.id}"
        # Validate instance attribute types and values
        self.assertIsInstance(r1.text, str)
        self.assertIsInstance(r1.user_id, str)
        self.assertIsInstance(r1.place_id, str)
        self.assertEqual(r3.text, "")

    # Test method for public instance attributes
    def test_init(self):
        """Test method for public instances"""
        # Create instances of Review class
        r1 = Review()
        r2 = Review(**r1.to_dict())
        # Validate instance attribute types and consistency
        self.assertIsInstance(r1.id, str)
        self.assertIsInstance(r1.created_at, datetime)
        self.assertIsInstance(r1.updated_at, datetime)
        self.assertEqual(r1.updated_at, r2.updated_at)

    # Test method for str representation
    def test_str(self):
        """Test method for str representation"""
        # Create an instance of Review class
        r1 = Review()
        # Construct the expected string representation
        string = f"[{type(r1).__name__}] ({r1.id}) {r1.__dict__}"
        # Validate the instance's string representation
        self.assertEqual(r1.__str__(), string)

    # Test method for 'save'
    def test_save(self):
        """Test method for save"""
        # Create an instance of Review class
        r1 = Review()
        # Record the current 'updated_at' attribute value
        old_update = r1.updated_at
        # Call the 'save' method
        r1.save()
        # Validate that 'updated_at' attribute changed
        self.assertNotEqual(r1.updated_at, old_update)

    # Test method for 'to_dict'
    def test_todict(self):
        """Test method for dict"""
        # Create instances of Review class
        r1 = Review()
        r2 = Review(**r1.to_dict())
        # Obtain the dictionary representation using 'to_dict'
        a_dict = r2.to_dict()
        # Validate the dictionary representation
        self.assertIsInstance(a_dict, dict)
        self.assertEqual(a_dict['__class__'], type(r2).__name__)
        self.assertIn('created_at', a_dict.keys())
        self.assertIn('updated_at', a_dict.keys())
        self.assertNotEqual(r1, r2)

# Execute the tests if this script is the main program
if __name__ == "__main__":
    unittest.main()
