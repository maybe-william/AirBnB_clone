#!/usr/bin/python3
from models.base_model import BaseModel
"""Review module"""


class Review(BaseModel):
    """Review class"""

    def __init__(self, *args, **kwargs):
        """Init"""
        super().__init__(self, *args, **kwargs)
        if "name" in kwargs.keys():
            self.name = kwargs["name"]
        if "place_id" in kwargs.keys():
            self.place_id = kwargs["place_id"]
        if "user_id" in kwargs.keys():
            self.user_id = kwargs["user_id"]

    place_id = ''
    user_id = ''
    name = ''
