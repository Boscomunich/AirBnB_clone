#!/usr/bin/python3
"""user class module"""
from models.base_model import BaseModel


class User(BaseModel):
    """class representing a user"""
    email: str = ""
    password = ""
    first_name = ""
    last_name = ""
