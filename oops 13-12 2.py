"""
there are 3 different types of member variables
1.local variables
2.instance variables
3.class/static
"""
class Student:
    college="Aditya"#it is a class variable
    def __init__(self,rollno,per):#rollno,per are the local variables  
        self.roll=rollno
        self.per=per
    def display_data(self):
        print(self.roll,self.per,Student.college)
s1=Student(123,88.7)
s1.display_data()
