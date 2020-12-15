#!/usr/bin/python3
"""punto 10 state my get"""
from model_state import Base, State
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
import sys


def input_parser(command):
    """parses an input removing really bad characters"""
    chars = [';', "'", '"']
    for char in chars:
        command = command.replace(char, '--')
    return command


def state_get():
    """print a state given by input"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    new = input_parser(sys.argv[4])
    g_state = session.query(State).filter(State.name == new)
    try:
        print(g_state[0].id)
    except:
        print("Not found")
    session.close()
    engine.dispose()


if __name__ == "__main__":
    state_get()
