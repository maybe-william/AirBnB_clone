#!/usr/bin/python3
import json
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
        return class(self).__objects

    def new(self, obj):
        """Add a new object into the dict"""
        name = class(obj).__name__()
        class(self).__objects[name + "." + str(obj.id)] = obj

    def save(self):
        """Save all objects in the dict into a file"""
        tempdict = {k: v.to_dict for k, v in class(self).__objects.items()}
        json.dump(tempdict, class(self).__file_path)

    def reload(self):
        """Reload all objects from a file into the dict"""
        tempdict = json.load(class(self).__file_path)
        for k, v in tempdict.items():
            classn = k.split(".")[0]
            class(self).__objects[k] = eval(classn + "(**v)")
