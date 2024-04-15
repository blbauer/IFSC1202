from math import sqrt
from math import atan
from math import pi
# Step 1 - Define the class object "Point"
class Point:
# Step 2 - Define the initializer and any default values
    def __init__(self, Xvalue, Yvalue):
# Step 3 - Define the object attributes
        self.x = Xvalue
        self.y = Yvalue
# Step 4 - Define the methods for the object
# ToString returns a nicely formated string to represent the data point
    def ToString(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"
# Function to calculate the distance between two points        
def Distance(pointA, pointB):
    return sqrt((pointB.x - pointA.x)**2 + (pointB.y - pointA.y)**2)
# Function to calculste the midpoint between two points    
def MidPoint(pointA, pointB):
    x = (pointB.x + pointA.x) / 2
    y = (pointB.y + pointA.y) / 2
    mymidpoint = Point(x,y)
    return mymidpoint
# Function to calculate the angle of the line compated to the x axis    
def XAngle(pointA, pointB):
    slope = (pointB.y - pointA.y) / (pointB.x - pointA.x)
    return atan(slope) * 180.0 / pi
# Step 5 - Create instances two Points using the data file
print("{:>20s} {:>20s} {:>20s} {:>20s} {:>20s}".format("Point A", "Point B", "Distance", "Midpoint", "Angle"))
print("{:>20s} {:>20s} {:>20s} {:>20s} {:>20s} ".format("-"*15, "-"*15, "-"*15, "-"*15,"-"*15))
pointsfile = open("10.05 Points.txt")
line = pointsfile.readline()
while line != "":
    pointvalues = line.split(",")
# First two value are Point A, second two values are Point B
    PointA = Point(float(pointvalues[0].strip()),float(pointvalues[1].strip()))
    PointB = Point(float(pointvalues[2].strip()),float(pointvalues[3].strip()))
    print("{:>20s} {:>20s} {:>20.7f} {:>20s} {:>20.7f}".format(PointA.ToString(), PointB.ToString(), Distance(PointA,PointB), MidPoint(PointA,PointB).ToString(),XAngle(PointA,PointB) )) 
    line = pointsfile.readline()
pointsfile.close()
