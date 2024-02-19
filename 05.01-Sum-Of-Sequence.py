sequencesum = 0
value = input("Enter a Number (CR to quit): ")
while value != '':
    sequencesum += int(value)
    value = input("Enter a Number (CR to quit): ")
print("Sum: {}".format(sequencesum))
