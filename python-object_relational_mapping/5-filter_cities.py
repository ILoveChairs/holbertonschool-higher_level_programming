#!/usr/bin/python3

'''
    Testing Databases with MySQLdb (python)
'''

from sys import argv
from typing import Any
# import sqlalchemy
import MySQLdb
from MySQLdb import cursors


def makeConnection() -> MySQLdb.Connection:
    '''
        Make a connection with the database and returns it.
    '''

    db: MySQLdb.Connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    return db


def makeAndPrintQuery(
    db: MySQLdb.Connection,
    cursor: cursors.Cursor,
    query: str
) -> None:
    '''
        Makes query and prints result as a tuple.
    '''

    user_input = db.escape_string(argv[4])
    cursor.execute(query, args=[user_input])
    rows = cursor.fetchall()
    for i, row in enumerate(rows):
        print(row[0], end="")
        if i == len(rows) - 1:
            print("\n", end="")
        else:
            print(", ", end="")


def runQueries(
    db: MySQLdb.Connection
) -> None:
    '''
        Part that defines all queries to run.
    '''

    cursor = db.cursor()

    query = '''SELECT cities.name
               FROM cities
               LEFT JOIN states
               ON cities.state_id = states.id
               WHERE states.name LIKE %s
               ORDER BY cities.name ASC'''
    makeAndPrintQuery(db, cursor, query)

    cursor.close()


def main() -> None:
    '''
        Calls all functions
    '''

    db = makeConnection()

    runQueries(db)

    db.close()


if __name__ == "__main__":
    main()
