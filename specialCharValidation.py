
import re

try:
    input = raw_input
except NameError:
    pass
char = input("Enter special character/characters(&, -, (, ),)\n")
pattern = re.compile(r"^([&()'\-']{1,})$")

if pattern.match(char):
    print("Valid special character/characters")
else:
    print("Invalid special character/characters")
