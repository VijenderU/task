## 01 filtering list of strings
lst = ['apple', 'banana', 'cherry', 'date']
char = 'a'
filtered_lst = list(filter(lambda x: char in x, lst))
print(filtered_lst)


## 02 filtering a list of dictionaries
lst = [{'name': 'John', 'age': 25}, {'name': 'Jane', 'age': 20}, {'name': 'Bob', 'age': 30}]
filtered_lst = list(filter(lambda x: x['age'] > 25, lst))
print(filtered_lst)


## 03 filtering list of  tuples
lst = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
filtered_lst = list(filter(lambda x: x[1] >= 90, lst))
print(filtered_lst)

## 04 prime number filtering
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

prime_lst = list(filter(is_prime, range(1, 101)))
print(prime_lst)

## 05 filtering a string
string = "Hello, World!"
vowels = "aeiou"
filtered_str = ''.join(filter(lambda x: x in vowels, string))
print(filtered_str)

## 06 fltering list of list
lst = [[1], [2], [3], [4], [5,6]]
filtered_lst = list(filter(lambda x: len(x) > 1, lst))
print(filtered_lst)
