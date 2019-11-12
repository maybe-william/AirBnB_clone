#!/usr/bin/python3
from models.base_model import BaseModel
"""State module"""


class State(BaseModel):
    """State class"""

    def __init__(self, *args, **kwargs):
        """Init"""
        super().__init__(self, *args, **kwargs)
        if "name" in kwargs.keys():
            self.name = kwargs["name"]

    name = ''
