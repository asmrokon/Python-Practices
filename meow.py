import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", help="Number of times to meow", type=int)
args = parser.parse_args()

for _ in range(int(args.n)):
    print("meow")