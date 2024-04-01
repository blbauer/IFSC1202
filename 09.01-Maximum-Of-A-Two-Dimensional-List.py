# Input the array sizes and split into values
dataline = input("Enter the number of rows and columns: ").split()
m = int(dataline[0])  # m is number of rows
n = int(dataline[1])  # n is number of columns
# Create the array based on the number of columns and rows
a = []
for i in range(m):
    a.append([0] * n)
# Read each row line by line
for i in range(m):
# Input the row and split into values
    dataline = input("Enter a line of data: ").split()
# Put row into array
    for j in range(n):
        a[i][j] = int(dataline[j])
# Print the array
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()
# Intialize largest value to first row and column value in array
best_i = 0
best_j = 0
curr_max = a[0][0]
# Loop through each row
for i in range(m):
# Loop through each column
        for j in range(n):
# If the value is greater than the current max, it is new new max
            if a[i][j] > curr_max:
                curr_max = a[i][j]
                best_i = i
                best_j = j
# All done - print out result
print("The maximum value {} occurred in row {} column {}".format(curr_max, best_i, best_j))
