import random
import sys

def main():
    # promtps for a level
    while True:
        try:
            num = int(input("Level: "))
            if num > 0:
                break
        except ValueError:
            pass
    # generates an integer
    to_num = random.randint(1, num)

    # prompts the user to guess the integer
    while True:
        try:
            game(to_num)
            break
        except ValueError:
            print(f"Guess a number between 1 and {num}")
            pass

def game(tn):
    tries = {"t": 5}
    while tries["t"] > 0:
        n = int(input("Guess: "))

        if n > 0:
            if n > tn:
                tries["t"] -= 1
                print(f"Too large! {tries["t"]} tries left")
            elif n < tn:
                tries["t"] -= 1
                print(f"Too small! {tries["t"]} tries left")
            elif n == tn:
                print("Just right!")
                break


main()
sys.exit()