#!/usr/bin/python3
"""Define city class"""
from models.base_model import BaseModel


class City(BaseModel):
    """Represent a City
    Attributes:
        state_id (str): The state id
        name (str): The name of the City
    """
    state_id = ""
    name = ""
