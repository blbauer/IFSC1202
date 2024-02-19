n = int(input("Enter Number of Cards: "))
sumallcards = 0
for i in range(1, n + 1):
    sumallcards += i
# Read each card and subtract the value
# The remaining value will be the missing card
sumcards = 0
for i in range(n - 1):
    sumcards += int(input("Enter Card: "))
print("Missing Card: {}".format(sumallcards - sumcards))
