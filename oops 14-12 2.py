"""
oops
5 types
single inheritance
if there are two different classes
1. superclass
2. sub class

     the super class has some methods and variables
if object is created in super class we can use only methods and variables of super class only
     the sub class also has some methods and vatiables
if object is created in sub class we can use both the subclass and mainclass methods and variables


"""
class Personal:
    def __init__(self,name,adhar):
        self.name=name
        self.adhar=adhar
    def display_data(self):
        print(self.name,self.adhar)

class Student(Personal):
    college="Aditya"
    def __init__(self,rollno,per,name,adhar):
        self.roll=rollno
        self.per=per
        self.grade=self.findgrade(self.per)
        super().__init__(name,adhar)
    def displaydata(self):
        print(self.roll,self.per,self.grade,self.college)
    @ classmethod
    def classmethod(cls):
        print(cls.college)
    @ staticmethod
    def findgrade(per):
        if per>75:
            return "A"
        if per>60:
            return "B"
        if per>50:
            return "C"

s1=Student(123,69.7,"trending","12345678456")
s1.displaydata()
