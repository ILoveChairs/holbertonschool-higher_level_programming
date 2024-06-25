#!/usr/bin/python3

'''
    Does stuff idk.
'''

import sys
from model_state import Base as Base1, State
from model_city import Base as Base2, City
from sqlalchemy.orm import Session
from sqlalchemy import (create_engine)


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    session = Session(engine)
    for city, state in session.query(City, State).\
            filter(State.id == City.state_id).\
            all():
        print(f"{state.name}: ({city.id}) {city.name}")
    session.close()
