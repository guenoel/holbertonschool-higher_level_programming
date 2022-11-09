#!/usr/bin/python3
"""Connect to a MySQL database with MySQLdb
connector and print result of query"""


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State

class City(Base):
    """city class: id + name"""

    __tablename__ = 'cities'
    id = Column("id", Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column("state_id", Integer, ForeignKey(State.id), nullable=False)
