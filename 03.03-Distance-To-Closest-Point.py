a = int(input("Enter Point A:"))
b = int(input("Enter Point B:"))
c = int(input("Enter Point C:"))
# Subtact b from a to get the distance - use absolute value
ab = abs(a - b)
# Subtact c from a to get the distance - use absolute value
ac = abs(a - c)
# Determine if ab or ac is smaller
if ab < ac:
    print (ab)
else:
    print (ac)
