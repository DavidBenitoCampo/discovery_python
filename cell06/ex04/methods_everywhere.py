#!/bin/python3

import sys

x =  sys.argv


def shrink(data):
   data = data[:8]
   return data

def enlarge(data):
  if len(data) < 8:
        data += 'Z' * (8 - (len(data)))
        return data

if len(sys.argv) < 2:
    print("none")
    exit(1)

for i in x:
    if len(i) > 8:
        print(shrink(i))
    else:  
        print(enlarge(i))






