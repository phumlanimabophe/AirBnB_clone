#!/usr/bin/python3
"""
Module: file_storage.py

Defines a `FileStorage` class.
"""

# Import necessary modules and classes
# Import the 'os' module
import os
# Import the 'json' module         
import json
# Import the 'BaseModel' class
from models.base_model import BaseModel
# Import the 'User' class
from models.user import User
# Import the 'State' class              
from models.state import State
# Import the 'City' class             
from models.city import City
# Import the 'Review' class               
from models.review import Review
# Import the 'Amenity' class           
from models.amenity import Amenity
# Import the 'Place' class         
from models.place import Place             

# Define a class for serializing instances to a JSON file and deserializing JSON file to instances
class FileStorage():
    """
    serializes instances to a JSON file and
    deserializes JSON file to instances
    """

    __file_path = "file.json"    # Path to the JSON file
    __objects = {}               # Dictionary to store objects

    def all(self):
        """
        returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        # Open the JSON file in write mode
        with open(FileStorage.__file_path, 'w') as f:
            # Serialize objects to JSON and write to the file
            json.dump(
                {k: v.to_dict() for k, v in FileStorage.__objects.items()}, f)

    def reload(self):
        """
        deserializes the JSON file to __objects only if the JSON
        file exists; otherwise, does nothing
        """
        # Dictionary mapping class names to their respective classes
        current_classes = {'BaseModel': BaseModel, 'User': User,
                           'Amenity': Amenity, 'City': City, 'State': State,
                           'Place': Place, 'Review': Review}

        # Check if the JSON file exists
        if not os.path.exists(FileStorage.__file_path):
            return

        # Open the JSON file in read mode
        with open(FileStorage.__file_path, 'r') as f:
            deserialized = None

            try:
                # Attempt to load the JSON data from the file
                deserialized = json.load(f)
            except json.JSONDecodeError:
                pass

            # If deserialization was successful, update __objects
            if deserialized is None:
                return

            # Populate __objects with deserialized instances
            FileStorage.__objects = {
                k: current_classes[k.split('.')[0]](**v)
                for k, v in deserialized.items()}