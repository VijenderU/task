## 01 Multiplying two numbers

multiply = lambda x, y: x * y
print(multiply(2, 3))


## 02 Sorting a list of tuples

lst = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
lst.sort(key=lambda x: x[1])
print(lst)

## 03 Sorting a list of strings by the last character

lst = ['apple', 'banana', 'cherry', 'date']
lst.sort(key=lambda x: x[-1])
print(lst)

## 04 Sorting a list of dictionaries

lst = [{'name': 'John', 'age': 25}, {'name': 'Jane', 'age': 20}, {'name': 'Bob', 'age': 30}]
lst.sort(key=lambda x: x['age'])
print(lst)

## 05 reversing string
reverse_str = lambda s: s[::-1]
print(reverse_str("Hello, World!"))

## 06 findng string length
str_len = lambda s: len(s)
print(str_len("Hello, World!"))
