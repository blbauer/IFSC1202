# Assume that it is not a leap year
NumDays = int(input("Enter Length of Time in Days: "))
Years = (NumDays // 365)
Weeks = (NumDays % 365) // 7
Days  = NumDays - ((Years * 365) + (Weeks * 7))
print("Years:", Years)
print("Weeks:", Weeks)
print("Days:", Days)