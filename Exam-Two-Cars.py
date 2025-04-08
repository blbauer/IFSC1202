# Cars list
cars = []
# open input file for reading
inputfilename = "CarSales.txt"
inputfile = open(inputfilename, 'r')  
# read the imput file
line = inputfile.readline()
# check for end of file
while line != '':
# split the line by commas
    carvalue = line.split(",")
# Strip and Title the car make
    carvalue[0] = carvalue[0].strip().title()
# Convert the value to an integer
    carvalue[1] = int(carvalue[1])
# insert into list
    cars.append(carvalue)
# read the next car
    line = inputfile.readline()
# close the input file
inputfile.close()

# Initialize count, sum and average
carcount = 0
carsum = 0
caraverage = 0
# loop through all the values
for i in range(len(cars)):
# increment car count
    carcount += 1
# add the value to the sum
    carsum += cars[i][1]
# compute the average (rounded)
caraverage = round(carsum/carcount)
# print the result
print(f"{carcount:d} Total Cars - Average Price: ${caraverage:d}")

# prompt for the make of the car - convert to title
carmake = input("Enter Car Make: ").title()
# loop until an empty car make is entered
while carmake != "":
# initialize count, sum and average
    carsoldcount = 0
    carsoldsum = 0
    carsoldaverage = 0
# loop trough all the values
    for i in range(len(cars)):
# check for match with entered make
        if cars[i][0] == carmake:
# match found, increment count and add value to sume
            carsoldcount += 1
            carsoldsum += cars[i][1]
# make sure we found at least one match
    if carsoldcount != 0:
# compute the average rounded
        carsoldaverage = round(carsoldsum/carsoldcount)
        print(f"{carsoldcount:6d} Cars Sold")
        print(f"${carsoldaverage:5d} Average Price")
# compute the percentage
        abovebelowaverage = (caraverage-carsoldaverage)/carsoldaverage
        print(f"{abovebelowaverage:6.2%} Above/Below Average")
    else:
# count was zero - no cars found
        print("Car Make Not Found")

    carmake = input("Enter Car Make: ").title()