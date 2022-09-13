def Palindrome(d):
    return d==d[::-1]
d= str(input("enter the string:"))
b=d[::-1]
a=Palindrome(d)
if a:
    print("Yes")
    print(d,"reads as",d,"from left to right and from right to left")
else:
    print("No")
    print("From left to right it reads",d," From right to left, it becomes", b," Therefore it is not a palindrome")
