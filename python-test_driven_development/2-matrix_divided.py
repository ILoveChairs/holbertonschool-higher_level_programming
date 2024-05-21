#!/usr/bin/python3

'''
    Defined a function that divides all numbers of a matrix by a number.
'''


def matrix_divided(matrix, div):
    '''
        Function that divides all numbers of a matrix by a number.
    '''
    def type_error_thrower():
        raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")

    ''' Type Checks '''
    if not (isinstance(div, int) or isinstance(div, int)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list):
        type_error_thrower()
    size = 0
    for row in matrix:
        if not isinstance(row, list):
            type_error_thrower()
        if size == 0:
            size = len(row)
        else:
            if size != len(row):
                raise TypeError("Each row of the matrix must \
have the same size")
        for element in row:
            if not (isinstance(element, int) or isinstance(element, float)):
                type_error_thrower()

    return list(map(lambda row:
                    list(map(lambda x: round(x / div, 2), row)),
                    matrix))
