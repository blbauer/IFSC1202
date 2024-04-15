# Step 1 - Define the class object "RetailItem"
class RetailItem ():
	
# Step 2 - Define the initializer and any default values
	def __init__(self, Description="", UnitsOnHand=0, Price=0):

# Step 3 - Define the object attributes
		self.Description = Description
		self.UnitsOnHand = UnitsOnHand
		self.Price = Price

# Step 4 - Define Actions (Methods) associated with the object
	def InventoryValue(self):
		return self.UnitsOnHand * self.Price
		
# Finds the inventory in the list and returns the index of the row where the inventory was found
def find_inventory(mylist, itemtofind):
	for i in range(len(mylist)):
		if mylist[i].Description == itemtofind:
			return i
	return -1		

def print_inventory(mylist):
	# Print the titles
	print("{:>20s}{:>20s}{:>20s}{:>20s}".format("Description", "Units On Hand", "Price", "Inventory Value"))
	
	# Loop through list and pring the attributes of the objects
	for i in range(len(mylist)):
		print("{:>20s}{:>20d}{:>20.2f}{:>20.2f}".format(mylist[i].Description, mylist[i].UnitsOnHand, mylist[i].Price, mylist[i].InventoryValue()))

# Step 5 - Create 3 instances of inventory using the data file
inventoryfile = open("11.01 Inventory.txt")

inventorylist = []

x = inventoryfile.readline()
while x != "":
	y = x.split(",")
	item = RetailItem(y[0].strip(), int(y[1].strip()), float(y[2].strip()))
	inventorylist.append(item)
	x = inventoryfile.readline()
inventoryfile.close()

# print inventory
print_inventory(inventorylist)

# open and read the inventory update file
inventoryupdatefile = open("11.01 InventoryUpdate.txt")
x = inventoryupdatefile.readline()
while x != "":
	y = x.split(",")
	# change the price by looking up the description
	inventorylist[find_inventory(inventorylist, y[0].strip())].Price = float(y[1].strip())
	x = inventoryupdatefile.readline()
inventoryupdatefile.close()

# print the inventory
print()
print_inventory(inventorylist)
