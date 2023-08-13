#!/usr/bin/python3
"""
This is the Amenity class that represents new amenities.
"""

# Import the BaseModel class
from models.base_model import BaseModel

# Define the Amenity class that inherits from BaseModel
class Amenity(BaseModel):
    """ Amenity subclass that inherits from BaseModel """
    
    # Initialize the 'name' attribute
    name = ""
