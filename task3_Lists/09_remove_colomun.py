## Write a Python program to remove a specified column from a given nested list.
# Method 1 
nst_lst = eval(input("Enter a nested list : ")) # [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
col = int(input("Enter column index : "))

for i in nst_lst:
    del i[col]
print(nst_lst)

# Method 2

nst_lst = eval(input("Enter a nested list : ")) # [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
col = int(input("Enter column index : "))

[i.pop(col) for i in nst_lst]

print(nst_lst)