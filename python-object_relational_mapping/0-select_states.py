#!/usr/bin/python3

'''
    Testing Databases with MySQLdb (python)
'''

import sys
from typing import Any
import sqlalchemy
import MySQLdb
from MySQLdb import cursors


def makeConnection(argv: list[str]
                   ) -> tuple[MySQLdb.Connection,
                              cursors.Cursor]:
    '''
        Make a connection with the database and return
        the connection and a cursor.

        Both must be closed later.
    '''

    db: MySQLdb.Connection
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cursor: cursors.Cursor
    cursor = db.cursor(cursorclass=cursors.Cursor)
    return db, cursor


def makeQuery(cursor: cursors.Cursor,
              query: str
              ) -> int:
    '''
        Makes a query to the database by the cursor arg.

        Execute apparently does it's things inside it's class.
        Also returns number of rows affected?
    '''

    return cursor.execute(query)


def makeAndPrintQuery(cursor: cursors.Cursor,
                      query: str
                      ) -> None:
    '''
        Calls makeQuery and prints result as a tuple.
    '''

    nOfRows: int = makeQuery(cursor, query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)


def main(argv: list[str]) -> None:
    '''
        Calls all functions
    '''

    db, cursor = makeConnection(argv)

    query = "SELECT * FROM states ORDER BY states.id ASC;"
    makeAndPrintQuery(cursor, query)

    db.close()
    cursor.close()


if __name__ == "__main__":
    main(sys.argv)
