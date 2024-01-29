# input is a function
# This function first takes the input from the user and converts it into a string.
# The value of var will be the input from me in answer to the question - it has to be a string
var = input("Please enter a value: ")
# takes the value of var and changes the case of the string to uppercase
# upper case doesn't take an argument
# it's a method
print(var.upper())
# outputs the length of the string in variable var
# len takes an argument - it's a function
print(len(var))
# does it contain numeric characters
# is a method so doesnt take arguments
# is decimal will only print true if all the digits in the string are numeric
print(var.isdecimal())
# using the for loop to iterate over the characters and where one is numeric, output the value and the string
for char in var:
    if char.isdecimal():
        print(char, ' is a numeric value')
    else:
        print(char, ' is not a numeric')
print(type(var))


