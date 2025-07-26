import re

url = input("URL: ")

name = re.sub(r"^(https?://)?(www\.)?x\.com/", "", url)
print(name)