n=int(input())
a = 0
b = 1
while (True):
    c=a+b
    if(c>n):
        x=b
        y=c
        break
    a=b
    b=c
r=abs(x-n)
s=abs(y-n)
if (r>s):
    print(y)
elif(r==s):
    print(x,y)
else:
    print(x)