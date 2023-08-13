#!usr/bin/python3
# Import the necessary base model class
from models.base_model import BaseModel

class User(BaseModel):
    """Creates a new user"""
    # Initialize user email as an empty string
    email = ""
    # Initialize user password as an empty string
    password = ""
    # Initialize user's first name as an empty string
    first_name = ""
    # Initialize user's last name as an empty string
    last_name = ""
