#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    dict_copy = a_dictionary.copy()
    for key in dict_copy:
        if a_dictionary[key] == value:
            a_dictionary.pop(key)
    return a_dictionary
