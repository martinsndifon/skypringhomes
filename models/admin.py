#!/usr/bin/python3
"""this module represent all admin users"""

from flask_login import UserMixin
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class Admin(UserMixin, BaseModel, Base):
    """Represents admin users"""
    __tablename__ = 'admin'
    name = Column(String(60), nullable=False)
    email = Column(String(60), nullable=False)
    password = Column(String(120), nullable=False)

    def __init__(self, *args, **kwargs):
        """initializes common attributes from basemodel"""
        super().__init__(*args, **kwargs)
