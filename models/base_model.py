#!/usr/bin/python3
"""Defines class BaseModel"""
from uuid import uuid4
from datetime import datetime
import models
import models.engine


class BaseModel:
    """Represents the BaswModel for AirBnB project"""

    def __init__(self, *args, **kwargs):
        """Initializes a new BaseModel.

        Args:
            *args (any): Unused
            **kwargs (dict): Keys for attributes
        """
        tset = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, w in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(w, tset)
                else:
                    self.__dict__[k] = w

    def save(self):
        """Updates updated_at with current datetime"""
        self.updated_at = datetime.today()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Return the dictionary of the BaseModel instance.

        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        wdict = self.__dict__.copy()
        wdict["created_at"] = self.created_at.isoformat()
        wdict["updated_at"] = self.updated_at.isoformat()
        wdict["__class__"] = self.__class__.__name__
        return wdict

    def __str__(self):
        """Print the string representation of BaseModel"""
        classname = self.__class__.__name__
        return "[{}] ({}) {}".format(classname, self.id, self.__dict__)
