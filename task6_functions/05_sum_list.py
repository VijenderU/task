'''5.Write a Python function to sum all the numbers in a list.
Sample List : (8, 2, 3, 0, 7)
Expected Output : 20'''

def sum_list(lst):
    return sum(lst)


print(sum_list((8, 2, 3, 0, 7)))


## 2
def list_sum(lst):
    tot = 0
    for i in lst:
      tot += i
    return tot


print(list_sum((8, 2, 3, 0, 7)))
