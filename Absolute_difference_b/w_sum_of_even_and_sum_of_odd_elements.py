n=int(input())
s=0
q=0
a=list(map(int,input().split()))
for i in range(n):
    if a[i]%2==0:
        s=s+a[i]
    else:
        q=q+a[i]
print(abs(s-q))