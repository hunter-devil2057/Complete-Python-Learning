# Write a python program to print the contents of a directory using the OS modules.
# Search online for the function which does that

# importing os modules from Python 
import os

# Select the directory whose content you want to list
# By Default '/your/directory/path'
directory_path='/'

# Using the os module to list the directory content
contents=os.listdir(directory_path)

# Printing the contents (each file and directory name) of the directory
for items in contents: 
    print(items)