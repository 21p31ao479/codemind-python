n=int(input())
l=[int(i) for i in input().split()]
s=0
c=0
for e in l:
    s=s+e
avg=s//len(l)
for e in l:
    if e>=avg:
        c+=1
print(c)