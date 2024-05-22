#!/usr/bin/python3

'''
    MasterClass
'''


class MyList(list):
    '''
        Class
    '''
    def print_sorted(self):
        new_list = self.copy()
        new_list.sort()
        print(new_list)
