# Graph Theory project Text Reader.
# by Owen Kelly
# G00366614@gmit.ie
import os

def menu():
    """Displays the menu to the user"""
    print("[1]Load a File")
    print("[2]")
    print("[3]")
    print("[0]Exit program")


# Load Text
def loadFile():
    """Ask user for a file path to the text file that will be read"""

    filepath = input("Enter the file path to your .txt file: ")
    filepathextension = 'txt'
    os.path.join(filepath, "*."+filepathextension)
    # If the file doesn't exist just ask the user again
    while not os.path.isfile(filepath):
        print("Whoops! No such file")

    # Outputs the file path for the user
    print("You have entered: " + filepath)

    # Prints out the file
    print("Outputting the file: ")
    # Open the file and read it
    with open(filepath) as f:
        contents = f.readlines()

    print(contents)
    f.close()


# Menu Call and option logic
menu()
option = int(input("Enter your option "))

while option != 0:
    if option == 1:
        loadFile()
    elif option == 2:
        print("This is option 2")
    elif option == 3:
        print("This is option 3")
    else:
        print("Invalid Option")

    print()
    menu()
    option = int(input("Enter your option "))

print()
print("--Exiting Program--")



