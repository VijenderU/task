## 2.Write a program to check String is Palindrome or not.

str1 = input("Enter a string : ")

if str1 == str1[::-1]:
    print("The String is Palindrome")
else:
    print("The String is not Palindrome")