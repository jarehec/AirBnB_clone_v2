#!/usr/bin/python3
"""
Review Class from Models Module
"""

from sqlalchemy.orm import relationship
from sqlalchemy import Column, Table, ForeignKey, MetaData
from sqlalchemy import String, Integer, Float
from models.base_model import BaseModel, Base

class Review(BaseModel, Base):
    """Review class handles all application reviews"""

    __tablename__ = 'reviews'
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)

    def __init__(self, *args, **kwargs):
        """instantiates a new review"""
        super().__init__(self, *args, **kwargs)
