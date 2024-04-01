# Open the file
inputfile = open("09.06 CityTemps.txt", "r") 
# Create the temps array
temps = []
#Read the imput file
line = inputfile.readline()
# Check for end of file
while line != '':
#   Split the input line into its parts
    tempsdata = line.split()
#   Append the temps data to the temps array
    temps.append(tempsdata)
#   Read the next line
    line = inputfile.readline()
# Close the input file
inputfile.close()
# Calculate the average temperature for each location
# loop through each row in temps
for i in range(len(temps)):
    total = 0.0
#   loop through each column in temps and add the temperature to a total
    for j in range(1,len(temps[i])):
        total += float(temps[i][j])
#   divide the total by the number of columns -1 (due to the cities in the
#   first column) and append the result to a row in the temps array
    avg =  float(total) / float(len(temps[i])-1)
#   convert the avg to an integer, then a string
    temps[i].append(str(int(avg)))
# Create a heading
print("{:8s} {:8s} {:8s} {:8s} {:8s} {:8s} {:8s} {:8s} {:8s}".format("City", "Mo", "Tu", "We", "Th", "Fr", "Sa", "Su", "Avg"))
# Create a each line of data
for i in range(len(temps)):
    for j in range(len(temps[i])):
        print("{:8s}".format(temps[i][j]), end=" ")
    print()
