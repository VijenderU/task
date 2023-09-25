## 1.write a python program to merge two lists.

#Method 1

lst1 = eval(input("Enter First list : "))
lst2 = eval(input("Enter second list : "))

lst3 = lst1 + lst2

print(f"Final list : {lst3}")


## Method 2

lst_first = eval(input("Enter First list : "))
lst_second = eval(input("Enter second list : "))

lst_first.extend(lst_second)

print(lst_first)