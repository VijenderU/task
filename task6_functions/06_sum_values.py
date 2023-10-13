'''6.write a function to find sum of given values, pass values has variable number of arguments to function.'''


def sum_values(*args):
    return sum(args)

print(sum_values(1, 2, 3, 4, 5))
