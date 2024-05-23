#!/usr/bin/python3

def matrix_mul(m_a, m_b):
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
        [
            (isinstance(num, int) or isinstance(num, float))
            for num in row
        ]
            for row in m_a]):
        raise TypeError("m_a should contain only integers or floats")
    if not all([
        [
            (isinstance(num, int) or isinstance(num, float))
            for num in row
        ]
            for row in m_b]):
        raise TypeError("m_b should contain only integers or floats")

    if min([len(row) for row in m_a]) != max([len(row) for row in m_a]):
        raise TypeError("each row of m_a must be of the same size")
    if min([len(row) for row in m_b]) != max([len(row) for row in m_b]):
        raise TypeError("each row of m_b must be of the same size")

    if False:
        raise TypeError("m_a and m_b can't be multiplied")

    m_a_height = len(m_a)
    m_a_width = len(m_a[0])
    m_b_height = len(m_b)
    m_b_width = len(m_b[0])

    def calc(x, y):
        output = 0
        for i in range(m_a_width):
            output += m_a[y][i] * m_b[i][x]
        return output

    output = []
    for y in range(m_a_height):
        new_list = []
        for x in range(m_a_width):
            if x >= m_b_width:
                break
            new_list.append(calc(x, y))
        output.append(new_list)
    return output
