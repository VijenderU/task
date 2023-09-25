## 7.write a python program to check the sizes of given two lists are same.

# Method 1

lst1 = eval(input("Enter First list : "))
lst2 = eval(input("Enter second list : "))

if len(lst1) == len(lst2):
    print("Given two lists sizes are same.")
else:
    print("Given two lists sizes are not same")

# Method 2

lst1 = eval(input("Enter First list : "))
lst2 = eval(input("Enter second list : "))

if sum(1 for n in lst1) == sum(1 for n in lst2):
    print("Given two lists sizes are same.")
else:
    print("Given two lists sizes are not same")