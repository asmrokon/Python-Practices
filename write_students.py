import csv


name = input("Name: ")
home = input("Home: ")

with open("write_students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})
