distances = {
    "Vorager 1": 163,
    "Vorager 2": 136,
    "Pioneer 10": 80,
    "New Horizons": 58,
    "Pioneer 11": 44
}

def main():
    for name, distance in distances.items():
        print(f"{distance} AU is {convert(distance)} KM")

def convert(distance):
    return distance * 1407000060

main()