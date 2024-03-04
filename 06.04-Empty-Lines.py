# The name of the file can be a string
inputfilename = "06.04 EmptyLinesInput.txt"
outputfilename = "06.04 EmptyLinesOutput.txt"
inputrecordcount = 0
outputrecordcount = 0
# Open the input file for reading
inputfile = open(inputfilename, 'r')
# Open the output file for writing
outputfile = open(outputfilename, 'w')  
# Read the first line
line = inputfile.readline()
# Read until the input is empty
while line != '':
# Increment the input count
     inputrecordcount += 1
# An empty line contains only a linefeed
     if line != "\n":
# Note that line already contains a linefeed character,
# so we don't have to add one when we write it.
          outputfile.write(line)
# increment the output count
          outputrecordcount += 1
# Read the next line
     line = inputfile.readline()
# Close both files
inputfile.close()
outputfile.close()
print("{} records read".format(inputrecordcount))
print("{} records written".format(outputrecordcount))
