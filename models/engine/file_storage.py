#!/usr/bin/python3
"""Define class file storage"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """class FileStorage for serialization and deserialization
    of json file
    """
    __classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "Place": Place,
            "City": City,
            "Amenity": Amenity,
            "Review": Review
            }

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets objects with key"""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        json_obj = {}
        for key in self.__objects:
            json_obj[key] = self.__objects[key].to_dict()

        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(json_obj, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        deserialized = {}
        try:
            with open(self.__file_path, 'r') as f:
                deserialized = json.load(f)
                for x in deserialized.values():
                    name = x["__class__"]
                    del x["__class__"]
                    self.new(eval(name)(**x))
        except FileNotFoundError:
            pass
