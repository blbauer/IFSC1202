FirstNumber = int(input("Enter First 2 Digit Number:"))
SecondNumber = int(input("Enter Second 2 Digit Number:"))
# Units Digit from First Number is the remainder divided by 10
UnitsDigitFirstNumber = FirstNumber % 10
# Tens Digit from the First Number is integer division by 10
TensDigitFirstNumber = FirstNumber // 10
# Units Digit from Second Number is the remainder divided by 10
UnitsDigitSecondNumber = SecondNumber % 10
# Tens Digit from the Second Number is integer division by 10
TensDigitSecondNumber = SecondNumber // 10
# Put the number together in the desired order and print
MergedNumber = str(TensDigitFirstNumber) + str(TensDigitSecondNumber) + str(UnitsDigitFirstNumber) + str(UnitsDigitSecondNumber)
print("Merged Number: {}".format(MergedNumber))
