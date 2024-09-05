#!/bin/python3

# your method definition here
persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}

full_names = []
def array_of_names(a):
    for first_name, last_name in a.items():
        temporary = f"{first_name.capitalize()} {last_name.capitalize()}"
        full_names.append(temporary)
    return full_names

print(array_of_names(persons))



