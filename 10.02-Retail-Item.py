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
# Step 5 - Create 3 instances of inventory using the data file
inventoryfile = open("10.02 Inventory.txt")
x = inventoryfile.readline()
y = x.split(",")
Item1 = RetailItem(y[0].strip(), int(y[1].strip()), float(y[2].strip()))
x = inventoryfile.readline()
y = x.split(",")
Item2 = RetailItem(y[0].strip(), int(y[1].strip()), float(y[2].strip()))
x = inventoryfile.readline()
y = x.split(",")
Item3 = RetailItem(y[0].strip(), int(y[1].strip()), float(y[2].strip()))
# Print the attributes
print("{:>20s}{:>20s}{:>20s}{:>20s}".format("Description", "Units On Hand", "Price", "Inventory Value"))
print("{:>20s}{:>20d}{:>20.2f}{:>20.2f}".format(Item1.Description, Item1.UnitsOnHand, Item1.Price, Item1.InventoryValue()))
print("{:>20s}{:>20d}{:>20.2f}{:>20.2f}".format(Item2.Description, Item2.UnitsOnHand, Item2.Price, Item2.InventoryValue()))
print("{:>20s}{:>20d}{:>20.2f}{:>20.2f}".format(Item3.Description, Item3.UnitsOnHand, Item3.Price, Item3.InventoryValue()))
