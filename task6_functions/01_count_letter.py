'''1.Write a Python function that accepts a string and counts the number of upper and lower case letters.
Sample String : 'The quick Brow Fox'
Expected Output :
No. of Upper case characters : 3
No. of Lower case Characters : 12'''

def upper_lower_count(str1):
    upper_tot = 0
    lower_tot = 0
    for s in str1:
        if s.isupper():
            upper_tot += 1
        if s.islower():
            lower_tot += 1

    print(f'No. of Upper case characters : {upper_tot}')
    print(f'No. of Lower case Characters : {lower_tot}')


string1 = 'The quick Brow Fox'

upper_lower_count(string1)