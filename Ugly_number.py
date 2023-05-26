def ugly(n):
    if n==1:
        return 1
    if n<=0:
        return 0
    if n%2==0:
        return(ugly(n//2))
    if n%3==0:
        return(ugly(n//3))
    if n%5==0:
        return(ugly(n//5))
        return 0
n=int(input())
k=ugly(n)
if k==1:
    print("Ugly Number")
else:
    print("Not Ugly Number")
        
