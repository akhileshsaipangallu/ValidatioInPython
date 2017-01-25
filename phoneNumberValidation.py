
import re

try:
    input = raw_input
except NameError:
    pass
ph = input("Enter a mobile phone number\n")
pattern = re.compile(r"^(\d{10})$")

if pattern.match(ph):
    print("Valid phone number")
else:
    print("Invalid phone number")
