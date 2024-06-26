#!/usr/bin/python3

'''
    Does stuff idk.
'''

import sys
from model_state import Base, State
from sqlalchemy.orm import Session
from sqlalchemy import (create_engine)


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    session = Session(engine)
    statesWA = session.query(State).filter(State.name.like('%a%')).all()
    for state in statesWA:
        session.delete(state)
    session.commit()
    session.close()
