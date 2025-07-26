import re


email = input("Email: ")
if re.search(r"^\w+@(\w+\.)?\w+\.(edu|com)$", email, re.IGNORECASE):
    print("VALID")
else:
    print("INVALID")
