## 1.Write a Python script to add a key to a dictionary.
#Sample Dictionary : {0: 10, 1: 20}
#Expected Result : {0: 10, 1: 20, 2: 30}


## method 1
dict1 = {0: 10, 1: 20}

dict1[2] = 30

print(dict1)

## method 2 

dict1 = {0: 10, 1: 20}

dict1.update({2:30})

print(dict1)