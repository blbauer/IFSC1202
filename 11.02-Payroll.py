# Step 1 - Define the class object "CarlItem"
class Employee:

# Step 2 - Define the initializer and any default values
    def __init__(self, firstname, lastname, idnumber, wage):

# Step 3 - Define the object attributes
        self.FirstName = firstname
        self.LastName = lastname
        self.IDNumber = idnumber
        self.HoursWorked = 0
        self.Wage = wage

# Step 4 - Define Actions (Methods) associated with the object
    def WeeklyPay(self):
        if self.HoursWorked <= 40:
            return float(self.HoursWorked) * float(self.Wage)
        else:
            standardwage = 40.0 * float(self.Wage)
            overtimehours = float(self.HoursWorked) - 40.0
            overtimewage = 1.5 * overtimehours * float(self.Wage)
            return standardwage + overtimewage

def find_employee(mylist, itemtofind):
	for i in range(len(mylist)):
		if mylist[i].IDNumber == itemtofind:
			return i
	return -1		
# Step 5 - Create 3 instances of Employee using the data file

employeelist = []
employeesfile = open("11.02 Employees.txt")

x = employeesfile.readline()
while x != "":
	y = x.split(",")
	Employee1 = Employee(y[0].strip(), y[1].strip(), y[2].strip(), float(y[3].strip()))
	employeelist.append(Employee1)
	x = employeesfile.readline()
employeesfile.close()

# open and read the hours file
hoursfile = open("11.02 Hours.txt")
x = hoursfile.readline()
while x != "":
	y = x.split(",")
	# change the employye by looking up the ID
	employeelist[find_employee(employeelist, y[0].strip())].HoursWorked = float(y[1].strip())
	x = hoursfile.readline()
hoursfile.close()


print("{:>8s}{:>8s}{:>8s}{:>8s}{:>8s}{:>8s}".format("First", "Last", "ID", "Hours", "Hourly", "Weekly"))
print("{:>8s}{:>8s}{:>8s}{:>8s}{:>8s}{:>8s}".format("Name", "Name", "Number", "Worked", "Wage", "Pay"))

for i in range(len(employeelist)):
	print("{:>8s}{:>8s}{:>8s}{:>8.2f}{:>8.2f}{:>8.2f}".format(employeelist[i].FirstName, employeelist[i].LastName, employeelist[i].IDNumber, employeelist[i].HoursWorked, employeelist[i].Wage, employeelist[i].WeeklyPay()))