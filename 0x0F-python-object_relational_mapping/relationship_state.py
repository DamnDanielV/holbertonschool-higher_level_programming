#!/usr/bin/python3
"""contains the class definition
    of a State and an instance Base
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()


class State(Base):
    """class to map a table"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all,delete", backref="state")
