s=input().split()
p=s[len(s)-1]
k=min(p)
if k and k.lower() in p:
    print(k.lower())
else:
    print(k)