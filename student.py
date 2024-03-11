input = open("07.Project Angles Input.txt")
output = open("07.Project Angles Output.txt", "a")

STRING = input.readline()
COUNT = 0

def decimalDegree(ddmmss):
    degSign = ddmmss.find(chr(176))
    minSign = ddmmss.find("'")
    secSign = ddmmss.find('"')
    DD = float(ddmmss[:degSign])
    MM = float(ddmmss[degSign+1:minSign])
    SS = float(ddmmss[minSign+1:secSign])
    decimalDegree = DD + (MM/60) + (SS/3600)
    return decimalDegree


while STRING != "":
    RESULTS = decimalDegree(STRING)
    output.write(str(RESULTS)+"\n")
    STRING = input.readline()
    COUNT += 1
else:
    print("{} Records Processed." .format(COUNT))

input.close()
output.close()
    
