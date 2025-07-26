def main():

    x = int(input("Enter a number: "))
    if is_even(x):
        print(f"{x} is even")
    else:
        print(f"{x} is odd")

def is_even(n):
    return True if n % 2 == 0 else False

main()