s=input()
count=0
for i in s:
    if i.isalpha()==False:
        count=count+1
print(count-s.count(" "))