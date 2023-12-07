class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Employee Name:", self.name)
        print("Employee Age:", self.age)


emp = Employee("ABC", 25)
emp.display()