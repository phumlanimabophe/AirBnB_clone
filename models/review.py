#!/usr/bin/python3
"""
This is the review class that represents new reviews
"""

# Import the BaseModel class
from models.base_model import BaseModel

# Define the Review class that inherits from BaseModel
class Review(BaseModel):
    """ Review subclass that inherits from BaseModel """
    
    # Initialize attributes for the review
    place_id = ""
    user_id = ""
    text = ""
