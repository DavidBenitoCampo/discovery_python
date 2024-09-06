#!/bin/python3

# your method definition here
women_scientists = {
    "ada": {"name": "Ada Lovelace", "date_of_birth": "1815" },
    "cecilia": {"name": "Cecila Payne", "date_of_birth": "1900" },
    "lise": {"name": "Lise Meitner", "date_of_birth": "1878" },
    "grace": {"name": "Grace Hopper", "date_of_birth": "1906" }
}



# Sort by date_of_birth and create a dictionary
famous = [(name, date_of_birthday) for name, date_of_birthday in women_scientists.items()]
scientists = sorted(famous, key=lambda x: x[1]["date_of_birth"])
dictionary = dict(scientists)

# Function to print out famous scientists
def famous_births(dictionary):
    for i, j in dictionary.items():
        print(f"{j['name']} is a great scientist born in {j['date_of_birth']}")





famous_births(dictionary)