def happynum(num):
    j=sum=0
    while(num>0):
        j=num%10
        sum=sum+(j*j)
        num=num//10
    return sum;
a=int(input("enter the number:"))
b=a
while(b!=1 and b!=4):
    b=happynum(b)
if(b==1):
    print(str(a),"is a happy number")
elif(b==4):
    print(str(a),"is not a happy number")
