## write a python program to find the sum of list elements.

#method 1

lst1 = eval(input("Enter a list : "))

print(f"sum of list elements is {sum(lst1)}")

# method 2 

lst = eval(input("Enter a list : "))

total = 0

for l in lst:
    total = total+l
print(total)