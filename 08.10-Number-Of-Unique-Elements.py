count = 0
x = input("Enter Values Separated by Spaces: ")
a = x.split()
print("Unique Elements:" , end = " ")
# Loop through each element
for i in range(len(a)):
# Loop again, looking for a match
    for j in range(len(a)):
# Match found - element not unique - skip to next element
        if i != j and a[i] == a[j]:
            break
    else:
# Match not found - print the element
        print(a[i], sep = " ", end = " ")
print()
