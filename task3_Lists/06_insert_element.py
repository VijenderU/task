## 6.write a python program to insert an elemet  at given index location.


# Method 1
lst = eval(input("Enter a list : "))
element = eval(input("Enter a element : "))
position = int(input("Enter index value : "))

lst.insert(position,element)
print(f"The final list is {lst}")

# Method2

lst = eval(input("Enter a list : "))
element = eval(input("Enter a element : "))
position = int(input("Enter index value : "))

final_list = lst[:position] + [element] + lst[position:]
print(f"The final list is {final_list}")
