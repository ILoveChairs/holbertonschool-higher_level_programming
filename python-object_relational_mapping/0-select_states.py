#!/usr/bin/python3

'''
    Testing Databases with MySQLdb (python)
'''

import sys
from typing import Any
import sqlalchemy
import MySQLdb


def makeConnection(argv: list[str]
                   ) -> tuple[MySQLdb.Connection,
                              MySQLdb.cursors.Cursor]:
    '''
        Make a connection with the database and return
        the connection and a cursor.

        Both must be closed later.
    '''

    db: MySQLdb.Connection
    db = MySQLdb.connect(host="localhost",
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cursor: MySQLdb.cursors.Cursor
    cursor = db.cursor(cursorclass=MySQLdb.cursors.Cursor)
    return db, cursor


def makeQuery(cursor: MySQLdb.cursors.Cursor,
              query: str
              ) -> int:
    '''
        Makes a query to the database by the cursor arg.

        Execute apparently does it's things inside it's class.
        Also returns number of rows affected?
    '''

    return cursor.execute(query)


def makeAndPrintQuery(cursor: MySQLdb.cursors.Cursor,
                      query: str
                      ) -> None:
    '''
        Calls makeQuery and prints result as a tuple.
    '''

    nOfRows: int = makeQuery(cursor, query)
    rows: tuple[tuple[Any]] = cursor.fetchall()
    for row in rows:
        print(row)


def main(argv) -> None:
    '''
        Calls all functions
    '''

    db, cursor = makeConnection(argv)

    query = "SELECT * FROM states ORDER BY states.id ASC;"
    makeAndPrintQuery(db, cursor, query)

    db.close()
    cursor.close()


if __name__ == "__main__":
    main(sys.argv)
