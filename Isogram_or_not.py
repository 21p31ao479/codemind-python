def solve(s):
    a=[]
    for char in s:
        if char.isalpha():
            if char in a:
                return False
            else:
                a.append(char)
    return True
s=input()
print(solve(s))