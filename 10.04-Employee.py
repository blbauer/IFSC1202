# Step 1 - Define the class object "CarlItem"
class Employee:
# Step 2 - Define the initializer and any default values
    def __init__(self, firstname, lastname, idnumber, hoursworked, wage):

# Step 3 - Define the object attributes
        self.FirstName = firstname
        self.LastName = lastname
        self.IDNumber = idnumber
        self.HoursWorked = hoursworked
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
# Step 5 - Create 3 instances of Employee using the data file
employeesfile = open("10.06 Payroll.txt")
x = employeesfile.readline()
y = x.split(",")
Employee1 = Employee(y[0].strip(), y[1].strip(), y[2].strip(), float(y[3].strip()), float(y[4].strip()))
x = employeesfile.readline()
y = x.split(",")
Employee2 = Employee(y[0].strip(), y[1].strip(), y[2].strip(), float(y[3].strip()), float(y[4].strip()))
x = employeesfile.readline()
y = x.split(",")
Employee3 = Employee(y[0].strip(), y[1].strip(), y[2].strip(), float(y[3].strip()), float(y[4].strip()))
print("{:>8s}{:>8s}{:>8s}{:>8s}{:>8s}{:>8s}".format("First", "Last", "ID", "Hours", "Hourly", "Weekly"))
print("{:>8s}{:>8s}{:>8s}{:>8s}{:>8s}{:>8s}".format("Name", "Name", "Number", "Worked", "Wage", "Pay"))
print("{:>8s}{:>8s}{:>8s}{:>8.2f}{:>8.2f}{:>8.2f}".format(Employee1.FirstName, Employee1.LastName, Employee1.IDNumber, Employee1.HoursWorked, Employee1.Wage, Employee1.WeeklyPay()))
print("{:>8s}{:>8s}{:>8s}{:>8.2f}{:>8.2f}{:>8.2f}".format(Employee2.FirstName, Employee2.LastName, Employee2.IDNumber, Employee2.HoursWorked, Employee2.Wage, Employee2.WeeklyPay()))
print("{:>8s}{:>8s}{:>8s}{:>8.2f}{:>8.2f}{:>8.2f}".format(Employee3.FirstName, Employee3.LastName, Employee3.IDNumber, Employee3.HoursWorked, Employee3.Wage, Employee3.WeeklyPay()))
