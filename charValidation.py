import re

try:
    input = raw_input
except NameError:
    pass
char = input("Enter character\n")
pattern = re.compile(r"^([a-zA-Z]{1,})$")

if pattern.match(char):
    print("Valid character/characters")
else:
    print("Invalid character/characters")
