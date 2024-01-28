# Question 1
import glob
import os

# os.environ is a mapping object
# It returns a dictionary having the user's environment variable as key and their values as value
# It's a list
home = os.environ['HOMEPATH']
# will output home drive
print(home)

# os.path.join(path, *paths) - makes the file path usable across operating systems
# path is the first part of the file or folders address - usually a string
# *paths - parts of the file or folders address you want to add to the first part - usually a string
# method concatenates the paths whilst inserting the separator
# os.path.join
getintotech_path = ['Code', 'Getintotech2024', 'Python_projects', '1_Python_practice', 'exercise8', 'say_my_name.py']

full_path = os.path.join(*getintotech_path)
print("Full path:", full_path)

# glob.glob()
# retrieves files/ path names matching a specific pattern
# wildcards * ? [ranges]
# wildcard * matches any sequence of characters
# gets the paths of any files in directory
print('Wildcard no specified file type')
for name in glob.glob('C:/Code/Getintotech2024/*'):
    print(name)

# gets the path of txt files - should bring back all xlsx files but not returning any
print('Wildcard file type')
for name in glob.glob('C:/Code/Getintotech2024/*PNG'):
    print(name)

# os.path.getsize()
# returns the size of bytes in the path
size = os.path.getsize('C:/Code/Getintotech2024/')
print(size)

# os.path.basename()
# accepts path like object
# goes to the base of the path file location
base = os.path.basename("C:/Code/Getintotech2024")
print(base)

# Exercise 10

# get the directory
home = os.environ['HOMEPATH']


# construct a portable wildcard pattern using ospathjoin
# creating the path of the directory where the files live
directory = '/Code/Getintotech2024/HTML_Practice'
# using the wildcard * for it to find any file that is .html
wildcard_pattern = '*.html'
# creating a variable that creates the pattern path name that can be used by multiple operating systems
file_path = os.path.join(directory, wildcard_pattern)
print(file_path)
# use glob.glob( function to obtain the list of filenames
# glob uses the pattern of file path that has been created by os join and then prints out the files that match that path
files_found = glob.glob(file_path)
print('Here are the found files: ', files_found)
# use os.path.getsize() find each file size
#  for loop is iterating over the files located using the glob function and then getting their size in bytes
for file_path in files_found:
    file_size = os.path.getsize(file_path)
    # using the string function to convert the output from bytes to string
    print('These are how big in bytes the files are:', str(file_path), str(file_size))
# add test to only display files that are not zero length - added an empty html file to my folder to do this
for file_path in files_found:
    file_size = os.path.getsize(file_path)
    # using the if statement to set a condition that it only shows files if it meets condition size over 0
    if file_size > 0:
        print('These are how big in bytes the files are that are over 0:', str(file_path), str(file_size))

