#!/usr/bin/python3
"""Unit tests for the `city` module.
"""
# Import the 'os' module
import os     
# Import the 'unittest' module             
import unittest    
# Import the 'FileStorage' class from the 'models.engine.file_storage' module        
from models.engine.file_storage import FileStorage   
# Import the 'Place' class from the 'models.place' module
from models.place import Place
# Import the 'storage' module from the 'models' package   
from models import storage   
# Import the 'datetime' class from the 'datetime' module
from datetime import datetime   

# Define a class for testing the 'Place' class
class TestPlace(unittest.TestCase):
    """Test cases for the `Place` class."""

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
        # Create instances of Place class with different parameters
        p1 = Place()
        p3 = Place("hello", "wait", "in")
        # Construct a key based on the instance's class name and ID
        k = f"{type(p1).__name__}.{p1.id}"
        # Validate instance attribute types and presence in storage
        self.assertIsInstance(p1.name, str)
        self.assertIn(k, storage.all())
        self.assertEqual(p3.name, "")

        self.assertIsInstance(p1.name, str)
        self.assertIsInstance(p1.user_id, str)
        self.assertIsInstance(p1.city_id, str)
        self.assertIsInstance(p1.description, str)
        self.assertIsInstance(p1.number_bathrooms, int)
        self.assertIsInstance(p1.number_rooms, int)
        self.assertIsInstance(p1.price_by_night, int)
        self.assertIsInstance(p1.max_guest, int)
        self.assertIsInstance(p1.longitude, float)
        self.assertIsInstance(p1.latitude, float)
        self.assertIsInstance(p1.amenity_ids, list)

    # Test method for public instance attributes
    def test_init(self):
        """Test method for public instances"""
        # Create instances of Place class
        p1 = Place()
        p2 = Place(**p1.to_dict())
        # Validate instance attribute types and consistency
        self.assertIsInstance(p1.id, str)
        self.assertIsInstance(p1.created_at, datetime)
        self.assertIsInstance(p1.updated_at, datetime)
        self.assertEqual(p1.updated_at, p2.updated_at)

    # Test method for str representation
    def test_str(self):
        """Test method for str representation"""
        # Create an instance of Place class
        p1 = Place()
        # Construct the expected string representation
        string = f"[{type(p1).__name__}] ({p1.id}) {p1.__dict__}"
        # Validate the instance's string representation
        self.assertEqual(p1.__str__(), string)

    # Test method for 'save'
    def test_save(self):
        """Test method for save"""
        # Create an instance of Place class
        p1 = Place()
        # Record the current 'updated_at' attribute value
        old_update = p1.updated_at
        # Call the 'save' method
        p1.save()
        # Validate that 'updated_at' attribute changed
        self.assertNotEqual(p1.updated_at, old_update)

    # Test method for 'to_dict'
    def test_todict(self):
        """Test method for dict"""
        # Create instances of Place class
        p1 = Place()
        p2 = Place(**p1.to_dict())
        # Obtain the dictionary representation using 'to_dict'
        a_dict = p2.to_dict()
        # Validate the dictionary representation
        self.assertIsInstance(a_dict, dict)
        self.assertEqual(a_dict['__class__'], type(p2).__name__)
        self.assertIn('created_at', a_dict.keys())
        self.assertIn('updated_at', a_dict.keys())
        self.assertNotEqual(p1, p2)

# Execute the tests if this script is the main program
if __name__ == "__main__":
    unittest.main()
