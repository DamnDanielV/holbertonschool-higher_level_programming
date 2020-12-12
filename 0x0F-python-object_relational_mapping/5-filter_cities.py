#!/usr/bin/python3
"""lists all cities from a given state"""
import sys
import MySQLdb


def cities_state():
    """list cities of a state"""
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cur = db.cursor()
    name = ''.join([i for i in sys.argv[4] if i != "'" and i != ";"])
    cur.execute("SELECT cities.name FROM cities\
                INNER JOIN states ON states.id = cities.state_id\
                WHERE states.name LIKE BINARY '%{}%'\
                ORDER BY cities.id ASC".format(name))
    print(', '.join([row[0] for row in cur.fetchall()]))
    cur.close()
    db.close()


if __name__ == '__main__':
    cities_state()
