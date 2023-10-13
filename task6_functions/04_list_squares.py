'''4.Write a Python function to create and print a list where the values are the squares of numbers between 1 and 10 (both included).
'''

def squares_list():
    squa_list = []
    for num in range(1,11):
        squa_list.append(num*num)

    return squa_list

print(squares_list())