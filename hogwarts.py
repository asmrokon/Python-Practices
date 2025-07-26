students = ["Kelsier" , "Vin" , "Sazed"]

def get_number():
    while True:
        n = int(input("Number: "))
        if n > 2 or n < 0:
            print("Put a number between 0 to 2")
            continue
        else:
            return n
n = get_number()

print(students[n])