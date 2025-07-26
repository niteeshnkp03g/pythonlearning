# Write a python program to print the contents of a directory using the os module. 
# Search online for the function which does that.

import os

path = "."

files = os.listdir(path)

print("Contents of the current directory:")
for file in files: 
    print(file)
