a = int(input("Enter a Number: "))
# Divide by 100 and get the remainder
remainder = a % 100
# Floor divide remainder to get the number of tens
tens = remainder // 10
print(f"Tens Digit: {tens}")