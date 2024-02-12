a = int(input("Enter First Number:"))
b = int(input("Enter Second Number:"))
c = int(input("Enter Third Number:"))
if a <= b and a <= c:
    print(a)
elif b <= a  and b <= c:
    print(b)
else:
    print(c)
