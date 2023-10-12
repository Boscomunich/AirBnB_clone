#!/usr/bin/python3
"""Review class module."""

from models.base_model import BaseModel


class Review(BaseModel):
    """Class representing a Review."""
    place_id: str = ""
    user_id: str = ""
    text: str = ""
