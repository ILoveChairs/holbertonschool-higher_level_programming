#!/usr/bin/python3
'''
    Does stuff idk.
'''

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    '''
        Does stuff idk.
    '''

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement="auto")
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
