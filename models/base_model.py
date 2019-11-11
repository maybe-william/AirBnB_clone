#!/usr/bin/python3
import uuid
from datetime import datetime
"""
    This is the basemodel for the console
    we are currently creating.
"""


class BaseModel():
    """
        BaseModel -
        @attributes
            id - the unique id for the instance
            created_at - the datetime of created instance
            update_at - the datetime of the updated instance
        @methods
            __init__ - initializes the object
            __str__ - prints string rep of instance
            save - updates the update_at
            to_dict - converts instance to dict
    """
    def __init__(self, *args, **kwargs):
        d = datetime.strptime
        if "id" not in kwargs:
            self.id = str(uuid.uuid4())
        else:
            self.id = kwargs["id"]
        if "created_at" not in kwargs:
            self.created_at = datetime.now()
        else:
            self.created_at = d(kwargs["created_at"], '%Y-%m-%dT%H:%M:%S.%f')
        if "update_at" not in kwargs:
            self.update_at = datetime.now()
        else:
            self.update_at = d(kwargs["update_at"], '%Y-%m-%dT%H:%M:%S.%f')

    def __str__(self):
        """ creates a string rep of the instance """
        s = self
        return "[{}] ({}) {}".format(type(s).__name__, s.id, s.__dict__)

    def save(self):
        """ updates the date time for update_at """
        self.update_at = datetime.now()

    def to_dict(self):
        """ converts instance to dictionary """
        __class__ = type(self)
        self.created_at = self.created_at.isoformat("T")
        self.update_at = self.update_at.isoformat("T")
        dic = self.__dict__
        dic["__class__"] = str(type(self).__name__)
        return dic
