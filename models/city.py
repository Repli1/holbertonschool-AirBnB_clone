#!/usr/bin/python3
"""define a class City"""
from models.base_model import BaseModel

class City(BaseModel):
    """State class that inherit from base class"""
    state_id = ""
    name = ""