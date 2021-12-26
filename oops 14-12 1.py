
class Student:
    college="Aditya"
    def __init__(self,rollno,per):
        self.roll=rollno
        self.per=per
        self.grade=self.findgrade(self.per)
    def displaydata(self):
        print(self.roll,self.per,self.grade,Student.college)
        #here both the class variables and instance variables can also access
        #first it will check the instances and later it will check for the class methods

    @classmethod#we can only access class variable
    #@ this is called as decerater
    def classmethod(cls):
        print(cls.college)
    #in class method we can only refer to class variables
    @staticmethod
    def findgrade(per):
        if per>75:
            return 'A'
        if per>60:
            return 'B'
        if per>50:
            return 'C'

s1=Student(123,88.7)

s1.displaydata()

Student.classmethod()


    
