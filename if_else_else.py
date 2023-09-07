# Assigning grades (A, B, C) based on marks obtained by a student
marks = 85

if marks > 90:
    grade = 'A'
elif marks > 75:
    grade = 'B'
elif marks > 65:
    grade = 'C'
else:
    grade = 'D'

print(grade)

# Checking if a number is positive or negative
num = -5

if num >= 0:
    print("Positive number")
else:
    print("Negative number")

# Checking if a number is even or odd

num = 4

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# Checking if a year is a leap year or not

year = 2024

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("Leap year")
else:
    print("Not a leap year")

# if statements to check if a number is positive, negative or zero

num = -1

if num >= 0:
    if num == 0:
        print("The number is zero")
    else:
        print("Positive number")
else:
    print("Negative number")
