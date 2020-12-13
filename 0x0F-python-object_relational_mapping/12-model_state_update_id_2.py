#!/usr/bin/python3
"""punto 12 update a state"""
from model_state import Base, State
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
import sys


def state_upd():
    """chnge the name of the state..."""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    upd_st = session.query(State).filter(State.id == 2).one()
    upd_st.name = "New Mexico"
    session.add(upd_st)
    session.commit()
    session.close()
    engine.dispose()


if __name__ == "__main__":
    state_upd()
