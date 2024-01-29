
# Rana and Katy shared code
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
