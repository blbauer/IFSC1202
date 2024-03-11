s = input("Enter a string: ")
# Find the first h and the last h
first_h = s.find('h')
last_h = s.rfind('h')
result = s[:first_h] + s[last_h + 1:]
print(result)
