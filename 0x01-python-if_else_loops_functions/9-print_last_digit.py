#!/usr/bin/python3
# 9-print_last_digit.py
def print_last_digit(number):
    # Get the absolute value of the number to handle negative numbers
    number = abs(number)

    # Get the last digit by taking the modulo 10 of the number
    last_digit = number % 10

    # Print the last digit
    print(last_digit, end='')

    # Return the value of the last digit
    return last_digit


