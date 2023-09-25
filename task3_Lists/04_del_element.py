## 4.write a python program to delete element of given index in list.

#method 1

lst = eval(input("Enter a list : "))
index_num = int(input("Enter index position of element you want to delete : "))

lst.pop(index_num)
print(f"The final list is {lst}")

#Method 2

lst1 = eval(input("Enter a list : "))
index_value = int(input("Enter index position of element you want to delete : "))

del lst1[index_value]
print(f"The final list is {lst1}")
