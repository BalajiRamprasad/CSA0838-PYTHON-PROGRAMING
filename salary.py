a=str(input("Enter your grade:"))
b=int(input("Enter your salary:"))
if b<=10000:
    x=b*0.02
else:
    x=0
if a=="A":
    y=b*0.05
elif a=="B":
    y=b*0.1
else:
    y=0
print("Bonus:",x+y)
print("Salary:",b)
tot=b+x+y
print ("Total to be paid:",tot)
