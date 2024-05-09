#!/usr/bin/python3

from calculator_1 import add, sub, mul, div
from sys import argv

if __name__ == "__main__":
    argc = len(argv)
    if argc != 4:
        print(f"Usage: {argv[0]} <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    operator = argv[2]
    b = int(argv[3])
    if operator not in "+-*/":
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print(f"{a} {operator} {b} = ", end="")
    match operator:
        case "+":
            print(add(a, b))
        case "-":
            print(sub(a, b))
        case "*":
            print(mul(a, b))
        case "/":
            print(div(a, b))
