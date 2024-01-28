import sys, glob, os

# Get the directory name
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']
print(hdir)
# Construct a portable wildcard pattern
# creating a variable that has the pattern path name that can be used by multiple operating systems
pattern = os.path.join(hdir, '*')
print(pattern)
# TODO: Use the glob.glob() function to obtain the list of filenames
# use glob.glob( function to obtain the list of filenames
# glob uses the pattern of file path that has been created by os join and then prints out the files that match that path
files_found = glob.glob(pattern)
print('Here are the found files: ', files_found)
# use os.path.getsize() find each file size
#  for loop is iterating over the files located using the glob function and then getting their size in bytes
# TODO: use os.path.getsize to find each file's size
for pattern in files_found:
    file_size = os.path.getsize(pattern)
    print('These are how big in bytes the files are:', str(pattern), str(file_size))
# TODO: Add a test to only display files that are not zero length
# loop is iterating over the found files located using glob and then only showing if they have byte size over 0
for pattern in files_found:
    file_size = os.path.getsize(pattern)
    # using the if statement to set a condition that it only shows files if it meets condition size over 0
    if file_size > 0:
        print('These are how big in bytes the files are that are over 0:', str(pattern), str(file_size))
# TODO: Remove the leading directory name(s) from each filename before you print it -
# using os.path.basename()
# accepts path like object as argument
# goes to the base of the path file location
for pattern in files_found:
    base = os.path.basename(pattern)
    print('This is the leading directory: ', base)
