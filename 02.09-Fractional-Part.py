x = float(input("Enter a Number: "))
# Conveert the number to an integer to get the whole number
whole = int(x)
# Subract the whole part from the number, leaving the fraction
fraction = (x - whole)
# Round the number to 10 digits so that it displays correctly
print(f"Fractional Part: {round(fraction,10)}")
