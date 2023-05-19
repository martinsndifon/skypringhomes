#!/usr/bin/python3
"""this module represent all rented properties"""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey
import sqlalchemy
import models


class Sale(BaseModel, Base):
    """Represents rented listings"""
    __tablename__ = 'sale'
    
