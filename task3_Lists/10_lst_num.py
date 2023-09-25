## 9. Write a Python program to convert a list of multiple integers into a single integer.

# Method 1 
lst = eval(input("Enter a list with numbers : "))#[11, 33, 50]
for i in lst:
    print(i ,end = '')

# Method 2
num  = ''
lst = eval(input("Enter a list with numbers : "))
for i in lst:
    num += str(i)
print(num)