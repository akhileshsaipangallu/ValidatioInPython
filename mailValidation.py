
import re

try:
    input = raw_input
except NameError:
    pass
mail = input("Enter a mailID\n")
pattern = re.compile(r"^([a-zA-Z0-9.-]{1,})\@(\w{1,}\.(\w{1,}))$")

if pattern.match(mail):
    print("Valid mailID")
else:
    print("Invalid mailID")
