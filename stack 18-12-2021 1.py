"""
what is about the stack
it is a one end thing
and key works we need to know is
top is initial at top=-1
stack is also a array
but it has a technique
LIFO/FILO
the basic operations are
1.push-->insert
2.pop--> delete
3.isempty
4.get_max_size
5.display

before inserting we need to check the size of the stack
push(10)
    check is stack is full:
        pass
    else:
        top+=1
        st[top]=v
in python stack
st.append(v)

"""
class Stack:
    def __init__(self,size,d=[]):
        self.size=size
        self.data=d
    def push(self,val):
        if len(self.data)==self.size:
            print("stack is full")
        else:
            self.data.append(val)
    def pop(self):
        if len(self.data)==0:
            print("stack is empty")
        else:
            return self.data.pop()
    def get_max_size(self):
        return self.size
    def is_empty():
        return len(self.data)==0
stack1=Stack(6,[1,2,3,4,5])
s1=Stack(10)









