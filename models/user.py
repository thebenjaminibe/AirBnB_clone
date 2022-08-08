#!/usr/bin/env python3
"""Module file for `User` class"""

from .base_model import BaseModel


class User(BaseModel):
    """A class that represent a User"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
