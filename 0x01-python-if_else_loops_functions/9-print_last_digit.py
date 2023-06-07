#!/usr/bin/python3
def print_last_digit(num):
    if num < 0:
        num = -num
    ls_digit = num % 10
    print(ls_digit, end="")
    return ls_digit
