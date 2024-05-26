#!/usr/bin/python3

'''
    Defines lazy_matrix_mul
'''

from numpy import matmul


def lazy_matrix_mul(m_a, m_b):
    '''
        Lazy matrix mul
    '''
    return matmul(m_a, m_b)
