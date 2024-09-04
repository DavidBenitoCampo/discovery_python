#!/bin/python3
import sys

a = sys.argv[1:]

for i in a:
    match i[-3:]:
        case "ism":
            pass  
        case _:
            print(i + "ism")
            

def future_function():
    pass