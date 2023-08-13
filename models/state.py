#!/usr/bin/python3
"""The `state` module

It defines one class, `State(),
which sub-classes the `BaseModel()` class.`
"""
# Import the necessary base model class
from models.base_model import BaseModel

# Define a class that represents a State and inherits from BaseModel
class State(BaseModel):
    """A state in the application.

    Attributes:
        name    # Name of the state
    """
    # Initialize the state name as an empty string
    name = ""