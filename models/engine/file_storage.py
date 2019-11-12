#!/usr/bin/python3
import json
import os
"""File Storage module. Currently to JSON files"""


class FileStorage:
    """Serialize into JSON file"""

    __file_path = "./temp.json"
    __objects = {}

    def __init__(self):
        """Init"""
        pass

    def all(self):
        """Return all objects in dict form"""
        return type(self).__objects

    def new(self, obj):
        """Add a new object into the dict"""
        name = type(obj).__name__
        type(self).__objects[name + "." + str(obj.id)] = obj

    def save(self):
        """Save all objects in the dict into a file"""
        tempdict = {k: v.to_dict() for k, v in type(self).__objects.items()}
        with open(type(self).__file_path, "w+") as f:
            json.dump(tempdict, f)

    def reload(self):
        """Reload all objects from a file into the dict"""
        from models.base_model import BaseModel
        if os.path.exists(type(self).__file_path):
            with open(type(self).__file_path) as f:
                tempdict = json.load(f)
            for k, v in tempdict.items():
                classn = v["__class__"]
                type(self).__objects[k] = eval(classn + "(**v)")
