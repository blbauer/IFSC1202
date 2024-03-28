numdistinct = 1
x = input("Enter Values Separated by Spaces: ")
a = x.split()
# Loop through list - stopping at next to last value
for i in range(0 , len(a) - 1):
# See if the current value is not equal to the next value
    if int(a[i]) != int(a[i + 1]):    	
        numdistinct += 1
print("Number of Distinct Elements: {}".format(numdistinct))
