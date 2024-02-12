x = int(input("Enter a Number:"))
# Get the units
units = x % 10
# Divide the number by 10 to get rid of the units
x = x // 10
# Get the tens
tens = x % 10
# Divide the number by 10 to get rid of of the tens
x = x // 10
# Get the hundreds
hundreds = x % 10
# Divide the number by 10 to get rid of of the hundres
thousands = x // 10
# First and last digits must match and second and third digits must match
if thousands == units and hundreds == tens:
    print("YES")
else:
    print("NO")
