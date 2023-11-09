# write a sample calculator python program 

# Addition
def addition():
    '''Adding two numbers'''
    num1 = eval(input("Enter first number: "))
    num2 = eval(input("Enter second number: "))
    return num1+num2

# Subtraction
def subtraction():
    '''Subtracting two numbers'''
    num1 = eval(input("Enter first number: "))
    num2 = eval(input("Enter second number: "))
    return num1-num2

# Multiplication
def multiplication():
    '''multiplication of two numbers'''
    num1 = eval(input("Enter first number: "))
    num2 = eval(input("Enter second number: "))
    return num1*num2

# Division
def division():
    '''division of two numbers'''
    num1 = eval(input("Enter first number: "))
    num2 = eval(input("Enter second number: "))
    return num1/num2

def calculator():

    operation = int(input("Choose one number from below:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n"))

    if operation == 1:
        print(addition())
    elif operation == 2:
        print(subtraction())
    elif operation == 3:
        print(multiplication())
    elif operation == 4:
        print(division())
    else:
        print("Kindly enter valid input\n------------------------------------")
        calculator()

# calling calculator function
calculator()