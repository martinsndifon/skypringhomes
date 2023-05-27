#!/usr/bin/python3
"""this module represent all rented properties"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer


class Sale(BaseModel, Base):
    """Represents rented listings"""
    __tablename__ = 'sale'
    title = Column(String(60), nullable=False)
    price = Column(Integer, default=0)
    description = Column(String(1500), nullable=True)
    location = Column(String(255), nullable=True)
    image_path = Column(String(128), nullable=False)
    # video_path = Column(String(128), nullable=False)

    def __init__(self, *args, **kwargs):
        """initializes common attributes from basemodel"""
        super().__init__(*args, **kwargs)
        self.image_path = "/static/media_storage/sale/images/" + self.id + "/"
        # self.video_path = "/static/media_storage/sale/videos/" + self.id + "/"
