#!/usr/bin/python3
"""lists all State objects from the database hbtn_0e_6_usa"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


def print_states():
    """function to print states"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)

    session = Session()
    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
    session.close()
    engine.dispose()


if __name__ == "__main__":
    print_states()
