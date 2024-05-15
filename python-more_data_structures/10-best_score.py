#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary == None or len(a_dictionary) == 0:
        return None
    max_num_key = None
    max_num = None
    for key in a_dictionary:
        if max_num == None or a_dictionary[key] > max_num:
            max_num_key = key
            max_num = a_dictionary[key]
    return max_num_key
