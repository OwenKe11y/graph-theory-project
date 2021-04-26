# Graph Theory project Text Reader.
# by Owen Kelly
# G00366614@gmit.ie
import os

# Thompsons Construction


class State():
    """A State and its arrows in thompsons construction"""
    # Constructor

    def __init__(self, label, arrows, accept):
        """Label is the arrow labels, arrows is a list of states to point to, accept is a boolean as to whether this is an accept state"""
        self.label = label
        self.arrows = arrows
        self.accept = accept

    def followEs(self):
        """The set of states that are gotten from following this state and all its e arrows"""
        # Include this state in the returned set
        states = {self}
        # If this state has e arrows, i,e label us None.
        if self.label is None:
            # Loop through this states arrows.
            for state in self.arrows:
                # Incorperate that state's earrow states in states
                states = (states | state.followEs())
            # returns the set of states
            return states


class NFA:
    """A non-deterministic finite automaton"""

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def match(self, s):
        """Return true if this NFA instance matches the string s."""
        # list of previous states that we are still in
        previous = self.start.followEs
        # Loop through the string, a character at a time
        for c in s:
            # Start with an empty set of current states
            current = set()
            # loop through the previous states
            for state in previous:
                # Check if there is a c arrow from state.
                if state.label == c:

                    # Add followEs for next state
                    current = (current | state.arrows[0].followEs())
            # replace previous with current
            previous = current
        # if the final state is in previous, that return true. false otherwise
        return (self.end in previous)


def menu():
    """Displays the menu to the user"""
    print("[1]Load a File")
    print("[2]Input Regular Expression")
    print("[3]Search file with regex")
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
        contents = f.read()

    print(contents)
    f.close()
    return contents


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


def re_to_nfa(postfix):
    # stack for nfas
    stack = []
    # loop through postfix r.e left to right
    for c in postfix:

        # concatination
        if c == '.':
            # pop nfa off the stack
            nfa2 = stack[-1]
            stack = stack[:-1]
            # pop the next nfa off the stack
            nfa1 = stack[-1]
            stack = stack[:-1]
            # make accept state of nfa1 non-accept
            nfa1.end.accept = False
            # make it point at the start of nfa2
            nfa1.end.arrows = [nfa2.start]
            # make a new nfa with nfa1's start state and nfa2's end state
            nfa = NFA(nfa1.start, nfa2.end)
            stack.append(nfa)

        elif c == '|':
            # pop nfa off the stack
            nfa2 = stack[-1]
            stack = stack[:-1]
            # pop the next nfa off the stack
            nfa1 = stack[-1]
            stack = stack[:-1]
            # Create new start and end states
            start = State(None, [], False)
            end = State(None, [], True)
            # make a new start state point at old start states
            start.arrows.append(nfa1.start)
            start.arrows.append(nfa2.start)
            # make old accept state of nfa1 non-accept
            nfa1.end.accept = False
            nfa2.end.accept = False
            # make a new nfa
            nfa = NFA(start, end)
            stack.append(nfa)

        elif c == '*':
            # pop 1 nfa off the stack
            nfa1 = stack[-1]
            stack = stack[:-1]
            # Create new start and end states
            start = State(None, [], False)
            end = State(None, [], True)
            # make a new start state point at old start states
            start.arrows.append(nfa1.start)
            # and at the new end state
            start.arrows.append(end)
            # make old accept state non-accept
            nfa1.end.accept = False
            # make old accept state point to new accept state
            nfa1.end.arrows.append(end)
            # make old accept state point to old accept state
            nfa1.end.arrows.append(start)
            # make a new nfa
            nfa = NFA(start, end)
            stack.append(nfa)
        else:
            # Create an NFA for the non-special character c

            # Create the end state
            end = State(None, [], True)
            # Create the start state, pointed at the end state
            start = State(c, [end], False)
            # Create the NFA with the start and end State
            nfa = NFA(start, end)
            # NFA to the nfa stack
            stack.append(nfa)

    if len(stack) != 1:
        return None
    else:
        return stack[0]


def RegInput(file):
    infix = "(a.b|b*)"
    postfix = shunt(infix)
    NonFA = re_to_nfa(postfix)
    print(f"Infix: {infix}")
    print(f"PostFix: {postfix}")
    print()
    print(f"NFA: {NonFA}")

    for word in file:
        print(word)

        for s in word():
            print("test " + s)
            match = NonFA.match(s)
            print(f"Match '{s}': {NonFA.match(s)}")
        print()


def Search(file, regex):
    nfa = re_to_nfa(regex)
    print(nfa)


# Menu Call and option logic
if __name__ == "__main__":
    menu()
    option = int(input("Enter your option "))

    while option != 0:
        if option == 1:
            contents = loadFile()
        elif option == 2:
            

            for word in contents:
                infix = "(a.b|b*)"
                postfix = shunt(infix)
                NonFA = re_to_nfa(postfix)
                print(f"Infix: {infix}")
                print(f"PostFix: {postfix}")
                print()
                print(f"NFA: {NonFA}")
                for s in word:
                    print("test " + s)
                    match = NonFA.match(s)
                    print(f"Match '{s}': {NonFA.match(s)}")
                print()
        elif option == 3:
            print("poo")
        else:
            print("Invalid Option")
        print()
        menu()
        option = int(input("Enter your option "))

    print()
    print("--Exiting Program--")
