#!/usr/bin/python3
"""this module represent all rented properties"""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey, Integer
import sqlalchemy
import models


class RentType(Base):
    """Represents rented listings"""
    __tablename__ = 'renttype'
    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(60), nullable=False)
    rent = relationship("Rent", backref="renttype")
