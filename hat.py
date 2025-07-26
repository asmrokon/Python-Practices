import random

class Hat:
    houses = ["sirajganj", "rajshahi", "thakurgaon", "dhaka"]

    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses).title())

Hat.sort("Rokon")