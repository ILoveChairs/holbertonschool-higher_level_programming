#!/usr/bin/python3
def magic_string() -> str:
    globals()['c'] = globals()['c'] + 1 if globals().get('c') is not None else 0
    return globals()['c'] * 'BestSchool, ' + 'BestSchool'
