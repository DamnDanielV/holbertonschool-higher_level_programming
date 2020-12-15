#!/usr/bin/python3
"""punto 14 model city fetch ..."""
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def cities_p():
    """prints all cities"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    instances = session.query(City, State).filter(State.id == City.state_id)
    for city, state in instances:
        print(state.name, ': ({}) '.format(city.id), city.name, sep='')
    session.close()
    engine.dispose()


if __name__ == "__main__":
    cities_p()
