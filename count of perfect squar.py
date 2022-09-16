a=int(input("Enter your limit:"))
count=0
for i in range(1,a+1):
    b=i*i
    if b>a:
        break
    else:
        print(b)
        count+=1
print ("count of perfect square:",count)
