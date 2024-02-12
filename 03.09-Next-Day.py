month = int(input("Enter Month:"))
day = int(input("Enter Day:"))
# is it the last day of the month?
# if so then add 1 to the month and reset the day to 1
if ((month == 1 and day == 31) or 
   (month == 2 and day == 28) or
   (month == 3 and day == 31) or
   (month == 4 and day == 30) or
   (month == 5 and day == 31) or
   (month == 6 and day == 30) or
   (month == 7 and day == 31) or
   (month == 8 and day == 31) or
   (month == 9 and day == 30) or
   (month == 10 and day == 31) or
   (month == 11 and day == 30)):
    month += 1
    day = 1
# is it the last day of the year?
# if so then reset to Jan 1
elif month == 12 and day == 31:
    month = 1
    day = 1
# just a normal day
# add 1 to the day
else:
    day += 1
# print the result
print("Next Day: {}/{}".format(month, day))
