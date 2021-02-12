#!/usr/bin/python3
"""
FileStorage Module - serializes instances to a JSON file and deserializes JSON file to instances
"""

import json
from models.base_model import BaseModel


class FileStorage():
    """Defines the attributes and methods for this class"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        json_copy = {}
        for key in self.__objects:
            json_copy[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as myfile:
            json.dump(json_copy, myfile)

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file (__file_path) exists"""
        try:
            with open(self.__file_path, 'r') as myfile:
                obj_dict = json.load(myfile)
            for key, value in obj_dict.items():
                self.__objects[key] = BaseModel(**value)
        except FileNotFoundError:
            pass
