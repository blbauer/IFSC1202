# https://www.cuemath.com/great-circle-formula/
# https://byjus.com/great-circle-formula/
# https://www.omnicalculator.com/math/great-circle
# https://dodona.be/en/activities/1281456553/

from math import pi
from math import sin
from math import cos
from math import acos

# Input radius and data points
print("Great Circle Calculator")
radius = input("Enter Radius of Sphere: ")
lat1 = input("Starting Point - Enter Latitude: ")
lon1 = input("Starting Point - Enter Longitude: ")
lat2 = input("Ending Point - Enter Latitude: ")
lon2 = input("Ending Point - Enter Longitude: ")
#lat1 = 38.8976   # Latitude of point 1 (e.g., Warsaw)
#lon1 = -77.0366   # Longitude of point 1 (e.g., Warsaw)
#lat2 = 39.9496   # Latitude of point 2 (e.g., Rome)
#lon2 = -75.1503   # Longitude of point 2 (e.g., Rome)
# Convert to floating point and radians
r = float(radius)
x1 = float(lat1) * pi / 180
y1 = float(lon1) * pi / 180
x2 = float(lat2) * pi / 180
y2 = float(lon2) * pi / 180

# Calculate great circle distance
distance = r * acos((sin(x1) * sin(x2)) + (cos(x1) * cos (x2) * cos(y1-y2)))

# Print result
print(f"The Great Circle Distance is {distance:.2f}")