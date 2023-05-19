#!/usr/bin/python3
"""storage module"""
from models.rent import Rent
from models.sale import Sale
from models.serviced import Serviced
from models.base_model import BaseModel, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv

models = {
        'rent': Rent,
        'sale': Sale,
        'serviced': Serviced
        }


class DBStorage:
    """interacts with the mysql database"""
    __engine = None
    __session = None

    def __init__(self) -> None:
        """Instantiate a DBStorage object"""
        SKY_MYSQL_USER = getenv('SKY_MYSQL_USER')
        SKY_MYSQL_PWD = getenv('SKY_MYSQL_PWD')
        SKY_MYSQL_HOST = getenv('SKY_MYSQL_HOST')
        SKY_MYSQL_DB = getenv('SKY_MYSQL_DB')
        SKY_ENV = getenv('SKY_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(SKY_MYSQL_USER,
                                             SKY_MYSQL_PWD,
                                             SKY_MYSQL_HOST,
                                             SKY_MYSQL_DB),
                                             pool_pre_ping=True)
        if SKY_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None, type_id=None) -> dict:
        """Return all objects in the db or all objects for the class passed"""
        objs = {}
        if not cls:
            for name, model in models.items():
                result = self.__session.query(model).all()
                for obj in result:
                    key = f'{obj.__class__.__name__}.{obj.id}'
                    objs[key] = obj
            return objs
        if not type_id:
            result = self.__session.query(cls).all()
        else:
            result = self.__session.query(cls).where(cls.type_id == type_id).all()
        for obj in result:
            key = f'{obj.__class__.__name__}.{obj.id}'
            objs[key] = obj
        return objs

    def new(self, obj=None) -> None:
        """Add the object passed to the db session"""
        if not obj:
            return
        self.__session.add(obj)

    def get(self, cls=None, id=None) -> object:
        """Return an object given its id and class"""
        if not cls or not id:
            return None
        obj = self.__session.query(cls).where(cls.id = id).first()
        if not obj:
            return None
        return obj

    def save(self) -> None:
        """Commit the current db session"""
        try:
            self.__session.commit()
        except Exception:
            self.__session.rollback()

    def close(self) -> None:
        """Close the current db session"""
        self.__session.close()

    def reload(self) -> None:
        """Initialize the db"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        session = scoped_session(session_factory)
        self.__session = session

    def update(self, cls, obj) -> None:
        """Update the current object"""
        self.__session.query(cls).update(obj)

    def delete(self, obj=None) -> None:
        """Delete the current object"""
        if obj is not None:
            self.__session.delete(obj)
