first_max = int(input("Enter the First Number: "))
second_max = int(input("Enter the Second Number: "))
# if the first_max is less than the second_max, then exchange first_max and second_max
if first_max < second_max:
    first_max, second_max = second_max, first_max
#   temp = first_max
#   first_max = second_max
#   second_max = temp

# get the next element
new_value = input("Enter a Number (CR to quit): ")
while new_value != "":
# if the new_value is greater than the first_max 
    if int(new_value) > first_max:
# the new value becomes first_max and
# the old first_max gets moved to the second_max
        first_max, second_max = int(new_value), first_max
#	temp = first_max
#	first_max = int(new_value)
#	second_max = temp

# if the new_value is also greater that the second_max
    elif int(new_value) > second_max:
# the new_value becomes the second second_max
        second_max = int(new_value)
    new_value = input("Enter a Number (CR to quit): ")
print("First Maximum: {}".format(first_max))
print("Second Maximum: {}".format(second_max))
