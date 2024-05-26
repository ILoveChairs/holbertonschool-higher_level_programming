#!/usr/bin/python3

'''
    Defines matrix_mul
'''


def matrix_mul(m_a, m_b):
    '''
        Multiplies to matrix together
    '''
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if all([isinstance(row, int) for row in m_a]):
        raise TypeError("m_a must be a list of lists")
    if all([isinstance(row, int) for row in m_b]):
        raise TypeError("m_b must be a list of lists")

    if len(m_a) == 0 or all([len(row) == 0 for row in m_a]):
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or all([len(row) == 0 for row in m_b]):
        raise ValueError("m_b can't be empty")

    if not all([
        all([(isinstance(num, int) or isinstance(num, float))
            for num in lst])
            for lst in m_a]):
        raise TypeError("m_a should contain only integers or floats")
    if not all([
        all([(isinstance(num, int) or isinstance(num, float))
            for num in lst])
            for lst in m_b]):
        raise TypeError("m_b should contain only integers or floats")

    if min([len(row) for row in m_a]) != max([len(row) for row in m_a]):
        raise TypeError("each row of m_a must be of the same size")
    if min([len(row) for row in m_b]) != max([len(row) for row in m_b]):
        raise TypeError("each row of m_b must be of the same size")

    m_a_w = len(m_a)
    m_a_h = len(m_a[0])
    m_b_w = len(m_b)
    m_b_h = len(m_b[0])

    if m_a_h != m_b_w:
        raise TypeError("m_a and m_b can't be multiplied")

    def calc(x, y):
        output = 0
        for i in range(m_a_h):
            output += m_a[x][i] * m_b[i][y]
        return output

    output = []
    for x in range(m_a_w):
        new_list = []
        for y in range(m_b_h):
            new_list.append(calc(x, y))
        output.append(new_list)
    return output
