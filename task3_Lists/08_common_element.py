# ## 8.Write a Python function that takes two lists and returns True if they have at least one common member.

# Method 1

lst1 = eval(input("Enter first list : "))
lst2 = eval(input("Enter second list : "))

res = False
for i in lst1 :
    for j in lst2:
        if i == j:
            res = True
print(res)

# Method 2

lst1 = eval(input("Enter first list : "))
lst2 = eval(input("Enter second list : "))

result = False
for i in lst1:
    if i in lst2:
        result = True
        break
print(result)

# Method 3

lst1 = eval(input("Enter first list : "))
lst2 = eval(input("Enter second list : "))

res =[True if x in lst2 else False for x in lst1 ]

if sum(res) > 0:
    print(True)
else:
    print(False)