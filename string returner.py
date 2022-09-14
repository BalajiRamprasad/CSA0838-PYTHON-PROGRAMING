x=int(input("Enter the number:"))
y=[]
for i in range(1,x):
    if(i%15==0):
        y.append("FIZZ BUZZ")
    elif(i%3==0):
        y.append("FIZZ")
    elif(i%5==0):
        y.append("BUZZ")
    else:
        y.append(i)
print(y)
