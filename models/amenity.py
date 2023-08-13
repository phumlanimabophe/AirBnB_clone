#!/usr/bin/python3
"""The `amenity` module

It defines one class, `Amenity(),
which sub-classes the `BaseModel()` class.`
"""
# Import the necessary base model class
from models.base_model import BaseModel

# Define a class that represents an Amenity and inherits from BaseModel
class Amenity(BaseModel):
    """An amenity provided by a place/house.

    Attributes:
        name    # Name of the amenity
    """
    # Initialize the amenity name as an empty string
    name = ""   