x = input("Enter Values Separated by Spaces: ")
a = x.split()
for i in range(len(a)):	
    if int(a[i]) % 2 == 1:
        print(a[i])
