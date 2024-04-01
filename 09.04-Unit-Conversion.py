# Create 2D List to hold conversion table
conversiontable = []
# Open a file for reading
conversionfile = open("09.04 Conversion.txt")
# Read the first line of the file
x = conversionfile.readline()
# End of file is indicated when the input is empty
while x != "":
# Print the contents - Note the embedded linefeeds
    y = x.split()
    conversiontable.append(y)
# Read the next line of the file
    x = conversionfile.readline() 
# Close the file
conversionfile.close()
# Enter Values
FromValue = input("Enter From Value: ")
FromUnit = input("Enter From Unit (mm, cm, m, km, in, yd, mi): ")
ToUnit = input("Enter To Unit (mm, cm, m, km, in, yd, mi): ")
# Set the indexes to zero
FromIndex = 0
ToIndex = 0
# Search the zeroth row of the conversion table for the FromUnit
for i in range(len(conversiontable[0])):
    # Look for the From Unit
    if conversiontable[0][i] == FromUnit:
        # From Unit Found - save column index
        FromIndex = i
        break
# Search the zeroth column of the conversion table fo the ToUnit
for i in range(len(conversiontable)):
    # Look for the To Unit
    if conversiontable[i][0] == ToUnit:
        # To Unit found - save the row index
        ToIndex = i
        break
# Error if From Index not found
if FromIndex == 0:
    print ("Invalid From Value")
# Error if To Index not found
elif ToIndex == 0:
    print ("Invalid To Value")
else:
    # Mutiply From Unit by conversion factor and print
    print("{} {} => {} {}".format(float(FromValue), FromUnit, round(float(FromValue) * float(conversiontable[FromIndex][ToIndex]),7),ToUnit))
