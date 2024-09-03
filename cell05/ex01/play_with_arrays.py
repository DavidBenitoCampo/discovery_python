#!/bin/python3

a = [2, 8, 9, 48, 8, 22, -12, 2]

print("Original list: " + str(a))

incremental_value = 2

new_list = [x + incremental_value for x in a]

print("New array: " + str(new_list))