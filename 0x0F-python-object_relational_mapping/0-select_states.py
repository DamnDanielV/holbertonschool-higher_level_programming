#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa"""
import sys
import MySQLdb


def list_db():
    """list a db"""
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8"
    )
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()


if __name__ == '__main__':
    list_db()
