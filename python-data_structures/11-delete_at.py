#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list
    new_list = my_list.copy()
    my_list.clear()
    for i, num in enumerate(new_list):
        if not i == idx:
            my_list.append(num)
    return my_list
