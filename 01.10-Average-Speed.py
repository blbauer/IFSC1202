km = float(input("Enter Length of Race in Kilometers: "))
min = int(input("Enter Minutes: "))
sec = int(input("Enter Seconds: "))
mi = km / 1.61
hr = (min / 60) + (sec / 3600)
mph = mi /hr
print(mph)
