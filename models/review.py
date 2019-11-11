#!/usr/bin/python3
from models.base_model import BaseModel
"""Review module"""


class Review(BaseModel):
    """Review class"""

    def __init__(self, *args, **kwargs):
        """Init"""
        super().__init__(self, *args, **kwargs)
        self.name = kwargs["name"]
        self.place_id = kwargs["place_id"]
        self.user_id = kwargs["user_id"]

    place_id = ''
    user_id = ''
    name = ''
