# Read classroom sizes
classroomA = int(input("Enter Classroom A: "))
classroomB = int(input("Enter Classroom B: "))
classroomC = int(input("Enter Classroom C: "))
# Calculate number of full and partial desks in Classroom A
fulldesksA = classroomA // 2
partialdesksA = classroomA % 2
# Calculate number of full and partial desks in Classroom B
fulldesksB = classroomB // 2
partialdesksB = classroomB % 2
# Calculate number of full and partial desks in Classroom C
fulldesksC = classroomC // 2
partialdesksC = classroomC % 2
# Total the number of desks needed
total = fulldesksA + partialdesksA + fulldesksB + partialdesksB + fulldesksC + partialdesksC
# Display the total
print(total)
