#!/usr/bin/python3
def magic_string() -> str:
    globals()['c'] = 0 if globals().get('c') is None else globals()['c'] + 1
    return globals()['c'] * 'BestSchool, ' + 'BestSchool'
