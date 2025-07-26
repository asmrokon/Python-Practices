import csv

students = []

with open("students.csv") as file:
    for row in csv.DictReader(file):
        students.append({"name": row["name"], "place": row["place"]})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student["name"]} lives in {student["place"]}")