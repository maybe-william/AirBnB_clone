#!/usr/bin/python3
from models.base_model import BaseModel
"""Place module"""


class Place(BaseModel):
    """Place class"""

    def __init__(self, *args, **kwargs):
        """Init"""
        super().__init__(self, *args, **kwargs)
        if "name" in kwargs.keys():
            self.name = kwargs["name"]
        if "city_id" in kwargs.keys():
            self.city_id = kwargs["city_id"]
        if "user_id" in kwargs.keys():
            self.user_id = kwargs["user_id"]
        if "description" in kwargs.keys():
            self.description = kwargs["description"]
        if "number_rooms" in kwargs.keys():
            self.number_rooms = kwargs["number_rooms"]
        if "number_bathrooms" in kwargs.keys():
            self.number_bathrooms = kwargs["number_bathrooms"]
        if "max_guest" in kwargs.keys():
            self.max_guest = kwargs["max_guest"]
        if "price_by_night" in kwargs.keys():
            self.price_by_night = kwargs["price_by_night"]
        if "latitude" in kwargs.keys():
            self.latitude = kwargs["latitude"]
        if "longitude" in kwargs.keys():
            self.longitude = kwargs["longitude"]
        if "amenity_ids" in kwargs.keys():
            self.amenity_ids = kwargs["amenity_ids"]

    city_id = ''
    user_id = ''
    name = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
