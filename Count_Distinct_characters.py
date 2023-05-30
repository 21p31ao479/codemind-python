a=input()
c=0
for i in range(0,26):
    if chr(97+i) in a:
        c+=1
print(c)