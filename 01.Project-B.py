# Assume that it is not a leap year
NumSeconds = int(input("Enter Length of Time in Seconds: "))

SecondsPerYear = 365 * 24 * 60 * 60
Years = NumSeconds // SecondsPerYear
NumSeconds = NumSeconds - (Years * SecondsPerYear)

SecondsPerDay = 24 * 60 * 60
Days  = NumSeconds // SecondsPerDay
NumSeconds = NumSeconds - (Days * SecondsPerDay)

SecondsPerHour = 60 * 60
Hours  = NumSeconds // SecondsPerHour
NumSeconds = NumSeconds - (Hours * SecondsPerHour)

SecondsPerMinute = 60
Minutes  = NumSeconds // SecondsPerMinute
NumSeconds = NumSeconds - (Minutes * SecondsPerMinute)

print("Years:", Years)
print("Days:", Days)
print("Hours:", Hours)
print("Minutes:", Minutes)
print("Seconds:", NumSeconds)