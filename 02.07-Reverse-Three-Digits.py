a = int(input("Enter a 3 Digit Number: "))
# Divide by ten; the remainder is the units digit
unitsdigit = a % 10
# Divide the original number by ten to get rid of the units digit
a = a // 10
# Divide by ten; the remainder is the tens digit
tensdigit = a % 10
# Divide the original number by ten to get rid of the tens digit
a = a // 10
# What is left is the hundreds digit
hundredsdigit = a
# Reverse the order of the digits, converting to a string, then print
reverse = str(unitsdigit) + str(tensdigit) + str(hundredsdigit)
print(f"Reverse of Digits: {reverse}")