def get_pfs(num):
    s=0
    for i in range(1,num):
        if num%i==0:
            s+=i
    return s
a=int(input())
b=int(input())
if get_pfs(a)==b and get_pfs(b)==a:
    print('Amicable')
else:
    print('Not Amicable')