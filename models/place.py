#!/usr/bin/python3
"""
This is the Place module.
"""

# Import the BaseModel class
from models.base_model import BaseModel

# Define the Place class that inherits from BaseModel
class Place(BaseModel):
    """
    Class representing a Place object.
    """
    
    # Attributes for a Place
    city_id = ""
    name = ""
    user_id = ""
    description = ""
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    number_rooms = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

