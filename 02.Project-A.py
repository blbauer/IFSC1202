from math import sqrt
s1 = float(input("Enter Side 1: "))
s2 = float(input("Enter Side 2: "))
s3 = float(input("Enter Side 3: "))
s = (s1 + s2 + s3) / 2.0
area = sqrt(s * (s - s1) * (s - s2) * (s - s3))
print("Area:", area)