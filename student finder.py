x=int(input("Enter the total user count:"))
y=int(input("Enter the staff user count:"))
z=y//3
k=y+z
e=x-k
if(x==y)or(y>x):
    print("Invalid input")
    pass
else:
    print("The student user count is:",e)
