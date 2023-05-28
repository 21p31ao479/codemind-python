import math
def isprime(num):
    sq=int(math.sqrt(num))
    for i in range(2,sq+1):
        if num%i==0:
            return False
    return True
def reverse(num):
    rev=0
    while num:
        d=num%10
        num=num//10
        rev=rev*10+d
    return rev
num=int(input())
if isprime(num):
    num=reverse(num)
    if isprime(num):
        print("circular prime")
    else:
        print("prime but not a circular prime")
else:
    print("not prime")