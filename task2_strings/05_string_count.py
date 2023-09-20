## 5.Write a python program to count alphabets, digits, and special characters in the string.

str1 = input("Enter a String : ")

alpha_count = 0
digit_count = 0
spel_count = 0

for s in str1 :
    if s.isalpha():
        alpha_count += 1
    elif s.isdigit():
        digit_count += 1
    else:
        spel_count += 1

print(f"Number of alphabets {alpha_count}.\nNumber of digits {digit_count}.\nNumber of special charaters {spel_count}.")