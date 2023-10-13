'''3.Write a Python function to check whether a string is a pangram or not.
Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
For example : "The quick brown fox jumps over the lazy dog".'''

def ispangram(str1):
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	for char in alphabet:
		if char not in str1.lower():
			return False

	return True
	
string1 = 'the quick brown fox jumps over the lazy dog'
if(ispangram(string1) == True):
	print("The given string is pangram!")
else:
	print("The given string not is pangram!")
