height =int(input("Enter maximum height: "))

for i in range(0, height):
    for j in range(0, i + 1):
        print("* ", end='')
    print()

for i in range(height, 0, -1):
    for j in range(0, i - 1):
        print("* ", end='')
    print()