start = int(input("Enter Start of Range: "))
end = int(input("Enter End of Range: "))
print("Prime Numbers between {} and {}".format(start ,end))
for n in range(start, end + 1):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
	    # found a number that evenly divides into n
	    # go to next number
            break
    else:
        # Nothing evenly divides into the number
        # Must be prime
        print(n)
