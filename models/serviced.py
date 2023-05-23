#!/usr/bin/python3
"""this module represent all rented properties"""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey, Integer
import sqlalchemy
import models


class Serviced(BaseModel, Base):
    """Represents rented listings"""
    __tablename__ = 'serviced'
    price = Column(Integer, default=0)
    description = Column(String(1500), nullable=True)
    location = Column(String(255), nullable=True)
    image_path = Column(String(128), nullable=False)
    video_path = Column(String(128), nullable=False)

    def __init__(self, *args, **kwargs):
        """initializes common attributes from basemodel"""
        super().__init__(*args, **kwargs)
