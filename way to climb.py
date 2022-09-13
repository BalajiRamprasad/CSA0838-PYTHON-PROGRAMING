def stair(j):
    if(j<=1):
        return j
    return stair(j-1)+stair(j-2)
def count(a):
    return stair(a+1)
d=int(input("enter the stair case limit:"))
print("number of ways to climb the stair case is:",count(d))

