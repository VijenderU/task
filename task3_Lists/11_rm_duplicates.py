## 10.Write a Python program to remove duplicates from a list.

## Method 1 
new_lst = []
lst = eval(input("Enter a list : "))

for num in lst:
    if num not in new_lst:
        new_lst.append(num)
print(f"final list is {new_lst}")


## Method 2 

lst = eval(input("Enter a list : "))

[new_lst.append(num) for num in lst if num not in new_lst ]

print(new_lst)

# Method 3

"""By this method first occurance of duplicate elements removed first later elements present in the list """

lst = eval(input("Enter a list : "))
new_lst = []

for num in lst:
    new_lst.append(num)
    if new_lst.count(num)>1:
        new_lst.remove(num)
print(new_lst)
