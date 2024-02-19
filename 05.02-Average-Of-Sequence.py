sequencesum = 0
sequencecount = 0
value = input("Enter a Number (CR to quit): ")
while value != '':
    sequencesum += int(value)
    sequencecount += 1
    value = input("Enter a Number (CR to quit): ")
if sequencecount != 0:
    sequenceaverage = sequencesum / sequencecount
    print("Average: {}".format(sequenceaverage))
else:
    print("Sequence Length is 0")
