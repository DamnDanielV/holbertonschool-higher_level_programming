#!/usr/bin/python3
"""lists all states with a given name"""
import sys
import MySQLdb


def safe_f():
    """SQL Injection"""
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8"
    )
    cur = db.cursor()
    name = ''.join([i for i in sys.argv[4] if i != "'" and i != ";"])
    cur.execute("SELECT * FROM states\
                WHERE name LIKE BINARY '%{}%'\
                    ORDER BY states.id ASC".format(name))
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()


if __name__ == '__main__':
    safe_f()
