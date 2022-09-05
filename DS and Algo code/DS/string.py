#find position of a substring in python
#Python 3 onwards
sub_str = "ful"
str1 = "beautiful"
print(str1.find(sub_str))

# Strings in Python are arrays of characters

# 1.  Loop through characters in String
for char in str1:
    print(char)

# 2. i) Check for substring in string
sub_str in str1

# ii) Check if substring DNE in string
sub_str_not = 'booty'
sub_str_not not in str1

# 3. Slicing strings
str1[2:6]

# 4. Modify Strings - upper(), lower(), strip(), replace(), split()
str1.upper()
str1.lower()

str2 = "  Hello World    " # strip()
str2 = str2.strip()

a = "Hello, World!" # replace()
a = a.replace("H", "J")

#Note default delimiter is space - split()
strM = "Hello Prachi What's up bro?"
lstM = strM.split()
print(lstM)

strO = "Spam-Spam-poop-loop"
delimiter = '-'
lstO = strO.split(delimiter)
print(lstO)

# 5. Concatenate 2 strings - + opeartor
str3 = ' girl'
print(str1+str3)
#Note - cannot concatenate non strings

# 6. Format strings to add non string variables into strings
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
myorder1 = myorder.format(quantity, itemno, price)

#OR
myorder2 = ("I want %s pieces of item %s for %s dollars." %(quantity, itemno, price))

# All string methods:
# capitalize()	Converts the first character to upper case
# count()	Returns the number of times a specified value occurs in a string
# endswith()	Returns true if the string ends with the specified value
# find()	Searches the string for a specified value and returns the position of where it was found
# format()	Formats specified values in a string
# index()	Searches the string for a specified value and returns the position of where it was found
# isalnum()	Returns True if all characters in the string are alphanumeric
# isalpha()	Returns True if all characters in the string are in the alphabet
# isdecimal()	Returns True if all characters in the string are decimals
# isdigit()	Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isspace()	Returns True if all characters in the string are whitespaces
# isupper()	Returns True if all characters in the string are upper case
# join()	Joins the elements of an iterable to the end of the string
# lower()	Converts a string into lower case
# lstrip()	Returns a left trim version of the string
# replace()	Returns a string where a specified value is replaced with a specified value
# rfind()	Searches the string for a specified value and returns the last position of where it was found
# rindex()	Searches the string for a specified value and returns the last position of where it was found
# rsplit()	Splits the string at the specified separator, and returns a list
# rstrip()	Returns a right trim version of the string
# split()	Splits the string at the specified separator, and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()	Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()	Converts the first character of each word to upper case
# translate()	Returns a translated string
# upper()	Converts a string into upper case 