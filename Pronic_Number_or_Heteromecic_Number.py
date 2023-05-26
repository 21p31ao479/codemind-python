def ispronicNumber(num):
    flag=False
    for j in range(1,num+1):
        if ((j*(j+1))==num):
            flag=True
            break
    return flag
num=int(input())
if (ispronicNumber(num)):
    print("YES")
else:
    print("NO")