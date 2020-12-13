#!/usr/bin/python3
"""punto 11 insert a state"""
from model_state import Base, State
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
import sys


def ins_state():
    """add a state in  the database"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    s = State()
    s.name = "Louisiana"
    session.add(s)
    session.commit()
    resp = session.query(State).filter(State.name == "Louisiana")
    print(resp[0].id)
    session.close()
    engine.dispose()


if __name__ == "__main__":
    ins_state()
