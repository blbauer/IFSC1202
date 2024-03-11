from math import acos,cos,sin, pi
# https://www.omnicalculator.com/math/great-circle
def DegreeStringToRadians(ds):
    # Take a degree string in the form of dd°mm'ss"d and converts it to radian
    # First parse the string into its parts
    degrees, minutes, seconds, direction = ParseDegreeString(ds)
    # Using the parts, convert to radians
    radians = DegreesToRadians(degrees, minutes, seconds, direction)
    return radians

def DegreesToRadians(degrees, minutes, seconds, direction):
    # Coverts degrees, minutes, seconds and direction to radians
    # There are 60 minutes in a degree and 3600 seconds in a degree
    decimaldegrees = degrees + (minutes / 60) + (seconds / 3600)
    # Multiply by pi and divide by 180 to get radians
    radians = decimaldegrees * pi / 180
    # S and E are defined to be a negative direction
    if direction == "N" or direction == "W":
        radians = abs(radians)
    else:
        radians = -abs(radians)
    return radians

def ParseDegreeString(ds):
    # Parses a coordinate string in the format: dd°mm'ss"d, where
    # dd is the number of degrees
    # mm is the number of minutes
    # ss is the number of seconds
    # d is the direction (N, S, E, or W)
    # Note that char(176) is the degree symbol

    # Find the degree symbol
    degreepos = ds.find(chr(176))
    # Degrees is located between the beginning of the string and the degree symbol position
    degrees = float(ds[:degreepos])
    # find the minutes symbol (')
    minutepos = ds.find("'")
    # Minutes is located between the degree symbol and the minutes symbol position
    minutes = float(ds[degreepos+1:minutepos])
    # Find the seconds symbol
    secondpos = ds.find('"')
    # Seconds is located betwween the minutes symbol position and the seconds symbol position
    seconds = float(ds[minutepos+1:secondpos])
    # Directions is 2 postions down from the seconds position
    direction = ds[secondpos+1:secondpos+2]
    return degrees, minutes, seconds, direction


def GreatCircleDistance(x1, y1, x2, y2, r):
    #x1, y1 are the x and y angles in radians of the from point
    #x2, y2 are the x and y angles in radians of the to point
    d = r * acos((cos(x1) * cos(x2) * cos(y1 - y2)) + (sin(x1) * sin(x2)))
    return d

inputfilename = "07.Project Distances.txt"
inputfile = open(inputfilename, 'r')
# Open the input file for reading
line = inputfile.readline().strip()
# First line is the radius
radius = float(line)
# Read until the input is empty
line = inputfile.readline()
while line != '':
    # find the dash so we can separate the from coordinate and the to coordinate
    dashpos = line.find("-")
    # Isolate the from coordinate based on the position of the dash
    fromlatlongstring = line[:dashpos-1].strip()
    # Find the space so we can separate the latitude and longitude
    spacepos = fromlatlongstring.find(" ")
    # Isolate the latitude
    fromlatstring = fromlatlongstring[:spacepos].strip()
    # Isolate the longitude
    fromlongstring = fromlatlongstring[spacepos+1:].strip()
    # Convert the latitude to radians
    fromlatradians = DegreeStringToRadians(fromlatstring)
    # Convert the longitude to radians
    fromlongradians = DegreeStringToRadians(fromlongstring)

    # Isolate the from coordinate based on the position of the dash
    tolatlongstring = line[dashpos+1:].strip()
    # Find the space so we can separate the latitude and longitude
    spacepos = tolatlongstring.find(" ")
    # Isolate the latitude
    tolatstring = tolatlongstring[:spacepos].strip()
    # isolate the longitude
    tolongstring = tolatlongstring[spacepos+1:].strip()
    # Convert the latitude to radians
    tolatradians = DegreeStringToRadians(tolatstring)
    # Convert the longitude to radians
    tolongradians = DegreeStringToRadians(tolongstring)

    distance = GreatCircleDistance(fromlatradians, fromlongradians, tolatradians, tolongradians, radius)

    print("{}".format(line))
    print("From Radian values = {:>21.15f},{:>21.15f}".format(fromlatradians, fromlongradians))
    print("To Radian values =   {:>21.15f},{:>21.15f}".format(tolatradians, tolongradians))
    print("Distance =           {:>21.15f}".format(distance))
    print()

    line = inputfile.readline().strip()

