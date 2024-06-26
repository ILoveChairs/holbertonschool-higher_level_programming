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
    state = session.query(State).filter(State.name == sys.argv[4]).\
        order_by(State.id).first()
    if state is None:
        print("Not found")
    else:
        print(state.id)
    session.close()
