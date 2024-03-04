# Converts Fahrenheit to Celsius
def FahrToCel(Fvalue):
    return (Fvalue - 32.0) * 5.0 / 9.0
# The name of the file can be a string
inputfilename = "06.03 FTemps.txt"
outputfilename = "06.03 CTemps.txt"
recordcount = 0
# Open the input file for reading
inputfile = open(inputfilename, 'r')
# Open the output file for writing
outputfile = open(outputfilename, 'w')  
# Read the first line
ftemp = inputfile.readline()
# Read until the input is empty
while ftemp != '':
# Float the input and convert it to Celsius
    ctemp = FahrToCel(float(ftemp))
# Round the result to one digit, convert to string, and write it
    outputfile.write("{:5.1f}".format(ctemp) + "\n")
# Increment the record count
    recordcount += 1
# Read the next line
    ftemp = inputfile.readline()
# Close both files
inputfile.close()
outputfile.close()
print("{} records written".format(recordcount))
