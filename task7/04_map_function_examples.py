## 01 Tripling all numbers in a list
lst = [1, 2, 3, 4, 5]
triple_lst = list(map(lambda x: x * 3, lst))
print(triple_lst)

## 02 adding given three lists
lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
lst3 = [7, 8, 9]
sum_lst = list(map(lambda x, y, z: x + y + z, lst1, lst2, lst3))
print(sum_lst)

## 03 Listifying the list of given strings individually

lst = ['apple', 'banana', 'cherry']
listified_lst = list(map(list, lst))
print(listified_lst)

## 04 Converting all characters into uppercase to lowercase  vicevursa from a given sequenceConverting
seq = "Hello World"
processed_seq = ''.join(list(map(lambda x: x.lower() if x.isupper() else x.upper(), seq)))
print(processed_seq)


## 05 finding the difference between two lists
lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
diff_lst = list(map(lambda x,y: abs(x-y), lst1,lst2))
print(diff_lst)
