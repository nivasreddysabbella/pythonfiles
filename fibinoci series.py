"""
for fibinoci series
0 1 1 2 3 5 8 13 21 34......

def series(n):
    a=0
    b=1
    if n==1:
        print(a)
    if n==2:
        print(a,b,end=" ")
    for i in range(3,n+1):
        c=a+b
        print(c,end=" ")
        a,b=b,c
n=int(input())
series(n)

in fibinoci series the first prime number from the last
fibinoci number using the lists concept

def series(n):
    d=[0]*n
    if n==1:
        print(*d)
        return
    d[1]=1
    for i in range(2,n):
        d[i]=d[i-1]+d[i-2]
        print(d[-2])
n=int(input())
series(n)

from last kth even number
def series(n,k):
    d=[0]*n
    if n==1:
        print(*d)
        return
    d[1]=1
    for i in range(2,n):
        d[i]=d[i-1]+d[i-2]
    j=0
    for i in d[::-1]:
        if i%2==0:
            j+=1
            if j==k:
                return i
    return -1
n,k=map(int,input().split())
print(series(n,k))

#for checking how many prime number in the series
from math import sqrt
def isprime(n):
    if n==1 or n==0:
        return False
    sq=int(sqrt(n))
    for i in range(2,sq+1):
        if n%i==0:
            return False
    return True
def series(n):
    d=[0]*n
    if n==1:
        print(*d)
        return
    d[1]=1
    for i in range(2,n):
        d[i]=d[i-1]+d[i-2]
    c=0
    for i in d[::-1]:
        if isprime(i):
            c+=1
    return c
n=int(input())
print(series(n))
"""
#secound prime number from the last

