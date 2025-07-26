words = {"PAIR": 4, "HAIR": 4, "CHAIR": 5, "GRAPHIC": 7}


def main():
    print("Welcome to Spelling Bee!")
    print("Your letters are: A I P C R H G")

    while len(words) > 0:
        print(f"{len(words)} words left")
        guess = input("Guess a word: ")

        if guess == "GRAPHIC":
            words.clear()
            print("You have won!")
        if guess in words.keys():
            points = words.pop(guess)
            print(f"Good job! You scored {points} points.")


    print("That's the game!")


main()