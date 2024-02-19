start = int(input("Enter Start of Range: "))
end = int(input("Enter End of Range: "))
print("Special Numbers between {} and {}".format(start, end))
# Python program to check if the number is a Special number or not
# take input from the user
for num in range(start, end):
# Find the number of digits
    numdigits = 0
    temp = num
    while temp > 0:
        temp = temp // 10
        numdigits = numdigits + 1
# initialize sum
    sum = 0
# find the sum each digit to the power of the number of digits
    temp = num
    while temp > 0:
        digit = temp % 10
        sum = sum + (digit ** numdigits)
        temp = temp // 10
# Compare the original number with the calculated number
# If equal, then the number is special
    if num == sum:
        print(num)