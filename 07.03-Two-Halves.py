s = input("Enter a string: ")
first_half = s[:(len(s) + 1) // 2]
second_half = s[(len(s) + 1) // 2:]
interchanged = second_half + first_half
print(interchanged)
