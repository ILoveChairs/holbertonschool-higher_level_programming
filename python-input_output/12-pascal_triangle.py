#!/usr/bin/python3

'''
    quick doc
'''


def pascal_triangle(n):
    '''
        quick doc
    '''

    if n <= 0:
        return []

    superlist = []
    for num in range(n):
        lst = [1]

        for i in range(1, num + 1):
            lst.append(i)

        superlist.append(lst)

    return superlist
