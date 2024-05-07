#!/usr/bin/python3

def print_last_digit(number):
    if number > 0:
        number %= 10
    elif number < 0:
        number %= -10
        number *= -1
    print(number, end="")
    return number
