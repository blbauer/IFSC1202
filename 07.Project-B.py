def DDMMSStoDecimal(degrees, minutes, seconds):
    # Coverts degrees, minutes, seconds to Decimal Degrees
    # There are 60 minutes in a degree and 3600 seconds in a degree
    decimaldegrees = degrees + (minutes / 60) + (seconds / 3600)
    return decimaldegrees

def ParseDDMMSS(ddmmss):
    # Parses a coordinate string in the format: dd°mm'ss", where
    # dd is the number of degrees
    # mm is the number of minutes
    # ss is the number of seconds
    # Note that char(176) is the degree symbol

    # Find the degree symbol
    degreepos = ddmmss.find(chr(176))
    # Degrees is located between the beginning of the string and the degree symbol position
    degrees = float(ddmmss[:degreepos])
    # find the minutes symbol (')
    minutepos = ddmmss.find("'")
    # Minutes is located between the degree symbol and the minutes symbol position
    minutes = float(ddmmss[degreepos+1:minutepos])
    # Find the seconds symbol
    secondpos = ddmmss.find('"')
    # Seconds is located betwween the minutes symbol position and the seconds symbol position
    seconds = float(ddmmss[minutepos+1:secondpos])
    return degrees, minutes, seconds


inputfilename = "07.Project Angles Input.txt"
inputfile = open(inputfilename, "r")
outputfilename = "07.Project Angles Output.txt"
outputfile = open(outputfilename, "w")
recordcount = 0
# Open the input file for reading

# Read until the input is empty
line = inputfile.readline()
while line != '':
    degrees, minutes, seconds = ParseDDMMSS(line)
    decimaldegree = DDMMSStoDecimal(degrees, minutes, seconds)
    outputfile.write(str(decimaldegree) + "\n")
    recordcount = recordcount + 1
    line = inputfile.readline()
inputfile.close()
outputfile.close()
print(recordcount,"records processed")