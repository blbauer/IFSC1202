s = input("Enter a string: ")
if s.count('f') == 1:
# found one f
    print("One f")
elif s.count('f') < 1:
# didnt find f
    print('Zero f')
else:
# found 2 fs
# find occurence of the first f
    first_f = s.find('f')
#  find the second occurrence beginning at the first occurrence + 1
    print(s.find('f', first_f + 1))
