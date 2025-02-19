n = int(input("Enter a Number: "))

length = 0
while n != 0:
    length += 1
    n //= 10
print('Length is', length)