inputFile = "07.Project Angles Input.txt"
outputFile = "07.Project Angles Output.txt"

input = open(inputFile, 'r')
output = open(outputFile, 'w')

recordCount = 0
decimalDegrees = 0.0
degrees = 0.0
minutes = 0.0
seconds = 0.0
i = 0

ddmmss = input.readline()

def ParseDegreeString(ddmmss):
    i = ddmmss.find(chr(176)) 
    if (ddmmss[i-2] == '"'):
        degreeNum = ddmmss[i-1]
    else:
        degreeNum = ddmmss[i-2] + ddmmss[i-1]
    degrees = float(degreeNum)

    j = ddmmss.find('\'') 
    if ddmmss[j-2] == chr(176):
        minsNum = ddmmss[j-1]
    else:
        minsNum = ddmmss[j-2] + ddmmss[j-1]
    minutes = float(minsNum)
    
    k = ddmmss.find('"') 
    if ddmmss[k-2] == '\'':
        secsNum = ddmmss[k-1]
    else:
        secsNum = ddmmss[k-2] + ddmmss[k-1]
    seconds = float(secsNum)
    return degrees, minutes, seconds

def DDMMSStoDecimal(degrees, minutes, seconds):
    decimalDegrees = (degrees*3600 + minutes*60 + seconds)/3600
    return decimalDegrees

while ddmmss != "":
    degrees, minutes, seconds = ParseDegreeString(ddmmss)
    decimalDegrees = DDMMSStoDecimal(degrees, minutes, seconds)
    output.write(str(decimalDegrees) + "\n")
    recordCount += 1
    ddmmss = input.readline()

print(recordCount, "records processed")

input.close()
output.close()