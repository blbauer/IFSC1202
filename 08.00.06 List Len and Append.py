# Create an empty list
a = []
# Open a file for reading
numbersfile = open("08.00.06 Numbers.txt", "r")
# Read the first line of the file
x = numbersfile.readline()
# End of file is indicated when the input is empty
while x != "":
# Convert the number to an integer and append it to the list
	a.append(int(x))
# Read the next line of the file
	x = numbersfile.readline()
# Close the file
numbersfile.close()
# Print the list - get the number of elements using the len() method
sum = 0
maximum = a[0]
maxindex = 0
for i in range(1,len(a)):
	print(a[i])
	sum = sum + a[i]
	if a[i] > maximum:
		maximum = a[i]
		maxindex = i
print("Avg:", sum / len(a))
print("Maximum:", maximum)
print("Max Index:", maxindex)