class Parent:
    def __init__(self):
        print("This is Parent")

    def print_parent(self):
        print("Printing parent")

    
class Child(Parent):
    def __init__(self):
        super().__init__()
        print("This is Child")

    def add_child(self):
        self.print_parent()
        print("Adding child")

# c1 = Parent()
c2 = Child()
c2.add_child()