year = int(input("Enter Year:"))
#   (Divisible by 4 and Not Divisible by 100) or (Divisible by 400)
if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
    print('LEAP YEAR')
else:
    print('COMMON YEAR')
