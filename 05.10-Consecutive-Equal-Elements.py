current_value = input("Enter a Number (CR to quit): ")
if current_value !="":
    previous_value = int(current_value)
    current_repeating_count = 1
    maximum_repeating_count = 1
    maximum_repeating_value = int(current_value)

    current_value = input("Enter a Number (CR to quit): ")
    while current_value != "":
    # if the current_value was a repeat of the previous value, then increment the count
        if previous_value == int(current_value):
            current_repeating_count += 1
        else:
    # if the current_value is not a repeat of the previous value, check to see if there is a new maximum count and value
            if current_repeating_count > maximum_repeating_count:
                maximum_repeating_count = current_repeating_count
                maximum_repeating_value = previous_value
    #  Reset the previous value to the current_value; reset the count
            previous_value = int(current_value)
            current_repeating_count = 1
        current_value = input("Enter a Number (CR to quit): ")

    # end of input - check to see if the last value caused a new maximum count and value
    if current_repeating_count > maximum_repeating_count:
        maximum_repeating_count = current_repeating_count
        maximum_repeating_value = previous_value
    print("{} repeated {} times".format(maximum_repeating_value, maximum_repeating_count))
else:
    print("Sequence Length is 0")