
import re

try:
    input = raw_input
except NameError:
    pass
ip = input("Enter an IP\n")

pattern = re.compile(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$")
flag = 1
if not pattern.match(ip):
    print("Invalid IP")
else:
    t = pattern.search(ip).groups()
    for elem in t:

        if int(elem) > 255:
            flag = 0
            break

    if flag is 1:
        print("Valid IP")
    else:
        print("Invalid IP")
