# capitalize() 
# it converts the first character of a string to uppercase

string = "hello world"
print(string.capitalize())

# casefold()
# casefold(): Converts a string to lowercase.

string = "HELLO WORLD"
print(string.casefold())

# center()
string = "hello"
print(string.center(10))

# count()
string = "hello world"
print(string.count("l")) 


# endswith()
string = "hello world"
print(string.endswith("world"))

# find()
string = "hello world"
print(string.find("world"))

# index()
string = "hello world"
print(string.index("world"))


# isalnum()
string = "hello123"
print(string.isalnum())


# isalpha()
string = "hello"
print(string.isalpha())

# isdigit()
string = "123"
print(string.isdigit())


# islower()
string = "hello"
print(string.islower()) 

# isupper()
string = "HELLO"
print(string.isupper()) 


# join()
list_of_strings = ["hello", "world"]
separator = "-"
print(separator.join(list_of_strings))

# lower()
string = "HELLO WORLD"
print(string.lower())


# lstrip()
string = "00000hello world00000"
print(string.lstrip("0"))

# replace()
string = "hello world"
print(string.replace("world", "python"))

# rfind()
string = "hello world"
print(string.rfind("l"))


# rindex()
string = "hello world"
print(string.rindex("l"))


# rstrip()
string = "_____hello world_____"
print(string.rstrip('_')) 

# split()
string = "hello,world"
print(string.split(","))


# startswith()
string = "hello world"
print(string.startswith("hello")) 

# strip()
string = "____hello world_____"
print(string.strip('_'))


# upper()
string = "hello world"
print(string.upper()) 
