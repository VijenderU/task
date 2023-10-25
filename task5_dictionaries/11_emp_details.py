## write a python program that allows you to add an employee with domain, name, empid, and email details using user input and then print the employee's details.

emp_details = {}
emp_num = int(input("How many employees you want to add : "))

for emp in range(emp_num):
    name = input(f"Enter employee {emp+1} name : ")
    empid = input(f"Enter employee {emp+1} ID: ")
    domain = input(f"Enter employee {emp+1} domain : ")
    email = input(f"Enter employee {emp+1} Email ID :")

    emp_details[empid] = {"Name":name, "Domain":domain, "Email":email}

print(emp_details)