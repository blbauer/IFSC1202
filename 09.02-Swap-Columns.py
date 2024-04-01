# Function to swap columns
def swap_columns(a, i, j):
	for k in range(len(a)):
	    a[k][i], a[k][j] = a[k][j], a[k][i]
def print_array(a):
# Loop through each row in the two dimensional array
	for i in range(len(a)):
# Loop though each element in the list
		for j in range(len(a[i])):
# Print each element in the list
			print(a[i][j], end=' ')
# End of list - go to next line
		print()
# Create the array
a = []
# Open the file and read the first line`
numbersfile = open("09.02 NumbersList.txt")
x = numbersfile.readline()
# While not at end of file
while x != "":
# Split the line into a list
	y = x.split(" ")
# Convert the values from string to an integer
	for i in range(len(y)):
		y[i] = int(y[i])
# Append the list to the two dimensional array
	a.append(y)
# Read the next line
	x = numbersfile.readline()
# Print the print_array
print_array(a)
# get the column numbers to swap
rowcolumnsline = input("Enter the columns to swap: ").split()
i = int(rowcolumnsline[0])  # Column to swap
j = int(rowcolumnsline[1])  # Column to swap
# swap the columns
swap_columns(a, i, j)
# print the array
print_array(a)
