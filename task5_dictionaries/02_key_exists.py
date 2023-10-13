## 02. Write a Python script to check whether a given key already exists in a dictionary.


dict1 = {101:"vijender", 102 : "praveen", 103 : "john"}
key = 103

if key in dict1:
    print(f"{key} present in dictionary")
else:
    print(f"{key}  not present in dictionary")