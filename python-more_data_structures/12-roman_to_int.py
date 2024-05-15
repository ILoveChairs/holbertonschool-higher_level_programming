#!/usr/bin/python3

def get_value_from_roman_char(roman_char):
    roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
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
    max_char = get_max_from_roman_str(roman_string)
    prior_max = True
    for roman_char in roman_string:
        if prior_max and roman_char == max_char:
            prior_max = False
        roman_char_value = get_value_from_roman_char(roman_char)
        if prior_max:
            sum -= roman_char_value
        else:
            sum += roman_char_value
    return sum
