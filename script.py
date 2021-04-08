# Graph Theory project Text Reader.
# by Owen Kelly
# G00366614@gmit.ie
import os

"""Ask user for a file path to the text file that will be read"""
filepath = input("Enter the file path to your .txt file: ")
# If the file doesn't exist just ask the user again 
while not os.path.isfile(filepath):
    print("Whoops! No such file")
    filepath = input("Enter the file path to your .txt file: ")
# Outputs the file path for the user 
print("You have entered: " + filepath)

print("Outputting the file: ")
# Open the file and read it
with open(filepath) as f:
    for contents in f:
        print(contents)

f.close()
