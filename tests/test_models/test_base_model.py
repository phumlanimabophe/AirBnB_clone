"""Testing the `base_model` module."""
# Import the 'json' module
import json   
# Import the 'os' module               
import os    
# Import the 'time' module                
import time 
# Import the 'unittest' module                 
import unittest
# Import the 'uuid' module              
import uuid
# Import the 'datetime' class from the 'datetime' module                  
from datetime import datetime
# Import the 'BaseModel' class from the 'models.base_model' module   
from models.base_model import BaseModel
# Import the 'FileStorage' class from the 'models.engine.file_storage' module   
from models.engine.file_storage import FileStorage   

# Define a class for testing the 'BaseModel' class
class TestBase(unittest.TestCase):
    """Test cases for the `Base` class."""

    # Set up any initial conditions for the tests
    def setUp(self):
        pass

    # Perform cleanup after each test
    def tearDown(self) -> None:
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    # Test passing cases 'BaseModel' initialization
    def test_initialization_positive(self):
        """Test passing cases `BaseModel` initialization."""
        # Create instances of BaseModel class with different parameters
        b1 = BaseModel()
        b2_uuid = str(uuid.uuid4())
        b2 = BaseModel(id=b2_uuid, name="The weeknd", album="Trilogy")
        # Validate instance attribute types and values
        self.assertIsInstance(b1.id, str)
        self.assertIsInstance(b2.id, str)
        self.assertEqual(b2_uuid, b2.id)
        self.assertEqual(b2.album, "Trilogy")
        self.assertEqual(b2.name, "The weeknd")
        self.assertIsInstance(b1.created_at, datetime)
        self.assertIsInstance(b1.created_at, datetime)
        self.assertEqual(str(type(b1)), "<class 'models.base_model.BaseModel'>")

    # Test method for dict
    def test_dict(self):
        """Test method for dict"""
        # Create instances of BaseModel class with different parameters
        b1 = BaseModel()
        b2_uuid = str(uuid.uuid4())
        b2 = BaseModel(id=b2_uuid, name="The weeknd", album="Trilogy")
        # Obtain the dictionary representation using 'to_dict'
        b1_dict = b1.to_dict()
        # Validate the dictionary representation
        self.assertIsInstance(b1_dict, dict)
        self.assertIn('id', b1_dict.keys())
        self.assertIn('created_at', b1_dict.keys())
        self.assertIn('updated_at', b1_dict.keys())
        self.assertEqual(b1_dict['__class__'], type(b1).__name__)
        # Test that 'to_dict' fails due to excess arguments
        with self.assertRaises(KeyError) as e:
            b2.to_dict()

    # Test method for 'save'
    def test_save(self):
        """Test method for save"""
        # Create an instance of BaseModel class
        b = BaseModel()
        # Pause for a short time
        time.sleep(0.5)
        # Record the current time
        date_now = datetime.now()
        # Call the 'save' method
        b.save()
        # Calculate the time difference and validate it
        diff = b.updated_at - date_now
        self.assertTrue(abs(diff.total_seconds()) < 0.01)

    # Test that 'storage.save()' is called from 'save()'
    def test_save_storage(self):
        """Tests that storage.save() is called from save()."""
        # Create an instance of BaseModel class
        b = BaseModel()
        # Call the 'save' method
        b.save()
        key = "{}.{}".format(type(b).__name__, b.id)
        d = {key: b.to_dict()}
        # Validate the existence and content of the storage file
        self.assertTrue(os.path.isfile(FileStorage._FileStorage__file_path))
        with open(FileStorage._FileStorage__file_path, "r", encoding="utf-8") as f:
            self.assertEqual(len(f.read()), len(json.dumps(d)))
            f.seek(0)
            self.assertEqual(json.load(f), d)

    # Test 'save' with no arguments
    def test_save_no_args(self):
        """Tests save() with no arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            BaseModel.save()
        msg = "save() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    # Test 'save' with too many arguments
    def test_save_excess_args(self):
        """Tests save() with too many arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            BaseModel.save(self, 98)
        msg = "save() takes 1 positional argument but 2 were given"
        self.assertEqual(str(e.exception), msg)

    # Test method for str representation
    def test_str(self):
        """Test method for str representation"""
        # Create an instance of BaseModel class
        b1 = BaseModel()
        # Construct the expected string representation
        string = f"[{type(b1).__name__}] ({b1.id}) {b1.__dict__}"
        # Validate the instance's string representation
        self.assertEqual(b1.__str__(), string)

# Execute the tests if this script is the main program
if __name__ == "__main__":
    unittest.main()
