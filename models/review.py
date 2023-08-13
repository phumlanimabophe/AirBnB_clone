#!/usr/bin/python3
"""The `review` module.

It defines one class, `Review(),
which sub-classes the `BaseModel()` class.`
"""
from models.base_model import BaseModel

class Review(BaseModel):
    """A review of a place/house.

    It represents a review posted by the users
    of the application about a place/house.

    Attributes:
        text        # Text content of the review
        user_id     # ID of the user who posted the review
        place_id    # ID of the place/house being reviewed
    """
    # Initialize the review text as an empty string
    text = ""
    # Initialize the user ID as an empty string
    user_id = ""
    # Initialize the place ID as an empty string
    place_id = ""
