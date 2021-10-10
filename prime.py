"""
def prime(n):
    if(n==1):
        return False
    else:1
        for i in range(2,n//2+1):
            if(n%i==0):
                return False
                break
        else:
            return True
"""
def sums(n):
    s=0
    while(n):
        r=n%10
        n=n//10
        s=s+r
        if(n==0 and s>9):
            n=s
            s=0
    return s

n=int(input())
d=sums(n)
m=0
if(d==1):
    m=0
else:
    for i in range(2,d//2+1):
        if(d%i==0):
            m=0
            break
    else:
        m=1
if(d%2 and m):
    print("yes")
else:
    print("no")

