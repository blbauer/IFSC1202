# Percent Change is todays value - yesterdays value
# divided by yesterdays value time 100
def percentchange(today, yesterday):
    return ((today - yesterday) / yesterday) * 100
# Open the stock file
inputfile = open("06.02 Stock.txt")
# Read the first line
line = inputfile.readline()
# Convert input line into floating point
todayvalue = float(line)
# Print Headings
print("{:>10s} {:>10s}".format("Price", "Change"))
# Print first value - there are no changes yet
print("{:10.2f}".format(todayvalue))
# Save todays value as yesterdays value
yesterdayvalue = todayvalue
# Read next line
line = inputfile.readline()
# Read until the input is empty
while line != '':
# Convert input line to a floating number
    todayvalue = float(line)
# Print the stock value and the percent change
    print("{:10.2f} {:10.2f}%".format(todayvalue, percentchange(todayvalue, yesterdayvalue)))
# Todays Value becomes Yesterdays Value
    yesterdayvalue = todayvalue
# Read the next line
    line = inputfile.readline()
# Close file
inputfile.close()
