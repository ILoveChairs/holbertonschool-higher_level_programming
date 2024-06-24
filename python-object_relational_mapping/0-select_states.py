#!/usr/bin/python3

'''
    Testing Databases with MySQLdb (python)
'''

import sys
import sqlalchemy
import MySQLdb


def makeConnection(argv) -> :
    '''
        Quickdoc
    '''

    db = 
    cursor = 
    return db, cursor


def makeQuery(cursor, query, printAsTuple=True) -> tuple:
    '''
        Makes a query to the database by the cursor arg.
    '''

    pass


def makeAndPrintQuery(cursor, query) -> None:
    '''
        Calls makeQuery and prints result as a tuple.
    '''

    pass


def main(argv) -> None:
    '''
        Calls all functions
    '''

    db, cursor = makeConnection(argv)

    makeAndPrintQuery(db, cursor, "")

    db.close()
    cursor.close()


if __name__ == "__main__":
    main(sys.argv)
