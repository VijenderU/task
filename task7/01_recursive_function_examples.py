## example 1

## Sum of natural numbers
def sum_natural_numbers(n):

    if n <= 1:
        return n
    else:
        return n + sum_natural_numbers(n-1)

num = int(input("Enter a number to find sum of natural numbers : "))
print(sum_natural_numbers(num))


## example 2

## Fibonacci series
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

count = int(input("Enter the limit: "))
if count <= 0:
    print("Enter a number greater than 0")
else:
    for i in range(count):
        print(fib(i), end=" ")


## example 3

## finding the power of a number
def power(base,exp):
    if exp == 0:
        return 1
    elif exp == 1:
        return base
    else:
        return base * power(base,exp-1)
    
b = int(input("Enter the base value : "))
e = int(input("Enter the exponent value: "))
print("The result is: ", power(b,e))


## example 4

def fact(n):
    if n == 1 or n== 0:
        return 1
    else:
        return n * fact(n-1)

num = int(input("Enter a number: "))
if num < 0:
    print("Negative numbers are not allowed.")
else:
    print("Factorial is: ", fact(num))
