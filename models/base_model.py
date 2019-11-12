#!/usr/bin/python3
import uuid
from datetime import datetime
from models import storage
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
            updated_at - the datetime of the updated instance
        @methods
            __init__ - initializes the object
            __str__ - prints string rep of instance
            save - updates the update_at
            to_dict - converts instance to dict
    """
    def __init__(self, *args, **kwargs):
        """Init"""
        d = datetime.strptime
        if "id" not in kwargs:
            self.id = str(uuid.uuid4())
        else:
            self.id = kwargs["id"]
        if "created_at" not in kwargs:
            self.created_at = datetime.now()
        else:
            self.created_at = d(kwargs["created_at"], '%Y-%m-%dT%H:%M:%S.%f')
        if "updated_at" not in kwargs:
            self.updated_at = datetime.now()
        else:
            self.updated_at = d(kwargs["updated_at"], '%Y-%m-%dT%H:%M:%S.%f')
        if kwargs is None or len(kwargs.items()) == 0:
            storage.new(self)

    def __str__(self):
        """ creates a string rep of the instance """
        s = self
        return "[{}] ({}) {}".format(type(s).__name__, s.id, s.__dict__)

    def save(self):
        """ updates the date time for update_at """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ converts instance to dictionary """
        dic = self.__dict__.copy()
        dic["created_at"] = self.created_at.isoformat("T")
        dic["updated_at"] = self.updated_at.isoformat("T")
        dic["__class__"] = str(type(self).__name__)
        return dic
