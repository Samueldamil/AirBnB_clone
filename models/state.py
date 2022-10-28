#!/usr/bin/python3
"""Define class State that inherits BaseModel"""

from models.base_model import BaseModel


class State(BaseModel):
    """Represents a State

    Attributes:
        name (str): name of a state
    """
    name = ""
