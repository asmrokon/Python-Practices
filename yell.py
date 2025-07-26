def main():
    yell("This", "is", "cs23")

def yell(*words):
    uppercased = [word.upper() for word in words]
    print(*uppercased)


main()