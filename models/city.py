#!/usr/bin/python3
"""City class module."""

from models.base_model import BaseModel


class City(BaseModel):
    """Class representing a City."""
    state_id: str  = ""
    name: str  =  ""
