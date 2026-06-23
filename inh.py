#SINGLE
class Parent:
    def land(self):
        print("i have 10 acres of land")
class Child(Parent):
    pass
obj=Child()
obj.land()



#MULTIPLE
class Parent1:
    def land(self):
        print("i have 10 acres of land")
class Parent2:
    def gold(self):
        print("i have 10 acres of gold")
class Child(Parent1,Parent2):
    #pass
    obj = Child()
# obj.land()
# obj.gold()
print("Hello")