#!/usr/bin/env python3
"""`Review` class module"""

from .base_model import BaseModel


class Review(BaseModel):
    """A class that represent a review"""
    place_id = ""
    user_id = ""
    text = ""
