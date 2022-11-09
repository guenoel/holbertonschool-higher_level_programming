#!/usr/bin/python3
"""List all state objects"""

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

if __name__ == "__main__":
    Base = declarative_base()
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                            .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State.id, State.name).filter(State.name == sys.argv[4])

    if result:
        for row in result:
            print(row.id)
    else:
        print("Not found")
