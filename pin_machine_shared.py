
# Rana's version
import getpass

# Set variable for correct pin code
pin = {8888}

# Count function will restrict pin attempts to three and to end if entered incorrect 3 times

attempts = 1
max_attempts = 3
count = 1

# Input function to request pin code
# Using "while true" function to allow the code to be repeated
# int is makes sure the input is a number
# Getpass used to hide characters typed in the pin get.pass is an imported module
# The "in" function is used to check if the value is present
while True:
    supplied_pin = int(getpass.getpass("Enter your pin: "))
    if supplied_pin in pin:
        print("")
        print("Correct pin")
        print("")
        break
# Else used to repeat question to allow a further attempt if wrong pin is provided & use "else" to prompt to try again
# "F" is used as a prefix for creating f-strings to format strings with the values of variables inserted in to them
# Used the number of attempts/ counts to determine when pin lock message to be returned
# End with a break statement at the end to exit the condition
# Added attempts count at the end to sure it runs in the right order
    else:
        remaining_attempts = max_attempts - attempts

        if remaining_attempts > 0:
            print(f"Incorrect PIN. {remaining_attempts} Attempts remaining. Please try again.")
        count += 1

        if count == 4:
            print("Incorrect pin entered three times, pin locked")
            break
        attempts += 1

# we both did quite similar but slightly different so couldnt decide how to merge
# Katy's version
# from getpass import getpass
# the operand of pin needs to be a string because the output of input is converting the users input to string
# defined the correct pin with string to match output of input as string
pin = '1234'
# defined the initial number of attempts as an integer which can be used to calculate number of attempts
# attempts = 1 - removed as used in range
# defined the count in order to iterate over attempts.
# add 1 to attempts value each time pin entered correctly
# count = 1 removed as used in range
# defined maximum number of time user can enter pin - value integer assigned to variable
max_num_attempts = 3

# used while loop to allow for the prompt to enter pin to run until either
# max number of attempts reacher or pin entered correctly
#
for attempts in range(1, 4):
    # while attempts < 3: removed as used in range
    # supplied_pin = getpass.getpass('Enter your pin: ')
    # input uses the prompt within the function and returns the input of the user as a string
    supplied_pin = input('Enter your pin: ')
    print(supplied_pin)

    # conditional statement
    # if pin given by user equals value of pin stored in variable below if code runs
    # statement returns true
    if supplied_pin in pin:
        print('Have lots of money')
        # added the break to stop the loop continuing to ask for pin
        break
    elif supplied_pin not in pin and attempts < 3:
        # chaining comparison - add value of count to value of attempts
        # attempts += count
        # assign value of attempts to new variable
        # total_attempts = attempts
        # output argument attempts
        print(attempts)
        # print(total_attempts)
        remaining_attempts = max_num_attempts - attempts
        print('Your pin is incorrect, you have ' + str(remaining_attempts) + ' left.')
        # if none of above statements return true, code will run
    else:
        print('Your account is now locked. Have a nice day!')
        # ends loop and stops pin being asked for
        break