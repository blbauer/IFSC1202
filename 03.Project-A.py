num1 = float(input("Enter First Number: "))
op = input("Enter Operator (+,-.*,/): ")
num2 = float(input("Enter Second Number: "))
# perform action based on operator
if op == "+":
    result = num1 + num2
    print(num1, op, num2, "=", result)
elif op == '-': 
    result = num1 - num2
    print(num1, op, num2, "=", result)
elif op == '*': 
    result = num1 * num2
    print(num1, op, num2, "=", result)
elif op == '/':
    result = num1 / num2
    print(num1, op, num2, "=", result)
else: 
    print("Invalid operator")