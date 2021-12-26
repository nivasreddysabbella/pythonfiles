"""
the hole oops concept
total 7 questions are from oops concept
that is oops
object oriented programming
a=10
type(a)
<class 'int'>
data=[]
<class 'data'>

how to create our own classes
properties of the class

a,b=map(int,input().split())
print(a,b)
"""
#class ClassName:
"""
first name should be capital letter
in the class we should have some methods
class is a collections of member variable and member functions
 going to create a student class
self is used to represent the required class name
def means methods
    class is a collections of functions variable and methods
"""

class Student:
    def __init__(self,rollno,per):#__init__ -->it is a constructer
        self.roll=rollno
        self.per=per
    def display_data(self):
        print(self.roll,self.per)
s1=Student(123,88.7)
s2=Student(124,66.7)
s1.display_data()
s2.display_data()
