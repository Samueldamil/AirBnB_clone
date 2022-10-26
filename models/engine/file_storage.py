#!/usr/bin/python3
"""Define class file storage"""
import json
from models.base_model import BaseModel


class FileStorage:
    """class FileStorage for serialization and deserialization
    of json file
    """
    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        """returns the dictionary __objects"""
        obj_dict = {}
        for key, value in self.__objects.items():
            if type(value) == BaseModel:
                obj_dict[key] = value
        return obj_dict


    def new(self, obj):
        """sets objects with key"""
        key = obj.__class__.__name__ +"."+ obj.id
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        json_obj = {}
        for key in self.__objects:
            json_obj[key] = self.__objects[key].to_dict()

        with open (self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(json_obj, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        deserialized = {}
        try:
            with  open(self.__file_path, 'r') as f:
                deserialized = json.load(f)
                for x in deserialized.values():
                    name = x["__class__"]
                    del x["__class__"]
                    self.new(eval(name)(**x))
        except FileNotFoundError:
            pass
