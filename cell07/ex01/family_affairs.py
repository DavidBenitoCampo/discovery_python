#!/bin/python3

# your method definition here
dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}



def find_the_redheads(a):
    family = []
    for name, color_hair in a.items():
        if color_hair == "red":
            family.append(name)
    return family


print(find_the_redheads(dupont_family))