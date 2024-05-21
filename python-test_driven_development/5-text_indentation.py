#!/usr/bin/env python3

'''
    Duck
'''


def text_indentation(text):
    '''
        Goes quack quack
    '''

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    flag = False
    for char in text:
        if flag and char == " ":
            pass
        elif char not in ".:?":
            print(char, end="")
            flag = False
        else:
            print(char, end="\n\n")
            flag = True
