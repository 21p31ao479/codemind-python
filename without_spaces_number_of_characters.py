s=input()
v=0
for k in range(0,len(s)):
    if((ord(s[k])!=32)):
        v+=1
print(v)