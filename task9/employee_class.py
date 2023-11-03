# create an employee class and add details of employee  using three deferent variables and access that variables in all possible ways.

#name, empid,mbl num, address,  location, company name, country
class Employee:

    company = "Marolix" # class variable

    print(f"Inside the class but outside of the methods Company name :{company}")
    print("\n\n")

    def __init__(self,name,empid):
        # instance variables
        self.name = name
        self.empid = empid

        Employee.country = "India" # static variable

        print(f"In constructor Name : {self.name}, EmpId : {self.empid}") # accessing instance variables
        print(f"In constructor accessing static variables Company : {Employee.company}, Country : {Employee.country}")
        print("\n\n")

    def method1(self):

        self.city = "Hyd" # instance variable
        Employee.country_code = "+91" # static variable
        emp_salary = 50000 # local variable 
        
        print(f"In method Name : {self.name}, EmpId : {self.empid}, City : {self.city}") # accessing instance variables
        print(f"In method accessing static variables Company : {Employee.company}, Country : {Employee.country}")
        print(f"In method accessing static variable : {Employee.country_code}")
        print(f"In method accesing local variable Employee salary : {emp_salary}")
        print("\n\n")

    @classmethod
    def method2_classmethod(cls):

        Employee.office_country = "India" # static variable
        cls.office_contact = "040xxxxxx" # static variable

        print(f"in class method accessig static variables Office contact {Employee.office_contact}, Office country {cls.office_country}")
        print(f"In class method accessing static variables Company : {Employee.company}, Country : {Employee.country}")
        print(f"in class method accessing static variable : {Employee.country_code}")
        print("\n\n")

    @staticmethod
    def method3_staticmethod():
        Employee.domain = "python"

        print(f"In static method accessing static variables Company : {Employee.company}, Country : {Employee.country}")
        print(f"in class method accessig static variables Office contact {Employee.office_contact}, Office country {Employee.office_country}")
        print(f"in method accessing static variable : {Employee.country_code}")
        print(f"Inside static method Employee domain ", Employee.domain)
        print("\n\n")




emp1 = Employee("ABC",101)
emp2 = Employee("XYZ",201)

# calling method1
emp1.method1()
emp2.method1()

# callng class method
emp1.method2_classmethod()
emp2.method2_classmethod()

# calling static method
emp1.method3_staticmethod()
emp2.method3_staticmethod()


emp1.mbl_num = "9989xxxxxx" # instance variable
emp2.mbl_num = "99088xxxxx"   # instance variable

Employee.education = "B.Tech" # static variable out side of the class

print("outside of the class instance variable Country of Emplooyee 1 ", emp1.mbl_num)
print("outside of the class instance variable Country of Emplooyee 2 ", emp2.mbl_num)
print("\n\n")

print("outside of the class static variable Office contact ", Employee.office_contact)
