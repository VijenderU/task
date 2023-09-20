### 3.Write a python program to check given character is vowel or consonant.


vowels = ["a","e","i","o","u"]
char = input("Enter a Character : ")

if len(char) == 1:
    if char in vowels:
        print(f"The given charater '{char}' is Vowel.")
    else:
        print(f"The given character '{char}' is Consonant.")
else:
    print("Please enter single charater.")