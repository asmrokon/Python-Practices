def main():
    names = []
    with open("name.txt") as file:
        for line in file:
            names.append(line.rstrip().title())
    for name in sorted(names, reverse=True):
        print(f"Hello, {name}")

main()