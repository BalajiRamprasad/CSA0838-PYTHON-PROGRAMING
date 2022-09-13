def countstr(o,start):
    if(o==0):
        return 1
    count=0
    for i in range(start,5):
        count+=countstr(o-1,i)
    return count
def vowel(o):
    return countstr(o,0)
y=int(input("enter the input:"))
print(vowel(y))
