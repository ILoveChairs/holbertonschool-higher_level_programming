#!/usr/bin/python3

def no_c(my_string):
    new_str = ""
    for char in my_string:
        if not (char == "c" or char == "C"):
            new_str += char
    return new_str
