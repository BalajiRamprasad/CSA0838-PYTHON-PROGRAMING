import re
s = input("Enter the first string:")
p = input("Enter the second string:")
p = r"{}".format(p)
p = re.compile(p)
if p.fullmatch(s):
    print("True")
else:
    print("False")
