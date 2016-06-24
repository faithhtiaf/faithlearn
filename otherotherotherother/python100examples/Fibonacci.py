import math

list=[]
for n in range(101,201):
    print int(math.sqrt(n))+1
    for num in range(101,int(math.sqrt(n))+1):
        if n%num==0 and n!=num:
            break
        elif n%num!=0 and num==int(math.sqrt(n))-1:
            print n
            list.appened(n)
            print list
print list

