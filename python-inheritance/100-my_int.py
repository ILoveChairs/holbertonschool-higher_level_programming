#!/usr/bin/python3

'''
    1 function is all it takes
'''


class MyInt(int):
    '''
        calls dir
    '''

    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
