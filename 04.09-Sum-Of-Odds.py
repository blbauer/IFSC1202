start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))
# If the start number is even, set it to the next higher odd number
a = start
if  start % 2 == 0:
    a = a + 1
# If the end number is even, set it to the nest lower odd number
b = end
if end % 2 == 0:
    b = b - 1
sum = 0
# Loop through the range, and include the last number, increment by 2
for i in range(a, b+1, 2):
    sum = sum + i
print("The sum of odd numbers between", start, "and", end, "is", sum)