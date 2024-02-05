# Read the number of students
n = int(input("Number of Students: "))
# Read the number of apples
k = int(input("Number of Apples: "))
# Use floor division to calculate apples per student
applesperstudent = k // n
# Use modulo division to calculate remaining apples
remainingapples = k % n
# Print the results
print (applesperstudent)
print (remainingapples)
