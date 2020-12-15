#!/usr/bin/python3
"""punto 13 delete states with a"""
from model_state import Base, State
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
import sys


def delete_a_states():
    """deletes states with a in the name"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    instances = session.query(State).filter(State.name.like('%a%'))
    for state in instances:
        session.delete(state)
    session.commit()
    session.close()
    engine.dispose()


if __name__ == "__main__":
    delete_a_states()
