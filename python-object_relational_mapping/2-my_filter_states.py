#!/usr/bin/python3

'''
    Testing Databases with MySQLdb (python)
'''

from sys import argv
from typing import Any
# import sqlalchemy
import MySQLdb
from MySQLdb import cursors


def makeConnection(
    argv: list[str]
) -> MySQLdb.Connection:
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
    cursor: cursors.Cursor,
    query: str
) -> None:
    '''
        Makes query and prints result as a tuple.
    '''

    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)


def runQueries(
    db: MySQLdb.Connection,
    argv: str
) -> None:
    '''
        Part that defines all queries to run.
    '''

    cursor = db.cursor()

    query = '''SELECT * FROM states
               WHERE BINARY name = '{}'
               ORDER BY id ASC'''.format(argv[4])
    query = db.escape_string(query)
    makeAndPrintQuery(cursor, query)

    cursor.close()


def main() -> None:
    '''
        Calls all functions
    '''

    db = makeConnection(argv)

    runQueries(db, argv)

    db.close()


if __name__ == "__main__":
    main()
