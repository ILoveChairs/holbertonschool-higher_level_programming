#!/usr/bin/python3

'''
    Counting iterator object
'''


class CountedIterator():
    '''
        CountedIterator
    '''

    def __init__(self, data):
        self.__iter = iter(data)
        self.__counter = 0
        self.__len = self.__iter.__length_hint__()

    def get_count(self):
        return self.__counter

    def __next__(self):
        if self.__len <= self.__counter:
            raise StopIteration()
        self.__counter += 1
        # return self.__iter.__getitem__(self.__counter)
        return self.__iter.__next__()
