from functools import reduce

## 01 Finding the sum of a list of numbers
lst = [1, 2, 3, 4, 5]
sum_lst = reduce(lambda x, y: x + y, lst)
print(sum_lst)

## 02 Finding the maximum element in a list
lst = [1, 2, 3, 4, 5]
max_lst = reduce(lambda x, y: x if x > y else y, lst)
print(max_lst)

## 03 Flattening a list of lists

lst = [[1, 2], [3, 4], [5, 6]]
flat_lst = reduce(lambda x,y: x+y,lst)
print(flat_lst)

## 04 Finding the factorial of a number
num = int(input("Enter a number: "))
fact_num = reduce(lambda x,y: x*y, range(1,num+1))
print(fact_num)

## 05 Reversing a string
string = "Hello World"
rev_string = reduce(lambda x,y: y+x,string)
print(rev_string)