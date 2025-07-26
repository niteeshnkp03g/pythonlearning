import os

# Get the current directory
path = "."

# List and print the contents of the directory
files = os.listdir(path)

print("Contents of the current directory:")
for file in files: 
    print(file)
