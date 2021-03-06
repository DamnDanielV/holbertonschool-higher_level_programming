#!/usr/bin/python3
"""lists all states with a given name"""
import sys
import MySQLdb


def list_g_name():
    """Filter states by user input"""
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8"
    )
    cur = db.cursor()
    cur.execute("SELECT * FROM states\
                WHERE name LIKE BINARY '%{}'\
                    ORDER BY states.id ASC".format(sys.argv[4]))
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()


if __name__ == '__main__':
    list_g_name()
