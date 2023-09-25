## 3.write a python program to print even and odd numbers seperatly in list.

lst = eval(input("Enter a list : "))

even_list = []
odd_list = []

for num in lst :
    if num%2 == 0:
        even_list.append(num)
    else:
        odd_list.append(num)

print(f"Even list is {even_list}\nOdd list is {odd_list}")


# Method 2

list_even = []
list_odd = []

lst1 = eval(input("Enter a list : "))

[list_even.append(num) if num%2 == 0 else list_odd.append(num) for num in lst1]

print(f"Even list is {list_even}\nOdd list is {list_odd}")