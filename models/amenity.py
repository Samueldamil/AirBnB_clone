#!/usr/bin/python3
"""Defines the class Amenity"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Customizing Amenity class

    Attributes:
        name (str): amenity name
    """
    name = ""
