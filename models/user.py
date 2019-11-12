#!/usr/bin/python3
from models.base_model import BaseModel
"""User module"""


class User(BaseModel):
    """User class"""

    def __init__(self, *args, **kwargs):
        """Init"""
        super().__init__(self, *args, **kwargs)
        if "first_name" in kwargs.keys():
            self.first_name = kwargs["first_name"]
        if "last_name" in kwargs.keys():
            self.last_name = kwargs["last_name"]
        if "password" in kwargs.keys():
            self.password = kwargs["password"]
        if "email" in kwargs.keys():
            self.email = kwargs["email"]

    email = ''
    password = ''
    first_name = ''
    last_name = ''
