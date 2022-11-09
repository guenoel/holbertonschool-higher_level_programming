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

    result = session.query(State.id, State.name)

    flag = False
    for row in result:
        if row.name == sys.argv[4]:
            print(row.id)
            flag = True
    if flag == False:
        print("Not found")
