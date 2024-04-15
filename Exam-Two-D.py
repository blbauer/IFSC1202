# properties list
#   Column 0 - Address
#   Column 1 - City
#   Column 2 - State
#   Column 3 - Zip Code
#   Column 4 - Price
properties = []
# open input file for reading
inputfilename = "Exam Two Properties.csv"
inputfile = open(inputfilename, 'r')  
# read the imput file
line = inputfile.readline()
# check for end of file
while line != '':
# split the line
    property = line.split(",")
    property[4] = float(property[4])
# insert into list
    properties.append(property)
# read the next number
    line = inputfile.readline()
# close the input file
inputfile.close()
# zipcodes list
# Column 0 - zip code
# Column 1 - count of the of properties in the zipcode
# Column 2 - sum of the property values in the zipcode
zipcodes = []
# loop through all of the properties
for i in range(len(properties)):
# loop through all the known zip codes
    for j in range(len(zipcodes)):
        if zipcodes[j][0] == properties[i][3]:
            zipcodes[j][1] = zipcodes[j][1] + 1
            zipcodes[j][2] = zipcodes[j][2] + properties[i][4]
            break
    else:
        zipcodes.append([properties[i][3], 1, properties[i][4]])
# Display the results
print(" {:>10s}  {:>5s}   {:>10s}".format("Zipcode","Count", "Average"))
for i in range(len(zipcodes)):
    print("{:>10s}  {:>5d}    ${:>,.2f}".format(zipcodes[i][0],zipcodes[i][1],zipcodes[i][2]/zipcodes[i][1]))