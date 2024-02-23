"""
A common security method used for online banking is to ask the user for three random characters from a passcode. For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse the file so as to determine the shortest possible secret passcode of unknown length.
"""

# Note: no 4s or 5s in file

code = 12367890

lines = [int(line) for line in open("Problem079.txt")]

def lineMatch(line, code):
    

def goodCode(code):
    for line in lines:
        if not lineMatch(line, code):
            return(False)
    return(True)

while code:
    if goodCode(code): break
    code += 1

print(code)

blah!
solved by eye :)=