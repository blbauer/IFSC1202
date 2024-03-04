# The name of the file can be a string
inputfilename = "06.Project Input File.txt"
outputfilename = "06.Project Output File.txt"
inputrecordcount = 0
mergefilerecordcount = 0
# Open the input file for reading
inputfile = open(inputfilename, 'r')
# Open the output file for writing
outputfile = open(outputfilename, 'w')  
# Read the first line of the input file
line = inputfile.readline()
# Read until the input is empty
while line != '':
# check to see 
    if line == "**Insert Merge File Here**\n":
        mergefilename = "06.Project Merge File.txt"
        mergefile = open(mergefilename, "r")
        mergeline = mergefile.readline()
        while mergeline != "":
# Found a record - increment the record count
            mergefilerecordcount = mergefilerecordcount + 1
# Write to the output file
# Note that line already contains a linefeed character,
# so we don't have to add one when we write it.
            outputfile.write(mergeline)
# Read the next line in the merge file
            mergeline = mergefile.readline()
        mergefile.close()
# The last line does not have a newline character, We will have to add it
        outputfile.write("\n")
# Read the next line of the input file
        line = inputfile.readline()
    else:
# Found a record - increment the record count
        inputrecordcount = inputrecordcount + 1
# Write to the output file
# Note that line already contains a linefeed character,
# so we don't have to add one when we write it.
        outputfile.write(line)
# Read the next line of the input file
        line = inputfile.readline()
# End of File on input file
# Close both files
inputfile.close()
outputfile.close()
print("{} input file records".format(inputrecordcount))
print("{} merge file records".format(mergefilerecordcount))
print("{} output file records".format(inputrecordcount + mergefilerecordcount))