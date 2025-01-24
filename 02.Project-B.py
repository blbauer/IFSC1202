# https://www.cuemath.com/great-circle-formula/
# https://byjus.com/great-circle-formula/
# https://www.omnicalculator.com/math/great-circle
# https://dodona.be/en/activities/1281456553/
import math
from math import pi
from math import sin
from math import cos
from math import acos
from math import radians

print("Great Circle Calculator")
radius = input("Enter Radius of Sphere: ")
lat1 = input("Starting Point - Enter Latitude: ")
lon1 = input("Starting Point - Enter Longitude: ")
lat2 = input("Ending Point - Enter Latitude: ")
lon2 = input("Ending Point - Enter Longitude: ")

r = float(radius)
x1 = radians(float(lat1))
y1 = radians(float(lon1))
x2 = radians(float(lat2))
y2 = radians(float(lon2))

d = r * acos((sin(x1) * sin(x2)) + (cos(x1) * cos (x2) * cos(y1-y2)))

print("The Great Circle Distance is", d)

rad = 6371
lat1 = 48.87   # Latitude of point 1 (e.g., Warsaw)
lon1 = -2.33   # Longitude of point 1 (e.g., Warsaw)
lat2 = 37.8  # Latitude of point 2 (e.g., Rome)
lon2 = 122.40   # Longitude of point 2 (e.g., Rome)


def greatcircle(lat1, lon1, lat2, lon2, r):

    a = radians(lat1)
    x = radians(lon1)
    b = radians(lat2)
    y = radians(lon2)

    cosa = cos(a)
    cosb = cos(b)
    cosxy = cos(x-y)
    sina = sin(a)
    sinb = sin(b)
    q = cos(a) * cos(b) * cos(x-y) + (sin(a) * sin(b))


    d = r * acos(cos(a) * cos(b) * cos(x-y) + (sin(a) * sin(b)))

    return d





def haversine(lat1, lon1, lat2, lon2, unit='km'):
    """
    Calculate the great circle distance in kilometers or miles between two points
    on the Earth's surface.
    
    Parameters:
    lat1, lon1 : float : Latitude and Longitude of the first point (in decimal degrees)
    lat2, lon2 : float : Latitude and Longitude of the second point (in decimal degrees)
    unit : str : 'km' for kilometers (default), 'miles' for miles

    Returns:
    float : Distance between the two points in the specified unit
    """
    
    # Convert degrees to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    
    # Earth radius in km or miles
    if unit == 'miles':
        R = 3958.8  # Earth's radius in miles
    else:
        R = 6371  # Earth's radius in kilometers

    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    # Calculate the distance
    distance = R * c
    return distance

# Example usage:

rad = 6371
lat1 = 48.87   # Latitude of point 1 (e.g., Warsaw)
lon1 = -2.33   # Longitude of point 1 (e.g., Warsaw)
lat2 = 37.8  # Latitude of point 2 (e.g., Rome)
lon2 = 122.40   # Longitude of point 2 (e.g., Rome)
distance = greatcircle(lat1, lon1, lat2, lon2, rad)
distance_miles = haversine(lat1, lon1, lat2, lon2, unit='km')

rad = 3958.8
lat1 = 59.5   # Latitude of point 1 (e.g., Warsaw)
lon1 = -30.3   # Longitude of point 1 (e.g., Warsaw)
lat2 = 37.8   # Latitude of point 2 (e.g., Rome)
lon2 = 122.4   # Longitude of point 2 (e.g., Rome)

distance = greatcircle(lat1, lon1, lat2, lon2, rad)
distance_miles = haversine(lat1, lon1, lat2, lon2, unit='miles')


rad = 3958.8
lat1 = 37.56   # Latitude of point 1 (e.g., Warsaw)
lon1 = 89.06   # Longitude of point 1 (e.g., Warsaw)
lat2 = 36.87   # Latitude of point 2 (e.g., Rome)
lon2 = 87.47   # Longitude of point 2 (e.g., Rome)

distance = greatcircle(lat1, lon1, lat2, lon2, rad)
distance_miles = haversine(lat1, lon1, lat2, lon2, unit='miles')

rad = 3958.8
lat1 = 25   # Latitude of point 1 (e.g., Warsaw)
lon1 = 34   # Longitude of point 1 (e.g., Warsaw)
lat2 = 48   # Latitude of point 2 (e.g., Rome)
lon2 = 67   # Longitude of point 2 (e.g., Rome)


distance = greatcircle(lat1, lon1, lat2, lon2, rad)
distance_miles = haversine(lat1, lon1, lat2, lon2, unit='miles')

rad = 3958.8
lat1 = 45   # Latitude of point 1 (e.g., Warsaw)
lon1 = 24   # Longitude of point 1 (e.g., Warsaw)
lat2 = 32   # Latitude of point 2 (e.g., Rome)
lon2 = 17   # Longitude of point 2 (e.g., Rome)

distance = greatcircle(lat1, lon1, lat2, lon2, rad)
distance_miles = haversine(lat1, lon1, lat2, lon2, unit='miles')



lat1 = 52.2296756   # Latitude of point 1 (e.g., Warsaw)
lon1 = 21.0122287   # Longitude of point 1 (e.g., Warsaw)
lat2 = 41.8919300   # Latitude of point 2 (e.g., Rome)
lon2 = 12.5113300   # Longitude of point 2 (e.g., Rome)

distance = greatcircle(lat1, lon1, lat2, lon2, rad)
distance_km = haversine(lat1, lon1, lat2, lon2, unit='km')
distance_miles = haversine(lat1, lon1, lat2, lon2, unit='miles')

print(f"Distance: {distance_km:.2f} km")
print(f"Distance: {distance_miles:.2f} miles")

lat1 = 40.71
lat2 = 51.51
lon1 = -74.01
lon2 = -0.13
rad = 6371
distance_km = haversine(lat1, lon1, lat2, lon2, unit='km')
distance_miles = haversine(lat1, lon1, lat2, lon2, unit='miles')
x = greatcircle(lat1, lon1, lat2, lon2, rad)

print(f"Distance: {distance_km:.2f} km")
print(f"Distance: {distance_miles:.2f} miles")
