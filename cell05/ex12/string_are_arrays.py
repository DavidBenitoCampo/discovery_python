#!/bin/python3

import sys


count = 0

a = sys.argv[1]
for element in a:
   if element == "z":
    count += 1
print("z"*count)