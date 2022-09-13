a=int(input("Enter the count of fresh loaves you purchased:"))
b=int(input("Enter the count of old loaves you purchased:"))
if(a>0)and(b>0):
    dis=185*0.6
    e=a*185
    f=b*dis
    total=e+f
    print("regular price=185.00")
    print("amount of new loaves=",'%.2f'%e)
    print("amount of old loaves=",'%.2f'%f)
    print("total amount=",'%.2f'%total)
else:
    print("invalid")
    pass
