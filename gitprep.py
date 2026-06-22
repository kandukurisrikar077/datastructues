class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def add_end(self,data):
        new=node(data)
        if self.head is None:
            self.head=new
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=new
    def add_beg(self,data):
        obj=node(data)
        if self.head is None:
            self.head=obj
            return
        obj.next=self.head
        self.head=obj

    def display(self):
        itr=self.head
        while itr:
            print(itr.data,end="-->")
            itr=itr.next
li=Linkedlist()
li.add_end(50)
li.add_end(150)
li.add_end(250)
li.add_end(350)
li.add_end(450)
li.add_beg(10)
li.display()
