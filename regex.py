# Graph Theory project Text Reader.
# by Owen Kelly
# G00366614@gmit.ie
import os


def menu():
    """Displays the menu to the user"""
    print("[1]Load a File")
    print("[2]Input Infix")
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


def shunt(infix):
    """Convert Infix expressions to postfix"""
    # eventual output

    postfix = ""
    # the shunting yard operator stack
    stack = ""
    # operator precedence
    prec = {'*': 100, '.': 90, '|': 80}

    # Loop through the input character at a time
    for c in infix:
        print(f"FOR:   c: {c}\tpostfix:  {postfix}\tstack: {stack}")
        # c is an operator
        if c in {'*', '.', '|'}:
            # Check what is on the stack
            while len(stack) > 0 and stack[-1] != '(' and prec[stack[-1]] >= prec[c]:
                # Move operator at top of stack to output
                postfix = postfix + stack[-1]
                # remove operator from stack
                stack = stack[:-1]
            # push c to stack
            stack = stack + c
        elif c == '(':
            # Push c to the stack
            stack = stack + c
        elif c == ')':
            while stack[-1] != "(":
                # Move operator at top of stack to output
                postfix = postfix + stack[-1]
                # remove operator from stack
                stack = stack[:-1]
             # remove open bracket  from stack
            stack = stack[:-1]
        # c is a non-special
        else:

            postfix = postfix + c
    while len(stack) != 0:
        print(f"While:   c: {c}\tpostfix:  {postfix}\tstack: {stack}")
        # Move operator at top of stack to output
        postfix = postfix + stack[-1]
        # remove operator from stack
        stack = stack[:-1]
    return postfix


def infixInput():
        infix = input("Enter an infix expression ")
        print(f"Infix: {infix}") 
        print(f"PostFix: {shunt(infix)}")
        print()

# Menu Call and option logic
menu()
option = int(input("Enter your option "))

while option != 0:
    if option == 1:
        loadFile()
    elif option == 2:
        infixInput()
    elif option == 3:
        print("This is option 3")
    else:
        print("Invalid Option")

    print()
    menu()
    option = int(input("Enter your option "))

print()
print("--Exiting Program--")
