'''2.Write a Python function that takes a list and returns a new list with distinct elements from the first list.
Sample List : [1,2,3,3,3,3,4,5]
Unique List : [1, 2, 3, 4, 5]'''

def unique_list(numbers):
    unique = []
    for item in numbers:
        if item not in unique:
            unique.append(item)
    return unique

print(unique_list([1, 2, 3, 3, 3, 3, 4, 5]))
