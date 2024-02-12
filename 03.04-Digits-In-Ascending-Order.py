x = int(input("Enter a Number:"))
# Get the units
units = x % 10
# Divide the number by 10 to get rid of the units
x = x // 10
# Get the tens
tens = x % 10
# Divide the number by 10 to get rid of the tebs
hundreds = x // 10
# Make sure the digits are in order
if hundreds < tens and tens < units:
    print("YES")
else:
    print("NO")
