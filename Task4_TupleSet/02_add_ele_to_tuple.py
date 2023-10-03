## 2.Write a Python program to add an item to a tuple.

#Method 1
tup = eval(input("Enter a tuple: "))

print(tup)
# adding element to the tuple
tup_list = list(tup)
ele = eval(input("Enter a elemet add in the squence : "))
tup_list.append(ele)
tup_add = tuple(tup_list)
print(tup_add)

