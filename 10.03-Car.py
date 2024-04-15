# Step 1 - Define the class object "CarlItem"
class Car():
# Step 2 - Define the initializer and any default values
	def __init__(self, Year, Make):

# Step 3 - Define the object attributes
		self.Year = Year
		self.Make = Make
		self.Speed = 0

# Step 4 - Define Actions (Methods) associated with the object
	def Accelerate(self, amount):
		self.Speed += amount
		return
	
	def Brake(self, amount):
		self.Speed -= amount
		if self.Speed < 0:
			self.Speed = 0
		return		
def changespeed(amount):
	if amount > 0:
		myCar.Accelerate(amount)
	else:
		myCar.Brake(abs(amount))
	return
# Step 5 - Create 3 instances of car using the data file
carfile = open("10.03 Cars.txt")
x = carfile.readline()
y = x.split(",")
myCar = Car(y[0].strip(), y[1].strip())
print("Make: {}".format(myCar.Make))
print("Year: {}".format(myCar.Year))
print()
print("Change    Speed")
x = carfile.readline()
changespeed(int(x.strip()))
print("{:6d}   {:6d}".format(int(x.strip()), myCar.Speed))
x = carfile.readline()
changespeed(int(x.strip()))
print("{:6d}   {:6d}".format(int(x.strip()), myCar.Speed))
x = carfile.readline()
changespeed(int(x.strip()))
print("{:6d}   {:6d}".format(int(x.strip()), myCar.Speed))
x = carfile.readline()
changespeed(int(x.strip()))
print("{:6d}   {:6d}".format(int(x.strip()), myCar.Speed))
