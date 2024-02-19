n = int(input("Enter Number: "))
for i in range(2,n):
    if n % i == 0:
        print (i, "is the smallest even divisor")
        break
else:
    print ("No even divisor")
