#!/usr/bin/python3
"""
This is the state class that represents new states
"""

# Import the BaseModel class
from models.base_model import BaseModel

# Define the State class that inherits from BaseModel
class State(BaseModel):
    """ State subclass that inherits from BaseModel """
    
    # Initialize the 'name' attribute
    name = ""

