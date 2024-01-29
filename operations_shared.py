# Input is a builtin function that prompts a user for an input
# Program runs and stops at this stage till an input has been entered in the terminal
# Once input has been entered it saves the string in to var, then the program resumes and prints var
var = input("Please enter a value: ")

print(var)

# Upper is a function used to capitalise the string
print(var.upper())

# Len counts the number of characters in the string
print(len(var))

# 'For loop' iterates the string/characters
# It runs the 'isdecimal' function for every character to check if it's a decimal
# 'Any' returns True if any item in an iterable are true, otherwise it returns False
# In this case it will look through each character to find a number and when it locates a number it will return true
# victoria? will the 'any' function run only till it finds a number or will it check every character
includes_digit = any(character.isdecimal() for character in var)
print(includes_digit)