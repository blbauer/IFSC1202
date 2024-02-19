n = int(input("Enter N:"))
# prime is a boolean that indicates if we have found
# a number that evenly divides into n
# assume that the number is prime (true)
prime = True
# loop through all numbers beginning with 2 
# check all of the numbers up to half of n + 1
for i in range(2, n // 2 + 1):
	if n % i == 0:
		# found a number that evenly divides into n
		# set prime to false
		prime = False
# finished with the loop
# check prime and print the appropriate value
if prime:
	print("PRIME")
else:
	print("COMPOSITE")
