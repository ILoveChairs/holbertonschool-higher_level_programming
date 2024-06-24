#!/usr/bin/python3
'''
    Does stuff idk.
'''

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    '''
        Does stuff idk.
    '''

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=1)
    name = Column(String(128), nullable=False)
