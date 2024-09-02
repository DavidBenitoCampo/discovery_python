#!/bin/python3
mul_table = int(input("Enter a number "))

multiplier = mul_table
counter = 0

while counter <= 10:
    result = multiplier + counter
    print(f"{multiplier} x {counter} = {result}")
    counter += 1