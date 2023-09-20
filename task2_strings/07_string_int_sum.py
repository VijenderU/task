## 7.Write a python program to find sum of integers in the string.

str1 = input("Enter a string which contain digits  : ")

total = 0
for s in str1:
    if s.isdigit():
        total = total + int(s)
print("Sum of digits in the string : ",total)