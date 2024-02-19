value = input("Enter a Number (CR to quit): ")
if value != "":
    maximum = int(value)
    maximumindex = 1
    currentindex = 1
    while value != "":
        if int(value) > maximum:
            maximum = int(value)
            maximumindex = currentindex
        value = input("Enter a Number (CR to quit): ")
        currentindex += 1
    print("Maximum: {}".format(maximum))
    print("Index of Maximum: {}".format(maximumindex))
else:
    print("Sequence Length is 0")