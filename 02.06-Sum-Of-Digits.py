a = int(input("Enter a 3 Digit Number: "))
# The units is modulus 10 of the entered number
units = a % 10
# Divide the entered number by ten and truncate to an integer
a = a // 10
# The tens is modulus 10 of the number
tens = a % 10
# Divide the number by ten and truncate to an integer
hundreds = a // 10
# Total up the values and print
total = hundreds + tens + units
print (f"Sum of Digits: {total}")