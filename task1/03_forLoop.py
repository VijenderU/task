# print the fallowing pattern
'''
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*

'''
for i in range(1,6):
    print("* "*i)
for i in range(4,0,-1):
    print("* "*i)

# 

words= ["Apple", "Banana", "Car", "Dolphin" ]
for word in words:
	print (word)
     
# 
nums = (1, 2, 3, 4)

sum_nums = 0

for num in nums:
    sum_nums = sum_nums + num

print(f'Sum of numbers is {sum_nums}')

#
words= ["Apple", "Banana", "Car", "Dolphin" ]
for word in words:
    print ("The following lines will print each letters of "+word)
    for letter in word:
        print (letter)
    print("")

# 

nums = [1, 2, -3, 4, -5, 6]

sum_positives = 0

for num in nums:
    if num < 0:
        continue
    sum_positives += num

print(f'Sum of Positive Numbers: {sum_positives}')