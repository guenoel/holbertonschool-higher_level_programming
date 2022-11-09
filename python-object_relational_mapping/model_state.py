#!/usr/bin/python3
"""Connect to a MySQL database with MySQLdb
connector and print result of query"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """state class: id + name"""

    __tablename__ = 'states'
    id=Column("id", Integer, primary_key=True)
    name=Column(String(128), nullable=False)
