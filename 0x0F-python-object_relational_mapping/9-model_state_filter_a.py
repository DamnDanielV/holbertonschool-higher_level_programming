#!/usr/bin/python3
"""punto 9 model state filter"""
from model_state import Base, State
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
import sys


def print_states_a():
    """lists all State objects that contain the letter a"""
    """initializes session instance of DB using sqlalchemy"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    instances = session.query(State).filter(State.name.like('%a%'))
    for state in instances:
        print("{}: {}".format(state.id, state.name))
    session.close()
    engine.dispose()


if __name__ == "__main__":
    print_states_a()
