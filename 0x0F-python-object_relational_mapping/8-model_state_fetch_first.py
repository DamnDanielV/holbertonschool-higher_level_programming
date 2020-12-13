#!/usr/bin/python3
"""punto 8 del proyectoooo"""
from model_state import Base, State
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
import sys


def print_f_state():
    """prints the first state of the db"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        state = session.query(State).first()
        print("{}: {}".format(state.id, state.name))
    except:
        print("Nothing")
    session.close()
    engine.dispose()


if __name__ == "__main__":
    print_f_state()
