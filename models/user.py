#!/usr/bin/python3
"""
User Module - contains the User class with its attributes/methods
"""

from models.base_model import BaseModel


class User(BaseModel):
    """Inherits from BaseModel class"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
