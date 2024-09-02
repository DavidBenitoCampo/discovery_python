#!/bin/python3
first_parameter = float(input("Enter the first number: ")) 
second_parameter = float(input("Enter the second number: ")) 
multyply = first_parameter * second_parameter

#if f_parameter > 0: 
if multyply > 0:
    print(f"{first_parameter} x {second_parameter} = {int(multyply)}"+ "\n" + "The result is positive")
elif multyply < 0: 
    print(f"{first_parameter} x {second_parameter} = {int(multyply)}"+ "\n" + "The result is negative")
else:
    print(f"{first_parameter} x {second_parameter} = {int(multyply)}"+ "\n" + "The result is positive and negative")