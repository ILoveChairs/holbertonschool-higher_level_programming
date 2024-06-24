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
    for row in rows:
        print(row)


def runQueries(
    db: MySQLdb.Connection,
) -> None:
    '''
        Part that defines all queries to run.
    '''

    cursor = db.cursor()

    query = '''SELECT * FROM states
               WHERE BINARY name = %s
               ORDER BY id ASC'''
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
