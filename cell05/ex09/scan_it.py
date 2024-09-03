#!/bin/python3

import sys
import re

a = sys.argv

if len(a) != 3:
    print("NONE")
    exit(1)

x = re.findall(a[1],a[2])
x = len(x)



print(x)
