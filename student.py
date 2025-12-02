def ParseDegreeString(ddmmss):
    deg_symbol = chr(176)
    min_symbol = "'"
    sec_symbol = '"'
    deg_pos = ddmmss.find(deg_symbol)
    min_pos = ddmmss.find(min_symbol)
    sec_pos = ddmmss.find(sec_symbol)
    deg_str = ddmmss[0:deg_pos]
    min_str = ddmmss[deg_pos + 1:min_pos]
    sec_str = ddmmss[min_pos + 1:sec_pos]
    degrees = float(deg_str)
    minutes = float(min_str)
    seconds = float(sec_str)
    return degrees, minutes, seconds
def DDMMStoDecimal(degrees, minutes, seconds):
    decimal = degrees + (minutes / 60.0) + (seconds / 3600.0)
    return decimal

print ("\nAngles Conversion Program\n")
infile = open("07.Project Angles Input.txt", "r")
outfile = open("07.Project Angles Output.txt", "w")
record_count = 0
line = infile.readline()
while line != "":
    line = line.strip()
    if line != "":
        deg, mins, secs = ParseDegreeString(line)
        decimal_angle = DDMMStoDecimal(deg, mins, secs)
        outfile.write(str(decimal_angle) + "\n")
        record_count += 1
        line = infile.readline()
infile.close()
outfile.close()
print (str(record_count) + " records processed")