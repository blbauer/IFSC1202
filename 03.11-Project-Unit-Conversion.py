# See http://www.unit-conversion.info/length.html
# Enter the From Value - must be a valid float
FromValue = float(input("Enter From Value:"))
# Enter the from unit - must be in, ft, yd, mi
FromUnit = input("Enter From Unit (in, ft, yd, mi):")
# Enter the to unit - must be in, ft, yd, mi
ToUnit = input("Enter To Unit (in, ft, yd, mi):")
if FromUnit != "in" and FromUnit != "ft" and FromUnit != "yd" and FromUnit != "mi":
    print ("FromUnit is not valid")
else:
    if ToUnit != "in" and ToUnit != "ft" and ToUnit != "yd" and ToUnit != "mi": 
        print ("ToUnit is not valid")
    else:
	multiplier = 0.0
	# Determine the multiplier based on the FromUnit and To Unit
	if FromUnit == "in" and ToUnit == "in": 
	    multiplier = 1.0
	if FromUnit == "in" and ToUnit == "ft": 
	    multiplier = 0.08333333333333
	if FromUnit == "in" and ToUnit == "yd": 
	    multiplier = 0.02777777777778 
	if FromUnit == "in" and ToUnit == "mi": 
	    multiplier = 0.00001578282828283 
	if FromUnit == "ft" and ToUnit == "in": 
	    multiplier = 12.0
	if FromUnit == "ft" and ToUnit == "ft": 
	    multiplier = 1.0
	if FromUnit == "ft" and ToUnit == "yd": 
	    multiplier = 0.3333333333333
	if FromUnit == "ft" and ToUnit == "mi": 
	    multiplier = 0.0001893939393939 	
	if FromUnit == "yd" and ToUnit == "in": 
	    multiplier = 36.0
	if FromUnit == "yd" and ToUnit == "ft": 
	    multiplier = 3.0
	if FromUnit == "yd" and ToUnit == "yd": 
	    multiplier = 1.0
	if FromUnit == "yd" and ToUnit == "mi": 
	    multiplier = 0.0005681818181818	
	if FromUnit == "mi" and ToUnit == "in": 
	    multiplier = 63360.0
	if FromUnit == "mi" and ToUnit == "ft": 
	    multiplier = 5280.0
	if FromUnit == "mi" and ToUnit == "yd": 
	    multiplier = 1760.0
	if FromUnit == "mi" and ToUnit == "mi": 
	    multiplier = 1.0	
	# Mutiply the FromValue by the multiplier and round to 7 digits
	ToValue = round(FromValue * multiplier, 7)
	# Format and Print the output
	print("{} {} => {} {}".format(FromValue, FromUnit, ToValue, ToUnit))
