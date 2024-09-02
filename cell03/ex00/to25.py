#!/bin/python3
l = int(input("Enter a number less than 25 " ))

i = 0 
if l >= 26 :
    print("ERROR")
    exit()

if l <= 25:
    while l <= 25:
        print("Inside the loop, my variable is", l)
        l = l +1
