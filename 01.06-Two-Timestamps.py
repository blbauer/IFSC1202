print("First Timestamp")
# Enter the hours, minutes, and seconds of the first timestamp
hours1 = int(input("Enter Hours: "))
minutes1 = int(input("Enter Minutes: "))
seconds1 = int(input("Enter Seconds: "))
# Enter the hours, minutes, and seconds of the second timestamp
print("Second Timestamp")
hours2 = int(input("Enter Hours: "))
minutes2 = int(input("Enter Minutes: "))
seconds2 = int(input("Enter Seconds: "))
# Calculate seconds for the first timestamp
totalseconds1 = (hours1 * 3600) + (minutes1 * 60) + seconds1
# Calculate seconds for the second timestamp
totalseconds2 = (hours2 * 3600) + (minutes2 * 60) + seconds2
# Calculate difference
difference = totalseconds2 - totalseconds1
# Print the difference
print(difference)
