#!/usr/bin/python3
"""
State Class from Models Module
"""

from models.base_model import BaseModel


class State(BaseModel):
    """State class handles all application states"""

    name = ''

    def __init__(self, *args, **kwargs):
        """instantiates a new state"""
        super().__init__(self, *args, **kwargs)

    @property
    def cities(self):
        """
        Public getter method that returns a list of 
        City objects from storage linked to the current State
        """
		
