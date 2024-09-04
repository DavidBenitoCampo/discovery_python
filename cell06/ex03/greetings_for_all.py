#!/bin/python3

def greetings(name = "Noble stranger"):
    if isinstance(name, str):
        print("Hello,", name)
    else:
        print("Error! It was not a name.")

greetings("David")