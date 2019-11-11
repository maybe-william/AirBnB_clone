#!/usr/bin/python3
from models.base_model import BaseModel
"""Place module"""


class Place(BaseModel):
    """Place class"""

    def __init__(self, *args, **kwargs):
        """Init"""
        super().__init__(self, *args, **kwargs)
        self.name = kwargs["name"]
        self.city_id = kwargs["city_id"]
        self.user_id = kwargs["user_id"]
        self.description = kwargs["description"]
        self.number_rooms = kwargs["number_rooms"]
        self.number_bathrooms = kwargs["number_bathrooms"]
        self.max_guest = kwargs["max_guest"]
        self.price_by_night = kwargs["price_by_night"]
        self.latitude = kwargs["latitude"]
        self.longitude = kwargs["longitude"]
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
