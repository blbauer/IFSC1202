def isEven(n):
# Returns true if n is even and false if n is odd
    if n % 2 == 0:
        return True
    else:
        return False
def isOdd(n):
# Returns true if n is odd and false if n is even
    if n % 2 == 1:
        return True
    else:
        return False
def isPrime(n):
# if prime then write to the prime file        
# Only positive integers greater than one are prime
    if n > 1:
        half = (n // 2) + 1
        for i in range(2, half):
# If the number is divisible by any number 
# other than 1 and self then it is not prime  
            if number % i == 0:
                return False	# Found an evenly divisible number
        return True				# Number is prime
    else:
        return False   # Negative Number - not prime

# See https://codeforwin.org/2018/01/c-program-write-even-odd-prime-numbers-separate-file.html
# names of files
inputfilename = "06.06 Numbers.txt"
oddfilename = "06.06 Oddnumbers.txt"
evenfilename = "06.06 Evennumbers.txt"
primefilename = "06.06 Primenumbers.txt"
# counters for files
inputfilecount = 0
oddfilecount = 0
evenfilecount = 0
primefilecount = 0
# open input file for reading
inputfile = open(inputfilename, 'r')  
# open output files for writing
oddfile = open(oddfilename, 'w')  
evenfile = open(evenfilename, 'w')  
primefile = open(primefilename, 'w')  
# read the imput file
line = inputfile.readline()
# check for end of file
while line != '':
# convert input to an integer
    number = int(line)    
# increment the input file count
    inputfilecount += 1
# if even then write the number to the even file
    if isEven(number):
          evenfile.write(str(number) + "\n")
          evenfilecount += 1
# if even then write the number to the even file
    if isOdd(number):
          oddfile.write(str(number) + "\n")
          oddfilecount += 1
# Either all numbers tested or an even divsor was found
    if isPrime(number):
        primefile.write(str(number) + "\n")            
        primefilecount += 1
# read the next number
    line = inputfile.readline()
# close the pointer to that file
inputfile.close()
oddfile.close()
evenfile.close()
primefile.close()

# print the results
print("{} even numbers".format(evenfilecount))
print("{} odd numbers".format(oddfilecount))
print("{} prime numbers".format(primefilecount))
print("{} numbers read".format(inputfilecount))
