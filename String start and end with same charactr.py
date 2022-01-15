# Python program to check if a string starts
# and ends with the same character

# import re module as it provides
# support for regular expressions
import re

# the regular expression
regex = r'^[a-z]$|^([a-z]).*\1$'

# function for checking the string
def check(string):

	# pass the regular expression
	# and the string in the search() method
	if(re.search(regex, string)):
		print("Valid")
	else:
		print("Invalid")

if __name__ == '__main__' :

	sample1 = "abba"
	sample2 = "a"
	sample3 = "abcd"

	check(sample1)
	check(sample2)
	check(sample3)
