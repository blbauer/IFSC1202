x = input("Enter Values Separated by Spaces: ")
# Split the values into a list
a = x.split()
# Assume that the first number is the max
indexofmax = 0
# Start at the second number
for i in range(1, len(a)):
    if int(a[i]) > int(a[indexofmax]):    	
        indexofmax = i
print("Largest Value: {}".format(a[indexofmax]))
print("Index of Largest Value: {}".format(indexofmax))
