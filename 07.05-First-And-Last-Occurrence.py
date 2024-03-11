s = input("Enter a string: ")
if s.count('f') == 1:
    first_f = s.find('f')
    print("{}".format(first_f))
elif s.count('f') >= 2:
    first_f = s.find('f')
    last_f = s.rfind('f')
    print("{} {}".format(first_f, last_f))
