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
    for state in session.query(State).filter(State.name.like('%a%')).\
        order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
    session.close()
