# Create 2D List to hold distance table
distancetable = []

# Open a file for reading
distancefile = open("09.Project Distances.csv")
# Read the first line of the file
x = distancefile.readline()
# End of file is indicated when the input is empty
while x != "":
#   Remove the newline
    x = x.strip()
#   CSV File - split the line into a list by commas
    y = x.split(",")
#   Appeend the list to the 2D list
    distancetable.append(y)
# Read the next line of the file
    x = distancefile.readline() 
# Close the file
distancefile.close()

# Print the distancetable
for i in range(len(distancetable)):
    for j in range(len(distancetable[i])):
        print("{:>10s}".format(distancetable[i][j]), end="")
    print()

# Enter From City
FromCity = input("Enter From City: ")
# Enter To City
ToCity = input("Enter To City: ")

# Set the indexes to zero
FromIndex = 0
ToIndex = 0

# Search the zeroth row for the From City
for i in range(len(distancetable[0])):
    # Look for the From City
    if distancetable[0][i].upper() == FromCity.upper():
        # From City Found - save column index
        FromIndex = i
        break

# Search the zeroth column for the To City
for i in range(len(distancetable)):
    # Look for the To City
    if distancetable[i][0].upper() == ToCity.upper():
        # To City found - save the row index
        ToIndex = i
        break

# Error if From City not found
if FromIndex == 0:
    print ("Invalid From City")

# Error if To  City not found
if ToIndex == 0:
    print ("Invalid To City")

# From and To City Found - Print the distance
if FromIndex != 0 and ToIndex != 0:
#   Display the From City, To City, and Distance
    print("{} to {} - {} miles".format(FromCity, ToCity, distancetable[FromIndex][ToIndex]))