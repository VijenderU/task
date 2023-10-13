## 9.Write a Python program to remove a key from a dictionary.

dict1 = {'physics': 80, 'math': 90, 'chemistry': 86}
key = 'physics'

if key in dict1:
    del dict1[key]

print(dict1)