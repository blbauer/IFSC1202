value = input("Enter a Number (CR to quit): ")
evencount = 0
while value != "":
    if int(value) % 2 == 0:
        evencount += 1
    value = input("Enter a Number (CR to quit): ")
print("Number of Even Values: {}".format(evencount))
