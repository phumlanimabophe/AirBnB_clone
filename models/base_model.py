#!/usr/bin/python3
"""
Module: base.py
"""
# Import the 'models' module
import models   
# Import the 'uuid' module
import uuid   
# Import the 'datetime' class from the 'datetime' module      
from datetime import datetime   


# Define a base class that contains common attributes/methods for other classes
class BaseModel():
    """
    Base class which defines all common
    attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        instatiates an object with it's
        attributes
        """
        # If keyword arguments are provided during instantiation
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == "created_at" or key == "updated_at":
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
            return

        # Generate a unique ID using uuid
        self.id = str(uuid.uuid4())
        # Set the creation and update timestamps
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        # Add the new instance to the storage
        models.storage.new(self)

    def __str__(self):
        """
        Returns the string representation
        of the instance
        """
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def save(self):
        """
        updates the public instance attribute
        updated_at with the current datetime
        """
        # Update the 'updated_at' attribute with the current datetime
        self.updated_at = datetime.now()
        # Save the updated information to the storage
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        # Create a dictionary with the instance's attributes
        dict = {**self.__dict__}
        dict['__class__'] = type(self).__name__
        dict['created_at'] = dict['created_at'].isoformat()
        dict['updated_at'] = dict['updated_at'].isoformat()

        return dict
