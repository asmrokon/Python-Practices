name = input("Name? ")

file = open("name.txt", "a")
file.write(f"{name}\n")
file.close