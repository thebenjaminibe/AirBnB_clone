#!/usr/bin/python3
"""
Serializes instances to a JSON file and
deserializes JSON file to instances.
"""

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage():
    """The file storage engine class"""

    __file_path = "file.json"
    __objects = dict()

    @classmethod
    def clear(cls):
        """clear the storage. A helper method for unittesting"""
        if os.path.exists(cls.__file_path):
            os.remove(cls.__file_path)
        cls.__objects = dict()

    def all(self):
        """Returns the dictionary __objects."""
        return (FileStorage.__objects)

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id.

        Args:
            obj (an object)
        """
        if obj.id in FileStorage.__objects:
            print("exists")
            return
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file __file_path."""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump([o.to_dict() for o in self.all().values()], f)

    def reload(self):
        """Deserializes the JSON file to __objects
        only if the JSON file exists."""
        if not os.path.exists(FileStorage.__file_path):
            return

        obj_kwargs = []
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            obj_kwargs = json.load(f)

        """ Reloading """
        for obj_kwarg in obj_kwargs:
            kclass = globals().get(obj_kwarg['__class__'])
            self.new(kclass(**obj_kwarg))
