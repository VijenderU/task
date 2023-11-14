# Multilevel Inheritance

#Base Class
class Employees:
    def Name(self):
        print("Employee Name: XYZ")

# Intermediate Class
class salary(Employees):
    def Salary(self):
        print("Salary: 50000")

# Derived Classs
class Designation(salary):
    def desig(self):
        print("Designation: Software Developer")


call = Designation()
call.Name()
call.Salary()
call.desig()
