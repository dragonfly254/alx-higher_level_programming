#!/usr/bi/python3
"""
This module lists all states from the database given
"""
import MySQLdb
import sys


def list_states(username, password, database):
    """
    lists all states from the db given

    Args:
        username: the user accessing the db
        password: security key
        database: the database given
    """
    try:
        db = MySQLdb.connect(
            host='localhost',
            user=username,
            passwd=password,
            db=database,
            port=3306
        )
        cursor = db.cursor()

        cursor.execute("SELECT * FROM states ORDER BY states.id ASC")

        states = cursor.fetchall()

        for state in states:
            print(state)

        cursor.close()
        db.close()
    except MySQLdb.Error as e:
        print("MySQL Error:", e)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
    else:
        username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
        list_states(username, password, database)
