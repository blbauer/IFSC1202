#ProperCase(s)
#Returns a properly cases string s by uppercasing the first character and lowercasing the rest of the string.
#Hint: use upper() and lower() methods
def ProperCase(s):
    return s[0:1].upper() + s[1:].lower()
#RemoveNewLine(s)
#Returns a string with the NewLine Character ("\n") removed from string s
#Hint: use replace() method
def RemoveNewLine(s):
    return s.replace("\n", "")
#Trim(s)
#Returns a string with the leading and trailing spaces removed from string s.
#Hint: use strip() methoddef Trim(s):
def Trim(s):
	return s.strip(" ")
#FirstName(s)
#Returns the first name of string s
#Hint:  Find the first space in string s using the find() method
#          Create a substring from the beginning of string s up to the first space
#          Call the ProperCase function
def FirstName(s):
# From the beginning of fullname, find the first blank    
    firstnameindex = s.find(" ")
# Pull out unformated first name
    firstname = s[:firstnameindex]
# Propercase first name
    firstname = ProperCase(firstname)
    return firstname

#LastName(s)
#Returns the last name of string s
#Hint:  Find the last space in string s using the rfind() method
#          Create a substring from the last space to the ending of  sring s
#          Call the ProperCase function
def LastName(s):
# From the end of fullname, find the first blank    
    lastnameindex = s.rfind(" ") + 1
# Pull out unformatted last name
    lastname = s[lastnameindex:]
# Propercase lastame
    lastname = ProperCase(lastname)
    return lastname

#MiddleName(s)
#Returns the middlename from string s
#Hint:  Find the first space in string s using the find() method
#          Find the last space in string s using the rfind() method
#          Create a substing from the first space to the last space of string s
#          Call the Trim function
#          Call the ProperCase function
#          If the length of the middle name is one, then it is an initial without a period.  Append a period.
def MiddleName(s):
# From the beginning of fullname, find the first blank    
	firstnameindex = s.find(" ")
# From the end of fullname, find the first blank    
	lastnameindex = s.rfind(" ") + 1
# Middle name start after the first name and before the last name.
	middlename = s[firstnameindex:lastnameindex]
# Trim off leading and trailing blanks
	middlename = Trim(middlename)
# Propercase middlename
	middlename = ProperCase(middlename)
# if middlename is one character long, 
# then it must be an initial and needs to have a period appended
	if len(middlename) == 1:
		middlename += "."
	return middlename
    
# Print Headings
print("{:10s} {:10s} {:10s}".format("First","Middle","Last"))
print("{:10s} {:10s} {:10s}".format("-"*10,"-"*10,"-"*10))
# Open the names.txt file for reading 
inputfile = open("7.11 Names.txt", 'r')  
#Read a record - Trim the record and remove the carriage return by call Trim() and RemoveCR() functions
fullname = Trim(RemoveNewLine(inputfile.readline()))
# check for end of file
while fullname != "":
# Print out the firstname, middlename, and lastname
	print("{:10s} {:10s} {:10s}".format(FirstName(fullname), MiddleName(fullname), LastName(fullname)))
# read the next record
	fullname = Trim(RemoveNewLine(inputfile.readline()))
