numzeroes = 0
n = int(input("Enter N: "))
for i in range(n):
    if int(input("Enter Number: ")) == 0:
        numzeroes += 1
print("Number of Zeros: {}".format(numzeroes))
