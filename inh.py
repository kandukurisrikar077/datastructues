"""#SINGLE
class Parent:
    def land(self):
        print("i have 10 acres of land")
class Child(Parent):
    pass
obj=Child()
obj.land()"""


#MULTIPLE
class Parent1:
    def land(self):
        print("i have 10 acres of land")

class Parent2:
    def gold(self):
        print("i have 10 acres of gold")

class Child(Parent1, Parent2):
    pass

obj = Child()   
obj.land()
obj.gold()

class Parent1:
    def land(self):
        print("I have 10 acres of land")

class Parent2(Parent1):
    pass

class Parent3(Parent2):
    pass

class Child(Parent3):
    pass

obj = Child()
obj.land()

#polymorphism