#!/usr/bin/env python3
"""`BaseModel` class module that defines all common attributs/methods
for other classes
"""
from uuid import uuid4
from datetime import datetime, timezone
import models


class BaseModel:
    """The base model class"""
    def __init__(self, *args, **kwargs):
        """Initialize an instance of `BaseModel` class

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """

        for attr_name, attr_value in kwargs.items():
            if attr_name == "__class__":
                continue
            if attr_name in ('created_at', 'updated_at'):
                attr_value = datetime.fromisoformat(attr_value)
            setattr(self, attr_name, attr_value)

        if not kwargs:
            self.id = str(uuid4())
            now = datetime.now(timezone.utc)
            self.created_at = now
            self.updated_at = now
            models.storage.new(self)

    def __str__(self):
        """Returns a string representation of `BaseModel` instance"""
        s = "[{}] ({}) {}"
        s = s.format(self.__class__.__name__, self.id, str(self.__dict__))
        return s

    def save(self):
        """
        Updates the public instance method updated_at with current datetime
        """
        self.updated_at = datetime.now(timezone.utc).isoformat()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionnary containing all keys/values of __dict__ """
        r = {}
        r["__class__"] = self.__class__.__name__

        for k, v in self.__dict__.items():
            if type(v) is datetime:
                r[k] = v.isoformat()
            else:
                r[k] = v
        return (r)
