x = input("Enter Values Separated by Spaces: ")
count = 0
a = x.split()
# Start at the second number and end at the next to last number
for i in range(1, len(a) - 1):
    if int(a[i]) > int(a[i + 1]) and int(a[i]) > int(a[i - 1]):
        count += 1
print(count)
