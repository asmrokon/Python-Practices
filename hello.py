name = input("What is your name? ").strip().title()

first, middle, last = name.split()

print(f"Hello, {first} {middle} {last}")

input("Press Enter to exit")