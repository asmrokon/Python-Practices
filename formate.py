import re

name = input("Name: ").strip().title()
if matches := re.search("^(.+), *(.+)$", name):
    
    n = matches.group(2) + " " + matches.group(1)
print(f"hello, {n}")  # type: ignore