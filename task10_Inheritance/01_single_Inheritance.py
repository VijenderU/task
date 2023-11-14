# Parent class
class Parent:
    def __init__(self):
        self.parent_name = "Parent"
    
    def display(self):
        print("Parent class method called")

# Child Class        
class Child(Parent):
    def __init__(self):
        self.child_name = "Child"
        
    def display(self):
        print("Child class method called")
        
c = Child()
c.display()
