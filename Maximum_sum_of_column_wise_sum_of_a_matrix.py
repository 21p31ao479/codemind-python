r,c=map(int,input().split())
l=[list(map(int,input().split())) for i in range(r)]
m=[]
for i in range(c):
    s=0
    for j in range(r):
        s+=l[j][i]
        m.append(s)
print(max(m))