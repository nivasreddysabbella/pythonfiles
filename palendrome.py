

#for palindrome number
"""
def reverse(n):
    rev=0
    while n:
        r=n%10
        n=n//10
        rev=rev*10+r
    return rev
n=int(input())
print(n==reverse(n))

n=int(input())
print(n==int(str(n)[::-1]))


for left palindrome value
n=int(input())
if n==int(str(n)[::-1]):
    print(n)
else:
    i=1
    while 1:
        if n-i==int(str(n-i)[::-1]):
            print(n-i)
            break
        i+=1
 for right palindrome
 n=int(input())
if n==int(str(n)[::-1]):
    print(n)
else:
    i=1
    while 1:
        if n+i==int(str(n+i)[::-1]):
            print(n+i)
            break
        i+=1

#nearer palindrome for the given number
def reverse(n):
    rev=0
    while n:
        r=n%10
        n=n//10
        rev=rev*10+r
    return rev
n=int(input())
if n==reverse(n):
    print(n)
else:
    i=1
    while True:
        if n+i==reverse(n+i):
            right=n+i
            break
        i+=1

    i=1
    while True:
        if n-i==reverse(n-i):
            left=n-i
            break
        i+=1
    if abs(n-right)>=abs(n-left):
        print(left)
    else:
        print(right)
"""
n=int(input())
if n==int(str(n)[::-1]):
    print(n)
else:
    i=1
    c=0
    while 1:
        if n+i==int(str(n+i)[::-1]):
            c=c+1
            if c==3:
                print(n+i)
                break
        i+=1

