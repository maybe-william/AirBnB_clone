#!/usr/bin/python3
from models.base_model import BaseModel
"""City module"""


class City(BaseModel):
    """City class"""

    def __init__(self, *args, **kwargs):
        """Init"""
        super().__init__(self, *args, **kwargs)
        if "name" in kwargs.keys():
            self.name = kwargs["name"]
        if "state_id" in kwargs.keys():
            self.state_id = kwargs["state_id"]

    state_id = ''
    name = ''
