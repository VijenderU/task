## 8.Write a Python program to access dictionary key's element by index.
#Expected Output:
#physics
#math
#chemistry

dict1 = {'physics': 80, 'math': 90, 'chemistry': 86}

for key, _ in dict1.items():
    print(key)