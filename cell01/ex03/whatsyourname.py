x = input("Hey, what's your first name? : ")
d = input("And your last name? : ")

#e= (f"Well, pleased to meet you, {x} {d}.")

e= (f"Well, pleased to meet you, " + x.strip() + " " + d.strip())
print(e)
