minindex = 0
maxindex = 0
x = input("Enter Values Separated by Spaces: ")
a = x.split()
# Find the index of the minimum and maximum
for i in range(1 , len(a)):
    if int(a[i]) > int(a[maxindex]):
    	maxindex = i
    if int(a[i]) < int(a[minindex]):
    	minindex = i
# Swap the minumum and maximum
temp = a[minindex]
a[minindex] = a[maxindex]
a[maxindex] = temp
# Print the list
print("Swapped Minimum and Maximum: ", end = "")
for i in range(len(a)):
    print(a[i], sep= " ", end = " ")
print()    
