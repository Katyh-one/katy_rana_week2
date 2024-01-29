
# Rana and Katy shared code
import sys, glob, os

# Get the directory name (this was imported from Victoria's Git repo)
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']

# Construct a portable wildcard pattern, also imported from Victoria's Git repo.
# • is declaring the wildcard
# creating a variable that has the pattern path name that can be used by multiple operating systems
pattern = os.path.join(hdir,'*')

# TODO: Use the glob.glob() function to obtain the list of filenames
# Declared file names with glob inc pattern
# glob uses the pattern of file path that has been created by os join and then prints out the files that match that path
file_names = glob.glob(pattern)
print(file_names)

# TODO: use os.path.getsize to find each file's size
# "File names" are returned as a list,
# for loop is iterating over the files located using the glob function and then getting their size in bytes
for name_of_file in file_names:
    print(name_of_file + " " + str(os.path.getsize(name_of_file)))

# TODO: Add a test to only display files that are not zero length
# loop is iterating over the found files located using glob and then only showing if they have byte size over 0
for name_of_file in file_names:
    file_size = os.path.getsize(name_of_file)
    if file_size > 0:
        print(name_of_file + " " + str(file_size))


# TODO: Remove the leading directory name(s) from each filename before you print it -
# using os.path.basename()
# accepts path like object as argument
# goes to the base of the path file location
for name_of_file in file_names:
    print(os.path.basename(name_of_file))