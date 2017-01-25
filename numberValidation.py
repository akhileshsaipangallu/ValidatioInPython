
import re

try:
    input = raw_input
except NameError:
    pass
num = input("Enter a number\n")
pattern = re.compile(r"^(\d{1,})$")

if pattern.match(num):
    print("Valid number")
else:
    print("Invalid number")
