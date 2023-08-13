#!/usr/bin/python3
"""
This is the base model that contains serial/deserial information
"""
# Import the datetime module
from datetime import datetime

# Import the uuid module
import uuid

# Import the storage module from the 'models' package
from models import storage

# Define the BaseModel class
class BaseModel():
    """ Defines all common attributes/methods for other classes """

    # Constructor method
    def __init__(self, *args, **kwargs):
        """ Initializes the instances attributes """
        if kwargs:
            # Define the date format
            date_format = "%Y-%m-%dT%H:%M:%S.%f"

            # Create a copy of the kwargs dictionary
            k_dict = kwargs.copy()

            # Remove the '__class__' key from the dictionary
            del k_dict["__class__"]

            # Convert datetime strings to datetime objects
            for key in k_dict:
                if (key == "created_at" or key == "updated_at"):
                    k_dict[key] = datetime.strptime(k_dict[key], date_format)

            # Update the instance's dictionary with the modified dictionary
            self.__dict__ = k_dict
        else:
            # Generate a unique ID using uuid
            self.id = str(uuid.uuid4())

            # Set 'created_at' to the current datetime
            self.created_at = datetime.today()

            # Set 'updated_at' to the current datetime
            self.updated_at = datetime.today()

            # Add the instance to the storage
            storage.new(self)

    # String representation method
    def __str__(self):
        """ Prints object in friendly format"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    # Save method
    def save(self):
        """ Updates update_at """
        # Update 'updated_at' to the current datetime
        self.updated_at = datetime.today()

        # Save changes to the storage
        storage.save()

    # to_dict method
    def to_dict(self):
        """ Generate a new dict with an extra field __class__ """
        # Create a copy of the instance's dictionary
        new_dict = self.__dict__.copy()

        # Add '__class__' key with class name
        new_dict["__class__"] = self.__class__.__name__

        # Convert 'created_at' to ISO format
        new_dict["created_at"] = self.created_at.isoformat()

        # Convert 'updated_at' to ISO format
        new_dict["updated_at"] = self.updated_at.isoformat()

        # Return the modified dictionary
        return new_dict

