"""def fun(n):
    if n==0:
        return 0
    return n+fun(n-1)

n=5
print(fun(n))
output 15

def fun(n):
    if n==1:
        return 1
    return n+fun(n-1)

n=4
print(fun(n))#4+3+2+1=10
"""
"""
def fun(n):
    if n<=0:
        return 1
    return n+fun(n-1)+fun(n-2)#first it will go for left hand side only

n=5
print(fun(n))#4+3+2+1=10

            f(5)#39
             |
        5+f(4)#22+f(3)#14
             |
        4+f(3)#14+f(2)#5
           |
    3+f(2)#5+f(1)#3
        |
   2+f(1)#3+f(0)#1
       |
1+f(0)#1+f(-1)#1

def fun(n):
    if n<=0:
        return 
    fun(n-1)            #line 1
    print(n,end=" ")    #line2
    fun(n-2)            #line3

n=5
fun(n)#1 2 3 (f3)1 (f4) 4 1 2  

f(5)      ---f(3)1 2

f(4)      ---f(2)1

f(3)      ---f(1)

f(2)      ---f(0)

            f(1)

f(0)#first line   f(-1)

def fun(n):
    if n<=0:
        return
    print("*",end=" ")    #line2
    fun(n-1)            #line 1

    fun(n-2)            #line3

n=5
fun(n)
"""
def fun(n):
    if n<=0:
        return 1
    return n+fun(fun(n-1)-2)
n=5
print(fun(n))



















