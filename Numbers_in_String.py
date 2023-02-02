n=input()
c=0
for i in n:
    if ord(i)>=48 and ord(i)<=57:
        c=c+int(i)
        
print(c)