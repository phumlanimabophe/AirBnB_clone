#!/usr/bin/python3
"""
This is the City module.
"""

# Import the BaseModel class
from models.base_model import BaseModel

# Define the City class that inherits from BaseModel
class City(BaseModel):
    """
    Class representing a City object.
    """
    
    # Attributes for a City
    state_id = ""
    name = ""
