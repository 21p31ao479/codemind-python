r,c=map(int,input().split())
m=[]
c=[]
for i in range(r):
    l=list(map(int,input().split()))
    for j in l:
        if i%2==0:
            m.append(j)
        else:
            c.append(j)
print(sum(m),sum(c))