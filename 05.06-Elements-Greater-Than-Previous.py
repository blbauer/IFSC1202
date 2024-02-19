value = input("Enter a Number (CR to quit): ")
if value != "":
    previousvalue = int(value)
    previouscount = 0
    while value !="":
        if previousvalue < int(value):
# previousvalue is less than current value so increment the count
            previouscount += 1
# set the previous value to the value we just read
        previousvalue = int(value)
        value = input("Enter a Number (CR to quit): ")
    print("Number of Values Greater Than the Previous: {}".format(previouscount))
else:
    print("Sequence Length is 0")