## 3.Write a Python program to iterate over dictionaries using for loops

## 1
dict1 = {101:"vijender", 102 : "praveen", 103 : "john"}


for key in dict1:
    print(key, dict1[key])

## 2 
dict1 = {101:"vijender", 102 : "praveen", 103 : "john"}

for key, value in dict1.items():
    print(key,value)