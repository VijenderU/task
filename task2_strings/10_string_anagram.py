## 10.Write a python program to check string is anagrams or not in Python.
str1 = input("Enter first string : ") 
str2 = input("Enter secound string : ")

if len(str1) != len(str2):
    print("The given strings are not Anagrams.")
else:
    if sorted(str1) == sorted(str2):
        print("The given strings are Anagrams.")