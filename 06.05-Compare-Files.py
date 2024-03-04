# The name of the file can be a string
inputfilenameA = "06.05 CompareFileA.txt"
inputfilenameB = "06.05 CompareFileB.txt"
differences = 0
linenumber = 0
# Open the input file A for reading
inputfileA = open(inputfilenameA, 'r')
# Open the input file B for reading
inputfileB = open(inputfilenameB, 'r')  
# Read the first line
lineA = inputfileA.readline()
lineB = inputfileB.readline()
linenumber += 1
# Read until the input is empty
while lineA != "" and lineB != "":
# An empty line contains only a linefeed
    if lineA != lineB:
        print("Line: {} - File A: {}".format(linenumber, lineA))
        print("Line: {} - File B: {}".format(linenumber, lineB))
# increment difference count
        differences += 1
# Read the next line
    lineA = inputfileA.readline()
    lineB = inputfileB.readline()
    linenumber += 1
# Close both files
print("{} differences".format(differences))
inputfileA.close()
inputfileB.close()
