n = int(input("Enter N: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end='')
    print()  # Prints a new line