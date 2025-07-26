def main():
    names = ["Mario", "Luigi", "Daisy", "Yoshi"]
    for i in names:
        print(write_letter(names, "Rokon"))

def write_letter(reciever, sender):
    return f"""
    Dear {reciever},

    You are invited to a part.

    Sincerely,
    {sender}

    """

main()
