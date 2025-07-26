def main():
    x = float(input("Enter first number: "))

    def square(x):
        return x * x
    print("Square of", x, "is", square(x))

main()

input("Press Enter to exit")