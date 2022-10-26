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
        return self.__objects


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
        try:
            with  open(self.__file_path, 'r') as f:
                json.load(f)
        except:
            pass
