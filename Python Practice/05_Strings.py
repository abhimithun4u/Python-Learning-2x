# Author:Abhishek Mukherjee
# Topic: Strings

# Concatenating Two Strings
fname = "Abhishek"
lname = "Mukherjee"
fullname = fname + " " + lname
print("Hello", fullname)  # Output Hello Abhishek Mukherjee

# String Slicing # String index starts from 0 to len-1 # fname[0] prints first character of fname
print(fname[0] + lname[0])  # Output AM

# program to slice Abhi from Abhishek where fname is Abhishek
print("Welcome", fname[0:4])  # Output : Welcome Abhi

# Negative index, write a program to find the last four word of a given string
name = "Abhishek005"
print(name[-4:])  # Output : k005

# Slicing with Skip values # 0::2 will start from 0 to end skipping 1 character at a time
quote = "Welcome to Python Programming"
print(quote[0::2])  # Output: Wloet yhnPormig

# Finding string length using len() function
text = "Welcome to Python Programming,Python is super easy!"
length = len(text)
print("The length of the above string is ", length)  # Output: The length of the above string is  51

# endswith() function of string where we can identify if the above string ends with a given string.
# it returns True or False
print(text.endswith("easy!"))  # Output: True

# count() counts the provided characters withing a string
text = "Welcome to Python Programming,Python is super easy!"
print(text.count("Python"))  # output : 2

# capitalize() function makes the first letter of the string in upper case
text2 = "this is string in lowercase"
print(text2.capitalize())  # Output: This is string in lowercase

# upper(): Returns a copy of the string with all characters converted to uppercase.
s = "hello, world!"
print(s.upper())  # Output: "HELLO, WORLD!"

# lower(): Returns a copy of the string with all characters converted to lowercase.
s = "Hello, World!"
print(s.lower())  # Output: "hello, world!"

# title(): Returns a copy of the string with the first character of each word capitalized.
s = "hello, world! this is my first python program"
print(s.title())  # Output: "Hello, World! This Is My First Python Program"

# find(substring): Returns the index of the first occurrence of a substring in the string, or -1 if not found.
s = "hello, world!"
print(s.find("world"))  # Output: 7

# replace(old, new): Returns a copy of the string with all occurrences of the old substring
# replaced by the new substring.
s = "hello, world!"
print(s.replace("world", "Python"))  # Output: "hello, Python!"

# strip(): Returns a copy of the string with leading and trailing whitespace removed. it is like trim function
s = "   hello, world!   "
print(s.strip())  # Output: "hello, world!"

# split(separator): Returns a list of substrings obtained by splitting the string at each occurrence
# of the specified separator.
s = "hello, world!"
print(s.split(","))  # Output: ['hello', ' world!']
