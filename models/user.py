#!/usr/bin/python3
"""Define user class"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class tha inherits from BaseModel:
    Attributes:
        email (string): email
        password (string): password
        first_name: first name
        last_name: last name
    """
    email, password, first_name, last_name = "", "", "", ""
