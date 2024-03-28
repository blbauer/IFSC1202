x = input("Enter Values Separated by Spaces: ")
# Split the values into a list
a = x.split()
# Loop through the list, beginning at the second value,
for i in range(1 , len(a), 2):
# Swap the ith and the previous value (ith - 1)
    temp = a[i]
    a[i] = a[i - 1]
    a[i - 1] = temp
# Print out the list
print("Swapped Values: ", end="")
for i in range(len(a)):
    print(a[i], sep = " ", end=" ")
print()
