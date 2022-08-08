#!/usr/bin/python3
"""
Instantiation file that starts the file storage system
"""
from models.engine import file_storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review


storage = file_storage.FileStorage()
storage.reload()
