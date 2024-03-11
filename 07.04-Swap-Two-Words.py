s = input("Enter a string: ")
first_word = s[:s.find(' ')]
second_word = s[s.find(' ') + 1:]
result = second_word + ' ' + first_word
print(result)
