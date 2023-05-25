r,c=map(int,input().split())
l=[list(map(int,input().split())) for i in range(r)]
m=[]
for i in range(r):
    s=0 
    for j in range(c):
        s+=l[i][j]
    m.append(s)
print(max(m))