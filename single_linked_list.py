class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    #Print Linked list
    def printl(self,head):
        if head == None:
            print("empty linked list")
        while(head!= None):
            print(head.data,end=" ")
            head=head.next
        print()

    #Convert array to linked list
    def arrtollist(self,arr):
        head=Node(arr[0])
        temp=head
        for i in range(1,len(arr)):
            temp.next=Node(arr[i])
            temp=temp.next
        return head
    # insertion at begining
    def insertbegin(self,head,val):
        temp=Node(val)
        temp.next=head
        head=temp
        return head
    # insert at end
    def insertend(self,head,val):
        temp=Node(val)
        if head==None:
            head.next=temp
            return head
        cur=head
        while(head.next!=None):
            head=head.next
        head.next=temp
        return cur
    # insertion at pos
    def insertatpos(self,head,val,pos):
        i=1
        root=head
        temp=Node(val)
        if head==None and pos==1:
            return temp
        while(head.next!=None):
            if pos==i+1:
                cur=head.next
                head.next=temp
                temp.next=cur
                break
            else:
                i+=1
                head=head.next
        if i==pos-1:
            head.next=temp
        return root

    # delete at begining
    def delatbegin(self,head):
        if head==None:
            return None
        return head.next
    
    # delete at end
    def delatend(self,head):
        if head==None or head.next==None:
            return None
        cur=head
        while(head.next.next!=None):
            head=head.next
        head.next=None
        return cur
    def delatpos(self,head,pos):
        i=1
        temp=head
        if head==None:
            return None
        elif pos==i:
            return head.next
        
        else:
            while(head.next!=None and pos!=i+1):
                head=head.next
                i+=1
            cur=head.next.next
            head.next=cur
        return temp
    
        
            
        
    


obj=Node(None)
arr=list(map(int,input().split()))
temp=obj.arrtollist(arr)
obj.printl(temp)
'''temp=obj.insertbegin(temp,0)
obj.printl(temp)
temp=obj.insertend(temp,6)
obj.printl(temp)
temp=obj.insertatpos(temp,4,4)
obj.printl(temp)
temp=obj.delatbegin(temp)
obj.printl(temp)
temp=obj.delatend(temp)
obj.printl(temp)'''
temp=obj.delatpos(temp,7)
obj.printl(temp)
