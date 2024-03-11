s = input("Enter a string: ")
before_h = s[:s.find('h')]
between_h = s[s.find('h'):s.rfind('h') + 1]
after_h = s[s.rfind('h') + 1:]
reverse_between_h = between_h[::-1]
result = before_h + reverse_between_h + after_h
print(result)
