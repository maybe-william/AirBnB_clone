#!/usr/bin/python3
from models.base_model import BaseModel
"""User module"""


class User(BaseModel):
    """User class"""

    def __init__(self, *args, **kwargs):
        """Init"""
        super().__init__(self, *args, **kwargs)
        self.first_name = kwargs["first_name"]
        self.last_name = kwargs["last_name"]
        self.password = kwargs["password"]
        self.email = kwargs["email"]

    email = ''
    password = ''
    first_name = ''
    last_name = ''
