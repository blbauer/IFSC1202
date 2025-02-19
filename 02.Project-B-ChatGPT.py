import math

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
lat1 = 38.8976   # Latitude of point 1 (e.g., Warsaw)
lon1 = -77.0366   # Longitude of point 1 (e.g., Warsaw)
lat2 = 39.9496   # Latitude of point 2 (e.g., Rome)
lon2 = -75.1503   # Longitude of point 2 (e.g., Rome)

distance_km = haversine(lat1, lon1, lat2, lon2, unit='km')
distance_miles = haversine(lat1, lon1, lat2, lon2, unit='miles')

print(f"Distance: {distance_km:.2f} km")
print(f"Distance: {distance_miles:.2f} miles")
