#!/usr/bin/python3

def get_value_from_roman_char(roman_char):
    roman_dict = {
        "I": 1, "V": 5,
        "X": 10, "L": 50,
        "C": 100, "D": 500,
        "M": 1000
        }
    return roman_dict[roman_char]


def get_max_from_roman_str(roman_string):
    max_char = None
    max = None
    for roman_char in roman_string:
        value = get_value_from_roman_char(roman_char)
        if max_char is None or value > max:
            max_char = roman_char
            max = value
    return max_char


def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    sum = 0
    for i, roman_char in enumerate(roman_string):
        max_char = get_max_from_roman_str(roman_string[i:])
        roman_char_value = get_value_from_roman_char(roman_char)
        if roman_char == max_char:
            sum += roman_char_value
        else:
            sum -= roman_char_value
    return sum
