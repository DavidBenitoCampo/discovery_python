#!/bin/python3

import sys


if len(sys.argv) != 2:
    print("none")
    exit(1)

a = sys.argv
b = input("What was the parameter? ")

if a[1] == b:
      print("Good job!")
else:
    print("Nope sorry...")