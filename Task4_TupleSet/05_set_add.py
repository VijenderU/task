## 5.Write a Python program to add members to a set.

set1 = eval(input("Enter a set :"))
mem = eval(input("Enter Second set to add to first set : "))

set1.update(mem)

print(set1)
