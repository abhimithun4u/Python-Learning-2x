# Author: Abhishek Mukherjee
# Topic : Escape Sequence

# \n:Represents a newline character. It moves the cursor to the beginning of the next line.
print("Line 1\nLine 2")
# Output:
# Line 1
# Line 2

# \t: Represents a tab character. It moves the cursor to the next tab stop.
print("Item\tPrice")
print("Apple\t$1.00")
# Output:
# Item    Price
# Apple   $1.00

# \: Represents a single backslash character.
print("C:\\Users\\John")
# Output: C:\Users\John

# ': Represents a single quote character within a single quoted string.
print('It\'s raining')
# Output: It's raining

# \r: Represents a carriage return character. It moves the cursor to the beginning of the current line
print("123\rabc")  # Carriage return replaces the digits with 'abc'
# Output: abc
