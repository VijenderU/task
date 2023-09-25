## 5.write a python program to delete given elemet from the list

# Method1

lst = eval(input("Enter a List : "))
element = eval(input("Enter a element you want delete from the list : "))

lst.remove(element)
print(f"The final list is {lst}")

# Method2

new_list = []
lst = eval(input("Enter a List : "))
element = eval(input("Enter a element you want delete from the list : "))

for ele in lst :
    if ele == element:
        pass
    else:
        new_list.append(ele)

print(f"The final new list is {new_list}")
