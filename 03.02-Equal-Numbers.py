a = int(input("Enter First Number:"))
b = int(input("Enter Second Number:"))
c = int(input("Enter Third Number:"))
# Check for all three numbers equal
if a == b and b == c:
    print(3)
# Check for two numbers equal
elif a == b or b == c or a == c:
    print(2)
# None of the number are equal
else:
    print(0)
