#!/usr/bin/python3
""" punto 100 relationships """
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from relationship_city import City
from relationship_state import State, Base
import sys


def create_cal():
    """creates the state california"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    state = State(name="California")
    state.cities = [City(name="San Francisco")]
    session.add(state)
    session.commit()
    session.close()


if __name__ == "__main__":
    create_cal()
