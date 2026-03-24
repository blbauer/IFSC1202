a = [] # create an empty list
n = int(input("Enter Size of List:")) # read number of element in the list
for i in range(n): 
    new_element = int(input("Enter a Number:")) # read next element
    a.append(new_element) # add it to the list
print(a)