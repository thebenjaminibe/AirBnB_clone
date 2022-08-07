#!/usr/bin/env python3
"""`City` class module"""

from .base_model import BaseModel


class City(BaseModel):
    """A class that represent a city"""
    state_id = ""
    name = ""
