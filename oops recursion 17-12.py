"""
                recursion
calling function inside the same function
 is called as the recursion
 we can only call the 1022 times the resurion
 in recursion we need to write the base condition
 

"""
def fun(n):#4
    if n==0:
        return

    fun(n-1)#fun(4)fun(3)fun(2)fun(1)
    print(n)#1 2 3 4 5
    #this is called as back traking
n=5
fun(n)#funcall
"""
if print(n)
1.if given before if n==0:
    543210
2.if given after return
    54321
3.if given after fun(n-1)
    12345
"""

