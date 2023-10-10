#!/usr/bin/python3
"""Module for BaseModel class of AirBnB"""
from uuid import uuid4
from datetime import datetime
from models import storage

class BaseModel:
    """
    The BaseModel class for AirBnB project.

    Class Attributes:
        id(str): unique id of the instance.
        created_at(datetime): datetime object the instance was created.
        updated_at(datetime): datetime object the instance was updated.
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of BaseModel.

        Args:
            *args: argument list.
            **kwargs: keyworded arguments.
        Note: args not used.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != "__class__":
                    setattr(self, key, value)

        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
	    storage.new(self)	
					
    def __str__(self) -> str:
        """
        Returns a string representation of the instance.

        Returns:
            str: String of the instance.
        """
        return ("[{}]({}){}".format(self.__class__,
                                    self.id, self.__dict__))

    def save(self):
        """
        Updates the updated_at attr with the current date and time.
        """
        self.updated_at = datetime.now()
	storage.save()

    def to_dict(self):
            """
            Returns a dictionary representation of the instance.

            This method returns a dictionary containing all the attr of the instance.
            The dictionary can be used to recreate the instance using the
            keyword args and serializes datetime objects to ISO format.

            Returns:
                dict: A dictionary containing all the attr of the instance.
            """
            new_obj_dict = self.__dict__.copy()
            new_obj_dict["__class__"] = self.__class__.__name__
            new_obj_dict["created_at"] = self.created_at.isoformat()
            new_obj_dict["updated_at"] = self.created_at.isoformat()
            return (new_obj_dict)

