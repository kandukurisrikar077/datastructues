class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None

    def add_end(self,data):
        new_node=node(data)
        if self.head is None:
            self.head=new_node
            return
        current_node=self.head
        while current_node.next:
            current_node=current_node.next
        current_node.next=new_node

    def del_end(self):
        if self.head is None:
            print("there is nothing to delete")
        elif self.head.next is None:
            self.head = None
        else:
            obj = self.head
            while obj.next and obj.next.next:
                obj=obj.next
            obj.next=None

    def add_beg(self,data):
        new_node=node(data)
        if self.head is None:
            self.head=new_node
            return
        new_node.next=self.head
        self.head=new_node
    def add_spec(self,data,position):
        new_node=node(data)
        if position is 0:
            new_node.next=self.head
            self.head=new_node
            return
        else:
            current_node=self.head
            for i in range(position-1):
                current_node = current_node.next
            new_node.next=current_node.next
            current_node.next=new_node

    def del_beg(self):
        if self.head is None:
            print("there is nothing to delete")
        else:
            current_node=self.head
            self.head=current_node.next
            current_node=None
    def find_middle(self):
        if self.head is None:
            print("The list is empty.")
            return None
        slow_pointer=self.head
        fast_pointer=self.head
        while fast_pointer and fast_pointer.next:
            slow_pointer=slow_pointer.next
            fast_pointer=fast_pointer.next.next
        print("\nMiddle node:",slow_pointer.data)

    def duplicates(self):
        if self.head is None:
            print("List is empty")
            return
        current_node = self.head
        while current_node and current_node.next:
            if current_node.data == current_node.next.data:
                 current_node.next = current_node.next.next
            else:
                current_node = current_node.next

    def reversing(self):
        previous_node= None
        current_node=self.head
        while current_node:
            next_node=current_node.next
            current_node.next=previous_node
            previous_node=current_node
            current_node=next_node
        self.head=previous_node

    def loop(self):
        if self.head is None:
            print("The list is empty,so no loop")
        else:
            slow_pointer=self.head
            fast_pointer=self.head
            while fast_pointer and fast_pointer.next:
                slow_pointer = slow_pointer.next
                fast_pointer = fast_pointer.next.next
                if slow_pointer == fast_pointer:
                    print("Loop detected!")
                    return
            print("No loop found.")


    def display(self):
        current_node=self.head
        while current_node:
            print(current_node.data,end="-->")
            current_node=current_node.next

li=Linkedlist()
li.add_end(50)
li.add_end(150)
li.add_end(250)
li.add_end(350)
li.add_end(450)
li.add_beg(10)
li.display()
print("\n")
li.del_beg()
li.display()
print("\n")
li.reversing()
li.display()
print("\n")
li.duplicates()
print("\n")
li.head.next.next.next.next = li.head  
li.loop()
print("\n")
li.find_middle()