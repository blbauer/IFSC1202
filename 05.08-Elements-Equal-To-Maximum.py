value = input("Enter a Number (CR to quit): ")
if value != "":
    maximum = int(value)
    number_of_maximum = 0
    while value != "":
    # check for a new maximum
        if int(value) > maximum:
    # found a new maximum
    # set the maximum to the new element
            maximum = int(value)
    # since this is a new maximum, the count has to be set to one
            number_of_maximum = 1
        elif int(value) == maximum:
    # same maximum found - increment the count
            number_of_maximum += 1       
        value = input("Enter a Number (CR to quit): ")
    print("Maximum: {}".format(maximum))
    print("Number of Occurrences: {}".format(number_of_maximum))
else:
    print("Sequence Length is 0")