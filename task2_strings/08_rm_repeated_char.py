## 8.Write a python program to Remove Repeated Character from String.

str1 = input("Enter a string : ")

for char in str1:
    if str1.count(char)>1:
        str1 = str1.replace(char,"")

print(str1)

