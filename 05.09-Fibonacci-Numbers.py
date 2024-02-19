# By definition, the second_previous_value is 0
second_previous_value = 0
# By definition, the first_previous_value is 0
first_previous_value = 1
n = int(input("Enter Fibonnaci Sequence Number: "))
if n == 0:
    print("Fibonacci Number: 0")
elif n == 1:
    print("Fibonacci Number: 1")
else:
    for i in range(2, n + 1):
#       The current_value is the sum of the two previous values (first_previous_value and second_previous_value)
        current_value = first_previous_value + second_previous_value
#       Move the first_previous_value to the second_previous_value
        second_previous_value = first_previous_value
#       Now the current_value becomes the first_previous_value
        first_previous_value = current_value
    print("Fibonacci Number: {}".format(current_value))
